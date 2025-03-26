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
import os
import shutil

import update
import dixie
import catchup
import sfile

import settings
settings.validate()

ADDON       = dixie.ADDON
HOME        = dixie.HOME
TITLE       = dixie.TITLE
VERSION     = dixie.VERSION

skin        = dixie.SKIN
addonpath   = dixie.RESOURCES
datapath    = dixie.PROFILE

default_ini = os.path.join(addonpath,  'addons.ini')
local_ini   = os.path.join(addonpath,  'local.ini')
current_ini = os.path.join(datapath,   'addons.ini')
plpath      = os.path.join(datapath,   'plists')
database    = os.path.join(datapath,   'program.db')
channel_xml = os.path.join(addonpath,  'chan.xml')
image       = xbmcgui.ControlImage


FIRSTRUN = dixie.GetSetting('FIRSTRUN') == 'true'

def CheckVersion():
    prev = dixie.GetSetting('VERSION')
    curr = VERSION
    dixie.log('****** On-Tapp.EPG %s LAUNCHED ******' % str(VERSION))

    if prev == curr:
        return

    if checkCurrentVersion(curr):
        cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/enableRecord.py)'
        xbmc.executebuiltin(cmd)

    dixie.SetSetting('VERSION', curr)

    dixie.DialogOK('Welcome to On-Tapp.TV', 'For online support, please join our new FaceBook Group', 'Search FaceBook for "On-Tapp-Networks Support"')

    # showChangelog()


def checkCurrentVersion(curr):
    version = [int(x) for x in curr.split('.')]

    if version[2] == 1:
        return True

    return False


def showChangelog(addonID=None):
    try:
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
            # return
        except:
            pass

def CheckPlaylists():
    if os.path.exists(plpath):
        os.remove(plpath)

    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/playlists.py)'
    dixie.log('---- Check playlists ----')
    xbmc.executebuiltin(cmd)


def CheckForChannels():
    dir    = dixie.GetChannelFolder()
    folder = os.path.join(dir, 'channels')
    files  = []
    try:    current, dirs, files = sfile.walk(folder)
    except: pass
    if len(files) == 0:
        dixie.SetSetting('updated.channels', -1) # force refresh of channels


def CheckDSF():
    try:
        if not dixie.isDSF():
            return

        dsf  = dixie.DSF
        path = dsf.getAddonInfo('path')

        sys.path.insert(0, path)
        import gvax
        gvax.getDSFJSON()
    except:
        pass


def CopyKeymap():
    return
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
    return
    src = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('profile')), 'super_favourites_menu.xml')

    if not os.path.exists(src):
        return

    dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'super_favourites_menu.xml')

    import shutil
    shutil.copyfile(src, dst)

    os.remove(src)

    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')


def main(doLogin=True):
    if not dixie.FirstRun():
        return

    dixie.ShowBusy()
    import gui

    try:
        if not dixie.validToRun():
            dixie.CloseBusy()
            dixie.notify('Failed to obtain a response from On-Tapp.TV')
            return

        CheckVersion()
        CheckPlaylists()
        dixie.validateDB()
        dixie.CheckForUpdate(silent=False)
        # CheckDSF()
        CheckForChannels()

        dixie.log('****** On-Tapp.EPG - All OK *******')

        #import message
        # message.check()
        dixie.CloseBusy()

        xbmcgui.Window(10000).setProperty('OTT_RUNNING', 'True')
        xbmcgui.Window(10000).clearProperty('OTT_CATCHUP')

        w = gui.TVGuide()

        CopyKeymap()
        w.doModal()
        RemoveKeymap()
        del w

        xbmcgui.Window(10000).clearProperty('OTT_RUNNING')
        xbmcgui.Window(10000).clearProperty('OTT_WINDOW')

    except Exception as e:
        dixie.DialogOK('ERROR', e)
        raise


kodi = True
if xbmcgui.Window(10000).getProperty('OTT_KODI').lower() == 'false':
    kodi = False
xbmcgui.Window(10000).clearProperty('OTT_KODI')


#Reset Now/Next information
xbmcgui.Window(10000).setProperty('OTT_NOW_TITLE',  '')
xbmcgui.Window(10000).setProperty('OTT_NOW_TIME',   '')
xbmcgui.Window(10000).setProperty('OTT_NEXT_TITLE',  '')
xbmcgui.Window(10000).setProperty('OTT_NEXT_TIME',   '')


#Initialise the window ID that was used to launch OTT (needed for SF functionality)
xbmcgui.Window(10000).setProperty('OTT_LAUNCH_ID', str(xbmcgui.getCurrentWindowId()))

import categories
categories.verifyCategories()

main(kodi)

xbmcgui.Window(10000).clearProperty('OTT_LAUNCH_ID')