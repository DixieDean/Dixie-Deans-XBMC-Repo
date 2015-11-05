
#       Copyright (C) 2013-2014
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

import urllib
import urllib2
import random
import re
import os

import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui

import cache
import yt

import utilsOTT as utils
import categories
    
ADDONID    = utils.ADDONID
ADDON      = utils.ADDON
HOME       = utils.HOME
PROFILE    = utils.PROFILE
TITLE      = utils.TITLE
VERSION    = utils.VERSION
ICON       = utils.ICON
FANART     = utils.FANART

SUPERFAVES   = 'plugin.program.super.favourites'
SF_INSTALLED = xbmc.getCondVisibility('System.HasAddon(%s)' % SUPERFAVES) == 1
SFFILE       = ''

try:
    import sys
    sfAddon = xbmcaddon.Addon(id = SUPERFAVES)
    sfPath  = sfAddon.getAddonInfo('path')
    sys.path.insert(0, sfPath)

    import chooser
    import favourite

    SFFILE = os.path.join(PROFILE, 'favourites.xml')
except:
    SF_INSTALLED = False


IMAGES = os.path.join(HOME, 'resources', 'images')

AUTOSTREAM = utils.getSetting('AUTOSTREAM') == 'true'
KIOSKMODE  = utils.getSetting('KIOSKMODE')  == 'true'

GETTEXT = utils.GETTEXT


global APPLICATION


_SCRIPT          = 100
_ADDON           = 200
_SETTINGS        = 300
_YOUTUBE         = 400
_CATCHUP         = 500
_TVSHOWS         = 600
_MOVIES          = 700
_SHOWSHORTCUTS   = 800
_ADDSHORTCUT     = 900
_VPNICITY        = 1000
_SUPERSEARCH     = 1100
_REMOVESHORTCUT  = 1200
_SYSTEM          = 1300
_LIBRARY         = 1400
_SUPERFAVE       = 1500
_REMOVESUPERFAVE = 1600

_CATEGORIES     = 2000
_SETTINS        = 2001
_TOOLS          = 2002
_VPN            = 2003



WINDOWID = 10005 #music


categoriesList = categories.getSetting('categories').split('|')
if categoriesList[0] == '':
    categoriesList = []


def Capitalize(text):
    if len(text) == 0:
        return text

    if len(text) == 1:
        return text.capitalize()

    return text[0].capitalize() + text[1:]


def Main():
    if AUTOSTREAM:
        if xbmc.getCondVisibility('Player.HasVideo') <> 1:
            url = xbmcaddon.Addon('script.tvguidedixie').getSetting('streamURL')
            if len(url) > 0:
                PlayMedia(url)

    AddAddon('TV Guide',   'script.tvguidedixie', _SCRIPT,  icon=os.path.join(IMAGES, 'OTTV-TV_Guide.png'))

    AddLibrary('Movies',   '',  _MOVIES,  icon=os.path.join(IMAGES, 'OTTV-Movies.png'))
    AddLibrary('TV Shows', '',  _TVSHOWS, icon=os.path.join(IMAGES, 'OTTV-TV_Shows.png'))

    AddSubFolder('TV Catch Up', _CATCHUP, icon=os.path.join(IMAGES, 'OTTV-TV_Catchup.png'), desc='Catch up on shows you have missed')

    AddAddon('Search',     SUPERFAVES, _SUPERSEARCH, icon=os.path.join(IMAGES, 'OTTV-Search.png'), desc='Search all your favourite addons all from one place')
    AddAddon('Favourites', SUPERFAVES, _ADDON,       icon=os.path.join(IMAGES, 'OTTV-Favourites.png'))

    # AddSubFolder('System',      _SYSTEM,  icon=os.path.join(IMAGES, 'OTTV-System.png'),  desc='Settings and Tools')

    if not KIOSKMODE:
        ShowShortcuts()
        ShowSFShortcuts()
        icon = os.path.join(IMAGES, 'OTTV-Shortcuts.png')
        AddDir('Add more...', '', _ADDSHORTCUT, iconimage=icon, description='Browse and select other shortcuts', isFolder=False, isPlayable=False)



