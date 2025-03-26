# -*- coding: utf-8 -*-
#
#       Copyright (C) 2014-
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
import re

import utilsTOOLS as utils
import lineuptools as tools

import sfile

import sys
path    = utils.OTT_HOME
sys.path.insert(0, path)

import categories

import channel as Channel
import session

session = session.loadSession()


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
DATAPATH = utils.DATAPATH

#FAVE_POSTFIX = utils.FAVE_POSTFIX


GETTEXT  = utils.GETTEXT
TITLE    = utils.TITLE
FRODO    = utils.FRODO
GOTHAM   = utils.GOTHAM
BASEURL  = utils.GetBaseUrl()


EXTRAS   = os.path.join(OTT_PROFILE, 'extras')
SKIN     = utils.getSetting('SKIN')
IMAGES   = os.path.join(PROFILE, 'skins', SKIN, 'resources', 'skins', 'Default', 'media')


# -----Addon Modes ----- #

_OTT            = 0
_MAIN           = 100
_EDIT           = 200
_RENAME         = 300
_TOGGLESORT     = 400
_SETTINGS       = 500
_LOGO           = 600
_SELECT         = 700
_CANCELSELECT   = 800
_INSERTABOVE    = 900
_INSERTBELOW    = 1000
_TOGGLEHIDE     = 1100
_HIDE           = 1200
_SHOW           = 1300
_PLAY           = 1400
_EDIT           = 1500
_NEWCHANNEL     = 1600
_REMOVE         = 1700
_CLONE          = 1800
_EDITCHANNELS   = 1900
_OFFSET         = 2000

_EDITCATEGORIES   = 1910
_EDITCATEGORY     = 1920
_BULKEDITCATEGORY = 1930
#_RENAMEFAVOURITE  = 1940

_BACKUPRESTORE   = 1950
_BACKUPCHANNELS  = 1960
_RESTORECHANNELS = 1970
_FULLBACKUP      = 1980
_FULLRESTORE     = 1990

_ADDSKINSLIST  = 2030
_INILINEUP     = 2040
_IPTVLINEUP    = 2050
_ADDLOGOSLIST  = 2100
_ADDLINEUPLIST = 2200
_GETSKINS      = 2300
_GETLOGOS      = 2400
_GETLINEUPS    = 2500

_MAKEALPHA     = 2600
_INI           = 2700
_RECORD        = 2800
_FIXHOME       = 2900


# ------------------------ Globals ------------------------ #
global ALPHASORT 
global SHOWHIDDEN
global SHOWSTREAM
global KODISOURCE
global USERLOGOS
global APPLICATION
global START_WEIGHT
global END_WEIGHT

xbmcgui.Window(10000).setProperty('OTT_TOOLS_TITLE', TITLE)

def initGlobals(application):
    global ALPHASORT 
    global SHOWHIDDEN
    global SHOWSTREAM
    global KODISOURCE
    global USERLOGOS
    global APPLICATION
    global START_WEIGHT
    global END_WEIGHT

    ALPHASORT  = ADDON.getSetting('SORT').lower()       == 'alphabetical'
    SHOWHIDDEN = ADDON.getSetting('SHOWHIDDEN').lower() == 'true'
    SHOWSTREAM = ADDON.getSetting('SHOWSTREAM').lower() == 'true'

    KODISOURCE =  ADDON.getSetting('KODISOURCE') == 'true'
    USERLOGOS  =  OTT_ADDON.getSetting('logo.type') == '1'

    APPLICATION = application

    START_WEIGHT = -1
    END_WEIGHT   = -1

    if not ALPHASORT:
        try:    START_WEIGHT = int(xbmcgui.Window(10000).getProperty('OTT_TOOLS_START'))
        except: pass

        try:    END_WEIGHT = int(xbmcgui.Window(10000).getProperty('OTT_TOOLS_END'))
        except: pass

# -------------------------------------------------------------- #

