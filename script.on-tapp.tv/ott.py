
#       Copyright (C) 2013-
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
SFFILE       = None
SFMOV        = None
SFTV         = None

TOOLS = 'script.tvguidedixie.tools'

try:
    import sys
    sfAddon = xbmcaddon.Addon(id = SUPERFAVES)
    sfPath  = sfAddon.getAddonInfo('path')
    sys.path.insert(0, sfPath)

    import chooser
    import favourite

    SFFILE = os.path.join(PROFILE, 'favourites.xml')
    SFMOV  = os.path.join(PROFILE, 'movie.xml')
    SFTV   = os.path.join(PROFILE, 'tv.xml')

    LABEL_NUMERIC = sfAddon.getSetting('LABEL_NUMERIC') == 'true'

except:
    SF_INSTALLED  = False
    LABEL_NUMERIC = False


IMAGES = os.path.join(HOME, 'resources', 'skins', 'Default Home Skin', 'resources', 'skins', 'Default', 'media')
# IMAGES = os.path.join(HOME, 'resources', 'images')
# SKIN   = utils.getSetting('SKIN')
# IMAGES = os.path.join(PROFILE, 'skins', SKIN, 'resources', 'skins', 'Default', 'media')
# print '============ OTT SKIN ============'
# print IMAGES


AUTOSTREAM = utils.getSetting('AUTOSTREAM') == 'true'
KIOSKMODE  = utils.getSetting('KIOSKMODE')  == 'true'

KODILIB = utils.getSetting('UseKodiLib')
MOVIES  = utils.getSetting('MOVIE')
TV      = utils.getSetting('TV')

utils.Log('LIBRARY SETTING:\t%s' % KODILIB)
utils.Log('MOVIE SETTING:\t%s'   % MOVIES)
utils.Log('TV SETTING:\t%s'      % TV)

GETTEXT = utils.GETTEXT


global APPLICATION


_SCRIPT            = 100
_ADDON             = 200
_SETTINGS          = 300
_YOUTUBE           = 400
_CATCHUP           = 500
_TV                = 600
_TVLIB             = 601
_TVADDON           = 602
_TVOPTIONS         = 603
_MOVIE             = 700
_MOVIELIB          = 701
_MOVIEADDON        = 702
_MOVIEOPTIONS      = 703
_SHOWSHORTCUTS     = 800
_ADDSHORTCUT       = 900
_VPNICITY          = 1000
_SUPERSEARCH       = 1100
_REMOVESHORTCUT    = 1200
_TOOLS             = 1300
_LIBRARY           = 1400
_SUPERFAVE         = 1500
_REMOVESUPERFAVE   = 1600
_REMOVESFMOVIE     = 1601
_REMOVESFTV        = 1602
_REMOVEMOVIE       = 1700
_REMOVETV          = 1800

_BACKUPRESTORE   = 1950
_BACKUPCHANNELS  = 1960
_RESTORECHANNELS = 1970
_FULLBACKUP      = 1980
_FULLRESTORE     = 1990

_CATEGORIES1 = 2000
_SETTINS     = 2001
_CHANNELS    = 2002
_CATEGORIES2 = 2003
_SKINS       = 2004
_LOGOS       = 2005
_INI         = 2006
_VPN         = 2007
_LINEUPS     = 2008


KRYPTON = utils.KRYPTON

#if KRYPTON:
#    WINDOWID = 10502 #music
#else:
#    WINDOWID = 10005 #music

WINDOWID = 10502


categoriesList = categories.getSetting('categories').split('|')
if categoriesList[0] == '':
    categoriesList = []


def removeNumeric(text):
    NUMBER_SEP = ' | '

    if not LABEL_NUMERIC:
        return text

    root = text.split(NUMBER_SEP, 1)[0]
    if root.startswith('['):
        root = root.rsplit(']', 1)[0] + ']'
    else:
        root = ''
        
    return root + text.split(NUMBER_SEP, 1)[-1]