def ShowCatchup():
    AddAddon('BBC iPlayer', 'plugin.video.iplayerwww', _ADDON, icon=os.path.join(IMAGES, 'OTTV-BBC_iPlayer.png'))
    AddAddon('ITV Player',  'plugin.video.itv',        _ADDON, icon=os.path.join(IMAGES, 'OTTV-ITV_Player.png'))
    AddAddon('UKTV Play',   'plugin.video.uktvplay',   _ADDON, icon=os.path.join(IMAGES, 'OTTV-UKTV_Play.png'))


def ShowSystem():
    AddAddon('Settings', 'script.tvguidedixie',       _SETTINGS,   icon=os.path.join(IMAGES, 'OTTV-Settings.png'), desc='Configure your TV Guide')
    AddAddon('Tools',    'script.tvguidedixie.tools', _ADDON,      icon=os.path.join(IMAGES, 'OTTV-Tools.png'),    desc='Use On-Tapp.TV Tools to edit your channels')
    AddVPNicity()


def ShowSettings(addonID):
    xbmc.executebuiltin('Addon.OpenSettings(%s)' % addonID)


def OpenTools():
    xbmc.executebuiltin('XBMC.RunAddon(script.tvguidedixie.tools)')


def PlayMedia(url, windowed=True):
    APPLICATION.setResolvedUrl(url, success=True, listItem=None, windowed=windowed)


def SelectSuperSearch(addonID):
    xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (WINDOWID, addonID, 25))


def ShowSFShortcuts():
    if not SF_INSTALLED:
        return

    faves        = favourite.getFavourites(SFFILE)
    mode         = _SUPERFAVE
    isFolder     = False
    isPlayable   = False
    replaceItems = False

    for fave in faves:
        name = fave[0]
        icon = fave[1]
        path = fave[2]

        #these currently don't work as they are removed by chooser.py :(
        fanart = favourite.getFanart(path) 
        desc   = favourite.getOption(path, 'desc')

        menu = []
        menu.append(('Remove %s Super Favourite' % (name), '?mode=%d&url=%s' % (_REMOVESUPERFAVE, urllib.quote_plus(path))))

        AddDir(name, path, mode, icon, desc, isFolder, isPlayable, fanart=fanart, contextMenu=menu, replaceItems=False)


def ShowShortcuts():
    addons = utils.getSetting('ADDONS').split('|')
    toSort = []
    
    for addon in addons:
        try:
            if addon:
                name = xbmcaddon.Addon(addon).getAddonInfo('name')
                toSort.append([Capitalize(name), addon])
        except:
            pass

    #toSort.sort()

    for addon in toSort:
        try:
            menu = []
            name = addon[0]
            url  = addon[1]
            menu.append(('Remove %s shortcut' % Capitalize(name), '?mode=%d&url=%s' % (_REMOVESHORTCUT, urllib.quote_plus(url))))

            if url.startswith('script'):
                AddAddon(name, url, _SCRIPT, contextMenu=menu)
            else:
                AddAddon(name, url, _ADDON, contextMenu=menu)
        except:
            pass


def RemoveSFShortcut(url):
    return favourite.removeFave(SFFILE, url)  


def RemoveShortcut(url):
    shortcuts = utils.getSetting('ADDONS')

    url += '|'

    if url not in shortcuts:
        return False

    update = shortcuts.replace(url,  '')

    utils.setSetting('ADDONS', update)

    return True


def AddShortcut():
    ADDMORE = int(utils.getSetting('ADDMORE'))

    if ADDMORE == 0:
        return AddAddonShortcut()

    if not SF_INSTALLED:
        return AddAddonShortcut()

    if ADDMORE == 2 and utils.DialogYesNo(GETTEXT(30313), GETTEXT(30314), '', GETTEXT(30315), GETTEXT(30316)):
        return AddAddonShortcut()

    return AddSFShortcut()


def AddSFShortcut():
    if not chooser.GetFave('OTT3'):
        return False

    path   = xbmc.getInfoLabel('Skin.String(OTT3.Path)')
    label  = xbmc.getInfoLabel('Skin.String(OTT3.Label)')
    icon   = xbmc.getInfoLabel('Skin.String(OTT3.Icon)')
    folder = xbmc.getInfoLabel('Skin.String(OTT3.IsFolder)') == 'true'

    if len(path) == 0 or path == 'noop':
        return False

    fave = [label, icon, path] 
    favourite.copyFave(SFFILE, fave)

    return True


