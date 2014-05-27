#
#      Copyright (C) 2014 Sean Poyser
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc
import xbmcaddon
import xbmcgui
import os

import datetime

import urllib2
import urllib
import requests
from requests.auth import HTTPBasicAuth
import json

import dixie


ADDON    = xbmcaddon.Addon(id = 'script.tvguidedixie')
TITLE    = ADDON.getAddonInfo('name')
DIXIEURL = ADDON.getSetting('dixie.url').upper()
username = ADDON.getSetting('username')
password = ADDON.getSetting('password')


try:
    #workaround Python bug in strptime which causes it to intermittently throws an AttributeError
    import datetime, time
    datetime.datetime.fromtimestamp(time.mktime(time.strptime('2013-01-01 19:30:00'.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
except:
    pass



def generateMD5(path):
    if not os.path.exists(path):
        return '0'

    try:
        import hashlib        
        return hashlib.md5(open(path, 'r').read()).hexdigest()
    except:
        pass

    try:
        import md5
        return md5.new(open(path, 'r').read() ).hexdigest()
    except:
        pass
        
    return '0'



def ok(title, line1, line2 = '', line3 = ''):
    dlg = xbmcgui.Dialog()
    dlg.ok(title, line1, line2, line3)



def yesno(title, line1, line2 = '', line3 = '', no = 'No', yes = 'Yes'):
    dlg = xbmcgui.Dialog()
    return dlg.yesno(title, line1, line2, line3, no, yes) == 1



def progress(title, line1 = '', line2 = '', line3 = ''):
    dp = xbmcgui.DialogProgress()
    dp.create(title, line1, line2, line3)
    dp.update(0)
    return dp



def parseDate(dateString):
    if type(dateString) in [str, unicode]:            
        dt    = dateString.split('-')
        year  = int(dt[0])
        month = int(dt[1])
        day   = int(dt[2])
        return datetime.datetime(year, month, day, 0, 0, 0)

    return dateString



def deleteFile(filename, attempts = 5):
    while os.path.exists(filename) and (attempts > 0): 
        attempts -= 1
        try: 
            os.remove(filename) 
            break 
        except: 
            xbmc.sleep(100)


# -----------------------------------------------------------------------


def checkForUpdate(silent = 1):
    # silent = 0
    xbmcgui.Window(10000).setProperty('OTT_UPDATING', 'True')

    silent = int(silent) == 1

    response = getResponse()
    isValid  = len(response) > 0

    if not isValid:
        if not silent:
            ok(TITLE, '', 'No EPG update available.', 'Please try again later.')
        return allDone(silent)
   
    if updateAvailable(response['Date']):
        print '%s EPG Update Available - %s' % (TITLE, response['Date'])
        getUpdate(response, silent) 
   
    elif not silent:
        ok(TITLE, 'EPG is up-to-date.')

    allDone(silent)


def allDone(silent, mins = 1 * 60 * 12): #12 hours
    setAlarm(mins)

    xbmcgui.Window(10000).clearProperty('OTT_UPDATING')

    # if not silent:
    #     ADDON.openSettings() 


def setAlarm(mins):
    #set script to run again in x minutes

    updateMins = mins
    addonPath  = xbmc.translatePath(ADDON.getAddonInfo('path'))
    name       = TITLE + ' EPG Update'
    script     = os.path.join(addonPath, 'update.py')
    args       = '1' #silent
    cmd        = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, updateMins)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)        
    xbmc.executebuiltin(cmd)


def getResponse():
    try:
        url      = dixie.GetDixieUrl(DIXIEURL) + 'update.txt'
        request  = requests.get(url)
        response = request.text
    except:
        return []

    return json.loads(u"" + (response))


def updateAvailable(latest):
    dir = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    db  = os.path.join(dir, 'program.db')
    if not os.path.exists(db):
        return True

    current = ADDON.getSetting('epg.date')
    current = parseDate(current)
    latest  = parseDate(latest)
    update  = latest > current
    return update



def getUpdate(response, silent):
    try:
        link    = response['Link']
        md5     = response['MD5']
        date    = response['Date']
        channel = response['Channel']
    except Exception, e:
        return

    path = getDownloadPath(date)

    db = path.replace('.zip', '.db')
    if not os.path.exists(db):
        dp = None
    
        if not silent:
            dp = progress(TITLE, 'Updating EPG.', 'Please Wait.')

        try:
            download(link, path, dp)
        except:
            deleteFile(path) 
            return False        

        #doesn't seem to want to work!
        #if generateMD5(path) != md5:
        #    deleteFile(path) 
        #    return False

        zip = path
        dst = xbmc.translatePath(ADDON.getAddonInfo('profile'))

        import dxmnew
        dxmnew.unzipAndMove(zip, dst, None)

        try:    deleteFile(zip)
        except: pass

    dixie.SetSetting('updated.channels', channel)

    xbmcgui.Window(10000).setProperty('OTT_UPDATE', date)

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING') == 'True':
        return

    newEPGAvailable()

    if not silent:
        ok(TITLE, '', 'EPG successfully updated.', '')



def newEPGAvailable():
    date = xbmcgui.Window(10000).getProperty('OTT_UPDATE')

    dir = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    deleteFile(os.path.join(dir, 'program.db'))   

    dst = os.path.join(dir, 'program.db')
    src = os.path.join(dir, 'program-XXXXXX.db')
    src = src.replace('XXXXXX', date)

    try:    os.rename(src, dst)
    except: pass

    dixie.SetSetting('epg.date', date)

    xbmcgui.Window(10000).clearProperty('OTT_UPDATE')



def getDownloadPath(date):
    try:
        path = ADDON.getAddonInfo('profile')
        path = xbmc.translatePath(path)
        path = os.path.join(path, 'program-%s.zip' % date)
        return path
    except:
        pass
    return None



def download(url, dest, dp = None, start = 0, range = 100):    
    r = requests.get(url)
    with open(dest, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)


def _pbhook(numblocks, blocksize, filesize, dp, start, range, url=None):
    try:
        percent = min(start+((numblocks*blocksize*range)/filesize), start+range)
        dp.update(int(percent))
    except Exception, e:
        utils.log('%s Error Downloading Update' % str(e))
        percent = 100
        dp.update(int(percent))
    if dp.iscanceled(): 
        raise Exception('Canceled')



def doMain():
    if len(sys.argv) > 1:
        checkForUpdate(sys.argv[1])
    else:
        checkForUpdate(True) #silent


if __name__ == '__main__': 
    try:
        print '+++++++++++++ OnTapp.TV - Running EPG Update +++++++++++++'
        doMain()
    except:
        xbmcgui.Window(10000).clearProperty('OTT_UPDATE')    