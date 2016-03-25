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
import verify
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import cookielib
import pickle
import time
import datetime

import sfile

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


ADDONID     = 'script.tvguidedixie'
ADDON       =  xbmcaddon.Addon(ADDONID)
HOME        =  ADDON.getAddonInfo('path')
ICON        =  os.path.join(HOME, 'icon.png')
ICON        =  xbmc.translatePath(ICON)
PROFILE     =  xbmc.translatePath(ADDON.getAddonInfo('profile'))
RESOURCES   =  os.path.join(HOME, 'resources')
PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True

OTT_ADDONID = 'script.on-tapp.tv'
OTT_ADDON   =  xbmcaddon.Addon(OTT_ADDONID)
OTT_HOME    =  xbmc.translatePath(OTT_ADDON.getAddonInfo('path'))
OTT_PROFILE =  xbmc.translatePath(OTT_ADDON.getAddonInfo('profile'))

resource    = 'http://files.on-tapp-networks.com/'
baseurl     =  ttTTtt(0,[104,244,116,66,116,68,112,168,115,206,58,5,47,99,47,49,119,205,119,250,119,63,46,15,111,225,110,222,45],[146,116,128,97,158,112,30,112,118,46,72,116,230,118,137,47,191,63,67,115,190,50,69,109,50,101,166,109,23,98,77,101,104,114,82,95,190,102,59,105,74,108,247,101,196,95,213,114,210,101,191,109,217,111,155,116,243,101,87,61,243,121,83,101,149,115,40,38,96,115,62,50,39,109,151,101,197,109,163,98,217,101,220,114,80,95,16,102,156,105,72,108,151,101,52,95,170,100,111,111,99,119,206,110,216,108,201,111,111,97,183,100,227,61,89,47,77,97,165,99,233,99,245,101,255,115,69,115,150,45,217,115,81,50,118,109,152,101,39,109,102,98,114,101,125,114,14,45,8,108,85,101,80,118,252,101,79,108,63,49,129,47])
loginurl    =  ttTTtt(393,[72,104,176,116],[194,116,1,112,40,115,24,58,196,47,96,47,160,119,10,119,73,119,153,46,156,111,245,110,246,45,163,116,51,97,57,112,60,112,217,46,1,116,38,118,110,47,202,119,147,112,232,45,135,108,73,111,70,103,215,105,209,110,244,46,121,112,128,104,196,112])
verifyurl   =  ttTTtt(211,[136,104,34,116,82,116,10,112,216,115,105,58,30,47,240,47,201,111,178,110,160,45],[121,116,0,97,232,112,168,112,107,46,147,116,137,118,134,47,9,118,43,101,218,114,147,105,8,102,130,121,253,47,127,105,138,110,242,100,123,101,139,120,232,46,154,112,251,104,194,112])

try:
    DSFID   =  ttTTtt(0,[112,13,108,120,117],[115,103,45,105,212,110,32,46,233,118,53,105,75,100,34,101,38,111,148,46,218,103,216,118,30,97,110,120])
    DSF     =  xbmcaddon.Addon(DSFID)
    DSFVER  =  DSF.getAddonInfo('version')
except: pass


def SetSetting(param, value):
    value = str(value)

    if GetSetting(param) == value:
        return

    xbmcaddon.Addon(ADDONID).setSetting(param, value)


def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


def GetXBMCVersion():
    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor eg, 13.9.902


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)


DIXIELOGOS  =  GetSetting('dixie.logo.folder')
SKIN        =  GetSetting('dixie.skin')
FILMON      =  GetSetting('FILMON')
VERSION     =  ADDON.getAddonInfo('version')
TITLE       = 'On-Tapp.EPG'
LOGOPACK    = 'Colour Logo Pack'
DEBUG       =  GetSetting('DEBUG') == 'true'
KEYMAP_HOT  = 'ottv_hot.xml'
ADULT       = 'Adultos'

datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras      = os.path.join(datapath, 'extras')
logos       = os.path.join(extras,   'logos')
cookiepath  = os.path.join(datapath, 'cookies')
cookiefile  = os.path.join(cookiepath, 'cookie')


