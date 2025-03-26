#
#       Copyright (C) 2014
#       Sean Poyser (seanpoyser@gmail.com)
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

import sfile


def GetXBMCVersion():
    #xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')

    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor


ADDONID  = 'script.tvguidedixie.tools'
ADDON    = xbmcaddon.Addon(ADDONID)
TITLE    = ADDON.getAddonInfo('name') #'On-Tapp.TV Tools v4'
HOME     = ADDON.getAddonInfo('path')
PROFILE  = ADDON.getAddonInfo('profile')
DATAPATH = xbmc.translatePath(PROFILE)


OTT_ADDONID = 'script.tvguidedixie'
OTT_ADDON   = xbmcaddon.Addon(OTT_ADDONID)
OTT_HOME    = xbmc.translatePath(OTT_ADDON.getAddonInfo('path'))
OTT_PROFILE = xbmc.translatePath(OTT_ADDON.getAddonInfo('profile'))
OTT_TITLE   = OTT_ADDON.getAddonInfo('name') #'On-Tapp.TV'


VERSION = ADDON.getAddonInfo('version')
ICON    = os.path.join(HOME, 'icon.png')
FANART  = os.path.join(HOME, 'fanart.jpg')
GETTEXT = ADDON.getLocalizedString
DEBUG   = ADDON.getSetting('DEBUG') == 'true'

FAVE_POSTFIX = '~OTTFAVE'


skin         = xbmc.getSkinDir()
invalid      = xbmc.getCondVisibility('System.HasAddon(%s)' % skin) == 0
ESTUARY_SKIN = skin.lower() == 'skin.estuary' or invalid


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)
GOTHAM       = (MAJOR == 13) or (MAJOR == 12 and MINOR == 9)


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


def installSkin():
    if getSetting('FIRSTRUN') =='true':
        return

    src = os.path.join(HOME, 'resources', 'skins', 'Default Tools Skin')
    dst = os.path.join(PROFILE, 'skins', 'Default Tools Skin')

    message = 'Updating Skins'

    try:
        notify(message)
        sfile.copytree(src, dst)
        ADDON.setSetting('SKIN', 'Default Tools Skin')
        ADDON.setSetting('FIRSTRUN', 'true')
    except:
        Log('=== tools skin failed to copy ===')
        pass


def getSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


baseurl = 'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/'

def GetBaseUrl():
    return baseurl


def GetChannelType():
    return OTT_ADDON.getSetting('chan.type')


def GetChannelFolder():
    CUSTOM = '1'

    channelType = GetChannelType()

    if channelType == CUSTOM:
        path = OTT_ADDON.getSetting('user.chan.folder')
    else:
        path = OTT_PROFILE

    return path


channelFolder = GetChannelFolder()

OTT_CHANNELS  = os.path.join(channelFolder, 'channels')


def Log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)

        path = os.path.join(OTT_PROFILE, 'log.txt')
        now = str(datetime.datetime.now())
        output = '%s - %s\r\n' % (now, output)
        sfile.append(path, output)

    except:
        pass


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, str(line1), str(line2), str(line3))


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def DialogNumeric(title, current=''):
    #d = xbmcgui.Dialog()
    #num = d.numeric(0, title, str(current))

    num = GetText(title, current) 
    
    try:    return int(num)
    except: pass
 
    return None


def GetText(title, text='', hidden=False):
    kb = xbmc.Keyboard(str(text), title)
    kb.setHiddenInput(hidden)
    kb.doModal()
    if not kb.isConfirmed():
        return None

    text = kb.getText().strip()

    if len(text) < 1:
        return None

    return text


