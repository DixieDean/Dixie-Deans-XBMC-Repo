
#       Copyright (C) 2013 On-Tapp-Networks Limited
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

import xbmcaddon
import xbmcgui
import xbmc
import os
import json
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


ADDONID = 'script.on-tapp.tv'
ADDON   =  xbmcaddon.Addon(ADDONID)
HOME    =  ADDON.getAddonInfo('path')
PROFILE =  ADDON.getAddonInfo('profile')
TITLE   =  ADDON.getAddonInfo('name')
VERSION =  ADDON.getAddonInfo('version')
ICON    =  os.path.join(HOME, 'icon.png')
FANART  =  os.path.join(HOME, 'fanart.jpg')
PATCHES =  os.path.join(HOME, 'resources', 'patch')

AddonID   = 'script.tvguidedixie'
Addon     =  xbmcaddon.Addon(AddonID)
epghome   =  Addon.getAddonInfo('path')
resources =  os.path.join(epghome, 'resources')
epgpath   =  xbmc.translatePath(Addon.getAddonInfo('profile'))
extras    =  os.path.join(epgpath, 'extras')
logos     =  os.path.join(extras,  'logos')
baseurl   = 'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/' # 'http://files.on-tapp.tv/'
# baseurl = 'http://files.on-tapp-networks.com/' https://github.com/DixieDean/Dixie-Deans-XBMC-Repo/tree/master/files/lineups

DSFID   = ttTTtt(0,[112,13,108,120,117],[115,103,45,105,212,110,32,46,233,118,53,105,75,100,34,101,38,111,148,46,218,103,216,118,30,97,110,120])
try:
    DSF     = xbmcaddon.Addon(DSFID)
    DSFVER  = DSF.getAddonInfo('version')
    home    = DSF.getAddonInfo('path')
    profile = xbmc.translatePath(DSF.getAddonInfo('profile'))
except: pass


def getSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


def getDSFSetting(param):
    try:    return xbmcaddon.Addon(DSFID).getSetting(param)
    except: return ''


def setSetting(param, value):
    if xbmcaddon.Addon(ADDONID).getSetting(param) == value:
        return
    xbmcaddon.Addon(ADDONID).setSetting(param, value)


GETTEXT = ADDON.getLocalizedString
DEBUG   = getSetting('DEBUG') == 'true'



def GetXBMCVersion():
    #xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')

    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor eg, 13.9.902


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)
GOTHAM       = (MAJOR == 13) or (MAJOR == 12 and MINOR == 9)
HELIX        = (MAJOR == 14) or (MAJOR == 13 and MINOR == 9)
KRYPTON      = (MAJOR == 17) or (MAJOR == 16 and MINOR == 9)


def getSkinPath(xmlFile):
    return os.path.join(HOME, 'resources', 'skins', 'Default Home Skin')


def getBaseURL():
    if isDSF():
        return baseurl + 'resources/swi/'

    return baseurl + 'resources/kodi/'


def isDSF():
    if xbmc.getCondVisibility('System.HasAddon(%s)' % DSFID) == 1:
        Log(DSFID)
        return True

    return False


def getSubSystem():
    return DSF.getSetting('GVAX-SUBSYS')


def Log(text):
    if not DEBUG:
        return

    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)

        path   =  os.path.join(PROFILE, 'log.txt')
        now    =  str(datetime.datetime.now())
        output = '%s - %s\r\n' % (now, output)
        sfile.append(path, output)
    except:
        pass


def Notify(message, length=10000):
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)



def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)



def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def HideCancelButton():
    xbmc.sleep(250)
    WINDOW_PROGRESS = xbmcgui.Window(10101)
    CANCEL_BUTTON   = WINDOW_PROGRESS.getControl(10)
    CANCEL_BUTTON.setVisible(False)


def CompleteProgress(dp, percent):
    for i in range(percent, 100):
        dp.update(i)
        xbmc.sleep(25)
    dp.close()


def DialogProgress(line1, line2='', line3='', hide=False):
    dp = xbmcgui.DialogProgress()
    dp.create(TITLE, line1, line2, line3)
    dp.update(0)
    if hide:
        HideCancelButton()
    return dp



def checkVersion():
    prev = getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    setSetting('VERSION', curr)

    #DialogOK(GETTEXT(30004), GETTEXT(30005), GETTEXT(30006))
    

def ClearCache():
    import cache
    cache.clearCache()


