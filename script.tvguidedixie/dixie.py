#
#      Copyright (C) 2014 Richard Dean
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
import dixie
import verify
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import cookielib
import pickle
import time
import datetime


ADDONID     = 'script.tvguidedixie'
ADDON       =  xbmcaddon.Addon(ADDONID)
HOME        =  ADDON.getAddonInfo('path')
ICON        =  os.path.join(HOME, 'icon.png')
ICON        =  xbmc.translatePath(ICON)
PROFILE     =  xbmc.translatePath(ADDON.getAddonInfo('profile'))
RESOURCES   =  os.path.join(HOME, 'resources')

def SetSetting(param, value):
    if GetSetting(param) == value:
        return
    xbmcaddon.Addon(ADDONID).setSetting(param, str(value))


def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)

DIXIEURL    =  GetSetting('dixie.url').upper()
DIXIELOGOS  =  GetSetting('dixie.logo.folder')
SKIN        =  GetSetting('dixie.skin')
FILMON      =  GetSetting('FILMON')
VERSION     =  ADDON.getAddonInfo('version')
TITLE       = 'On-Tapp.EPG'
LOGOPACK    = 'Colour Logo Pack'
SKINVERSION = '25'
SKINZIP     = 'skins-03-08-2015.zip'
INIVERSION  = '1'
DEBUG       =  GetSetting('DEBUG') == 'true'

datapath   = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras     = os.path.join(datapath, 'extras')
logos      = os.path.join(extras,   'logos')
cookiepath = os.path.join(datapath, 'cookies')
cookiefile = os.path.join(cookiepath, 'cookie')


def log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def CloseBusy():
    xbmc.executebuiltin('Dialog.Close(busydialog)')


def ShowBusy(hideProgress=False):
    xbmc.executebuiltin('ActivateWindow(busydialog)')

    #try:
    #    busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
    #    busy.show()

    #    if hideProgress:
    #        try:    busy.getControl(10).setVisible(False)
    #        except: pass

    #    return busy
    #except:
    #    pass

    return None




def notify(message, length=5000):
    CloseBusy()
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)


ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
 t = ooOOOoo
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0  
 for c in t2:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t


baseurl   = ttTTtt(0,[104,244,116,66,116,68,112,168,115,206,58,5,47,99,47,49,119,205,119,250,119,63,46,15,111,225,110,222,45],[146,116,128,97,158,112,30,112,118,46,72,116,230,118,137,47,191,63,67,115,190,50,69,109,50,101,166,109,23,98,77,101,104,114,82,95,190,102,59,105,74,108,247,101,196,95,213,114,210,101,191,109,217,111,155,116,243,101,87,61,243,121,83,101,149,115,40,38,96,115,62,50,39,109,151,101,197,109,163,98,217,101,220,114,80,95,16,102,156,105,72,108,151,101,52,95,170,100,111,111,99,119,206,110,216,108,201,111,111,97,183,100,227,61,89,47,77,97,165,99,233,99,245,101,255,115,69,115,150,45,217,115,81,50,118,109,152,101,39,109,102,98,114,101,125,114,14,45,8,108,85,101,80,118,252,101,79,108,63,49,129,47])
resource  = ttTTtt(0,[104,229,116,71,116,131,112,130,115],[164,58,247,47,243,47,178,119,209,119,132,119,192,46,155,111,36,110,223,45,89,116,143,97,161,112,156,112,39,46,173,116,225,118,126,47,102,119,13,112,241,45,163,99,12,111,122,110,91,116,140,101,66,110,153,116,80,47,134,117,66,112,86,108,157,111,41,97,89,100,189,115,87,47])
loginurl  = ttTTtt(393,[72,104,176,116],[194,116,1,112,40,115,24,58,196,47,96,47,160,119,10,119,73,119,153,46,156,111,245,110,246,45,163,116,51,97,57,112,60,112,217,46,1,116,38,118,110,47,202,119,147,112,232,45,135,108,73,111,70,103,215,105,209,110,244,46,121,112,128,104,196,112])
verifyurl = ttTTtt(211,[136,104,34,116,82,116,10,112,216,115,105,58,30,47,240,47,201,111,178,110,160,45],[121,116,0,97,232,112,168,112,107,46,147,116,137,118,134,47,9,118,43,101,218,114,147,105,8,102,130,121,253,47,127,105,138,110,242,100,123,101,139,120,232,46,154,112,251,104,194,112])

def GetDixieUrl(DIXIEURL):
    if DIXIEURL == 'ALL CHANNELS':
        return baseurl + 'all/'

    if DIXIEURL == 'GVAX':
        return baseurl + 'gvax/'


def GetExtraUrl():
    return resource


def GetLoginUrl():
    return loginurl


def GetVerifyUrl():
    return verifyurl


def GetGMTOffset():
    gmt = GetSetting('gmtfrom').replace('GMT', '')

    if gmt == '':
        offset = 0
    else:
        offset = int(gmt)

    return datetime.timedelta(hours = offset)


