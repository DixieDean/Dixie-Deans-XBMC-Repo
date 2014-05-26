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
import urllib
import urllib2
from hashlib import md5
import socket 
import os
import shutil
import download
import extract
import update
import dixie


socket.setdefaulttimeout(10) # 10 seconds 

VERSION     = '2.0.9'

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
HOME        = ADDON.getAddonInfo('path')
TITLE       = 'OnTapp.TV'
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
dest        = os.path.join(skinfolder, 'skins-28-04-2014.zip')
addonpath   = os.path.join(ADDON.getAddonInfo('path'), 'resources')
default_ini = os.path.join(addonpath, 'addons.ini')
local_ini   = os.path.join(addonpath, 'local.ini')
current_ini = os.path.join(datapath, 'addons.ini')
database    = os.path.join(datapath, 'program.db')


if ADDON.getSetting('dixie.url') == 'G-Box Midnight MX2':
    dixie.SetSetting('dixie.url', 'Dixie')

dixie.SetSetting('gmtfrom', 'GMT')
dixie.SetSetting('autoStart', 'false')


print '****** ONTAPP.TV LAUNCHED ******'
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
       try:
           os.remove(database)
       except:
           pass
           
           CheckForUpdate()


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    if prev != '2.0.9':
        d = xbmcgui.Dialog()
        d.ok(TITLE + ' - ' + VERSION, 'New! Custom MyChannels in the Dixie URL listings.', 'There are now 5 Channels you can make your own!', 'For all support and news - www.ontapp.tv')

    
    dixie.SetSetting('VERSION', curr)


def GetCats():
    path = os.path.join(datapath, 'cats.xml')
    url  = dixie.GetExtraUrl() + 'cats.xml'
    try:
        urllib.urlretrieve(url, path)
    except:
        pass


def CheckSkinVersion():
    prev = ADDON.getSetting('SKINVERSION')
    curr = SKINVERSION

    if not prev == curr:
        DownloadSkins()

    dixie.SetSetting('SKINVERSION', curr)


def CheckForUpdate():
    if xbmcgui.Window(10000).getProperty('OTT_UPDATING') != 'True':
        import update
        update.checkForUpdate(silent = True)
        return

    while xbmcgui.Window(10000).getProperty('OTT_UPDATING') == 'True':
        xbmc.sleep(1000)


def DownloadSkins():
    url  = dixie.GetExtraUrl() + 'skins-28-04-2014.zip'

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


def CopyKeymap():
    src = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'zOTT.xml')
    dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'zOTT.xml')
    
    if os.path.exists(dst):
        return
        
    shutil.copyfile(src, dst)
    
    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')


def RemoveKeymap():
    dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'zOTT.xml')
    
    if not os.path.exists(dst):
        return
        
    os.remove(dst)
    
    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')


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


def main():
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
        CheckDixieURL()
        CheckVersion()
        GetCats()
        CheckSkinVersion()
        CheckForUpdate()
    
        xbmcgui.Window(10000).setProperty('OTT_RUNNING', 'True')
        xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    
        w = gui.TVGuide()
    
        if busy:
           busy.close()
           busy = None
    
        # CopyKeymap()
        w.doModal()
        RemoveKeymap()
        del w
    
        xbmcgui.Window(10000).clearProperty('OTT_RUNNING')

    except Exception:
       buggalo.onExceptionRaised()


main()