def main():
    utils.CheckVersion()

    menu = []
    menu.append(('Add-on settings', '?mode=%d' % (_SETTINGS)))

    try:
        _ = xbmcaddon.Addon(id = 'plugin.video.ottplanner')
        addDir('Enable/Disable Recording Feature',  _RECORD,          thumbnail=ICON, fanart=FANART, isFolder=False, menu=menu)
    except:
        pass

    addDir('Add Channel Line-up',               _ADDLINEUPLIST,   thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu, desc='Install customised channel line-ups created by the On-Tapp.TV Community')
    addDir('Edit Channels',                     _EDITCHANNELS,    thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu, desc='Change logos, change visibility, change order or even add your own!')
    addDir('Edit Categories',                   _EDITCATEGORIES,  thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu, desc='Add new categories[CR]Change a category name or remove a category altogether')
    addDir('Back-up + Restore',                 _BACKUPRESTORE,   thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu, desc='Make full back ups or just back-up your channel line-up')
    addDir('Add Skins',                         _ADDSKINSLIST,    thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu, desc='Install new skins and use them to change the EPG look and feel')
    addDir('Add Logo Packs',                    _ADDLOGOSLIST,    thumbnail=ICON, fanart=FANART, isFolder=True,   menu=menu)
    #addDir('Rename Favourites Category',        _RENAMEFAVOURITE, thumbnail=ICON, fanart=FANART, isFolder=False, menu=menu)
    addDir('Set Alphabetical Channel Order',    _MAKEALPHA,       thumbnail=ICON, fanart=FANART, isFolder=False,  menu=menu)
    addDir('Update Add-on Links',               _INI,             thumbnail=ICON, fanart=FANART, isFolder=False,  menu=menu)
    addDir('Create Line-up from INI File',      _INILINEUP,       thumbnail=ICON, fanart=FANART, isFolder=False,  menu=menu)
    addDir('Create Line-up from IPTV Settings', _IPTVLINEUP,      thumbnail=ICON, fanart=FANART, isFolder=False,  menu=menu)
    addDir('Update Home Page Skin',             _FIXHOME,         thumbnail=ICON, fanart=FANART, isFolder=False,  menu=menu)


def createINILineup():
    tools.createINIFileLineup()


def createIPTVLineup():
    tools.createIPTVLineup()


def getSkinList(id):
    regex = 'skin name="(.+?)" url="(.+?)" icon="(.+?)" fanart="(.+?)" description="(.+?)"'
    url   =  BASEURL + 'skins/'

    skins = url + 'skinlist.xml'
    req   = session.get(skins)
    html  = req.content
    items = re.compile(regex).findall(html)

    for item in items:
        label  = item[0]
        id     = url + item[1]
        icon   = url + item[2]
        fanart = url + item[3]
        desc   = item[4]

        addDir(label, _GETSKINS, id, desc=desc, thumbnail=icon, fanart=fanart, isFolder=False)


def getSkin(label, url):
    path    = os.path.join(EXTRAS, 'skins')
    zipfile = os.path.join(path,   'skins.zip')

    if not sfile.exists(path):
        sfile.makedirs(path)

    if utils.DialogYesNo('Would you like to install ' + label, 'and make it your active skin?', 'It will be downloaded and installed into your system.'):
        utils.download(url, path, zipfile)
        utils.DialogOK(label + ' skin has been installed successfully.', 'It is now set as your active EPG skin.', 'Please restart On-Tapp.TV. Thank you.')
        OTT_ADDON.setSetting('dixie.skin', label)


def getLogosList(id):
    regex = 'logopack name="(.+?)" url="(.+?)" icon="(.+?)" fanart="(.+?)" description="(.+?)"'
    url   =  BASEURL + 'logos/'

    logos = url + 'logopacklist.xml'
    req   = session.get(logos)
    html  = req.content
    items = re.compile(regex).findall(html)

    for item in items:
        label  = item[0]
        id     = url + item[1]
        icon   = url + item[2]
        fanart = url + item[3]
        desc   = item[4]
           
        addDir(label, _GETLOGOS, id, desc=desc, thumbnail=icon, fanart=fanart, isFolder=False)


def getLogos(label, url):
    path    = os.path.join(EXTRAS, 'logos')
    zipfile = os.path.join(path,   'logos.zip')

    if not sfile.exists(path):
        sfile.makedirs(path)

    if utils.DialogYesNo('Would you like to install ' + label, 'and make it your active logo-pack?', 'It will be downloaded and installed into your system.'):
        utils.download(url, path, zipfile)
        utils.DialogOK(label + ' logo-pack has been installed successfully.', 'It is now set as your active logo-pack.', 'Please restart On-Tapp.TV. Thank you.')
        OTT_ADDON.setSetting('dixie.logo.folder', label)


def getLineupList():
    baseurl = BASEURL + 'lineups/'

    url = baseurl + 'lineups.json'
    req = session.get(url)

    response = req.json()
    result   = response['lineups']

    lineups  = result['lineup']

    for lineup in lineups:
        label = lineup['-name']
        id     = baseurl + lineup['-url']
        icon   = baseurl + lineup['-icon']
        fanart = baseurl + lineup['-fanart']
        sfZip  = baseurl + lineup['-sfzip']
        isSF   = lineup['-sf'].lower() == 'true'
        desc   = lineup['-description']

        addDir(label, _GETLINEUPS, id, desc=desc, thumbnail=icon, fanart=fanart, isSF=isSF, sfZip=sfZip, isFolder=False)


