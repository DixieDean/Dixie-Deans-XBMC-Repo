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
import urllib
import urllib2
from hashlib import md5
import socket 
import os
import re
import shutil
import download
import extract
import update
import dixie
import session
import getIni

try:
    import requests2 as requests
except:
    import requests

socket.setdefaulttimeout(10) # 10 seconds 

VERSION     = '2.2.6'

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
HOME        = ADDON.getAddonInfo('path')
TITLE       = 'OnTapp.TV'
MASHMODE    = (ADDON.getSetting('mashmode') == 'true')
DIXIEURL    = dixie.GetSetting('dixie.url').upper()
DIXIELOGOS  = dixie.GetSetting('dixie.logo.folder')
SKIN        = ADDON.getSetting('dixie.skin')
SKINVERSION = '8'
INIVERSION  = '1'

addon       = xbmcaddon.Addon()
addonid     = addon.getAddonInfo('id')
versioninfo = addon.getAddonInfo('version')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras      = os.path.join(datapath, 'extras')
logos       = os.path.join(extras, 'logos')
logofolder  = os.path.join(logos, 'None')
skinfolder  = os.path.join(extras, 'skins')
skin        = ADDON.getSetting('dixie.skin')
dest        = os.path.join(skinfolder, 'skins-12-06-2014.zip')
addonpath   = os.path.join(ADDON.getAddonInfo('path'), 'resources')
default_ini = os.path.join(addonpath, 'addons.ini')
local_ini   = os.path.join(addonpath, 'local.ini')
current_ini = os.path.join(datapath, 'addons.ini')
database    = os.path.join(datapath, 'program.db')
username    = ADDON.getSetting('username')
password    = ADDON.getSetting('password')


dixie.SetSetting('gmtfrom', 'GMT')
dixie.SetSetting('dixie.url', 'All Channels')
dixie.SetSetting('DIXIEURL', 'All Channels')



print '****** ONTAPP.TV %s LAUNCHED ******' % str(versioninfo)

try:
    os.makedirs(logofolder)
    
    if not os.path.exists(skinfolder):
        DownloadSkins()
except:
    pass


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    if curr == '2.2.6':
        d = xbmcgui.Dialog()
        d.ok(TITLE + ' - ' + VERSION, 'Improved Super Favourites integration.', 'For info and support - www.on-tapp.tv')
        showChangelog()
    
    dixie.SetSetting('VERSION', curr)


def showChangelog(addonID=None):
    try:
        if addonID:
            ADDON = xbmcaddon.Addon(addonID)
        else: 
            ADDON = xbmcaddon.Addon()

        f     = open(ADDON.getAddonInfo('changelog'))
        text  = f.read()
        title = '%s - %s' % (xbmc.getLocalizedString(24054), ADDON.getAddonInfo('name'))

        showText(title, text)

    except:
        pass


def showText(heading, text):
    id = 10147

    xbmc.executebuiltin('ActivateWindow(%d)' % id)

    win = xbmcgui.Window(id)

    xbmc.sleep(1000)

    win.getControl(1).setLabel(heading)
    win.getControl(5).setText(text)


def GetCats():
    path = os.path.join(datapath, 'cats.xml')
    url  = dixie.GetExtraUrl() + 'resources/cats.xml'

    try:
        urllib.urlretrieve(url, path)
    except:
        pass


def GetChannels():
    path = os.path.join(datapath, 'chan.xml')
    url  = dixie.GetDixieUrl(DIXIEURL) + 'chan.xml'
    r    = requests.get(url, auth=(username, password))
    
    with open(path, 'wb') as f:
        for chunk in r.iter_content(512):
            f.write(chunk)


def CheckForChannels():
    dir    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    folder = os.path.join(dir, 'channels')
    files  = []
    try:    current, dirs, files = os.walk(folder).next()
    except: pass
    if len(files) == 0:
        dixie.SetSetting('updated.channels', -1) #force refresh of channels


def CheckSkin():
    path = os.path.join(skinfolder, skin)
    curr = SKINVERSION

    if not os.path.exists(path):
        DownloadSkins()
        dixie.SetSetting('SKINVERSION', curr)


def CheckSkinVersion():
    prev = ADDON.getSetting('SKINVERSION')
    curr = SKINVERSION

    if not prev == curr:
        DownloadSkins()
        dixie.SetSetting('SKINVERSION', curr)


def CheckIniVersion():
    getIni.getIni()


def CheckForUpdate():
    if xbmcgui.Window(10000).getProperty('OTT_UPDATING') != 'True':
        import update
        update.checkForUpdate(silent = True)
        return

    while xbmcgui.Window(10000).getProperty('OTT_UPDATING') == 'True':
        xbmc.sleep(1000)