def AddAddonShortcut():
    import glob

    path      = xbmc.translatePath(os.path.join('special://home' , 'addons', '*.*'))
    shortcuts = utils.getSetting('ADDONS').split('|')

    #don't allow sortcut to self
    shortcuts.append(ADDONID)

    names = []

    for addon in glob.glob(path):
        try:
            name = addon.lower().rsplit(os.path.sep, 1)[-1]
            if name not in shortcuts:
                realname = xbmcaddon.Addon(name).getAddonInfo('name')
                names.append([Capitalize(realname), name])
        except:
            pass

    if len(names) < 1:
        return

    names.sort()

    addons = []
    for name in names:
        addons.append(name[0])

    option = xbmcgui.Dialog().select('Select addon', addons)

    if option < 0:
        return False

    update = utils.getSetting('ADDONS') + names[option][1] + '|'

    utils.setSetting('ADDONS', update)

    return True


def AddShowShortcuts():
    icon = os.path.join(IMAGES, 'OTTV-Shortcuts.png')
    AddDir('Shortcuts...', '', _SHOWSHORTCUTS, iconimage=icon, description='Custom addon shortcuts', isFolder=True, isPlayable=False)


def AddVPNicity():
    try:
        addonID    = 'plugin.program.vpnicity'
        properties = GetAddon(addonID)
        desc       = 'Select a VPN' #properties[6]
        icon       = properties[7]
        fanart     = properties[8]

        AddDir('Select VPN', addonID, _VPNICITY, icon, desc, False, fanart)
    except:
        pass


def SelectVPNicity(addonID):
    properties = GetAddon(addonID)
    script     = os.path.join(properties[1], 'manual.py')
    cmd = 'RunScript(%s)' % script
    xbmc.executebuiltin(cmd)


def PlayYT(id):
    xbmc.executebuiltin('Dialog.Show(busydialog)')

    video, links = yt.GetVideoInformation(id)

    xbmc.executebuiltin('Dialog.Close(busydialog)')

    if 'best' not in video:
        return False

    url   = video['best']          
    title = video['title']
    image = video['thumbnail']

    liz = xbmcgui.ListItem(title, iconImage=image, thumbnailImage=image)

    liz.setInfo( type="Video", infoLabels={ "Title": title} )

    windowed = utils.getSetting('PLAYBACK') == '1'

    APPLICATION.setResolvedUrl(url, success=True, listItem=liz, windowed=windowed)


def AddYT(name, id):
    video, links = yt.GetVideoInformation(id)

    url   = video['best']   
    desc  = video['title']       
    image = video['thumbnail']

    AddDir(name, id, _YOUTUBE, image, desc, False, True, image)


def GetAddon(addonID):
    addon   = xbmcaddon.Addon(addonID)
    home    = addon.getAddonInfo('path')
    profile = addon.getAddonInfo('profile')
    title   = addon.getAddonInfo('name')
    version = addon.getAddonInfo('version')
    summary = addon.getAddonInfo('summary')
    desc    = addon.getAddonInfo('description')
    icon    = os.path.join(home, 'icon.png')
    fanart  = os.path.join(home, 'fanart.jpg')

    return [addon, home, profile, title, version, summary, desc ,icon, fanart]


def AddAddon(name, addonID, mode, icon=None, fanart=None, desc=None, contextMenu=[], replaceItems=False):
    try:    properties = GetAddon(addonID)
    except: return

    if desc == None:
        desc = properties[6]

    if icon == None:
        icon = properties[7]

    if fanart == None:
        fanart = properties[8]
    
    AddDir(name, addonID, mode, icon, desc, False, False, fanart, contextMenu, replaceItems)


def AddSubFolder(name, mode, icon=None, fanart=None, desc=''):
    if icon == None:
        icon = ICON

    if fanart == None:
        fanart = FANART

    AddDir(name, '', mode, icon, desc, True, False, fanart)