def removeKeymap():
    try:
        xbmc.sleep(1000)
        file = 'zOTT_Keymap.xml'
        dst  = os.path.join('special://profile/keymaps', file)

        if sfile.exists(dst):
            sfile.remove(dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def GetHTML(url, maxAge = 86400):
    import cache
    html = cache.getURL(url, maxSec=5*86400, agent='Firefox')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    return html


def Execute(cmd):
    Log(cmd)
    xbmc.executebuiltin(cmd) 


def Launch(param=None):
    name      = 'launch'
    addonPath = HOME
    addonID   = addonPath.rsplit(os.sep, 1)[-1]
    script    = os.path.join(addonPath, 'launch.py')
    args      = ADDONID
    if param:
        args += ',' + param
    cmd       = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)  
    xbmc.executebuiltin(cmd) 



def GetText(title, text='', hidden=False, allowEmpty=False):
    kb = xbmc.Keyboard(text.strip(), title)
    kb.setHiddenInput(hidden)
    kb.doModal()
    if not kb.isConfirmed():
        return None

    text = kb.getText().strip()

    if (len(text) < 1) and (not allowEmpty):
        return None

    return text


def setKodiSetting(setting, value):
    setting = '"%s"' % setting

    if isinstance(value, list):
        text = ''
        for item in value:
            text += '"%s",' % str(item)

        text  = text[:-1]
        text  = '[%s]' % text
        value = text

    elif isinstance(value, bool):
        value = 'true' if value else 'false'

    elif not isinstance(value, int):
        value = '"%s"' % value

    query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % (setting, value)
    Log(query)
    response = xbmc.executeJSONRPC(query)
    Log(response)



def getKodiSetting(setting):
    try:
        setting = '"%s"' % setting
 
        query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (setting)
        Log(query)
        response = xbmc.executeJSONRPC(query)
        Log(response)

        response = json.loads(response)

        if response.has_key('result'):
            if response['result'].has_key('value'):
                return response ['result']['value'] 
    except:
        pass

    return None


def doBackup():
    import datetime

    src = os.path.join(epgpath, 'channels')
    dst = os.path.join(epgpath, 'channels-backup')

    try:
        sfile.remove(dst)
        sfile.copy(src, dst)
    except:
        pass

    if os.path.exists(logos):
        now  = datetime.datetime.now()
        date = now.strftime('%B-%d-%Y %H-%M')

        cur = Addon.getSetting('dixie.logo.folder')
        src = os.path.join(logos, cur)
        dst = os.path.join(logos, cur+'-%s' % date)

        try:
            sfile.rename(src, dst)
        except:
            pass


def patchLeia():
    ottdatapath = xbmc.translatePath(PROFILE) # /addon_data/script.on-tapp.tv/
    currentskin = Addon.getSetting('dixie.skin')

    homeskin    = os.path.join(ottdatapath, 'skins', 'Default Home Skin', 'resources', 'skins', 'Default', '720p')
    epgskin     = os.path.join(extras, 'skins', currentskin, 'resources', 'skins', 'Default', '720p')

    srcA = os.path.join(PATCHES, 'leia', 'leiapatch-home.xml')
    srcB = os.path.join(PATCHES, 'leia', 'leiapatch-epg.xml')

    dstA = os.path.join(homeskin, 'main.xml')
    dstB = os.path.join(epgskin,  'script-tvguide-streamsetup.xml')

    try:
        message = 'Updating skin files...'
        Notify(message)

        if sfile.exists(homeskin):
            sfile.copy(srcA, dstA)

        if sfile.exists(epgskin):
            sfile.copy(srcB, dstB)

        message = 'Skin files updated...'
        Notify(message)

        setSetting('LEIAFIX', 'true')
    except:
        pass