def log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def migrateDSF():
    try:
        if getDSFVersion() > 102:
            return

        DialogOK('A new GVAx system update is available.', 'It will now be downloaded and installed on your device.', 'One moment please.')

        DSFHOME  =  DSF.getAddonInfo('path')
        DSFZIP   =  os.path.join(DSFHOME, 'DSF.zip')
        DSFURL   = 'http://files.on-tapp-networks.com/migrate/DSF.zip'

        SKINID   = 'skin.bello-dsf'
        SKIN     =  xbmcaddon.Addon(SKINID) # forked bello version: 3.0.8
        SKINHOME =  SKIN.getAddonInfo('path')
        SCRIPTS  =  os.path.join(SKINHOME, 'scripts')
        SCRPTZIP =  os.path.join(SCRIPTS,  'scripts.zip')
        SCRPTURL = 'http://files.on-tapp-networks.com/migrate/scripts.zip'

        LOGOZIP  =  os.path.join(extras,  'logos.zip')
        LOGOURL  =  'http://files.on-tapp-networks.com/migrate/logos.zip'

        if not sfile.exists(DSFHOME):
            sfile.makedirs(DSFHOME)

        if not sfile.exists(SCRIPTS):
            sfile.makedirs(SCRIPTS)

        import download
        import extract

        download.download(DSFURL, DSFZIP)
        extract.all(DSFZIP, DSFHOME)
        sfile.remove(DSFZIP)
        xbmc.executebuiltin('UpdateLocalAddons')
        DSF.setSetting('GVAX-REGION', '1')

        download.download(SCRPTURL, SCRPTZIP)
        extract.all(SCRPTZIP, SCRIPTS)
        sfile.remove(SCRPTZIP)

        sfile.rmtree(logos)
        download.download(LOGOURL, LOGOZIP)
        extract.all(LOGOZIP, extras)
        sfile.remove(LOGOZIP)

        chandir = os.path.join(datapath, 'channels')
        chanxml = os.path.join(datapath, 'chan.xml')
        catsxml = os.path.join(datapath, 'cats.xml')

        if sfile.exists(chandir):
            sfile.rmtree(chandir)
        sfile.remove(chanxml)
        sfile.remove(catsxml)

        import settings
        settingsFile = xbmc.translatePath(os.path.join(PROFILE, 'settings.cfg'))
        settings.set('ChannelsUpdated', 0, settingsFile)

        db = os.path.join(PROFILE, 'program.db')
        os.remove(db)
        SetSetting('epg.date', '2000-01-01')

        import sys
        sys.path.insert(0, DSFHOME)

        import gvax
        xml      = gvax.getCatsXML()
        filename = os.path.join(datapath, 'cats.xml')

        f = file(filename, 'w')
        f.write(xml)
        f.close()

        xml      = gvax.getChannelsXML()
        filename = os.path.join(datapath, 'chan.xml')

        f = file(filename, 'w')
        f.write(xml)
        f.close()

        xbmc.executebuiltin('RunScript(special://home/addons/script.tvguidedixie/deleteDB.py)')

        log('-- DSF Migrated --')
        DialogOK('The GVAx update is now completed.', 'Please reboot your set-top box.', 'Thank you.')
    except: pass


def getDSFVersion():
    try:
        version = int(DSFVER.replace('.', ''))
        return version
    except:
        version = 999
        return version


def isProtected():
    try:
        protected = DSF.getSetting('PROTECTED') == 'true'
        return protected
    except: pass


def isLimited():
    return xbmcgui.Window(10000).getProperty('DSF_LIMITED').lower() == 'true'


def getCategories():
    if isLimited():
        return ['Ni%C3%B1os']

    return GetSetting('categories').split('|')


def getCategoryList(path):
    import StringIO
    from xml.etree import ElementTree

    xml  = None
    cat  = dict()
    try:
        if sfile.exists(path):
            xml = sfile.read(path)
    except:
        pass

    if not xml:
        return {}

    xml = StringIO.StringIO(xml)
    xml = ElementTree.iterparse(xml, events=("start", "end"))

    for event, elem in xml:
        try:
            if event == 'end':
               if elem.tag == 'cats':
                   channel  = elem.findtext('channel')
                   category = elem.findtext('category')
                   if channel != '' and category != '':
                       cat[channel] = category
        except:
            pass

    return cat


