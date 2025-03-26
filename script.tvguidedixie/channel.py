
#       Copyright (C) 2018
#       On-Tapp-Networks Limited
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
import os
import threading
import re
import json

import copy

import sfile
import dixie

import categories


DSF     = dixie.isDSF()
PATH    = os.path.join(dixie.GetChannelFolder(), 'channels')
CATFILE = os.path.join(dixie.PROFILE, 'catfile')

try:
    os.makedirs(PATH)
except:
    pass

def tidy(item):
    if isinstance(item, bool):
        return '1' if item else '0'

    if isinstance(item, list):
        return item

    if (not isinstance(item, unicode)) and (not isinstance(item, str)):
        item = str(item)

    item = item.replace('\n', '')
    item = item.replace('\r', '')
    item = item.replace('\\', '/')
    return item


def Filename(text):
    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text
    

class Channel(object):
    def __init__(self, id, title='', logo='', streamUrl='', visible=1, weight=-1, categories='', userDef=0, desc='', isClone=0, isFave=0, offset=0):
        if isinstance(id, list):
            self.setFromList(id)
        else:
            self.set(id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone, isFave, offset)



    def set(self, id, title, logo, streamUrl, visible, weight, categories, userDef, desc, isClone, isFave, offset):
        if logo:
            logo = tidy(logo)

        self.id         = tidy(id)
        self.title      = tidy(title)
        self.categories = tidy(categories)
        self.logo       = logo
        self.streamUrl  = tidy(streamUrl)
        self.visible = int(tidy(visible))
        self.weight  = int(tidy(weight))
        self.userDef = int(tidy(userDef))
        self.isClone = int(tidy(isClone))

        try:     self.isFave = int(tidy(isFave))
        except:  self.isFave = 0

        try:     self.offset = int(tidy(offset))
        except:  self.offset = 0

        self.desc = tidy(desc)

        if DSF:
            self.title = urllib.unquote_plus(self.title)

        if not isinstance(self.categories, list):
            try:
                self.categories = json.loads(self.categories)
            except Exception as e: 
                categories = []
                for cat in self.categories.split('|'):
                    if cat: 
                        categories.append(cat)
                self.categories = categories

        self.categories.sort()
        self.setIsFave()


    def setIsFave(self):
        self.isFave = 0 in self.categories


    def isProtected(self):
        return dixie.ADULT in self.categories


    def setFromList(self, list):
        userDef = False
        isClone = False
        isFave  = False
        offset  = 0
        desc    = ''
           
        if len(list) > 7:
            userDef = list[7]

        if len(list) > 8:
            desc = list[8]

        if len(list) > 9:
            isClone = list[9]
        
        if len(list) > 10:
            isFave = list[10]

        if len(list) > 11:
            offset = list[11]


        self.set(list[0], list[1], list[2], list[3], list[4], list[5], list[6], userDef, desc, isClone, isFave, offset)


    def safeWriteToFile(self, file, item):
        if isinstance(item, list):
            newList = []
            for text in item:
                try:    text = text.encode('utf8')
                except: pass
                newList.append(text)
            file.write(json.dumps(newList))

        elif item:
            try:    file.write(item.encode('utf8'))
            except: file.write(item)

        file.write('\n')


    def writeToFile(self, filename=None):
        if not filename:
            filename = os.path.join(PATH, Filename(self.id)) 

        cloneID = -1
        localID = self.id

        if self.isClone:
            filename, cloneID = self.cloneFilename(filename)
            localID += cloneID

        try:    f = sfile.file(filename, 'w')
        except: return False

        self.safeWriteToFile(f, localID)
        self.safeWriteToFile(f, self.title)
        self.safeWriteToFile(f, self.logo)
        self.safeWriteToFile(f, self.streamUrl)

        if self.visible:
            f.write('1\n')
        else:
            f.write('0\n')

        f.write(str(self.weight) + '\n')

        self.safeWriteToFile(f, self.categories)

        if self.userDef:
            f.write('1\n')
        else:
            f.write('0\n')

        self.safeWriteToFile(f, self.desc)

        if self.isClone:
            f.write('1\n')
        else:
            f.write('0\n')

        if self.isFave:
            f.write('1\n')
        else:
            f.write('0\n')

        f.write(str(self.offset) + '\n')

        f.close()
        return True


    def cloneFilename(self, filename):
        if '_clone_' in filename:
            return filename, ''

        index    = 1
        root     = filename
        filename = root + '_clone_%d' % index

        while sfile.exists(filename):
            index += 1
            filename = root + '_clone_%d' % index

        return filename, '_clone_%d' % index


    def clone(self):
        return copy.deepcopy(self)
      

    def compare(self, channel):
        if self.visible != channel.visible:
            return False

        if self.weight != channel.weight:
            return False

        if self.title != channel.title:
            return False

        if self.logo != channel.logo:
            return False

        if self.categories != channel.categories:
           return False

        if self.isFave != channel.isFave:
           return False

        if self.offset != channel.offset:
           return False

        return True


    def __eq__(self, other):
        if not hasattr(self, 'id'):
            return False

        if not hasattr(other, 'id'):
            return False

        return self.id == other.id


    def __repr__(self):
        try:
            return 'Channel(id=%s, title=%s, categories=%s, logo=%s, streamUrl=%s, weight=%s, visible=%s userDef=%s desc=%s isClone=%s isFave=%s, offset=%s)' \
               % (self.id, self.title, str(self.categories), self.logo, self.streamUrl, str(self.weight), str(self.visible), str(self.userDef), self.desc, str(self.isClone), str(self.isFave), str(self.offset))
        except:
            return 'Can\'t display channel'


    def getWeight(self):
        return self.weight


    def updateCategories(self, categoryList):
        categoryList.sort()
        if self.categories == categoryList:
            return False

        self.categories = categoryList
        self.setIsFave()
        self.writeToFile()
        return True


    def extendCategories(self, categoryList):
        if not self.categories:
            return self.updateCategories(categoryList)

        categoryList.sort()
        if self.categories == categoryList:
            return False

        extended = set(self.categories)
        extended.update(categoryList)
        extended = list(extended)

        return self.updateCategories(extended)


    def removeCategory(self, id):
        cats = self.categories
        if id not in cats:
            return False

        cats.remove(id)
        return channel.updateCategories(cats)


    def updateStreamUrl(self, streamUrl):
        if not streamUrl:
            return

        if not self.streamUrl:
            self.streamUrl = streamUrl
            return

        if '|%s|' % streamUrl not in '|%s|' % self.streamUrl:
            self.streamUrl += '|' + streamUrl