def saveCookies(requests_cookiejar, filename):
    if not os.path.isfile(cookiefile):
        try: os.makedirs(cookiepath)
        except: pass

    with open(cookiefile, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def loadCookies(filename):
    if not os.path.isfile(cookiefile):
        try: os.makedirs(cookiepath)
        except: pass
        
        open(cookiefile, 'a').close()
        
    try:
        with open(cookiefile, 'rb') as f:
            return pickle.load(f)
    except: pass
        
    return ''


def resetCookies():
    try:
        if os.path.isfile(cookiefile):
            os.remove(cookiefile)
    except: pass


def BackupChannels():
    import shutil
    src = os.path.join(datapath, 'channels')
    dst = os.path.join(datapath, 'channels-backup')
    
    try:    shutil.rmtree(dst)
    except: pass
    
    try:    shutil.copytree(src, dst)
    except: pass


def CheckUsername():
    if GetSetting('username') != '' and GetSetting('password') != '':
        return True

    dlg = DialogYesNo('On-Tapp.TV requires a subscription.', '', 'Would you like to enter your account details now?')

    if dlg == 1:
        username = DialogKB('', 'Enter Your On-Tapp.TV Username')
        SetSetting('username', username)

        password = DialogKB('', 'Enter Your On-Tapp.TV Password')
        SetSetting('password', password)
        
        verify.CheckCredentials()
        
        # ShowSettings()
        # xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.tvguidedixie/openSettings.py)')

    return False


def ShowSettings():
    ADDON.openSettings()


def getPreviousTime():
    time_object = dixie.GetSetting('LOGIN_TIME')
    
    if time_object == '':
        time_object = '2001-01-01 00:00:00'
        
    previousTime = parseTime(time_object)
    
    return previousTime


def parseTime(when):
    if type(when) in [str, unicode]:
        dt = when.split(' ')
        d  = dt[0]
        t  = dt[1]
        ds = d.split('-')
        ts = t.split(':')
        when = datetime.datetime(int(ds[0]), int(ds[1]) ,int(ds[2]), int(ts[0]), int(ts[1]), int(ts[2].split('.')[0]))
        
    return when


def validToRun(silent=False):
    previousTime = getPreviousTime()
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    
    if nSeconds > 45 * 60:        
        if not doLogin(silent):
            return False

        dixie.SetSetting('LOGIN_TIME', str(now))
        
    return True


def doLogin(silent=False):
    log ('************ On-Tapp.EPG Login ************')
    with requests.Session() as s:
        try:
            s.get(GetLoginUrl())
        except: 
            #Rich, you might want to log something here???
            return False
            
        PAYLOAD  = { 'log' : GetSetting('username'), 'pwd' : GetSetting('password'), 'wp-submit' : 'Log In' }
        response = 'login_error'
        code     =  0
        
        if GetSetting('username') and GetSetting('password'):
            login    = s.post(GetLoginUrl(), data=PAYLOAD)
            response = login.content
            code     = login.status_code
            saveCookies(s.cookies, cookiefile)
            
        if 'no-access-redirect' in response:
            error   = '301 - No Access.'
            message = 'It appears that your subscription has expired.'
            log(message + ' : ' + error)
            if not silent:
                DialogOK(message, error, 'Please check your account at www.on-tapp.tv')
            return False
            
        areLost    = 'Are you lost' in response
        loginError = 'login_error' in response
        okay       =  (not areLost) and (not loginError)
        
        if okay:
            message = 'Logged into On-Tapp.TV'
            log(message)
            if not silent:
                notify(message)
            return True
            
        try:
            error = re.compile('<div id="login_error">(.+?)<br />').search(response).groups(1)[0]
            error = error.replace('<strong>',  '')
            error = error.replace('</strong>', '')
            error = error.replace('<a href="https://www.on-tapp.tv/wp-login.php?action=lostpassword">Lost your password?</a>', '')
            error = error.strip()
        except:
            error = ''
        
        message = 'There was a problem logging into On-Tapp.TV.'
        log(message + ' : ' + error)
        if not silent:
            DialogOK(message, error, 'Please check your account at www.on-tapp.tv')
        return False


def GetCats():
    path = os.path.join(PROFILE, 'cats.xml')


def GetChannels():
    path = os.path.join(PROFILE , 'chan.xml')

    return path


def CheckLogos():
    logofolder = os.path.join(logos, 'None')

    if not os.path.exists(logofolder):
        os.makedirs(logofolder)


def DownloadLogos():
    import download
    import extract
    
    logofolder  = os.path.join(logos, 'None')
    logodest    = os.path.join(logos, 'logos.zip')
    
    url  = dixie.GetExtraUrl() + 'resources/logos.zip'

    try:
        os.makedirs(logofolder)
    except:
        pass

    download.download(url, logodest)
    
    if os.path.exists(logos):
        now  = datetime.datetime.now()
        date = now.strftime('%B-%d-%Y %H-%M')
    
        import shutil
        cur = dixie.GetSetting('dixie.logo.folder')
        src = os.path.join(logos, cur)
        dst = os.path.join(logos, cur+'-%s' % date)
    
        try:
            shutil.copytree(src, dst)
            shutil.rmtree(src)
        except:
            pass
        
        extract.all(logodest, extras)
        dixie.SetSetting('dixie.logo.folder', LOGOPACK)

    try:
        os.remove(logodest)
    except:
        pass


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)


def DialogKB(value = '', heading = ''):
    kb = xbmc.Keyboard('', '')
    kb.setHeading(heading)
    kb.doModal()
    if (kb.isConfirmed()):
        value = kb.getText()
    return value


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def Progress(line1 = '', line2 = '', line3 = '', hide = False):
    dp = xbmcgui.DialogProgress()
    dp.create(TITLE, line1, line2, line3)
    dp.update(0)

    if hide:
        try:
            xbmc.sleep(250)
            WINDOW_PROGRESS = xbmcgui.Window(10101)
            CANCEL_BUTTON   = WINDOW_PROGRESS.getControl(10)
            CANCEL_BUTTON.setVisible(False)
        except:
            pass

    return dp


def DeleteFile(path):
    tries = 5
    while os.path.exists(path) and tries > 0:
        tries -= 1 
        try: 
            os.remove(path) 
            break 
        except: 
            xbmc.sleep(500)