def notify(message):
    # CloseBusy()
    cmd = 'XBMC.notification(%s,%s)' % ('On-Tapp.TV Tools', message)
    xbmc.executebuiltin(cmd)


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:        
        return

    ADDON.setSetting('VERSION', curr)

    if prev == '0.0.0' or prev == '1.0.0':
        folder  = xbmc.translatePath(PROFILE)
        try:
            if not sfile.isdir(folder):
                sfile.makedirs(folder) 
        except: pass

    #call showChangeLog like this to workaround bug in openElec
    script = os.path.join(HOME, 'showChangelog.py')
    cmd    = 'AlarmClock(%s,RunScript(%s),%d,True)' % ('changelog', script, 0)
    xbmc.executebuiltin(cmd)


def GetFolder(title):
    default = ''
    folder  = xbmc.translatePath(PROFILE)

    if not sfile.isdir(folder):
        sfile.makedirs(folder) 

    folder = xbmcgui.Dialog().browse(3, title, 'files', '', False, False, default)
    if folder == default:
        return None

    return xbmc.translatePath(folder)


def showBusy():
    busy = None
    try:
        import xbmcgui
        busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        busy.show()

        try:    busy.getControl(10).setVisible(False)
        except: pass
    except:
        busy = None

    return busy


def clean(text):
    if not text:
        return None

    text = re.sub('[:\\\\/*?\<>|"]+', '', text)
    text = text.strip()
    if len(text) < 1:
        return  None

    return text


def deleteFile(path):
    tries = 5
    while os.path.exists(path) and tries > 0:
        tries -= 1 
        try: 
            sfile.remove(path) 
            break 
        except: 
            xbmc.sleep(500)


def deleteCFG():
    path    = OTT_PROFILE
    cfgfile = os.path.join(path, 'settings.cfg')
    catfile = os.path.join(path, 'catfile')

    deleteFile(cfgfile)
    deleteFile(catfile)


def installSF(sfZip):
    sfData  = os.path.join('special://profile', 'addon_data', 'plugin.program.super.favourites')
    sfDir   = xbmc.translatePath(sfData)
    path    = os.path.join(sfDir, 'Super Favourites')
    zipfile = os.path.join(path, 'sfZip.zip')

    if not os.path.isdir(path):
        sfile.makedirs(path)

    download(sfZip, path, zipfile)


def download(url, path, zipfile):
    import download
    import extract

    line1 = 'Downloading files.'
    line2 = 'Please Wait.'
    line3 = ''
    dp = DialogProgress(line1, line2, line3)

    download.download(url, zipfile, dp)
    extract.all(zipfile, path)
    sfile.remove(zipfile)


def showText(heading, text):
    id = 10147

    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)

    win = xbmcgui.Window(id)

    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass


def showChangelog(addonID=None):
    try:
        if addonID:
            _ADDON = xbmcaddon.Addon(addonID)
        else: 
            _ADDON = xbmcaddon.Addon(ADDONID)

        path  = os.path.join(_ADDON.getAddonInfo('path'), 'changelog.txt')
        text  = sfile.read(path)
        title = '%s - %s' % (xbmc.getLocalizedString(24054), _ADDON.getAddonInfo('name'))

        showText(title, text)

    except:
        pass


def DialogProgress(line1, line2='', line3='', hide=False):
    dp = xbmcgui.DialogProgress()
    dp.create(TITLE, line1, line2, line3)
    dp.update(0)
    if hide:
        HideCancelButton()
    return dp


def HideCancelButton():
    log('====== HideCancelButton ======')
    xbmc.sleep(250)
    WINDOW_PROGRESS = xbmcgui.Window(10101)
    CANCEL_BUTTON   = WINDOW_PROGRESS.getControl(10)
    CANCEL_BUTTON.setVisible(False)


def Launch(param=None):
    name      = 'launch'
    addonPath = HOME
    addonID   = addonPath.rsplit(os.sep, 1)[-1]
    script    = os.path.join(addonPath, 'launch.py')
    args      = ADDONID
    if param:
        args += ',' + param

    cmd = 'RunScript(%s,%s)' % (script, args)
    cmd = 'AlarmClock(%s,%s,%d,True)' % (name, cmd, 0)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name) 
    xbmc.executebuiltin(cmd)
