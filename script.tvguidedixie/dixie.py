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
import requests
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
    xbmcaddon.Addon(ADDONID).setSetting(param, str(value))


def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)

DIXIEURL    =  GetSetting('dixie.url').upper()
DIXIELOGOS  =  GetSetting('dixie.logo.folder')
SKIN        =  GetSetting('dixie.skin')
FILMON      =  GetSetting('FILMON')
VERSION     =  ADDON.getAddonInfo('version')
TITLE       = 'OnTapp.TV'
SKINVERSION = '15'
INIVERSION  = '1'
DEBUG       = GetSetting('DEBUG') == 'true'

datapath   = xbmc.translatePath(ADDON.getAddonInfo('profile'))
cookiepath = os.path.join(datapath, 'cookies')
cookiefile = os.path.join(cookiepath, 'cookie')

if not os.path.exists(cookiepath):
    os.makedirs(cookiepath)


def log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def notify(message, length=5000):
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


baseurl  = ttTTtt(0,[104],[128,116,233,116,39,112,137,58,87,47,190,47,150,119,9,119,172,119,212,46,41,111,17,110,181,45,46,116,32,97,122,112,209,112,193,46,150,116,127,118,118,47,127,63,244,115,228,50,178,109,40,101,249,109,151,98,205,101,83,114,65,95,94,102,136,105,63,108,54,101,233,95,107,114,94,101,225,109,165,111,97,116,44,101,95,61,219,121,239,101,144,115,133,38,245,115,175,50,161,109,51,101,118,109,123,98,207,101,30,114,245,95,246,102,250,105,133,108,40,101,20,95,100,100,210,111,90,119,255,110,98,108,109,111,55,97,77,100,19,61,183,47,8,97,101,99,40,99,176,101,217,115,130,115,63,45,170,115,1,50,233,109,146,101,146,109,76,98,119,101,217,114,140,45,68,108,196,101,236,118,58,101,205,108,95,49,49,47])
resource = ttTTtt(780,[190,104,148,116,210,116,205,112],[191,58,177,47,147,47,90,119,222,119,146,119,115,46,212,111,185,110,224,45,4,116,112,97,179,112,138,112,63,46,246,116,183,118,57,47,129,119,107,112,19,45,208,99,252,111,242,110,143,116,79,101,182,110,134,116,127,47,236,117,22,112,36,108,120,111,61,97,57,100,174,115,186,47])
loginurl = ttTTtt(405,[214,104,237,116,83,116,218,112,124,58,69,47,167,47],[81,119,8,119,207,119,155,46,158,111,222,110,18,45,225,116,76,97,104,112,70,112,228,46,44,116,205,118,254,47,48,119,39,112,128,45,209,108,156,111,112,103,129,105,123,110,174,46,118,112,99,104,151,112])


def GetDixieUrl(DIXIEURL):
    if DIXIEURL == 'ALL CHANNELS':
        return baseurl + 'all/'


def GetExtraUrl():
    return resource


def GetLoginUrl():
    return loginurl


def GetGMTOffset():
    gmt = GetSetting('gmtfrom').replace('GMT', '')

    if gmt == '':
        offset = 0
    else:
        offset = int(gmt)

    return datetime.timedelta(hours = offset)


def saveCookies(requests_cookiejar, filename):
    with open(cookiefile, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def loadCookies(filename):
    if not os.path.isfile(cookiefile):
        os.makedirs(cookiepath)
        open(cookiefile, 'a').close
        
    with open(cookiefile, 'rb') as f:
        return pickle.load(f)


def resetCookies():
    try:
        if os.path.isfile(cookiefile):
            os.remove(cookiefile)
    except: pass



def getPreviousTime():
    time_object = xbmcgui.Window(10000).getProperty('OTT_LOGIN_TIME')
    
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
    
    if nSeconds > 35 * 60:        
        if not doLogin(silent):
            return False

        xbmcgui.Window(10000).setProperty('OTT_LOGIN_TIME', str(now))
        
    return True


def doLogin(silent=False):
    log ('************ On-Tapp.TV Login ************')
    with requests.Session() as s:
        try:    s.get(GetLoginUrl())
        except: return False

        USERNAME    =  GetSetting('username')
        PASSWORD    =  GetSetting('password')
        PAYLOAD     =  { 'log' : USERNAME, 'pwd' : PASSWORD, 'wp-submit' : 'Log In' }

        code = 'login_error'

        if USERNAME and PASSWORD:        
            login = s.post(GetLoginUrl(), data=PAYLOAD)
            code  = login.content
            saveCookies(s.cookies, cookiefile)
        
        if ('Are you lost' not in code) and ('login_error' not in code):
            message = 'Logged into On-Tapp.TV'
            log(message)
            if not silent:
                notify(message)
            
            return True
            
        try:
            error = re.compile('<div id="login_error">(.+?)<br />').search(code).groups(1)[0]
            error = error.replace('<strong>',  '')
            error = error.replace('</strong>', '')
            error = error.replace('<a href="http://www.on-tapp.tv/wp-login.php?action=lostpassword">Lost your password</a>?', '')
            error = error.strip()
        except:
            error = ''

        message = 'There was a problem logging into On-Tapp.TV.'
        #notify(message)
        log(message + ' : ' + error)
        if not silent:
            DialogOK(message, '', error)
        
        return False


def GetCats():
    import urllib

    path = os.path.join(PROFILE, 'cats.xml')
    url  = GetExtraUrl() + 'resources/cats.xml'

    try:
        urllib.urlretrieve(url, path)
    except:
        pass


def GetChannels():
    path = os.path.join(PROFILE , 'chan.xml')
    url  = GetDixieUrl(DIXIEURL) + 'chan.xml'

    r = requests.get(url, cookies=loadCookies(cookiefile))
    
    with open(path, 'wb') as f:
        for chunk in r.iter_content(512):
            f.write(chunk)

    return path


def ShowBusy(hideProgress=True):
    try:
        busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        busy.show()

        if hideProgress:
            try:    busy.getControl(10).setVisible(False)
            except: pass

        return busy
    except:
        pass

    return None



def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)


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