def Capitalize(text):
    if len(text) == 0:
        return text

    if len(text) == 1:
        return text.capitalize()

    return text[0].capitalize() + text[1:]


def Main():
    MOVIETAB  = utils.getSetting('MOVIETAB')  == 'true'
    TVTAB     = utils.getSetting('TVTAB')     == 'true'
    CATCHTAB  = utils.getSetting('CATCHTAB')  == 'true'
    SEARCHTAB = utils.getSetting('SEARCHTAB') == 'true'
    FAVESTAB  = utils.getSetting('FAVESTAB')  == 'true'
    TOOLSTAB  = utils.getSetting('TOOLSTAB')  == 'true'

    if AUTOSTREAM:
        if xbmc.getCondVisibility('Player.HasVideo') <> 1:
            url = xbmcaddon.Addon('script.tvguidedixie').getSetting('streamURL')
            if len(url) > 0:
                # PlayMedia(url)
                path = os.path.join(utils.epghome, 'player.py')
                xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d)' % (path, url, True))
                # utils.removeKeymap()

    AddAddon('TV Guide',   'script.tvguidedixie',     _SCRIPT,  icon=os.path.join(IMAGES, 'OTTV-TV_Guide.png'))
    AddAddon('Planner',    'plugin.video.ottplanner', _ADDON,   icon=os.path.join(IMAGES, 'OTTV-Planner.png'))

    if MOVIETAB:
        ShowMovie()
    if TVTAB:
        ShowTV()

    # if CATCHTAB:
    #     AddSubFolder('TV Catch Up', _CATCHUP,   icon=os.path.join(IMAGES, 'OTTV-TV_Catchup.png'), desc='Catch up on shows you have missed')

    # if SEARCHTAB:
    #     AddAddon('Search',          SUPERFAVES, _SUPERSEARCH, icon=os.path.join(IMAGES, 'OTTV-Search.png'), desc='Search all your favourite addons all from one place')

    # if FAVESTAB:
    #     AddAddon('Favourites',      SUPERFAVES, _ADDON,       icon=os.path.join(IMAGES, 'OTTV-Favourites.png'))

    if TOOLSTAB:
        AddAddon('Tools', 'script.tvguidedixie.tools', _SCRIPT, icon=os.path.join(IMAGES, 'OTTV-Tools.png'))
        # AddSubFolder('Tools',       _TOOLS,     icon=os.path.join(IMAGES, 'OTTV-Tools.png'),  desc='Settings and Tools')

    ShowShortcuts()
    ShowSFShortcuts(SFFILE, _REMOVESUPERFAVE)
    icon = os.path.join(IMAGES, 'OTTV-Shortcuts.png')

    if not KIOSKMODE:
        AddDir('Add more...', '', _ADDSHORTCUT, iconimage=icon, description='Browse and select other shortcuts', isFolder=False, isPlayable=False)


def ShowMovie():
    sfave = favourite.getFavourites(SFMOV) if SFMOV else []
    addon = utils.getSetting('MOVIE')

    if utils.getSetting('UseKodiLib') == 'true':
        AddLibrary('Movies', '', _MOVIE, icon=os.path.join(IMAGES, 'OTTV-Movies.png'))

    elif (len(sfave) == 0) and (addon == ''):
        AddLibrary('Movies', '', _MOVIEOPTIONS, icon=os.path.join(IMAGES, 'OTTV-Movies.png'))

    elif not addon == '':
        AddMovieLibrary('Movies', '', _MOVIEADDON, icon=os.path.join(IMAGES, 'OTTV-Movies.png'))

    else:
        ShowSFShortcuts(SFMOV, _REMOVESFMOVIE)


def ShowTV():
    sfave = favourite.getFavourites(SFTV) if SFTV else []
    addon = utils.getSetting('TV')

    if utils.getSetting('UseKodiLib') == 'true':
        AddLibrary('TV Shows', '', _TV, icon=os.path.join(IMAGES, 'OTTV-TV_Shows.png'))

    elif (len(sfave) == 0) and (addon == ''):
        AddLibrary('TV Shows', '', _TVOPTIONS, icon=os.path.join(IMAGES, 'OTTV-TV_Shows.png'))

    elif not addon == '':
        AddTVLibrary('TV Shows', '', _TVADDON, icon=os.path.join(IMAGES, 'OTTV-TV_Shows.png'))
    
    else:
        ShowSFShortcuts(SFTV, _REMOVESFTV)