#############################################################


def GetChannelFromFile(filename):
    try:    return Channel(sfile.readlines(filename))
    except: return None


def _ConfirmUpdate(folder):
    src = os.path.join(folder, 'tempchannels')
    dst = os.path.join(folder, 'channels')

    CheckForNewChannels(src)

    newFiles = []

    current, dirs, files = sfile.walk(src)
    for file in files:
        filename = os.path.join(dst, file)
        if not sfile.exists(filename):
            newFiles.append(file)

    if len(newFiles) == 0:
        return

    channels = []
    titles   = ['[I]All Channels[/I]']

    for file in newFiles:
        channel = GetChannelFromFile(os.path.join(src, file))
        if channel:
            channels.append(channel)
            titles.append(channel.title)

    import xbmcgui

    selections = xbmcgui.Dialog().multiselect('New channels detected - please choose those you wish to add', titles)

    if not selections:
        selections = []

    addAll = 0 in selections

    for idx, channel in enumerate(channels):
        visible = addAll
        if idx+1 in selections: # +1 to account for 'All Channels' item
            visible = True

        channel.visible = visible
        channel.writeToFile(os.path.join(dst, newFiles[idx]))

    sfile.rmtree(src)



def ConfirmUpdate(folder):
    try:
        return _ConfirmUpdate(folder)
    except Exception as e:
        dixie.DialogOK('ConfirmUpdate', str(e))

def CheckForNewChannels(src):
    try:
        _CheckForNewChannels(src)
    except Exception as e:
        dixie.DialogOK('CheckForNewChannels', str(e))
        pass


def _CheckForNewChannels(src):
    if not os.path.exists(src):
        sfile.makedirs(src)

    logoFolder = dixie.GetLogoFolder() # Get the logo folder setting.
    if dixie.GetSetting('logo.type') == '1':
        logoPath = logoFolder
    else:
        logoPath = 'special://profile/addon_data/script.tvguidedixie/extras/logos/' + logoFolder + '/'

    newChannelList = dixie.loadChannelList() # Read channels.json and return a list. File is downloaded in DB.zip.

    built_in_cats = categories.getBuiltIns()
    updated_cats  = categories.merge(built_in_cats)
    # updated_cats is a dict of the current categories merged with the new ones
    # key - name, value - category integer index

    oldChannelList = dixie.getAllChannels()  # Read files in existing channels folder and return a list
            
    newChannels   = []
    oldChannels   = []
    oldCategories = []

    max_weight = 0
    for oldChannel in oldChannelList:
        title  = oldChannel[2].title
        weight = oldChannel[2].weight

        oldChannels.append(title)

        if max_weight < weight:
            max_weight = weight
            

    for newChannel in newChannelList:
        title  = newChannel[1]
        if title in oldChannels:
            continue

        id   = newChannel[0]
        cats = newChannel[2]
        logo = logoPath + title + '.png'

        newCategories  = categories.convertTextToID(cats, updated_cats)
        channelToAdd   = Channel(id, title, weight=max_weight, logo=logo, categories=newCategories)
        newChannelItem = [id, channelToAdd]
        newChannels.append(newChannelItem)

        max_weight += 1

    for item in newChannels:
        chID = item[0]
        ch   = item[1]
        ch.writeToFile(os.path.join(src, dixie.CleanFilename(chID)))


def checkCategories(oldCategories, newCategories):
    for cat in newCategories:
        if cat in oldCategories:
            return cat

    return cat[0]


def GetChannelFromFile(id):
    path = os.path.join(PATH, id)

    if not sfile.exists(path):
        return None
    cfg = sfile.readlines(path)

    return Channel(cfg)


class ChannelLoader(threading.Thread):
    def __init__(self, id):
        super(ChannelLoader, self).__init__()
        self.id      = id
        self.channel = None

    def run(self):
        try:    self.channel = GetChannelFromFile(self.id)
        except: self.channel = None


def GetChannelsFromFile(channelIDs):
    loaders = []
    for id in channelIDs:
        channel = ChannelLoader(id)
        channel.start()
        loaders.append(channel)

    [loader.join() for loader in loaders]

    return [loader.channel for loader in loaders]


def GetCategoriesFromFile():
    return categories.GetCategoriesFromFile()

#def UpdateCatFile(categoryList):
#    return categories.UpdateCatFile(categoryList)

def createCatFile(channels):
    return createCatFile(channels)

def simplifyCat(cat):
    return simplifyCat(cat)