def getLineups(label, url, isSF, sfZip):
    path    = OTT_PROFILE
    zipfile = os.path.join(path, 'lineups.zip')
    chandir = OTT_CHANNELS #os.path.join(path, 'channels')

    line1    = 'Would you like to [COLOR orange]INSTALL[/COLOR] ' + label + ' line-up'
    line2    = 'or [COLOR orange]MERGE[/COLOR] it with your existing line-up?'
    line3    = ''
    nolabel  = 'MERGE'
    yeslabel = 'INSTALL'

    noChannels = True

    try:
        current, dirs, files = sfile.walk(OTT_CHANNELS)
        noChannels = not bool(files)
    except Exception as e:
        noChannels = True
    
    if noChannels or utils.DialogYesNo(line1, line2, line3, nolabel, yeslabel):
        if isSF:
            utils.DialogOK(label + ' requires some links added to your Super Favourites', 'We will install these first and then install your line-up', 'Thank you.')
            utils.installSF(sfZip)

        if os.path.isdir(chandir):
            sfile.rmtree(chandir)

        utils.deleteCFG()
        # sfile.remove(os.path.join(OTT_PROFILE, 'catfile'))

        utils.download(url, path, zipfile)
        OTT_ADDON.setSetting('dixie.lineup', label)

        categories.verifyCategories()

        utils.DialogOK(label + ' line-up has been installed successfully.', 'It is now set as your active channel line-up.')

    else:
        if tools.mergeLineups(label, isSF, sfZip, url):
            pass
            #utils.DialogOK(label + ' line-up has been merged successfully.', 'It is now part of your active channel line-up.')

    

def editChannels():
    channels   = getAllChannels(ALPHASORT)
    totalItems = len(channels)

    cats = getCategoriesList()
    cat_dict = { cat[1]:cat[0] for cat in cats }

    for ch in channels:
        channel    = ch[2]
        hidden     = channel.visible == 0

        if hidden and not SHOWHIDDEN:
            continue

        id         = ch[1]
        title      = channel.title
        logo       = channel.logo
        weight     = channel.weight
        stream     = channel.streamUrl
        userDef    = channel.userDef == 1
        desc       = channel.desc
        categories = channel.categories
        isClone    = channel.isClone == 1

        menu  = []
        #menu.append(('Rename channel', '?mode=%d&id=%s' % (_RENAME, urllib.quote_plus(id))))
        #menu.append(('Change logo',    '?mode=%d&id=%s' % (_LOGO,   urllib.quote_plus(id))))
        menu.append(('Edit channel',   '?mode=%d&id=%s' % (_EDIT,   urllib.quote_plus(id))))

        if inSelection(weight):
            menu.append(('Bulk edit categories', '?mode=%d' % (_BULKEDITCATEGORY)))
            menu.append(('Hide selection',       '?mode=%d' % (_HIDE)))
            if SHOWHIDDEN:
                menu.append(('Show selection', '?mode=%d' % (_SHOW)))
        else:
            hideLabel = 'Show channel' if hidden else 'Hide channel'
            menu.append((hideLabel, '?mode=%d&id=%s' % (_TOGGLEHIDE, urllib.quote_plus(id))))

        if (not ALPHASORT) and (weight != START_WEIGHT) and (weight != END_WEIGHT):
            menu.append(('Select channel', '?mode=%d&id=%s&weight=%d' % (_SELECT, urllib.quote_plus(id), weight)))

        if inSelection(weight):
            pass

        elif isSelection() and (not ALPHASORT):
            menu.append(('Insert selection above',   '?mode=%d&weight=%d' % (_INSERTABOVE, weight)))
            menu.append(('Insert selection below',   '?mode=%d&weight=%d' % (_INSERTBELOW, weight)))

        if START_WEIGHT > -1:
            menu.append(('Clear selection', '?mode=%d' % (_CANCELSELECT)))

        if not userDef:
            menu.append(('Clone channel', '?mode=%d&id=%s' % (_CLONE, urllib.quote_plus(id))))

        menu.append(('Set time offset', '?mode=%d&id=%s' % (_OFFSET, urllib.quote_plus(id))))

        menu.append(('Create new channel', '?mode=%d' % (_NEWCHANNEL)))

        if userDef or isClone:
            menu.append(('Remove channel', '?mode=%d&id=%s' % (_REMOVE, urllib.quote_plus(id))))

        #if len(stream):
        #    menu.append(('Activate stream', '?mode=%d&stream=%s' % (_PLAY, urllib.quote_plus(stream))))

        addStdMenu(menu)

        desc = []
        if userDef:
            desc.append('%s (user-defined)' % title)
        elif isClone:
            desc.append('%s (clone)' % title)
        else:
            desc.append(title)
        
        #if SHOWSTREAM and stream:
        #    desc.append(stream)

        if channel.desc:
            desc.append(channel.desc)

        if categories:
            desc.append('')
        for cat in categories:
            if cat in cat_dict:
                desc.append('    %s' % cat_dict[cat])

        desc = '[CR]'.join(desc)

        #title = title + '[COLOR orange] %r [/COLOR]' % categories #TODO

        #if userDef:
        #    title += ' (user-defined)'

        #if SHOWSTREAM:
        #    if len(stream) > 0:
        #        title += ' (stream set)'

        #if len(desc):
        #    title += ' - %s' % desc

        if hidden:
            title = '[COLOR red]' + title  + '[/COLOR]'

        if inSelection(weight):
            title = '[I]' + title  + '[/I]'

        addDir(title, _EDIT, id, weight=weight, thumbnail=logo, fanart=FANART, isFolder=False, menu=menu, infolabels={}, totalItems=totalItems, desc=desc)


