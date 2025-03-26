#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by#  the Free Software Foundation; either version 2, or (at your option)
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
import xbmcgui
import os
import re
import datetime
import pickle
import json

import dixie
import sfile

home       = dixie.HOME
datapath   = dixie.PROFILE
extras     = os.path.join(datapath, 'extras')
logos      = os.path.join(extras,   'logos')
logofolder = os.path.join(logos,    'None')
logodest   = os.path.join(logos,    'logos.zip')


try:
    #workaround Python bug in strptime which causes it to intermittently throws an AttributeError
    import datetime, time
    datetime.datetime.fromtimestamp(time.mktime(time.strptime('2013-01-01 19:30:00'.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
except:
    pass


def generateMD5(path):
    if not sfile.exists(path):
        return '0'

    try:
        import hashlib
        return hashlib.md5(sfile.read(path)).hexdigest()
    except:
        pass

    try:
        import md5
        return md5.new(sfile.read(path)).hexdigest()
    except:
        pass

    return '0'



def parseDate(dateString):
    if type(dateString) in [str, unicode]:
        dt    = dateString.split('-')
        year  = int(dt[0])
        month = int(dt[1])
        day   = int(dt[2])
        return datetime.datetime(year, month, day, 0, 0, 0)

    return dateString



def deleteFile(filename, attempts = 5):
    while sfile.exists(filename) and (attempts > 0): 
        attempts -= 1
        try: 
            sfile.remove(filename) 
            break 
        except: 
            xbmc.sleep(100)


# -----------------------------------------------------------------------

def onBoot():
    return allDone(True, mins=30, ret=True)

    retry  = 12
    update = checkForUpdate(silent=True, addons=True)

    while (not xbmc.abortRequested) and (not update) and (retry > 0):
        dixie.log('Failed to checkForUpdate (%d) - Trying again in 5 seconds' % retry)
        xbmc.sleep(5000)
        retry -= 1
        update = checkForUpdate(silent=True, addons=True)

    dixie.log('onBoot returning %s' % str(update))
    return update


def checkForUpdate(silent=1, addons=True):
    #return
    # silent = 0 #switches on dialogs

    silent   = int(silent) == 1 #turn into a proper bool

    if not dixie.isInternetConnected(maxWait=30):
        if not silent:
            dixie.DialogOK('No internet connection', 'Please check your network and try again')
        return allDone(silent, mins=30, ret=False)

    if not dixie.GetUser() and not dixie.GetPass():
        return True #stops further retries

    if addons:
        cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/getIni.py)'
        #dixie.log('=== CF Check ini files ===')
        xbmc.executebuiltin(cmd)
    #extra debug check
    else:
        dixie.log('======== ADDONS FALSE =======')

    xbmcgui.Window(10000).setProperty('OTT_UPDATING', 'True')

    response = getResponse(silent)

    if 'Error' in response:
        if not silent:
            dixie.DialogOK('Oops! An error has occured: ', response['Error'], 'Please contact support or our Facebook Group')
        return allDone(silent, ret=False)

    isValid = len(response) > 0

    if not isValid:
        if not silent:
            dixie.DialogOK('', 'No EPG update available.', 'Please try again later.')
        return allDone(silent, ret=False)

    try:
        if updateAvailable(response['Date']):
            dixie.log ('EPG Update Available - %s' % response['Date'])
            getUpdate(response, silent)

        else:
            # do restore to ensure not malformed
            # restoreFromZip()
            if not silent:
                # pass
                dixie.DialogOK('EPG is up-to-date.')
    except:
        pass

    return allDone(silent, ret=True)

def allDone(silent, mins=1*60*48, ret=True): # 48 hours
    try:    setAlarm(mins)
    except: pass

    xbmcgui.Window(10000).clearProperty('OTT_UPDATING')

    # if not silent:
    #     ADDON.openSettings()

    return ret


def setAlarm(mins):
    #set script to run again in x minutes

    updateMins = mins
    addonPath  = home
    name       = dixie.TITLE + ' EPG Update'
    script     = os.path.join(addonPath, 'update.py')
    args       = '1' #silent
    cmd        = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, updateMins)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)
    xbmc.executebuiltin(cmd)
    dixie.log('OTTV update timer started')


def getResponse(silent=False):
    URL = dixie.GetDixieUrl() + 'update.txt'
    #dixie.log('=== OTTV Update Check ===')

    code, response = _getResponse(URL)

    if dixie.isCF(code):
        return {'Error' : 'Error while updating listings'}

    try:
        return json.loads(u"" + (response))

    except Exception, e:
        dixie.log(e)
        return {'Error' : e}


def _getResponse(URL):
    import session
    # session.getSession(silent=True)

    sess = session.loadSession()
    req  = sess.get(URL, verify=False)
    code = req.status_code

    #dixie.log('===== update _getResponse =====')
    #dixie.log(code)

    response = req.content
    #dixie.log(response)

    return code, response


