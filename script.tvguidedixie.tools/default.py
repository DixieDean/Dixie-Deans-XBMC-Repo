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

_OTT          = 0
_MAIN         = 100
_CHANNEL      = 200
_RENAME       = 300
_TOGGLESORT   = 400
_SETTINGS     = 500
_LOGO         = 600
_SELECT       = 700
_CANCELSELECT = 800
_INSERTABOVE  = 900
_INSERTBELOW  = 1000


# --------------------- Addon Settings --------------------- #

ALPHASORT = ADDON.getSetting('SORT').lower() == 'alphabetical'

# ---------------------------------------------------------- #


# --------------------- 'Global' Variables --------------------- #

START_WEIGHT = -1
END_WEIGHT   = -1

try:    
    START_WEIGHT = int(xbmcgui.Window(10000).getProperty('OTT_TOOLS_START'))

    try:   
        END_WEIGHT = int(xbmcgui.Window(10000).getProperty('OTT_TOOLS_END'))
    except: 
        pass
except: 
    pass

# -------------------------------------------------------------- #



def main():
    utils.CheckVersion()

    channels   = getAllChannels(ALPHASORT)
    totalItems = len(channels)
    count      = 1

    for ch in channels:        
        channel = ch[2]
        id      = ch[1]         
        title   = channel.title
        logo    = channel.logo
        weight  = channel.weight

        menu  = []
        menu.append(('Rename channel', 'XBMC.RunPlugin(%s?mode=%d&id=%s)' % (sys.argv[0], _RENAME, urllib.quote_plus(id))))
        menu.append(('Change logo',    'XBMC.RunPlugin(%s?mode=%d&id=%s)' % (sys.argv[0], _LOGO,   urllib.quote_plus(id))))

        if weight != START_WEIGHT and weight != END_WEIGHT:
            menu.append(('Select Channel', 'XBMC.RunPlugin(%s?mode=%d&id=%s&weight=%d)' % (sys.argv[0], _SELECT, urllib.quote_plus(id), weight)))

        if inSelection(weight):
            #title = '[COLOR red]' + title  + '[/COLOR]'
            title = '[I]' + title  + '[/I]'
        elif isSelection():
            menu.append(('Insert Above', 'XBMC.RunPlugin(%s?mode=%d&weight=%d)' % (sys.argv[0], _INSERTABOVE, weight)))
            menu.append(('Insert Below', 'XBMC.RunPlugin(%s?mode=%d&weight=%d)' % (sys.argv[0], _INSERTBELOW, weight)))

        if START_WEIGHT > -1:
            menu.append(('Clear Selection', 'XBMC.RunPlugin(%s?mode=%d)' % (sys.argv[0], _CANCELSELECT)))

        count += 1

        addStdMenu(menu)

        addDir(title, _CHANNEL, id, thumbnail=logo, fanart=FANART, isFolder=True, menu=menu, infolabels={}, totalItems=totalItems)


def insertSelection(above, theWeight):
    channels   = getAllChannels() #these will be sorted by weight

    toMove   = []
    original = []

    while len(channels) > 0:
        channel = channels.pop(0)
        weight  = channel[2].weight
        if inSelection(weight):
            toMove.append(channel)
        else:
            original.append(channel)

    fullList = []

    if above:
        fullList = insertAbove(theWeight, original, toMove)
    else:
        fullList = insertBelow(theWeight, original, toMove)

    writeChannelsToFile(fullList)

    cancelSelection()
    
    return True


def insertBelow(theWeight, original, toMove):
    fullList = []

    inserted = False

    for channel in original:
        weight = channel[2].weight

        if weight > theWeight and not inserted:
            inserted = True
            for ch in toMove:
                fullList.append(ch)
                   
        fullList.append(channel)

    #special case if inserting below bottom
    if not inserted:
        for ch in toMove:
            fullList.append(ch)

    return fullList


def insertAbove(theWeight, original, toMove):
    fullList = []

    inserted = False

    for channel in original:
        weight = channel[2].weight

        if weight >= theWeight and not inserted:
            inserted = True
            for ch in toMove:
                fullList.append(ch)

        fullList.append(channel)

    return fullList
  
        

def inSelection(weight):
    return weight >= START_WEIGHT and weight <= END_WEIGHT


def isSelection():
    return START_WEIGHT > -1

    
def cancelSelection():
    xbmcgui.Window(10000).clearProperty('OTT_TOOLS_START')
    xbmcgui.Window(10000).clearProperty('OTT_TOOLS_END')
    return True


def selectChannel(weight):
    value = str(weight)

    if START_WEIGHT < 0: # nothing set
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_START', value)
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_END',   value)
        return True

    if weight > END_WEIGHT: #after current end
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_END', value)
        return True

    if weight > START_WEIGHT and END_WEIGHT < 0: #only start set
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_END', value)
        return True

    if weight > START_WEIGHT and weight < END_WEIGHT: #between current start and end
        startDelta = weight     - START_WEIGHT
        endDelta   = END_WEIGHT - weight
        if startDelta < endDelta:
            xbmcgui.Window(10000).setProperty('OTT_TOOLS_START', value)
        else:
            xbmcgui.Window(10000).setProperty('OTT_TOOLS_END', value)
        return True

    if weight < START_WEIGHT and END_WEIGHT < 0: #before start, end not set
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_START', value)
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_END',   str(START_WEIGHT))
        return True

    if weight < START_WEIGHT:
        xbmcgui.Window(10000).setProperty('OTT_TOOLS_START', value)
        return True

    return False


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



def writeChannelsToFile(fullList):
    weight = 1
    for item in fullList:
        id        = item[1]
        ch        = item[2]
        ch.weight = weight
        weight   += 1

        updateChannel(ch, id)
        

def getAllChannels(alphaSort = False):
    channels = []

    try:
        current, dirs, files = os.walk(OTT_CHANNELS).next()
    except Exception, e:
        return channels
    
    for file in files:
        channels.append(file)

    sorted = []

    for id in channels:
        channel = getChannelFromFile(id)

        sorter  = channel.title.lower() if ALPHASORT else channel.weight

        sorted.append([sorter, id, channel])

    sorted.sort()

    return sorted



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

    liz = xbmcgui.ListItem(label, iconImage=thumbnail, thumbnailImage=thumbnail)

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
utils.log(params)


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


if mode == _SELECT:
    try:    
        weight = int(params['weight'])
        doRefresh = selectChannel(weight)
    except:
        doRefresh = False


if mode == _CANCELSELECT:
    doRefresh = cancelSelection()


if mode == _INSERTABOVE:
    try:
        weight = int(params['weight'])
        doRefresh = insertSelection(above=True, theWeight=weight)
    except:
        pass


if mode == _INSERTBELOW:
    try:
        weight = int(params['weight'])
        doRefresh = insertSelection(above=False, theWeight=weight)
    except:
        pass


if doRefresh:
    refresh()


xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=cacheToDisc)
