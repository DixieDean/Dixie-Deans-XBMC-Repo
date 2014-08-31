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
import xbmcplugin
import xbmcgui

import urllib
import os

import utils

from channel import Channel


OTT_TITLE    = utils.OTT_TITLE
OTT_ADDON    = utils.OTT_ADDON
OTT_PROFILE  = utils.OTT_PROFILE
OTT_CHANNELS = utils.OTT_CHANNELS


ADDONID  = utils.ADDONID
ADDON    = utils.ADDON
HOME     = utils.HOME
PROFILE  = utils.PROFILE
VERSION  = utils.VERSION
ICON     = utils.ICON
FANART   = utils.FANART


GETTEXT  = utils.GETTEXT
TITLE    = utils.TITLE
FRODO    = utils.FRODO
GOTHAM   = utils.GOTHAM



# -----Addon Modes ----- #

_OTT        = 0
_MAIN       = 100
_CHANNEL    = 200
_RENAME     = 300
_TOGGLESORT = 400
_SETTINGS   = 500
_LOGO       = 600


# --------------------- Addon Settings --------------------- #

ALPHASORT = ADDON.getSetting('SORT').lower() == 'alphabetical'

# ---------------------------------------------------------- #


def main():
    utils.CheckVersion()

    channels = getAllChannels()

    sorted = []

    for id in channels:
        channel = getChannelFromFile(id)
        title   = channel.title
        logo    = channel.logo

        sorter  = channel.title.lower() if ALPHASORT else channel.weight

        sorted.append([sorter, title, id, logo])

    sorted.sort()
    totalItems = len(sorted)

    for ch in sorted:
        title   = ch[1]
        id      = ch[2]
        logo    = ch[3]

        menu  = []
        menu.append(('Rename channel', 'XBMC.RunPlugin(%s?mode=%d&id=%s)' % (sys.argv[0], _RENAME, urllib.quote_plus(ch[2]))))
        menu.append(('Change logo',    'XBMC.RunPlugin(%s?mode=%d&id=%s)' % (sys.argv[0], _LOGO,   urllib.quote_plus(ch[2]))))

        addStdMenu(menu)

        addDir(title, _CHANNEL, id, thumbnail=logo, fanart=FANART, isFolder=True, menu=menu, infolabels={}, totalItems=totalItems)


def addStdMenu(menu):
    sort = 'Sort by ONTapp.TV Order' if ALPHASORT else 'Sort Alphabetically'
    menu.append((sort, 'XBMC.RunPlugin(%s?mode=%d)' % (sys.argv[0], _TOGGLESORT)))

    menu.append(('Launch ONTapp.TV', 'XBMC.RunPlugin(%s?mode=%d)' % (sys.argv[0], _OTT)))

    menu.append(('Add-on settings', 'XBMC.RunPlugin(%s?mode=%d)' % (sys.argv[0], _SETTINGS)))


def toggleSort():
    if ALPHASORT:
        ADDON.setSetting('SORT', 'ONTapp.TV Order')
    else:
        ADDON.setSetting('SORT', 'Alphabetical')

    return True


def rename(id):
    channel = getChannelFromFile(id)    
    title   = channel.title
    
    name = getText('Rename Channel', text=title)

    if not name:
        return False

    if name == title:
        return False

    if len(name) == 0:
        return False

    channel.title = name

    return updateChannel(channel, id)


def updateLogo(id):
    channel = getChannelFromFile(id)    
    logo    = channel.logo

    logo = getImage(logo)

    if not logo:
        return False

    logo = convertToHome(logo)

    channel.logo = logo

    return updateChannel(channel, id)



def getImage(logo):
    logo = logo.replace('\\', '/')
    root  = logo.rsplit('/', 1)[0] + '/'
    image = xbmcgui.Dialog().browse(2, 'Choose logo', 'files', '', False, False, root)
    
    if image and image != root:
        return image

    return None