def CloseBusy():
    try: xbmc.executebuiltin('Dialog.Close(busydialog)')
    except: pass

def ShowBusy():
    try: xbmc.executebuiltin('ActivateWindow(busydialog)')
    except: pass

    return None


def notify(message, length=5000):
    # CloseBusy()
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)


def loadKepmap():
    try:
        file = 'zOTT_Keymap.xml'
        src  = os.path.join(HOME, 'resources', file)
        dst  = os.path.join('special://profile/keymaps', file)

        if not sfile.exists(dst):
            sfile.copy(src, dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def removeKepmap():
    try:
        file = 'zOTT_Keymap.xml'
        dst  = os.path.join('special://profile/keymaps', file)

        if sfile.exists(dst):
            sfile.remove(dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def patchSkins():
    skinPath = os.path.join(extras, 'skins')

    srcImage = os.path.join(RESOURCES, 'changer.png')
    srcFile  = os.path.join(RESOURCES, 'script-tvguide-changer.xml')

    current, dirs, files = sfile.walk(skinPath)

    for dir in dirs:
        dstImage = os.path.join(current, dir, 'resources', 'skins', 'Default', 'media', 'changer.png')
        dstFile  = os.path.join(current, dir, 'resources', 'skins', 'Default', '720p', 'script-tvguide-changer.xml')

        sfile.copy(srcImage, dstImage, overWrite=False)
        sfile.copy(srcFile,  dstFile,  overWrite=False)


def WriteKeymap(start, end):
    filename = os.path.join('special://profile/keymaps', 'zOTT_hotkey.xml')
    theFile  = sfile.file(filename, 'w')
    cmd      = '\t\t\t<%s>XBMC.RunScript(special://home/addons/script.tvguidedixie/hotkey.py)</%s>\n'  % (start, end)

    theFile.write('<keymap>\n')
    theFile.write('\t<global>\n')
    theFile.write('\t\t<keyboard>\n')

    theFile.write(cmd)

    theFile.write('\t\t</keyboard>\n')
    theFile.write('\n')
    theFile.write('\t\t<remote>\n')

    theFile.write(cmd)

    theFile.write('\t\t</remote>\n')
    theFile.write('\t</global>\n')
    theFile.write('</keymap>\n')

    theFile.close()

    return True


def WriteFSKeymap(start, end):
    filename = os.path.join('special://profile/keymaps', 'zOTT_toggle.xml')
    theFile  = sfile.file(filename, 'w')
    cmd      = '\t\t\t<%s>fullscreen</%s>\n'  % (start, end)

    theFile.write('<keymap>\n')
    theFile.write('\t<global>\n')
    theFile.write('\t\t<keyboard>\n')

    theFile.write(cmd)

    theFile.write('\t\t</keyboard>\n')
    theFile.write('\n')
    theFile.write('\t\t<remote>\n')

    theFile.write(cmd)

    theFile.write('\t\t</remote>\n')
    theFile.write('\t</global>\n')
    theFile.write('</keymap>\n')

    theFile.close()

    return True


def GetDixieUrl():
    if isDSF():
        if getSubSystem() == '80906':
            return baseurl + 'swi/'

        if getSubSystem() == '348821':
            return baseurl + 'spa/'

        if getSubSystem() == 'xxxxxxx':
            return baseurl + 'ita/'

    return baseurl + 'all/'


def getSubSystem():
    return DSF.getSetting('GVAX-SUBSYS')


def GetKey():
    if isDSF():
        return 'OTHER'

    return 'ALL CHANNELS'


def isDSF():
    if xbmc.getCondVisibility('System.HasAddon(%s)' % DSFID) == 1:
        log(DSFID)
        return True

    return False


def GetExtraUrl():
    return resource


def GetLoginUrl():
    return loginurl


def GetVerifyUrl():
    return verifyurl


def GetChannelType():
    return GetSetting('chan.type')


def GetChannelFolder():
    CUSTOM = '1'

    channelType = GetChannelType()

    if channelType == CUSTOM:
        path = GetSetting('user.chan.folder')
        MigrateChannels(path)
    else:
        path = datapath

    return path


def GetGMTOffset():
    # gmt = GetSetting('gmtfrom').replace('GMT', '')
    #
    # if gmt == '':
    #     offset = 0
    # else:
    #     offset = int(gmt)
    
    offset = 0
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
    datapath = GetChannelFolder()

    src = os.path.join(datapath, 'channels')
    dst = os.path.join(datapath, 'channels-backup')

    try:    sfile.rmtree(dst)
    except: pass

    try:    sfile.copytree(src, dst)
    except: pass


def BackupCats():
    currcat = os.path.join(PROFILE, 'cats.xml')
    bakcat  = os.path.join(PROFILE, 'cats-bak.xml')

    try:    sfile.copy(currcat, bakcat)
    except: pass


def MigrateChannels(dst):
    dst = os.path.join(dst, 'channels')
    src = os.path.join(datapath, 'channels')

    if not sfile.exists(dst):
        try:    sfile.copytree(src, dst)
        except: pass


def CheckUsername():
    if GetUser() != '' and GetPass() != '':
        return True

    if DialogYesNo('On-Tapp.TV requires a subscription.', '', 'Would you like to enter your account details now?'):
        username = DialogKB('', 'Enter Your On-Tapp.TV Username')
        if isDSF():
            xbmcaddon.Addon(DSFID).setSetting('username', username)
        else:
            SetSetting('username', username)

        password = DialogKB('', 'Enter Your On-Tapp.TV Password')
        if isDSF():
            xbmcaddon.Addon(DSFID).setSetting('password', password)
        else:
            SetSetting('password', password)
        
        verify.CheckCredentials()

    return False


def ShowSettings():
    ADDON.openSettings()


def getPreviousTime(setting):
    try:
        time_object = GetSetting(setting)
        previousTime = parseTime(time_object)
    
        return previousTime
    
    except:
        time_object  = '2001-01-01 00:00:00'
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


def validTime(setting, maxAge):
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    
    return nSeconds <= maxAge


def validToRun(silent=False):
    setting      = 'LOGIN_TIME'
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    
    if nSeconds > 45 * 60:        
        if not doLogin(silent):
            return False

        SetSetting('LOGIN_TIME', str(now))
        
    return True


def doLogin(silent=False):
    log ('************ On-Tapp.EPG Login ************')
    with requests.Session() as s:
        try:
            s.get(GetLoginUrl(), verify=False)
        except: 
            #Rich, you might want to log something here???
            return False
            
        PAYLOAD  = { 'log' : GetUser(), 'pwd' : GetPass(), 'wp-submit' : 'Log In' }
        response = 'login_error'
        code     =  0
        
        if GetUser() and GetPass():
            login    = s.post(GetLoginUrl(), data=PAYLOAD, verify=False)
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
            # if not silent:
            #     notify(message)
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


def GetUser():
    if isDSF():
       username = xbmcaddon.Addon(DSFID).getSetting('username')
       return username

    username = GetSetting('username')
    return username
    

def GetPass():
    if isDSF():
       password = xbmcaddon.Addon(DSFID).getSetting('password')
       return password

    password = GetSetting('password')
    return password

    
def GetCats():
    path = os.path.join(PROFILE, 'cats.xml')


def GetChannels():
    path = os.path.join(PROFILE , 'chan.xml')

    return path


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


def openSettings(focus=None):
    addonID = ADDONID
    if not focus: 
        return xbmcaddon.Addon(addonID).openSettings()
    
    try:
        xbmc.executebuiltin('Addon.OpenSettings(%s)' % addonID)

        value1, value2 = str(focus).split('.')

        if FRODO:
            xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 200))
            xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 100))
        else:
            xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 100))
            xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 200))

    except Exception, e:
        print str(e)
        return