def editCategories():
    cats = getCategoriesList()
    for category in sorted(cats, key=lambda x: x[0].upper()):
        addDir(category[0], _EDITCATEGORY, id=category[1], isFolder=False)


def getCategoriesList():
    cat_file = categories.readCatFile()
    cats = []
    for category in cat_file:
        category      = category.split(',')
        id            = int(category[0])
        name          = category[1]
        cats.append((name, id))

    return cats


def editCategory(category):
    ADD    = 101
    RENAME = 201
    REMOVE = 301

    menu = []
    menu.append(['Add new category',    ADD])
    menu.append(['Rename category', RENAME])
    menu.append(['Remove category', REMOVE])

    option = selectMenu(category, menu)

    if option == ADD:
        return addNewCategory()

    if option == RENAME:
        return renameCategory(category)

    if option == REMOVE:
        return removeCategory(category)

    return False


def addNewCategory():
    newcat = None
    cats = getCategoriesList()
    names = [x[0].upper() for x in cats]

    while newcat is None:
        newcat = utils.GetText('Add new category')
        if not newcat:
            return False

        if newcat.upper() in names:
            utils.DialogOK("'%s' category already exists" % newcat, 'Please enter a unique category name')
            newcat = None
            
    ids = [x[1] for x in cats]
    ids.sort()
    newId = ids[-1] + 1

    newCats = categories.readCatFile()

    newCats.append('%d,%s,1' % (newId, newcat))  # new categories default to be visible
    categories.writeCatFile(newCats)

    return True


def getCategoryByID(categoryID):
    categoryID = int(categoryID)
    cats = getCategoriesList()
    for category in cats:
        if categoryID == category[1]:
            return category

    return None


def renameCategory(category):
    newcat = None

    while newcat is None:
        newcat = utils.GetText('Rename %s' % category[0])
        if not newcat:
            return False

    if newcat.upper() == category[0].upper():
        return

    id = category[1]

    cats = getCategoriesList()
    
    newCats  = []
    cat_file = categories.readCatFile()

    for category in cat_file:
        cat  = category.split(',')

        if id == int(cat[0]):
            visible = cat[2]
            newCats.append('%d,%s,%s' % (id, newcat, visible))
        else:
            newCats.append(category)

    categories.writeCatFile(newCats)

    return True


def removeCategory(category):
    id = category[1]

    if id == 0:
        utils.DialogOK("You cannot remove the 'Favourites' category")
        return False

    if not utils.DialogYesNo(category[0], 'Are you sure you wish to remove this category'):
        return False

    found = False

    newCats  = []
    cat_file = categories.readCatFile()

    for cat in cat_file:
        if id == int(cat.split(',')[0]):
            found = True
            continue
        else:
            newCats.append(cat)  

    if not found:
        return False

    categories.writeCatFile(newCats)

    channels = getAllChannels()
    for channel in channels:
        channel[2].removeCategory(id)

    return True


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

    channelList = []

    if above:
        channelList = insertAbove(theWeight, original, toMove)
    else:
        channelList = insertBelow(theWeight, original, toMove)

    writeChannelsToFile(channelList)

    cancelSelection()
    
    return True


def insertBelow(theWeight, original, toMove):
    channelList = []

    inserted = False

    for channel in original:
        weight = channel[2].weight

        if weight > theWeight and not inserted:
            inserted = True
            for ch in toMove:
                channelList.append(ch)
                   
        channelList.append(channel)

    #special case if inserting below bottom
    if not inserted:
        for ch in toMove:
            channelList.append(ch)

    return channelList