def convertToHome(image):
    HOMESPECIAL = 'special://home/'
    HOMEFULL    = xbmc.translatePath(HOMESPECIAL)

    if image.startswith(HOMEFULL):
        image = image.replace(HOMEFULL, HOMESPECIAL)

    return image


def updateChannel(channel, id):
    path = os.path.join(OTT_CHANNELS, id) 

    try:    f = open(path, mode='w')
    except: return

    try:    f.write(channel.id.encode('utf8') + '\n')
    except: f.write(channel.id + '\n')

    f.write(channel.title.encode('utf8') + '\n')

    if channel.logo:
        f.write(channel.logo.encode('utf8') + '\n')
    else:
        f.write('\n')

    if channel.streamUrl:
        f.write(channel.streamUrl.encode('utf8') + '\n')
    else:
        f.write('\n')

    if channel.visible:
        f.write('1\n')
    else:
        f.write('0\n')

    f.write(str(channel.weight) + '\n')
    f.write(channel.categories.encode('utf8') + '\n')

    f.close()

    return True


def getAllChannels():
    channels = []

    try:
        current, dirs, files = os.walk(OTT_CHANNELS).next()
    except Exception, e:
        return channels
    
    for file in files:
        channels.append(file)

    return channels


def getChannelFromFile(id):
    path = os.path.join(OTT_CHANNELS, id)

    if not os.path.exists(path):
        return None

    f = open(path, mode='r')
    cfg = f.readlines()
    f.close
        
    ch = Channel(cfg[0].replace('\n', ''), cfg[1].replace('\n', ''), cfg[2].replace('\n', ''), cfg[3].replace('\n', ''), cfg[4].replace('\n', ''), cfg[5].replace('\n', ''), cfg[6].replace('\n', ''))

    return ch


def getText(title, text='', hidden=False):
    kb = xbmc.Keyboard(text, title)
    kb.setHiddenInput(hidden)
    kb.doModal()
    if not kb.isConfirmed():
        return None

    text = kb.getText().strip()

    if len(text) < 1:
        return None

    return text


def openSettings():
    ADDON.openSettings()
    return True



def refresh():
    xbmc.executebuiltin('Container.Refresh')

    
def addDir(label, mode, id = '', thumbnail='', fanart=FANART, isFolder=True, menu=None, infolabels={}, totalItems=0):
    u  = sys.argv[0]

    u += '?label=' + urllib.quote_plus(label)
    u += '&mode='  + str(mode)

    if len(id) > 0:
        u += '&id=' + urllib.quote_plus(id)

    if len(thumbnail) > 0:
        u += '&image=' + urllib.quote_plus(thumbnail)

    if len(fanart) > 0:
        u += '&fanart=' + urllib.quote_plus(fanart)

    liz = xbmcgui.ListItem(urllib.unquote_plus(label), iconImage=thumbnail, thumbnailImage=thumbnail)

    if len(infolabels) > 0:
        liz.setInfo(type='Video', infoLabels=infolabels)

    if menu:
        liz.addContextMenuItems(menu, replaceItems=True)

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder, totalItems=totalItems)

   
def get_params(p):
    param=[]
    paramstring=p
    if len(paramstring)>=2:
        params=p
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
           params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param


params = get_params(sys.argv[2])


doRefresh   = False
cacheToDisc = True


try:    mode = int(params['mode'])
except: mode = _MAIN

try:    id = urllib.unquote_plus(params['id'])
except: id = ''

    
utils.log(sys.argv[2])
utils.log(sys.argv)
utils.log('Mode = %d' % mode)


if mode == _MAIN:
    main()


if mode == _RENAME:
    doRefresh = rename(id)
    

if mode == _LOGO:
    doRefresh = updateLogo(id)


if mode == _TOGGLESORT:
    doRefresh = toggleSort()


if mode == _OTT:
    xbmc.executebuiltin('RunScript(script.tvguidedixie)')


if mode == _SETTINGS:
    doRefresh = openSettings()


if doRefresh:
    refresh()


xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=cacheToDisc)
