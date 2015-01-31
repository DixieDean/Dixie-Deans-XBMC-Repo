#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
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
import re
import datetime
import urllib2
import urllib
import requests
import json

import dixie

ADDON    = xbmcaddon.Addon(id = 'script.tvguidedixie')
TITLE    = ADDON.getAddonInfo('name')
DIXIEURL = ADDON.getSetting('dixie.url').upper()
username = ADDON.getSetting('username')
password = ADDON.getSetting('password')
response = ''

datapath   = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookiepath = os.path.join(datapath, 'cookies')
cookiefile = os.path.join(cookiepath, 'cookie')

if not os.path.exists(cookiepath):
    os.makedirs(cookiepath)

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



#def ok(title, line1, line2 = '', line3 = ''):
#    dlg = xbmcgui.Dialog()
#    dlg.ok(title, line1, line2, line3)



#def yesno(title, line1, line2 = '', line3 = '', no = 'No', yes = 'Yes'):
#    dlg = xbmcgui.Dialog()
#    return dlg.yesno(title, line1, line2, line3, no, yes) == 1



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

def onBoot():
    dixie.log('onBoot')
    retry  = 12
    update = checkForUpdate(silent=True)

    while (not xbmc.abortRequested) and (not update) and (retry > 0):
        xbmc.sleep(5000)
        dixie.log('Failed to checkForUpdate (%d) - Trying again in 5 seconds' % retry)
        retry -= 1
        update = checkForUpdate(silent=True)

    dixie.log('onBoot returning %s' % str(update))
    return update


def checkForUpdate(silent = 1):
    # silent = 0
    xbmcgui.Window(10000).setProperty('OTT_UPDATING', 'True')

    silent = int(silent) == 1

    response = getResponse(silent)
    
    if 'Error' in response:
        if not silent:
            ok(TITLE, 'There was a problem: ', response['Error'], '')
        
        allDone(silent)
        return False
        
    isValid  = len(response) > 0

    if not isValid:
        if not silent:
            ok(TITLE, '', 'No EPG update available.', 'Please try again later.')
        allDone(silent)
        return False
   
    try:
        if updateAvailable(response['Date']):
            dixie.log ('%s EPG Update Available - %s' % (TITLE, response['Date']))
            getUpdate(response, silent)

        else:
            #do restore to ensure not malformed
            restoreFromZip()
            if not silent:
                ok(TITLE, 'EPG is up-to-date.')

    except:
        pass

    allDone(silent)
    return True


def allDone(silent, mins = 1 * 60 * 24): #24 hours
    try:    setAlarm(mins)
    except: pass

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


def getResponse(silent=False):
    if not dixie.validToRun(silent):
        return {'Error' : 'Failed to obtain a valid response from On-Tapp.TV'}

    url      = dixie.GetDixieUrl(DIXIEURL) + 'update.txt'
    request  = requests.get(url, allow_redirects=False, cookies=dixie.loadCookies(cookiefile))
    code     = request.status_code
    response = request.content

    if not code == 200:
        response = re.sub('<(.+?)>', '', response)
        response = response.replace('<strong>',  '')
        response = response.replace('</strong>', '')
        dixie.log ('OTT status_code %s ' % code)
        dixie.log ('OTT response %s ' % response)
        
        return {'Error' : response}

    return json.loads(u"" + (response))


# def getResponse():
#     url      = dixie.GetDixieUrl(DIXIEURL) + 'update.txt'
#     request  = requests.get(url, cookies=dixie.loadCookies(cookiefile))
#     code     = request.status_code
#     response = request.content
#
#     if not code == 200:
#         response = re.sub('<(.+?)>', '', response)
#         return {'Error' : response}
#
#     return json.loads(u"" + (response))


def updateAvailable(latest):
    dir    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    folder = os.path.join(dir, 'channels')

    files = []
    try:    current, dirs, files = os.walk(folder).next()
    except: pass

    if len(files) == 0:
        dixie.SetSetting('updated.channels', -1) #force refresh of channels
        return True

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

    db = path.replace('.newzip', '.db')
    if not os.path.exists(db):
        dp = None
    
        if not silent:
            dp = progress(TITLE, 'Updating EPG.', 'Please Wait.')        

        try:
            download(link, path, dp)
        except:
            deleteFile(path) 
            return False  

        profile = xbmc.translatePath(ADDON.getAddonInfo('profile'))

        #delete existng zips files
        file = []
        try:    current, dirs, files = os.walk(profile).next()
        except: pass

        for file in files:
            if file.endswith('.zip'):
                filename = os.path.join(profile, file)
                deleteFile(filename)

        oldpath = path
        path    = path.replace('.newzip', '.zip')

        try:    os.rename(oldpath, path)
        except: pass

        #doesn't seem to want to work!
        #if generateMD5(path) != md5:
        #    deleteFile(path) 
        #    return False

        import dxmnew
        dxmnew.unzipAndMove(path, profile, None)

        #try:    deleteFile(path)
        #except: pass

    dixie.SetSetting('updated.channels', channel)

    #xbmcgui.Window(10000).setProperty('OTT_UPDATE', date)

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING') == 'True':
        return

    newEPGAvailable(date)

    if not silent:
        ok(TITLE, '', 'EPG successfully updated.', '')


def restoreFromZip():
    profile = xbmc.translatePath(ADDON.getAddonInfo('profile'))

    file = []
    try:    current, dirs, files = os.walk(profile).next()
    except: pass

    for file in files:
        if file.endswith('.zip'):
            date = file.split('-', 1)[-1].replace('.zip', '')

            import dxmnew
            dxmnew.unzipAndMove(os.path.join(profile, file), profile, None)

            newEPGAvailable(date)
            return


def newEPGAvailable(date):
    dir = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    deleteFile(os.path.join(dir, 'program.db'))   

    dst = os.path.join(dir, 'program.db')
    src = os.path.join(dir, 'program-XXXXXX.db')
    src = src.replace('XXXXXX', date)

    try:    os.rename(src, dst)
    except: pass

    dixie.SetSetting('epg.date', date)

    #xbmcgui.Window(10000).clearProperty('OTT_UPDATE')



def getDownloadPath(date):
    try:
        path = ADDON.getAddonInfo('profile')
        path = xbmc.translatePath(path)
        path = os.path.join(path, 'program-%s.newzip' % date)
        return path
    except:
        pass
        
    return None



def download(url, dest, dp = None, start = 0, range = 100):    
    r = requests.get(url, cookies=dixie.loadCookies(cookiefile))

    with open(dest, 'wb') as f:
        for chunk in r.iter_content(512):
            f.write(chunk)

        return


def _pbhook(numblocks, blocksize, filesize, dp, start, range, url=None):
    try:
        percent = min(start+((numblocks*blocksize*range)/filesize), start+range)
        dp.update(int(percent))
    except Exception, e:
        dixie.log('%s Error Downloading Update' % str(e))
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
        doMain()
    except:
        xbmcgui.Window(10000).clearProperty('OTT_UPDATE')