def insertAbove(theWeight, original, toMove):
    channelList = []

    inserted = False

    for channel in original:
        weight = channel[2].weight

        if weight >= theWeight and not inserted:
            inserted = True
            for ch in toMove:
                channelList.append(ch)

        channelList.append(channel)

    return channelList
  

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
    sort = 'Sort by ONTapp.TV order' if ALPHASORT else 'Sort alphabetically'
    menu.append((sort, '?mode=%d' % (_TOGGLESORT)))

    if xbmcgui.Window(10000).getProperty('OTT_RUNNING').lower() != 'true':
        menu.append(('Launch On-Tapp.TV', '?mode=%d' % (_OTT)))

    menu.append(('Add-on settings', '?mode=%d' % (_SETTINGS)))


def toggleSort():
    if ALPHASORT:
        ADDON.setSetting('SORT', 'ONTapp.TV Order')
    else:
        ADDON.setSetting('SORT', 'Alphabetical')

    return True


def rename(id):
    channel = getChannelFromFile(id)
    title   = channel.title
    
    name = utils.GetText('Rename Channel', text=title)

    if not name:
        return False

    if name == title:
        return False

    if len(name) == 0:
        return False

    channel.title = name

    return updateChannel(channel, id)


def toggleHide(id):
    channel = getChannelFromFile(id)
    channel.visible = not channel.visible
    return updateChannel(channel, id)


def showSelection(_show):
    channels   = getAllChannels() #these will be sorted by weight

    show = 1 if _show else 0

    updated = False

    for ch in channels:
        channel = ch[2]
        id      = ch[1]
        weight  = channel.weight

        if weight > END_WEIGHT:
            break

        if weight >= START_WEIGHT:
            updated = True
            channel.visible = show
            updateChannel(channel, id)

    if not SHOWHIDDEN and not _show:
        cancelSelection()

    #actually makes sense to always cancel selection
    cancelSelection()

    return updated


def editChannel(id):
    channel = getChannelFromFile(id)
    if not channel:
        return False

    RENAME       = 100
    LOGO         = 200
    TOGGLEHIDE   = 300
    SELECT       = 400
    REMOVE       = 500
    DESC         = 600
    CATEGORY     = 700
    CLONE        = 800
    OFFSET       = 900

    title      = channel.title
    weight     = channel.weight
    categories = channel.categories
    hidden     = int(channel.visible) == 0
    userDef    = int(channel.userDef) == 1
    isClone    = int(channel.isClone) == 1

    hideLabel  = 'Show channel' if hidden else 'Hide channel'

    menu = []
    menu.append(['Rename channel', RENAME])
    menu.append(['Change logo',    LOGO])

    menu.append(['Edit description', DESC])
    menu.append(['Edit categories',  CATEGORY])
    menu.append([hideLabel,          TOGGLEHIDE])

    if not inSelection(weight):            
        menu.append(['Select channel', SELECT])

    if userDef or isClone:
        menu.append(['Remove channel', REMOVE])

    if not userDef:
        menu.append(['Clone channel', CLONE])

    menu.append(['Set time offset', OFFSET])
    
    option = selectMenu(title, menu)

    if option == RENAME:
        return rename(id)

    if option == LOGO:
        return updateLogo(id)

    if option == TOGGLEHIDE:
        return toggleHide(id)

    if option == SELECT:
        return selectChannel(weight)

    if option == REMOVE:
        return removeChannel(id)

    if option == DESC:
        return editChannelDescription(id)

    if option == CATEGORY:
        return editChannelCategory(id)

    if option == CLONE:
        return cloneChannel(id)

    if option == OFFSET:
        return setChannelOffset(id)

    return False


def editChannelDescription(id):
    channel = getChannelFromFile(id) 

    if not channel:
        return False

    desc = utils.GetText('Enter channel description', text=channel.desc)

    if not desc:
        return False

    channel.desc = desc
    return updateChannel(channel, id)


def editChannelCategory(id):
    channel = getChannelFromFile(id) 

    if not channel:
        return False

    cats = getCategoriesList()
    cat_dict = { cat[0]:cat[1] for cat in cats }

    index = 0
    options = []

    for category in sorted(cats, key=lambda x: x[0].upper()):
        if category[1] == 0:  # i.e. the Favourites category
            options.insert(0, category[0])
        else:
            options.append(category[0])

    # build preselect
    index = -1
    preselect = []
    for option in options:
        index += 1
        id = cat_dict[option]
        if id in channel.categories:
            preselect.append(index)

    return _editCategories('Please choose categories to add %s to' % channel.title, options, preselect, cat_dict, [channel])


