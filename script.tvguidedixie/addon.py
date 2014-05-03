#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html

import xbmc
import xbmcaddon
import urllib
import urllib2
import cookielib
# from t0mm0.common.net import Net
from hashlib import md5
import socket 
import os
import shutil
import download
import extract
import update
import dixie


socket.setdefaulttimeout(10) # 10 seconds 

VERSION     = '2.0.2'

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
HOME        = ADDON.getAddonInfo('path')
TITLE       = 'TV Guide Dixie'
MASHMODE    = (ADDON.getSetting('mashmode') == 'true')
DIXIELOGOS  = ADDON.getSetting('dixie.logo.folder')
SKIN        = ADDON.getSetting('dixie.skin')
SKINVERSION = '5'

addon       = xbmcaddon.Addon()
addonid     = addon.getAddonInfo('id')
versioninfo = addon.getAddonInfo('version')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras      = os.path.join(datapath, 'extras')
logos       = os.path.join(extras, 'logos')
logofolder  = os.path.join(logos, 'None')
skinfolder  = os.path.join(extras, 'skins')
skin        = ADDON.getSetting('dixie.skin')
dest        = os.path.join(skinfolder, 'skins-update.zip')
addonpath   = os.path.join(ADDON.getAddonInfo('path'), 'resources')
default_ini = os.path.join(addonpath, 'addons.ini')
local_ini   = os.path.join(addonpath, 'local.ini')
current_ini = os.path.join(datapath, 'addons.ini')
database    = os.path.join(datapath, 'program.db')


if DIXIELOGOS == 'None':
    dixie.SetSetting('dixie.logo.folder', '')

dixie.SetSetting('gmtfrom', 'GMT')

print '****** TV GUIDE DIXIE LAUNCHED ******'
print versioninfo


try:
    os.makedirs(logofolder)
except:
    pass


def CheckDixieURL():
   curr = ADDON.getSetting('dixie.url')
   prev = ADDON.getSetting('DIXIEURL')

   dixie.SetSetting('DIXIEURL', curr)

   if prev != curr:
       os.remove(database)
       
       CheckForUpdate()


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    if prev == '2.0.1':
        d = xbmcgui.Dialog()
        d.ok(TITLE + ' - ' + VERSION, 'For all listings, change settings from "Basic" to "Dixie"', 'Full listings are FREE for a limited period only.', 'Please go to www.tvguidedixie.com for more info.')

    
    dixie.SetSetting('VERSION', curr)


def GetCats():
    path = os.path.join(datapath, 'cats.xml')
    if not os.path.exists(path):
        try:
            url = dixie.GetExtraUrl() + 'cats.xml'
            urllib.urlretrieve(url, path)
        
        except:
            pass


def CheckSkin():
    path = os.path.join(skinfolder, skin)

    if not os.path.exists(path):
        DownloadSkins()


def CheckSkinVersion():
    prev = ADDON.getSetting('SKINVERSION')
    curr = SKINVERSION

    if not prev == curr:
        DownloadSkins()

    dixie.SetSetting('SKINVERSION', curr)


def CheckForUpdate():
    if xbmcgui.Window(10000).getProperty('TVDIXIE_UPDATING') != 'True':
        import update
        update.checkForUpdate(silent = True)
        return

    while xbmcgui.Window(10000).getProperty('TVDIXIE_UPDATING') == 'True':
        xbmc.sleep(1000)


def DownloadSkins():
    url  = dixie.GetExtraUrl() + 'skins-update.zip'

    try:
        os.makedirs(skinfolder)
    except:
        pass

    download.download(url, dest)
    extract.all(dest, extras)

    try:
        os.remove(dest)
    except:
        pass


try:
    path = os.path.join(datapath, 'tvgdinstall.txt')
    
    if not os.path.exists(path):
        url = dixie.GetExtraUrl() + 'tvgdinstall.txt'
        urllib.urlretrieve(url, path)

    if not os.path.exists(current_ini):
        try: os.makedirs(datapath)
        except: pass
        shutil.copy(default_ini, datapath)
        shutil.copy(local_ini, datapath)
except:
    pass


busy = None
try:
    import xbmcgui
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
    CheckDixieURL()
    CheckVersion()
    GetCats()
    CheckSkin()
    CheckSkinVersion()
    CheckForUpdate()


    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    w = gui.TVGuide()

    if busy:
       busy.close()
       busy = None

    w.doModal()
    del w

except Exception:
   buggalo.onExceptionRaised()
