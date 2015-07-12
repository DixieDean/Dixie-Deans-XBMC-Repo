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
import xbmcvfs
import urllib
import urllib2
from hashlib import md5
import socket
import os
import re
import shutil
import datetime
import download
import extract
import update
import dixie
import getIni
import filmon

import settings
settings.validate()


ADDON       = dixie.ADDON
HOME        = dixie.HOME
TITLE       = dixie.TITLE
VERSION     = dixie.VERSION
DIXIEURL    = dixie.DIXIEURL
DIXIELOGOS  = dixie.DIXIELOGOS
LOGOPACK    = dixie.LOGOPACK
LOGOVERSION = dixie.LOGOVERSION
SKIN        = dixie.SKIN
SKINVERSION = dixie.SKINVERSION
INIVERSION  = dixie.INIVERSION

skin        = dixie.SKIN
addonpath   = dixie.RESOURCES
datapath    = dixie.PROFILE
extras      = os.path.join(datapath,   'extras')
logos       = os.path.join(extras,     'logos')
logofolder  = os.path.join(logos,      'None')
logodest    = os.path.join(logos,      'logos.zip')
skinfolder  = os.path.join(extras,     'skins')
dest        = os.path.join(skinfolder, 'skins.zip')
default_ini = os.path.join(addonpath,  'addons.ini')
local_ini   = os.path.join(addonpath,  'local.ini')
current_ini = os.path.join(datapath,   'addons.ini')
database    = os.path.join(datapath,   'program.db')
channel_xml = os.path.join(addonpath,  'chan.xml')
image       = xbmcgui.ControlImage


def CheckVersion():
    prev = dixie.GetSetting('VERSION')
    curr = VERSION
    dixie.log('****** ONTAPP.TV %s LAUNCHED ******' % str(VERSION))

    if prev == curr:
        return

    dixie.SetSetting('VERSION', curr)

    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, 'NEW UPDATE.', 'New channels - see message.', 'New default Colour Logo Pack.')
    # showChangelog()


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


def CheckChanXML():
    chanpath = os.path.join(datapath, 'chan.xml')
    if not os.path.exists(chanpath):
        try:
            shutil.copy(channel_xml, datapath)
        except:
            dixie.log('Error in CheckChanXML()')    

def CheckForChannels():
    dir    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
    folder = os.path.join(dir, 'channels')
    files  = []
    try:    current, dirs, files = os.walk(folder).next()
    except: pass
    if len(files) == 0:
        dixie.SetSetting('updated.channels', -1) # force refresh of channels


def CheckSkin():
    path = os.path.join(skinfolder, skin)
    curr = SKINVERSION

    if not os.path.exists(path):
        DownloadSkins()
        dixie.SetSetting('SKINVERSION', curr)


def CheckLogos():
    path = os.path.join(extras, logos)
    curr = LOGOVERSION

    if not os.path.exists(path):
        DownloadLogos()
        dixie.SetSetting('LOGOVERSION', curr)


def CheckSkinVersion():
    prev = dixie.GetSetting('SKINVERSION')
    curr = SKINVERSION

    if not prev == curr:
        DownloadSkins()
        dixie.SetSetting('SKINVERSION', curr)


def CheckLogoVersion():
    prev = dixie.GetSetting('LOGOVERSION')
    curr = LOGOVERSION

    if not prev == curr:
        line1 = 'UPDATE: New Colour Logo Pack Available.'
        line2 = 'A back-up of your logos will created first.'
        line3 = 'Are you sure you want to download this update?'

        if dixie.DialogYesNo(line1, line2, line3):
            DownloadLogos()
            dixie.SetSetting('LOGOVERSION', curr)
        else:
            dixie.SetSetting('LOGOVERSION', curr)


def CheckIniVersion():
    getIni.getIni()


def CheckFilmOn():
    getIni.ftvIni()


def CheckForUpdate():
    if xbmcgui.Window(10000).getProperty('OTT_UPDATING') != 'True':
        import update
        update.checkForUpdate(silent = True)
        return

    while xbmcgui.Window(10000).getProperty('OTT_UPDATING') == 'True':
        xbmc.sleep(1000)


def DownloadSkins():
    url  = dixie.GetExtraUrl() + 'resources/skins-05-18-2015.zip'

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


def DownloadLogos():
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
        dixie.SetSetting('LOGOVERSION', LOGOVERSION)
        dixie.SetSetting('dixie.logo.folder', LOGOPACK)

    try:
        os.remove(logodest)
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
    if not os.path.exists(current_ini):
        try: os.makedirs(datapath)
        except: pass
        shutil.copy(default_ini, datapath)
        shutil.copy(local_ini, datapath)
except:
    pass


def main(doLogin=True):
    dixie.CheckUsername()
    import message
    message.check()
    CheckChanXML()
    CheckSkin()
    CheckLogos()
    dixie.ShowBusy()

    import buggalo
    import gui

    buggalo.GMAIL_RECIPIENT = 'write2dixie@gmail.com'


    try:
        if not dixie.validToRun():
            dixie.notify('Failed to obtain a response from On-Tapp.TV')
            return
            
        CheckVersion()
        CheckSkinVersion()
        CheckLogoVersion()
        CheckIniVersion()
        CheckFilmOn()
        
        CheckForUpdate()
        CheckForChannels()

        dixie.log('****** OnTapp.TV - All OK *******')

        dixie.CloseBusy()

        xbmcgui.Window(10000).setProperty('OTT_RUNNING', 'True')
        xbmc.executebuiltin('XBMC.ActivateWindow(home)')

        w = gui.TVGuide()

        CopyKeymap()
        w.doModal()
        RemoveKeymap()
        del w

        xbmcgui.Window(10000).clearProperty('OTT_RUNNING')

    except Exception:
        buggalo.onExceptionRaised()


kodi = True
if xbmcgui.Window(10000).getProperty('OTT_KODI').lower() == 'false':
    kodi = False
xbmcgui.Window(10000).clearProperty('OTT_KODI')


main(kodi)

filmon.logout()