def bulkEditCategory():
    cats = getCategoriesList()
    cat_dict = { cat[0]:cat[1] for cat in cats }

    index = 0
    options = []

    for category in sorted(cats, key=lambda x: x[0].upper()):
        if category[1] == 0:  # i.e. the Favourites category
            options.insert(0, category[0])
        else:
            options.append(category[0])

    #build selected channels / categories
    all_channels = getAllChannels()
    selected_channels = []
    categories_counts = {}
    for channel in all_channels:
        channel = channel[2]
        weight  = channel.weight

        if inSelection(weight):
            selected_channels.append(channel)
            for cat in channel.categories:
                categories_counts[cat] = categories_counts.get(cat, 0) + 1

    nmr_expected = len(selected_channels)

    # build preselect
    index = -1
    preselect = []
    for option in options:
        index += 1
        id = cat_dict[option]
        if categories_counts.get(id, 0) == nmr_expected:
            preselect.append(index)

    return _editCategories('Please choose categories to add the selected channels to', options, preselect, cat_dict, selected_channels)


def _editCategories(text, options, preselect, cat_dict, channels):
    selections = xbmcgui.Dialog().multiselect(text, options, preselect=preselect)

    if selections is None:
        return False

    updatedCats = []
    for id in selections:
        cat = options[id]
        updatedCats.append(cat_dict[cat])

    refresh = False
    for channel in channels:
        if channel.updateCategories(updatedCats):
            refresh = True

    return refresh 


def setChannelOffset(id):
    channel = getChannelFromFile(id) 

    if not channel:
        return False

    current = channel.offset
    offset  = utils.DialogNumeric('%s - enter offset (+/- minutes)' % channel.title, current=current)

    if offset == None or offset == current:
        return False

    channel.offset = offset
    return updateChannel(channel, id)


def cloneChannel(id):
    channel = getChannelFromFile(id) 

    if not channel:
        return False 

    channel.isClone = True
    channel.id      = channel.id.split('_clone_')[0]

    clone = [[channel.weight, id.split('_clone_')[0], channel]]
    
    channels = getAllChannels() 

    channelList = insertBelow(channel.weight, channels, clone)

    writeChannelsToFile(channelList)

    return True


def removeChannel(id):
    channel = getChannelFromFile(id) 

    if not channel:
        return False

    if channel.userDef != 1 and channel.isClone != 1:
        return False

    if not utils.DialogYesNo('Remove %s' % channel.title, noLabel='Cancel', yesLabel='Confirm'):
        return False

    path = os.path.join(OTT_CHANNELS, id)
    utils.deleteFile(path)

    return True


def newChannel():
    title = ''

    while True:
        title = utils.GetText('Please enter channel name', title)
        if not title :
            return False

        id = createID(title)

        try:
            current, dirs, files = sfile.walk(OTT_CHANNELS)
        except Exception as e:
            return False

        duplicate = False
    
        for file in files:
            if id.lower() == file.lower():
                duplicate = True
                break

        if not duplicate:
            break

        utils.DialogOK('%s clashes with an existing channel.' % title, 'Please enter a different name.')

    weight  = 0
    channel = Channel.Channel(id, title, weight=weight, categories='', userDef=1, desc='')
    item    = [weight, id,  channel]

    channels = getAllChannels()
    channels.insert(0, item)

    writeChannelsToFile(channels)

    editChannelDescription(id)
    editChannelCategory(id)

    return True


def updateLogo(id):
    channel = getChannelFromFile(id)
    logo    = channel.logo

    logo = getImage(logo)

    if not logo:
        return False

    if not USERLOGOS:
        logo = convertToHome(logo)

    channel.logo = logo

    return updateChannel(channel, id)


def showBackupRestore():
    addDir('Back-up My Line-up', _BACKUPCHANNELS,  thumbnail=ICON, fanart=FANART, isFolder=False)
    addDir('Restore My Line-up', _RESTORECHANNELS, thumbnail=ICON, fanart=FANART, isFolder=False)
    addDir('Do Full Back-up',    _FULLBACKUP,      thumbnail=ICON, fanart=FANART, isFolder=False)
    addDir('Do Full Restore',    _FULLRESTORE,     thumbnail=ICON, fanart=FANART, isFolder=False)


def lineBackup():
    return


def lineRestore():
    return


def backupChannels():
    if not utils.DialogYesNo('Would you like to do a back-up of your channel line-up?', ''):
        return
    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/backup.py, channel)'
    xbmc.executebuiltin(cmd)


def restoreChannels():
    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/restore.py, channel)'
    xbmc.executebuiltin(cmd)


def fullBackup():
    if not utils.DialogYesNo('Would you like to do a full back-up of On-Tapp.TV?', ''):
        return
    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/backup.py, full)'
    xbmc.executebuiltin(cmd)