def downloadDefaults(url):
    import download
    import extract

    # checkforOSMC()

    DialogOK('Welcome to On-Tapp.TV', 'We will now install some needed files.', 'This may take a few minutes, so please be patient.')

    ottdatapath = xbmc.translatePath(PROFILE) # /addon_data/script.on-tapp.tv/
    epgdatapath = epgpath # /addon_data/script.tvguidedixie/extras/

    if not sfile.exists(ottdatapath):
        sfile.makedirs(ottdatapath)

    if not sfile.exists(epgdatapath):
        sfile.makedirs(epgdatapath)


    otturl = url + 'ott/v4ottdefaults.zip'
    epgurl = url + 'ottepg/v4ottepgdefaults.zip'

    ottzip = os.path.join(ottdatapath, 'ottdefaults.zip')
    epgzip = os.path.join(epgdatapath, 'ottepgdefaults.zip')


    dp = DialogProgress('Downloading files.', 'Please Wait.')

    download.download(otturl, ottzip, dp)
    extract.all(ottzip, ottdatapath)
    sfile.remove(ottzip)

    download.download(epgurl, epgzip, dp)
    extract.all(epgzip, epgdatapath)
    sfile.remove(epgzip)

    Addon.setSetting('dixie.skin', 'Default Skin')
    setSetting('SKIN', 'Default Home Skin')

    setSetting('V4UPGRADE', 'true')

    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/enableRecord.py)'

    # Log('---- V4UPGRADE: Install Record ----')
    # Log(cmd)
    # xbmc.executebuiltin(cmd)

    import sys
    sys.path.insert(0, epghome)
    import enableRecord
    import extras


    if DialogYesNo('Would you like to choose from one of our Channel Line-ups?', 
                'These are customised listings all set up to save you time.',
                'You can change this later using On-Tapp.TV Tools'):

        baseurl  =  'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/lineups/'
        jsonurl  =  baseurl + 'lineups.json'
        response =  extras.getList(jsonurl, 'lineups', 'lineup')
        Log('---- Choose Line-up ----')
        Log(baseurl)
        Log(jsonurl)
        Log(response)

        lineups  = []
        for result in response:
            label  = result['-name']
            url    = baseurl + result['-url']
            sfZip  = baseurl + result['-sfzip']
            isSF   = result['-sf']

            lineups.append((label, url, isSF, sfZip))

        menu = []
        for lineup in lineups:
            menu.append(lineup[0])

        title  = 'Please select a Channel Line-up'
        option =  xbmcgui.Dialog().select(title, menu)
        extras.installLineup(lineups[option])


    Log('---- V4UPGRADE: Install Record ----')
    enableRecord.enableRecord()


def checkforOSMC():
    logpath = xbmc.translatePath('special://logpath')
    logfile = os.path.join(logpath, 'kodi.log')

    if os.path.exists(logfile):
        with open(logfile) as f:
            result = f.read()

        if 'Open Source Media Center' in result:
            Log('======= OSMC log TRUE =======')
            Addon.setSetting('SUDOPASS', 'osmc')
            return True

    Log('======= OSMC log FALSE =======')
    return False


def downloadSkins(url, path, zipfile):
    import download
    import extract

    DialogOK('A new skin update is available.', 'It will be downloaded and installed', 'into your On-Tapp.TV system.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing skin update')
    sfile.remove(zipfile)


def downloadLogos(url, path, zipfile):
    import download
    import extract

    DialogOK('Some new logos are available.', 'They will be downloaded and added to your logopack.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing logo update')
    sfile.remove(zipfile)


def doOTTUpdate(url, path, zipfile, ottupdate):
    import download
    import extract

    DialogOK('An On-Tapp.TV "Live Update" is available.', 'OTTV Update %s will be downloaded and installed on your system.' % (ottupdate), 'Thank you.')
    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing python update')
    sfile.remove(zipfile)
    Log('OTT Update %s installed' % str(ottupdate))
    xbmc.executebuiltin('UpdateLocalAddons')


def doEPGUpdate(url, path, zipfile, epgupdate):
    import download
    import extract

    DialogOK('An On-Tapp.EPG "Live Update" is available.', 'EPG Update %s will be downloaded and installed on your system.' % (epgupdate), 'Thank you.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing python update')
    sfile.remove(zipfile)
    Log('EPG Update %s installed' % str(epgupdate))
    xbmc.executebuiltin('UpdateLocalAddons')


def installSFPlugin():
    sfavourites  = 'plugin.program.super.favourites'
    sf_installed =  xbmc.getCondVisibility('System.HasAddon(%s)' % sfavourites) == 1

    if not sf_installed:
        return

    try:
        filename = 'OTTV Mini-Guide.py'
        sfaddon  =  xbmcaddon.Addon(id = sfavourites)
        path     =  sfaddon.getAddonInfo('profile')
        file     =  os.path.join(path, 'Plugins', filename)
        src      =  os.path.join(epghome, 'resources', filename)

        if not os.path.exists(path):
            sfile.makedirs(path)

        sfile.copy(src, file)

    except: pass