def ShowCatchup():
    AddAddon('BBC iPlayer', 'plugin.video.iplayerwww', _ADDON, icon=os.path.join(IMAGES, 'OTTV-BBC_iPlayer.png'))
    AddAddon('ITV Player',  'plugin.video.itv',        _ADDON, icon=os.path.join(IMAGES, 'OTTV-ITV_Player.png'))
    AddAddon('UKTV Play',   'plugin.video.uktvplay',   _ADDON, icon=os.path.join(IMAGES, 'OTTV-UKTV_Play.png'))


def ShowTools():
    AddAddon('Add Channel Line-up', TOOLS,  _LINEUPS,       icon=os.path.join(IMAGES, 'OTTV-add-lineups.png'),     desc='Install customised channel line-ups created by the On-Tapp.TV Community.')
    AddAddon('Channels',            TOOLS,  _CHANNELS,      icon=os.path.join(IMAGES, 'OTTV-edit-channels.png'),   desc='Edit your channels - Change logos, change visibility, change order or even add your own!')
    AddAddon('Categories',          TOOLS,  _CATEGORIES2,   icon=os.path.join(IMAGES, 'OTTV-edit-categories.png'), desc='Edit your categories - Change a category name or remove a category altogether.')
    AddAddon('Back-up + Restore',   TOOLS,  _BACKUPRESTORE, icon=os.path.join(IMAGES, 'OTTV-backup-restore.png'),  desc='Make full back ups or just back-up your channel line-up.')
    AddAddon('Install Skins',       TOOLS,  _SKINS,         icon=os.path.join(IMAGES, 'OTTV-install-skins.png'),   desc='Install new skins and use them to change the EPG look and feel.')
    AddAddon('Install Logo-Packs',  TOOLS,  _LOGOS,         icon=os.path.join(IMAGES, 'OTTV-install-logos.png'),   desc='Install new logo-packs and use them in the EPG.')
    AddAddon('Update Add-on Links', TOOLS,  _INI,           icon=os.path.join(IMAGES, 'OTTV-update-addons.png'),   desc='Update the built-in Add-on links to 3rd party live TV add-ons available for Kodi.')
    AddVPNicity()


def ShowSettings(addonID):
    xbmc.executebuiltin('Addon.OpenSettings(%s)' % addonID)


def OpenTools():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.tvguidedixie.tools/",return)')


def PlayMedia(url, windowed=True):
    APPLICATION.setResolvedUrl(url, success=True, listItem=None, windowed=windowed)


def SelectSuperSearch(addonID):
    xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (WINDOWID, addonID, 25))


def ShowSFShortcuts(file, removeMode):
    if not SF_INSTALLED:
        return

    faves        = favourite.getFavourites(file)
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
        menu.append(('Remove %s Super Favourite' % (name), '?mode=%d&url=%s' % (removeMode, urllib.quote_plus(path))))

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
                AddA_scrddon(name, url, _SCRIPT, contextMenu=menu)
            else:
                AddAddon(name, url, _ADDON, contextMenu=menu)
        except:
            pass


def RemoveSFShortcut(file, url):
    return favourite.removeFave(file, url)  


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

    return AddSFShortcut(SFFILE)


def AddSFShortcut(file):
    if not chooser.GetFave('OTT'):
        return False

    path   = xbmc.getInfoLabel('Skin.String(OTT.Path)')
    label  = xbmc.getInfoLabel('Skin.String(OTT.Label)')
    icon   = xbmc.getInfoLabel('Skin.String(OTT.Icon)')
    folder = xbmc.getInfoLabel('Skin.String(OTT.IsFolder)') == 'true'

    if len(path) == 0 or path == 'noop':
        return False

    fave = [removeNumeric(label), icon, path] 
    favourite.copyFave(file, fave)

    return True