def AddLibrary(name, windowID, mode, icon=None, fanart=None, desc=''):
    if icon == None:
        icon = ICON
    
    if fanart == None:
        fanart = FANART
    
    AddDir(name, '', mode, icon, '', '', '', fanart)


def ShowCategories(categoriesList):
    d = categories.CategoriesMenu(categoriesList)
    d.doModal()
    categoriesList = d.currentCategories
    del d
    
    categories.setSetting('categories', '|'.join(categoriesList))


def AddShowCategories():
    icon = os.path.join(IMAGES, 'OTTV-Categories.png')
    fanart = FANART

    AddDir('Categories', '', _CATEGORIES, icon, 'Edit which On-Tapp.TV Categories are displayed in the TV Guide', '', '', fanart)


def AddDir(name, url, mode, iconimage, description, isFolder, isPlayable, fanart='', contextMenu=[], replaceItems=False):
    u  = ''
    u += "?url="         + urllib.quote_plus(url)
    u += "&mode="        + str(mode)
    u += "&name="        + urllib.quote_plus(name)
    u += "&iconimage="   + urllib.quote_plus(iconimage)
    u += "&description=" + urllib.quote_plus(description)
    u += "&fanart="      + urllib.quote_plus(fanart)

    infoLabels = {'title':name, 'fanart':fanart, 'description':description, 'thumb':iconimage}

    APPLICATION.addDir(name, mode, u, iconimage, isFolder=isFolder, isPlayable=isPlayable, infoLabels=infoLabels, contextMenu=contextMenu, replaceItems=replaceItems)


def get_params(params):
    if not params:
        return {}

    param = {}

    cleanedparams = params.replace('?','')

    if (params[len(params)-1] == '/'):
       params = params[0:len(params)-2]

    pairsofparams = cleanedparams.split('&')    

    for i in range(len(pairsofparams)):
        splitparams = pairsofparams[i].split('=')

        if len(splitparams) == 2:
            param[splitparams[0]] = splitparams[1]

    return param

    
def onBack(application, _params):
    pass

    
def onParams(application, _params):
    global APPLICATION
    APPLICATION = application

    params = get_params(_params)
    mode   = None

    try:    mode = int(urllib.unquote_plus(params['mode']))
    except: pass

    try:    url = urllib.unquote_plus(params['url'])
    except: url = None
    

    if mode == _SCRIPT:
        cmd = 'RunScript(%s)' % url
        xbmc.executebuiltin(cmd)


    elif mode == _ADDON:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/",return)' % (WINDOWID, url))


    elif mode == _SUPERFAVE:
        xbmc.executebuiltin(url)


    elif mode == _REMOVESUPERFAVE:
        if RemoveSFShortcut(url):
            APPLICATION.containerRefresh()
        
    elif mode == _MOVIES:
        if utils.getSetting('KodiLib') == 'true':
            xbmc.executebuiltin('ActivateWindow(10501,plugin://plugin.video.genesis/?action=movieNavigator,return)')
        else:
            xbmc.executebuiltin('ActivateWindow(10025,videodb://1/2,return)')


    elif mode == _TVSHOWS:
        if utils.getSetting('KodiLib') == 'true':
            xbmc.executebuiltin('ActivateWindow(10025,plugin://plugin.video.genesis/??action=tvNavigator,return)')
        else:
            xbmc.executebuiltin('ActivateWindow(10025,videodb://2/2,return)')


    elif mode == _CATEGORIES:
        ShowCategories(categoriesList)


    elif mode == _SETTINGS:
        ShowSettings()


    elif mode == _TOOLS:
        OpenTools()


    elif mode == _SYSTEM:
        ShowSystem()


    elif mode == _YOUTUBE:
        PlayYT(url)


    elif mode == _VPNICITY:
        SelectVPNicity(url)


    elif mode == _CATCHUP:
        ShowCatchup() 


    elif mode == _SUPERSEARCH:
        SelectSuperSearch(url)


    elif mode == _SHOWSHORTCUTS:
        ShowShortcuts()


    elif mode == _ADDSHORTCUT:
        if AddShortcut():
            APPLICATION.containerRefresh()


    elif mode == _REMOVESHORTCUT:
        if RemoveShortcut(url):
            APPLICATION.containerRefresh()

    else:
        Main()