def updateAvailable(latest):
    dir    = datapath
    folder = os.path.join(dir, 'channels')

    files = []
    try:    current, dirs, files = os.walk(folder).next()
    except: pass

    if len(files) == 0:
        dixie.SetSetting('updated.channels', -1) #force refresh of channels
        return True

    db = os.path.join(dir, 'program.db')
    if not sfile.exists(db):
        return True

    current = dixie.GetSetting('epg.date')
    current = parseDate(current)
    latest  = parseDate(latest)
    update  = latest > current
    return update


def getUpdate(response, silent):
    try:
        link     = response['Link']
        md5      = response['MD5']
        date     = response['Date']
        channel  = response['Channel']
    except Exception, e:
        return

    path = getDownloadPath(date)

    db = path.replace('.newzip', '.db')
    if not sfile.exists(db):
        dp = None

        if not silent:
            dp = dixie.Progress('Updating EPG.', 'Please Wait.')

        ok = False
        try:
            download(link, path, dp)
            ok = True
        except:
            ok = False

        if dp:
            dp.close()
 
        if not ok:
            deleteFile(path)
            return

        profile = datapath

        #delete existng zips/db files
        files = []
        try:    current, dirs, files = os.walk(profile).next()
        except: pass

        for file in files:
            if file.endswith('.zip'):
                deleteFile(os.path.join(profile, file))

            if file.startswith('program-') and file.endswith('.db'):
                deleteFile(os.path.join(profile, file))

        oldpath = path
        path    = path.replace('.newzip', '.zip')

        try:    sfile.rename(oldpath, path)
        except: pass

        #doesn't seem to want to work!
        #if generateMD5(path) != md5:
        #    deleteFile(path) 
        #    return False

        import extract
        extract.all(path, profile)

        from channel import ConfirmUpdate
        channelFolder = dixie.GetChannelFolder()
        #dixie.log('===== Check for updated channels =====')
        #dixie.log(channelFolder)
        ConfirmUpdate(channelFolder)

        #try:    deleteFile(path) #don't delete the zip file
        #except: pass

    dixie.SetSetting('updated.channels', channel)

    #xbmcgui.Window(10000).setProperty('OTT_UPDATE', date)

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING') == 'True':
        return

    src = os.path.join(datapath, 'program-XXXXXX.db')
    src = src.replace('XXXXXX', date)
    newEPGAvailable(src)

    #newEPGAvailable(date)

    #if not silent:
    #    dixie.DialogOK('', 'EPG successfully updated.', '')


def newEPGAvailable(filename):
    dst = os.path.join(datapath, 'program.db')

    deleteFile(dst)

    try:    sfile.rename(filename, dst)
    except: pass

    date = filename.split('-', 1)[-1].split('.', 1)[0]

    dixie.SetSetting('epg.date', date)


def getDownloadPath(date):
    try:
        path = datapath
        path = xbmc.translatePath(path)
        path = os.path.join(path, 'program-%s.newzip' % date)
        return path
    except:
        pass

    return None


def download(url, dest, dp=None, tries=0):
    #dixie.log('========== listings downloading ==========')
    #dixie.log('========== TRIES ==========')
    dixie.log(tries)

    #have we already downloaded and renamed this file?
    testDest = dest.replace('.newzip', '.zip')
    if sfile.exists(testDest):
        try:    sfile.rename(testDest, dest)
        except: pass

    if sfile.exists(dest):
        #dixie.log('========== listings already downloaded :) ==========')
        return

    import session
    try:
        #dixie.log('========== listings download - Loading Session ==========')
        s = session.loadSession()
        r = s.get(url, cookies=session.loadCookies(session.cookiefile), stream=True)
    except Exception, e:
        #dixie.log('******* LISTINGS EXCEPTION *******')
        dixie.log(e)

    code = r.status_code
    #dixie.log('========== download listings login code ==========')
    dixie.log(code)

    if dixie.isCF(code):
        #log('===== SERVER ISSUE: CF ACTIVE =====')
        return

    if code == 401: #unauthorized
        #dixie.log('******* 401: UNAUTHORIZED *******')
        if tries == 0:
            session.getSession(silent=True)
            return download(url, dest, dp, tries+1)

        if dixie.DialogYesNo('Failed to verify your credentials', 'Would you like to change them and retry?'):
            dixie.openSettings(focus=0.2)
            return download(url, dest, dp)

    if code != 200:
        #dixie.log('========== listings error ==========')
        content = r.content.replace('<strong>',  '').replace('</strong>', '')
        dixie.log(content)
        dixie.DialogOK('There was an error with the TV listings', 'Please contact our Facebook Page quoting the following error message:', '[COLOR orange][B]%s[/B][/COLOR]' % content)
        return

    try:
        length = int(r.headers['Content-Length'])
    except:
        length = 15000000
        dixie.log('Failed to get Content-Length - using default of %d' % length)

    chunkSize  = 512
    currLength = float(0)

    with open(dest, 'wb') as f:
        for chunk in r.iter_content(chunkSize):
            f.write(chunk)
            if dp:
                currLength += chunkSize
                percent     = currLength /  length * 100
                dp.update(int(percent))

    #dixie.log('========= listings downloaded =========')


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
