# -*- coding: utf-8 -*-
#
#       Copyright (C) 2016
#       On-Tapp-Networks Limited

import xbmc
import xbmcaddon
import xbmcgui

import json
import os

import utilsTOOLS as utils
import sfile

import sys
path = utils.OTT_HOME
sys.path.insert(0, path)

import mapping
import playlists
import dixie
import channel as dixieChannel
import categories


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

inipath  = os.path.join(OTT_PROFILE, 'ini')

MAPSFILE   = os.path.join(inipath, 'maps.json')
PREFIXFILE = os.path.join(inipath, 'prefixes.json')

maps      = json.load(open(MAPSFILE))
prefixes  = json.load(open(PREFIXFILE))


def mergeLineups(label, isSF, sfZip, url):
    try:
        dixie.ShowBusy()
        ret = _mergeLineups(label, isSF, sfZip, url)
    except Exception as e:
        ret = False
        utils.DialogOK('Error', e)

    dixie.CloseBusy()
    return ret


def _mergeLineups(label, isSF, sfZip, url):
    if not utils.DialogYesNo('Are you sure you want to continue and merge channels?', 'We highly recommend you back-up your channel line-up first', 'THERE IS NO UNDO!'):
        return False

    path    = os.path.join(OTT_PROFILE, 'chanstomerge')
    zipfile = os.path.join(OTT_PROFILE, 'tomerge.zip')

    if isSF:
        utils.installSF(sfZip)

    utils.download(url, path, zipfile)

    toMerge = os.path.join(path, 'channels')

    new_channels = getAllChannels(toMerge)

    sfile.rmtree(path)

    if not new_channels:
        utils.DialogOK('We cannot detect any channels.', 'Please check your settings.')
        return False

    line1 = 'Merging channels with existing lineup...'

    dp = xbmcgui.DialogProgress()
    dp.create('On-Tapp.TV', line1)

    update = 0
    nmr_new_channel = len(new_channels)

    dp.update(update, line1, 'This may take a few minutes.')

    current_channels = dixie.getAllChannels()

    updated_channels = []

    def merge_channel(new_channel):
        new_title   = new_channel.title

        # is new_channel already a current_channel
        for current_channel in current_channels:
            current_channel = current_channel[2]
            current_title   = current_channel.title

            if new_title == current_title:
                current_channel.updateStreamUrl(new_channel.streamUrl)
                current_channel.visible = True
                updated_channels.append((current_channel, new_channel.categories, True))  # True - pre-existing
                return

        # new_channel was not in current_channel so add
        updated_channels.append((new_channel, new_channel.categories, False))  #False - NOT pre-existing

    # do the merge      
    for idx, new_channel in enumerate(new_channels):
        new_channel = new_channel[2]

        update = 50 * idx / nmr_new_channel
        dp.update(update, line1, 'Processing %s' % new_channel.title)
        if dp.iscanceled():
            dp.close()
            return False

        if new_channel.visible:
            merge_channel(new_channel)

    update = 100
    dp.update(update, line1, 'Saving Channel Line-up...')

    # it is only at this point that we actually start applying
    # changes, therefore at this point the user can no longer
    # cancel so close the progress dialog
    dp.close()

    #utils.deleteCFG()

    #dp.close()

    # update weights of channels that weren't pre-existing
    update_weight = current_channels[-1][2].weight

    for channel, cats, preexisting in updated_channels:
        if not preexisting:
            update_weight += 1
            channel.weight = update_weight

    _merge_cats(updated_channels)

    utils.DialogOK('Your Channel Line-ups have now been merged.', 'If there are any mis-matches due to similar names,', 'You can edit the channels in the EPG.')
    return True