def fullRestore():
    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/restore.py, full)'
    xbmc.executebuiltin(cmd)


def getImage(logo):
    if len(logo) == 0:
        root = '/'
    else:
        logo = logo.replace('\\', '/')
        root = logo.rsplit('/', 1)[0] + '/'

    if KODISOURCE:
        image = xbmcgui.Dialog().browse(2, 'Choose logo', 'files', '')
    else:
        root   = xbmc.translatePath('special://userdata').split(os.sep, 1)[0] + os.sep
        image  = xbmcgui.Dialog().browse(2, 'Choose logo', 'files', '', False, False, root)

    if image and image != root:
        utils.Log(image)
        utils.Log('********** logo image: %s' % image)
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

    return channel.writeToFile(path)


def writeChannelsToFile(channelList, updateWeight=True):
    weight = 1

    for item in channelList:
        id        = item[1]
        ch        = item[2]

        if updateWeight:
            ch.weight = weight
            weight   += 1

        updateChannel(ch, id)


def getAllChannels(alphaSort = False):
    channels = []

    try:
        current, dirs, files = sfile.walk(OTT_CHANNELS)
    except Exception as e:
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

    if not sfile.exists(path):
        return None

    cfg = sfile.readlines(path)

    return Channel.Channel(cfg)



def createID(title):
    title = title.replace('*', '_star')
    title = title.replace('+', '_plus')
    title = title.replace(' ', '_')

    title = re.sub('[:\\/?\<>|"]', '', title)
    title = title.strip()
    try:    title = title.encode('ascii', 'ignore')
    except: title = title.decode('utf-8').encode('ascii', 'ignore')

    return title.lower()


def selectMenu(title, menu):
    import contextmenus
    return contextmenus.showMenu(None, menu, True)
    
    options = []
    for option in menu:
        options.append(option[0])

    option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]


def openSettings():
    ADDON.openSettings()
    return True



def makeAlphabetical():
    if utils.DialogYesNo('Changing to alphabetical channel order CANNOT be undone.', 'Do a back-up first to be safe.', 'Are you sure you want to do this?'):
        channels = []

        try:
            current, dirs, files = sfile.walk(OTT_CHANNELS)
        except Exception as e:
            return channels
    
        for file in files:
            channels.append(file)

        sorted = []

        for id in channels:
            channel = getChannelFromFile(id)

            sorter  = channel.title.lower()

            sorted.append([sorter, id, channel])

        sorted.sort()
        writeChannelsToFile(sorted)
        return
    return


def GetINI():
    line1 = 'We will now download the latest add-on integration files.'
    line2 = 'Please wait a minute or two. After that...'
    line3 = 'The updates will be active the next time you open the EPG.'

    utils.DialogOK(line1, line2, line3)

    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/getIni.py, return)'
    xbmc.executebuiltin(cmd)
    return


def GetRecord():
    cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/enableRecord.py, return)'
    xbmc.executebuiltin(cmd)
    return


def fixHomeSkin():
    ott_addon   = 'script.on-tapp.tv'
    ott_addon   =  xbmcaddon.Addon(ott_addon)

    ott_profile =  xbmc.translatePath(ott_addon.getAddonInfo('profile'))

    otturl = 'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/resources/kodi/ott/v4ottdefaults.zip'
    ottzip =  os.path.join(ott_profile, 'ottdefaults.zip')

    utils.download(otturl, ott_profile, ottzip)
    utils.DialogOK('Home Page updated successfully')


def addDir(label, mode, id = '', weight = -1, desc='', thumbnail='', fanart=FANART, isFolder=True, menu=None, infolabels={}, totalItems=0, isSF=False, sfZip='', listID=None):
    u  = ''

    u += '?label=' + urllib.quote_plus(label)
    u += '&mode='  + str(mode)

    u += '&id=' + urllib.quote_plus(str(id))

    if weight > 0:
        u += '&weight=' + urllib.quote_plus(str(weight))

    if len(thumbnail) > 0:
        u += '&image=' + urllib.quote_plus(thumbnail)

    if len(fanart) > 0:
        u += '&fanart=' + urllib.quote_plus(fanart)

    infolabels['title']  = label
    infolabels['fanart'] = fanart

    # if desc:
        # infolabels['plot'] = desc
    infolabels['desc'] = desc

    if isSF:
        u += '&isSF=' + urllib.quote_plus(str(isSF))

    if sfZip:
        u += '&sfZip=' + urllib.quote_plus(sfZip)

    # if favourite category add a '*' prefix
    if mode == _EDITCATEGORY and id == 0:
        label = '*%s' % label

    APPLICATION.addDir(label, mode, u, thumbnail, isFolder, not isFolder, totalItems=totalItems, contextMenu=menu, replaceItems=True, infoLabels=infolabels, listID=listID)