def AddAddonShortcut():
    shortcuts = utils.getSetting('ADDONS').split('|')

    #don't allow sortcut to self
    shortcuts.append(ADDONID)

    names  = getNames()
    addons = getAddons(names)

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
        addonID = 'plugin.program.vpnicity'

        AddDir('Select VPN', addonID, _VPNICITY, iconimage=os.path.join(IMAGES, 'OTTV-vpnicity.png'), description='Activate VPNicity Connect and pick a country.', isFolder=False, isPlayable=False)
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

    return [addon, home, profile, title, version, summary, desc, icon, fanart]


def RemoveVideo(url, setting):
    shortcut = utils.getSetting(setting)

    if url not in shortcut:
        return False

    update = shortcut.replace(url,  '')

    utils.setSetting(setting, update)

    return True


def AddVideoOptions(setting, file):
    if not SF_INSTALLED or utils.DialogYesNo(GETTEXT(30313), GETTEXT(30314), '', GETTEXT(30315), GETTEXT(30316)):
        return AddVideo(setting)

    return AddSFShortcut(file)


def AddVideo(setting):
    item = utils.getSetting(setting)

    if not item == '':
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/",return)' % (WINDOWID, item))
        return False

    return _AddVideoShortcut(setting)


def _AddVideoShortcut(setting):
    names  = getNames()
    addons = getAddons(names)

    option = xbmcgui.Dialog().select('Select addon', addons)

    if option < 0:
        return False

    update = names[option][1]

    utils.setSetting(setting, update)

    return True


def getAddons(names):
    addons = []

    for name in names:
        addons.append(name[0])

    if addons < 0:
        return False

    return addons


def getNames():
    import glob
    path  = xbmc.translatePath(os.path.join('special://home' , 'addons', '*.*'))
    names = []

    for addon in glob.glob(path):
        try:
            name     = addon.rsplit(os.path.sep, 1)[-1]
            realname = xbmcaddon.Addon(name).getAddonInfo('name')
            provides = xbmcaddon.Addon(name).getAddonInfo('type')

            if (provides == 'xbmc.python.pluginsource') or (provides == 'xbmc.python.script'):
                names.append([Capitalize(realname), name])
        except:
            pass

    if len(names) < 1:
        return

    names.sort()

    return names


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


def AddLibrary(name, windowID, mode, icon=None, fanart=None, desc='', contextMenu=''):
    if icon == None:
        icon = ICON

    if fanart == None:
        fanart = FANART

    AddDir(name, '', mode, icon, '', '', '', fanart, contextMenu='')


def AddMovieLibrary(name, windowID, mode, icon=None, fanart=None, desc='', contextMenu=''):
    addon = utils.getSetting('MOVIE')
    
    if addon == '':
        if icon == None:
            icon = ICON

        if fanart == None:
            fanart = FANART

        AddDir(name, '', mode, icon, '', '', '', fanart, contextMenu='')

    try:    properties = GetAddon(addon)
    except: return

    if not addon == '':
        icon = properties[7]

    if not addon == '':
        fanart = properties[8]

    # name = xbmcaddon.Addon(addon).getAddonInfo('name')
    menu = []
    menu.append(('Remove %s shortcut' % Capitalize(name),'?mode=%d&url=%s' % (_REMOVEMOVIE, urllib.quote_plus(addon))))

    AddDir(name, '', mode, icon, '', '', '', fanart, contextMenu=menu)


def AddTVLibrary(name, windowID, mode, icon=None, fanart=None, desc='', contextMenu=''):
    addon = utils.getSetting('TV')

    if addon == '':
        if icon == None:
            icon = ICON

        if fanart == None:
            fanart = FANART

        AddDir(name, '', mode, icon, '', '', '', fanart, contextMenu='')

    try:    properties = GetAddon(addon)
    except: return

    if not addon == '':
        icon = properties[7]

    if not addon == '':
        fanart = properties[8]

    # name = xbmcaddon.Addon(addon).getAddonInfo('name')
    menu = []
    menu.append(('Remove %s shortcut' % Capitalize(name),'?mode=%d&url=%s' % (_REMOVETV, urllib.quote_plus(addon))))

    AddDir(name, '', mode, icon, '', '', '', fanart, contextMenu=menu)