def _merge_cats(updated_channels):
    # create look up for mapping category names to indexes
    lookup = {}

    # first do existing categories
    max_id = -1
    file_cats = categories.GetCategoriesFromFile()
    for category in file_cats:
        category = category.split(',')
        id = int(category[0])
        lookup[category[1]] = id
        if max_id < id:
            max_id = id 
 
    # create a set containing the new categories
    new_cats = set()
    for channel, cats, preexisting in updated_channels:
        for cat in cats:
            if type(cat) in [str, unicode]:
                new_cats.add(cat)

    # now add new categories to lookup
    for cat in new_cats:
        index, cat = categories.OldStyle(cat)
        if cat not in lookup:
            max_id += 1
            lookup[cat] = max_id
            # also add to file_cats to rewrite to CATFILE
            file_cats.append('%d,%s,1' % (lookup[cat], cat))  # 1 - visible
    
    # patch channels to new categories format
    for channel, cats, preexisting in updated_channels:
        categoryList = []
        for cat in cats:
            index, cat = categories.OldStyle(cat)
            id = lookup.get(cat, None)
            if id:
                categoryList.append(id)

        if preexisting:
            channel.extendCategories(categoryList)
        else:
            channel.updateCategories(categoryList)

    # write catfile changes to file
    categories.writeCatFile(file_cats)

    # write updated channels to file
    for channel, cats, preexisting in updated_channels:
        channel.writeToFile()
        
    
def createINIFileLineup():
    utils.DialogOK('Please choose an INI file to create a channel line-up from.', 'This may take a while, please be patient')

    lineup = readINIFile()
    return _createLineup(lineup)


def createIPTVLineup():
    utils.DialogOK('We will now create a channel line-up from your IPTV settings', 'This may take a while, please be patient')

    plfile = os.path.join(OTT_PROFILE, 'plists')

    if os.path.exists(plfile):
        sfile.remove(plfile)

    lineup = playlists.loadPlaylists()

    return _createLineup(lineup)


def _createLineup(lineup):
    dp = xbmcgui.DialogProgress()
    dp.create('On-Tapp.TV', 'Creating channels...')

    OPEN_OTT  = '_OTT['
    CLOSE_OTT = ']OTT_'

    channels = dixie.getAllChannels()

    update = 0

    dp.update(update, 'Adding links to channels...', 'This may take a few minutes.')
    toEdit   = {}
    found    = []

    nItem = len(lineup)

    if nItem == 0:
        utils.DialogOK('We cannot detect any links.', 'Please check your settings.')
        return

    for idx, item in enumerate(lineup):
        lineupTag   = item[0]

        cleanTitle  = mapping.cleanLabel(item[1])
        editTitle   = mapping.editPrefix(prefixes, cleanTitle)
        lineupTitle = mapping.mapEPGLabel(prefixes, maps, editTitle)

        lineupLabel = lineupTag + lineupTitle

        # cleanlabel = mapping.cleanLabel(var5)
        # tmplabel   = mapping.editPrefix(prefixes, cleanlabel)
        # epglabel   = mapping.mapEPGLabel(prefixes, maps, tmplabel)

        lineupStream = item[2]

        update = 100 * idx / nItem
        dp.update(update, 'Adding links to channels...', 'Processing %s' % lineupLabel)
        if dp.iscanceled():
            dp.close()
            return

        for channel in channels:
            chTitle  = channel[2].title

            FUZZY = False
            EXACT = dixie.exactMatch(chTitle, lineupTitle)

            if not EXACT:
                FUZZY = dixie.fuzzyMatch(chTitle, lineupTitle)

            EXACT = dixie.exactMatch(chTitle, lineupTitle) == True
            FUZZY = dixie.fuzzyMatch(chTitle, lineupTitle) == True

            if EXACT or FUZZY:
                if item[1] not in found:
                    found.append(item[1])

                urlStream = OPEN_OTT + lineupLabel.upper() + CLOSE_OTT + lineupStream

                if chTitle in toEdit:
                    toEdit[chTitle].append(urlStream)
                else:
                    toEdit[chTitle] = [urlStream]

            if EXACT:
                break

    update = 100

    dp.update(update, 'Adding links to channels...', 'Saving Channel Line-up...')

    toWrite = []

    for channel in channels:
        chan = channel[2]

        if chan.title in toEdit:
            chan.streamUrl = '|'.join(toEdit[chan.title])
            toWrite.append(channel)
        else:
            chan.visible = 0
            toWrite.append(channel)

    dp.update(update, 'Adding links to channels...', 'Saving Channel Line-up...')
    dp.close()

    # attempt to get default category to use
    default_category = []
    for cat in categories.GetCategoriesFromFile():
        cat = cat.split(',')
        if cat[1].lower() == 'unmatched':
            default_category = [int(cat[0])]
        if cat[1].lower() == 'uncategorised':
            default_category = [int(cat[0])]

    from channel import Channel
    for idx, item in enumerate(lineup):
        if item[1] not in found:
            tag   = item[0]
            title = item[1]
            label = tag + title
            chID  = dixie.CleanFilename(title)

            streamUrl = OPEN_OTT + label + CLOSE_OTT + item[2]

            channelToAdd   = Channel(chID, title, streamUrl=streamUrl, desc=title, categories=default_category, userDef=1)
            newChannelItem = [idx, chID, channelToAdd]
            toWrite.append(newChannelItem)

    writeChannelsToFile(toWrite, updateWeight=True)

    utils.DialogOK('Your Channel Line-up has now been created.', 'If there are any mis-matches due to similar names,', 'You can edit the channels in the EPG.')