def _get_params(params):
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


def get_params(path):
    import urllib
    params = {}
    path   = path.split('?', 1)[-1]
    pairs  = path.split('&')

    for pair in pairs:
        split = pair.split('=')
        if len(split) > 1:
            params[split[0]] = urllib.unquote_plus(split[1])

    return params

    

def onParams(application, _params):
    initGlobals(application)
    
    params = get_params(_params)
    mode   = _MAIN
    id     = ''

    doRefresh = False

    try:    mode = int(params['mode'])
    except: pass

    try:    id = params['id']
    except: pass   
    
    if mode == _RENAME:
        doRefresh = rename(id)

    elif mode == _TOGGLEHIDE:
        doRefresh = toggleHide(id)

    elif mode == _HIDE or mode == _SHOW:
        doRefresh = showSelection(mode == _SHOW)

    elif mode == _LOGO:
        doRefresh = updateLogo(id)

    elif mode == _TOGGLESORT:
        doRefresh = toggleSort()

    elif mode == _OTT:
        xbmc.executebuiltin('RunScript(script.tvguidedixie)')


    elif mode == _SETTINGS:
        doRefresh = openSettings()


    elif mode == _SELECT:
        doRefresh = False
        try:    
            if not ALPHASORT:
                weight = int(params['weight'])
                doRefresh = selectChannel(weight)
        except:
            doRefresh = False

    elif mode == _PLAY:
        doRefresh = False
        try:
            stream   = params['stream']

            #ottAddon = xbmcaddon.Addon(id = 'script.tvguidedixie')
            #path     = ottAddon.getAddonInfo('path')

            #sys.path.insert(0, path)

            import player
            player.play(stream, False)
        except Exception as e:
            pass

    elif mode == _CANCELSELECT:
        doRefresh = cancelSelection()


    elif mode == _INSERTABOVE:
        try:
            weight = int(params['weight'])
            doRefresh = insertSelection(above=True, theWeight=weight)
        except:
            pass


    elif mode == _INSERTBELOW:
        try:
            weight = int(params['weight'])
            doRefresh = insertSelection(above=False, theWeight=weight)
        except:
            pass

    elif mode == _EDIT:
        doRefresh = editChannel(id)


    elif mode == _EDITCATEGORY:
        category = getCategoryByID(id)
        if category:
            doRefresh = editCategory(category)


    elif mode == _NEWCHANNEL:
        doRefresh = newChannel()


    elif mode == _REMOVE:
        doRefresh = removeChannel(id)


    elif mode == _CLONE:
        doRefresh = cloneChannel(id)


    elif mode == _OFFSET:
        doRefresh = setChannelOffset(id)


    elif mode == _EDITCHANNELS:
        editChannels()


    elif mode == _EDITCATEGORIES:
        editCategories()


    #elif mode == _RENAMEFAVOURITE:
    #    renameFavourite()


    elif mode == _BULKEDITCATEGORY:
        doRefresh = bulkEditCategory()


    elif mode == _ADDSKINSLIST:
        getSkinList(id)


    elif mode == _GETSKINS:
        label = params['label']
        url   = params['id']

        getSkin(label, url)


    elif mode == _ADDLOGOSLIST:
        getLogosList(id)


    elif mode == _GETLOGOS:
        label = params['label']
        url   = params['id']

        getLogos(label, url)


    elif mode == _ADDLINEUPLIST:
        getLineupList()


    elif mode == _GETLINEUPS:
        label = params['label']
        url   = params['id']
        isSF  = params.get('isSF', 'false').lower() == 'true'
        sfZip = params['sfZip']

        getLineups(label, url, isSF, sfZip)


    elif mode == _INILINEUP:
        createINILineup()


    elif mode == _IPTVLINEUP:
        createIPTVLineup()


    elif mode == _BACKUPRESTORE:
        showBackupRestore()


    elif mode == _BACKUPCHANNELS:
        backupChannels()


    elif mode == _RESTORECHANNELS:
        restoreChannels()


    elif mode == _FULLBACKUP:
        fullBackup()


    elif mode == _FULLRESTORE:
        fullRestore()


    elif mode == _MAKEALPHA:
        makeAlphabetical()

    elif mode == _INI:
        GetINI()

    elif mode == _RECORD:
        GetRecord()


    elif mode == _FIXHOME:
        fixHomeSkin()


    #elif mode == _MAIN:
    else:
        main()

    if doRefresh:
        APPLICATION.containerRefresh()