def ShowCategories(categoriesList):
    d = categories.CategoriesMenu(categoriesList)
    d.doModal()
    categoriesList = d.currentCategories
    del d
    
    categories.setSetting('categories', '|'.join(categoriesList))


def GetINI():
    line1 = 'We will now download the latest add-on integration files.'
    line2 = 'Please wait a minute or two. After that...'
    line3 = 'The updates will be active the next time you open the EPG.'

    utils.DialogOK(line1, line2, line3)

    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/getIni.py)'
    xbmc.executebuiltin(cmd)


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


def get_params(path):
    params = {}
    path   = path.split('?', 1)[-1]
    pairs  = path.split('&')

    for pair in pairs:
        split = pair.split('=')
        if len(split) > 1:
            params[split[0]] = urllib.unquote_plus(split[1])

    return params


    
def onBack(application, _params):
    pass

    
def onParams(application, _params):
    global APPLICATION
    APPLICATION = application

    params = get_params(_params)
    mode   = None

    try:    mode = int(params['mode'])
    except: pass

    try:    url = params['url']
    except: url = None

    refresh = False

    if mode == _SCRIPT:
        cmd = 'RunScript(%s)' % url
        xbmc.executebuiltin(cmd)


    elif mode == _ADDON:
        #utils.removeKeymap()
        cmd = 'ActivateWindow(%d,"plugin://%s/",return)' % (WINDOWID, url)
        xbmc.executebuiltin(cmd)


    elif mode == _SUPERFAVE:
        try:
            import player
            player.playCommand(url)
        except:
            pass


    elif mode == _REMOVESUPERFAVE:
        refresh = RemoveSFShortcut(SFFILE, url)


    elif mode == _REMOVESFMOVIE:
        refresh = RemoveSFShortcut(SFMOV, url)


    elif mode == _REMOVESFTV:
        refresh = RemoveSFShortcut(SFTV, url)


    elif mode == _MOVIE:
        xbmc.executebuiltin('ActivateWindow(10025,videodb://1/2,return)')


    elif mode == _TV:
        xbmc.executebuiltin('ActivateWindow(10025,videodb://2/2,return)')


    elif mode == _MOVIEOPTIONS:
        refresh = AddVideoOptions('MOVIE', SFMOV)


    elif mode == _TVOPTIONS:
        refresh = AddVideoOptions('TV', SFTV)


    elif mode == _MOVIEADDON:
        refresh = AddVideo('MOVIE')


    elif mode == _TVADDON:
        refresh = AddVideo('TV')


    elif mode == _CATEGORIES1:
        ShowCategories(categoriesList)


    elif mode == _SETTINGS:
        ShowSettings()


    elif mode == _INI:
        GetINI()


    elif mode == _CHANNELS:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 1900))


    elif mode == _CATEGORIES2:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 1910))


    elif mode == _SKINS:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 2000))


    elif mode == _LOGOS:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 2100))


    elif mode == _LINEUPS:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 2200))


    elif mode == _BACKUPRESTORE:
        xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d")' % (10025, TOOLS, 1950))


    elif mode == _TOOLS:
        xbmc.executebuiltin('RunScript(script.tvguidedixie.tools),return')
        # xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.tvguidedixie.tools/?content_type=video",return)')
        # ShowTools()


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
        refresh = AddShortcut()


    elif mode == _REMOVESHORTCUT:
        refresh = RemoveShortcut(url)


    elif mode == _REMOVEMOVIE:
        refresh = RemoveVideo(url, 'MOVIE')


    elif mode == _REMOVETV:
        refresh = RemoveVideo(url, 'TV')
    
    else:
        Main()

    if refresh:
        APPLICATION.containerRefresh()