def updateChannel(dixieChannel, id):
    try:
        os.makedirs(OTT_CHANNELS)
    except:
        pass

    path = os.path.join(OTT_CHANNELS, id)

    return dixieChannel.writeToFile(path)


def writeChannelsToFile(channelList, updateWeight=True):
    weight = 1

    for item in channelList:
        id = item[1]
        ch = item[2]

        if updateWeight:
            ch.weight = weight
            weight   += 1

        updateChannel(ch, id)


def readINIFile():
    # import glob
    # ini   = os.path.join(OTT_PROFILE, 'ini', '*.*')
    # files = glob.glob(ini)
    #
    # for item in files:
    #     fullPath = os.path.split(item)
    #     iniPath  = fullPath[0]
    #     iniFile  = fullPath[1]
    #     dixie.log('===== PATH =====')
    #     dixie.log(iniPath)
    #     dixie.log('===== FILE =====')
    #     dixie.log(iniFile)

    # dialog = xbmcgui.Dialog().browse(1, 'Choose an INI File', os.path.join(OTT_PROFILE, 'ini'))
    # PATH = os.path.join(OTT_PROFILE, 'ini', )
    # inipath = os.path.join(OTT_PROFILE, 'ini')

    inipath = xbmc.translatePath(os.path.join(OTT_PROFILE, 'ini'))

    PATH = xbmcgui.Dialog().browse(1, 'Choose an INI File', 'files', mask='.ini')

    try:
        with open(xbmc.translatePath(PATH)) as content:
            items = content.readlines()

            tag = 'INI: '
            lineup = []
            for item in items:
                if '=' in item:
                    chans = item.split('=', 1)
                    chan  = chans[0]
                    strm  = chans[1].replace('\n', '')
                    if len(strm) != 0:
                        lineup.append([tag, chan, strm])

            return lineup
    except:
        return []


def getAllChannels(folder):
    channels = []

    try:
        current, dirs, files = sfile.walk(folder)
    except Exception as e:
        return channels

    for file in files:
        channels.append(file)

    sorted = []

    for id in channels:
        channel = getChannelFromFile(id, folder)

        sorter  = channel.weight

        sorted.append([sorter, id, channel])

    sorted.sort()

    return sorted


def getChannelFromFile(id, folder):
    from channel import Channel
    path = os.path.join(folder, id)

    if not sfile.exists(path):
        return None

    cfg = sfile.readlines(path)

    return Channel(cfg)


def main(cmd):
    if cmd == 'createIPTVLineup':
        createIPTVLineup()


if __name__ == '__main__':
    cmd = sys.argv[1]
    main(cmd)