def DownloadSkins():
    url  = dixie.GetExtraUrl() + 'resources/skins-05-08-2014.zip'

    try:
        os.makedirs(skinfolder)
    except:
        pass

    download.download(url, dest)
    extract.all(dest, extras)
    dixie.SetSetting('SKINVERSION', SKINVERSION)

    try:
        os.remove(dest)
    except:
        pass


def CopyKeymap():
   src = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'zOTT.xml')
   if os.path.exists(src):
       os.remove(src)

   src = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'super_favourites_menu.xml')

   if not os.path.exists(src):
       return

   dst = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('profile')), 'super_favourites_menu.xml')

   import shutil
   shutil.copyfile(src, dst)

   os.remove(src)

   xbmc.sleep(1000)
   xbmc.executebuiltin('Action(reloadkeymaps)')


def RemoveKeymap():
   src = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('profile')), 'super_favourites_menu.xml')

   if not os.path.exists(src):
       return

   dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'super_favourites_menu.xml')

   import shutil
   shutil.copyfile(src, dst)

   os.remove(src)

   xbmc.sleep(1000)
   xbmc.executebuiltin('Action(reloadkeymaps)')


try:
    path = os.path.join(datapath, 'tvgdinstall.txt')
    
    if not os.path.exists(path):
        url = dixie.GetExtraUrl() + 'resources/tvgdinstall.txt'
        urllib.urlretrieve(url, path)

    if not os.path.exists(current_ini):
        try: os.makedirs(datapath)
        except: pass
        shutil.copy(default_ini, datapath)
        shutil.copy(local_ini, datapath)
except:
    pass


def main(doLogin=True):
    busy = None
    try:
        busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        busy.show()

        try:    busy.getControl(10).setVisible(False)
        except: pass

    except:
        busy = None

    import buggalo
    import gui

    buggalo.GMAIL_RECIPIENT = 'write2dixie@gmail.com'

        
    try:
        if doLogin:
            url      = dixie.GetDixieUrl(DIXIEURL) + 'update.txt'
            code     = session.doLogin()
            response = session.checkFiles(url)
        else:
            code = 200
            response = ''
            
        if code == 503:
            d = xbmcgui.Dialog()
            d.ok(TITLE + ' Error', 'OnTapp.TV failed with error code - %s.' % code, 'Something went wrong with your login', 'Please check your settings.')
            d.ok(TITLE + ' Error', 'OnTapp.TV failed with error code - %s.' % code, 'Daily IP Address limit reached.', 'Restricted for 2 hours.')
            print '****** OnTapp.TV Error 503. Too many login attempts/IPs exceeded *******'
            return
        
        if response == 401:
            d = xbmcgui.Dialog()
            d.ok(TITLE + ' Error', 'OnTapp.TV failed with error code - %s.' % response, 'Something went wrong with your login', 'Check your settings, or subscribe at www.on-tapp.tv.')
            print '****** OnTapp.TV Error 401. Access Denied. Not a paid member. *******'
            return
        
        if response == 301:
            xbmc.executebuiltin('XBMC.RunScript($CWD/deleteDB.py)')
            d = xbmcgui.Dialog()
            d.ok(TITLE + ' Error', 'OnTapp.TV failed with error code - %s.' % response, 'It looks like you do not have a paid subcription.', 'Check your settings, or subscribe at www.on-tapp.tv.')
            print '****** OnTapp.TV Error 301. Free member. No paid subscription. *******'
            return

        if doLogin:
            # CheckDixieURL()
            CheckVersion()
            GetChannels()
            GetCats()
            CheckSkin()
            CheckSkinVersion()
            CheckIniVersion()
            CheckForUpdate()
            CheckForChannels()

        print '****** OnTapp.TV - All OK *******'

        xbmcgui.Window(10000).setProperty('OTT_RUNNING', 'True')
        xbmc.executebuiltin('XBMC.ActivateWindow(home)')

        w = gui.TVGuide()

        if busy:
           busy.close()
           busy = None

        CopyKeymap()
        w.doModal()
        RemoveKeymap()
        del w

        xbmcgui.Window(10000).clearProperty('OTT_RUNNING')

    except Exception:
       buggalo.onExceptionRaised()


doLogin = True
if xbmcgui.Window(10000).getProperty('OTT_LOGIN').lower() == 'false':
    doLogin = False
xbmcgui.Window(10000).clearProperty('OTT_LOGIN')


main(doLogin)