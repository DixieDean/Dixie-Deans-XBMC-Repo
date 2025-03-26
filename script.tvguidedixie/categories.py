
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

import os
import json

import sfile
import dixie


PATH    = os.path.join(dixie.GetChannelFolder(), 'channels')
CATFILE = os.path.join(dixie.PROFILE, 'catfile')

VERSION = 1


# def OldStyle(cat):
#     items = cat.split('. ', 1)
#     if len(items) == 2:
#         try:
#             index = int(items[0])
#             cat = items[1]
#             return index, cat
#         except:
#             pass

#     return None, cat

def OldStyle(cat):
    try:
        items = cat.split('. ', 1)
        if len(items) == 2:
            index = int(items[0])
            if index == 0:  # 0 is the 'Favourites' category index
                index = 999
            cat = items[1]
            return index, cat
    except:
        pass

    return None, cat


def verifyCategories():
    """
    Called from various places to validate category versioning and patch if necessary
    """
    if not dixie.getAllChannels():
        db_file = os.path.join(dixie.PROFILE, 'program.db')
        sfile.remove(db_file)
        return
    
    dixie.ShowBusy()
    _verifyCategories()
    dixie.CloseBusy()


def _verifyCategories():
    if not sfile.exists(CATFILE):
        return patchV0()

    line = sfile.readlines(CATFILE)[0]

    if not line.startswith('~'):
        return patchV1()

    version = int(line.replace('~v', ''))

    msg = 'Version %r catfile detected, does not require patching' % version
    dixie.log(msg)


def patchV0():
    """
    Creates file when it is missing but channels exists
    """

    channelCats = GetCategoriesFromChannels('Updating categories')

    if not channelCats:        
        return

    newCatIndices = []
    newCatDict = {}
    newCats = []
    unindexed = []
    baseIndex = 9999
    defaultIndex = baseIndex

    max_id = -1
    
    for cat in channelCats:
        cat = cat.rsplit(',')[0]
        index, title = OldStyle(cat)

        if index is None:
            if title in unindexed:
               continue

            unindexed.append(title)
            defaultIndex += 1
            index = defaultIndex  # these will be corrected once we know max_id

        elif max_id < index:
            max_id = index

        if index not in newCatIndices:
            newCatIndices.append(index)
            newCatDict[index] = (index, title) 

    # now correct those that were unindexed
    cats = []
    for index in sorted(newCatIndices):
        if index > baseIndex:
            title   = newCatDict[index][1]
            max_id += 1 
            index   = max_id
            cats.append((index, title))
        else:
            cats.append(newCatDict[index])

    reverseLookup = {}

    newCats = []
    for cat in cats:
        name  = cat[1]
        index = cat[0]
        newCats.append('%d,%s,1' % (index, name))
        reverseLookup[name] = index

    fave = dixie.GetSetting('FAVOURITE').strip()
    if not fave:

        fave = 'Favourites'

    dixie.SetSetting('FAVOURITE', fave)
    dixie.SetSetting('categories', '')

    newCats.insert(0, '0,%s,1' % fave)  # doesn't need to be in reverseLookup dictionary
    
    writeCatFile(newCats)

    # now patch channel files
    def patch(categories):
        patched = []
        for cat in categories:
            index, title = OldStyle(cat)
            index = reverseLookup.get(title, None)
            if index is not None:
                patched.append(index)

        return patched

    patchChannels(patch)


def patchV1():
    """
    Huge refactor
    Categories are now identified by an ID which maps to the display name via the catfile
    Channel categories are now stored as a list of integers in the channel files
    Settings file now contains IDs of channels rather than the display names
    """

    fileCats, channelCats = GetCategories('Updating categories')

    combined = fileCats

    for cat in channelCats:
        if cat not in combined:
            combined.append(cat)    

    faveCat = dixie.GetFaveCategory() # this will include the FAVE_POSTFIX, i.e. ~OTTFAVE
    newCats = []
    reverseLookup = {}  # this will allow us to convert catergory names into their new indexes

    # patch catfile (categories are now stored along with an index, this index will now be used
    # to represent categories in the channel files     
    # cat Zero is the Favourites category

    _builtins = getBuiltIns()
    builtins = {}
    maximumID = 0

    #convert to a dict and get the maximum ID
    for builtin in _builtins:
        index = builtin[0]
        name  = builtin[1]
        builtins[name] = index
        if index > maximumID:
            maximumID = index
 
    for cat in combined:
        name = cat.rsplit(',', 1)[0] 
        if name != faveCat:
            if name in builtins:
                index = builtins[name]
            else:
                maximumID += 1
                index = maximumID
            cat = '%d,%s' % (index, cat)
            newCats.append(cat)
            reverseLookup[name] = index

    # add favourite category
    reverseLookup[faveCat] = 0
    newCats.insert(0, '0,%s,1' % dixie.GetSetting('FAVOURITE')) #default Favourite category to visible
    writeCatFile(newCats)

    # now patch channel files
    def patch(categories):
        patched = []
        for cat in categories:
            index = reverseLookup.get(cat, None)
            if index is not None:
                patched.append(index)

        return patched

    patchChannels(patch)

    categories = dixie.GetSetting('categories').split('|')
    categories = [reverseLookup[cat] for cat in categories]
    
    dixie.SetSetting('FAVOURITE', reverseLookup[faveCat])
    dixie.SetSetting('categories', json.dumps(categories))


def patchChannels(patch):
    if not sfile.exists(CATFILE):
        return
    
    dixie.ShowBusy()
    
    datapath    = dixie.PROFILE
    destination = os.path.join(datapath, 'channels')
    channels    = dixie.getAllChannels() # Read files in existing channels folder and return a list

    for channel in channels:
        channel = channel[2]
        patched = patch(channel.categories)

        channel.categories = patched

        channel.writeToFile(os.path.join(destination, dixie.CleanFilename(channel.id)))

    dixie.CloseBusy()


def GetCategories(msg=None):
    channelCats = GetCategoriesFromChannels(msg)

    if not sfile.exists(CATFILE):
        newCats = channelCats
        newCats.insert(0, '0,%s,1' % dixie.GetSetting('FAVOURITE')) #default Favourire cateory to visible
        writeCatFile(newCats)

    fileCats = GetCategoriesFromFile()
    
    return fileCats, channelCats


def GetCategoriesFromFile(msg=None):
    if sfile.exists(CATFILE):
        return readCatFile()

    categories = GetCategoriesFromChannels(msg)
    writeCatFile(categories)
    return categories


def GetVisibleCategoriesFromChannels():
    channels = dixie.getAllChannels() # Read files in existing channels folder and return a list

    visible = set()
    for channel in channels:
        channel = channel[2]
        if channel.visible:
            for category in channel.categories:
                visible.add(category)
          
    return visible 


def GetCategoriesFromChannels(msg=None):
    if msg:
        dixie.notify(msg)

    def patch(categories):
        if isinstance(categories, list):
            return categories

        patched = []
        for cat in categories.split('|'):
            cat = cat.split('. ', 1)[-1]  #remove anything before the first '.'
            patched.append(cat)

        return patched

    patchChannels(patch)

    channels = dixie.getAllChannels() # Read files in existing channels folder and return a list

    return createCategoriesFromChannels(channels)


def UpdateCatFile(categoryList):
    #[name, visible, id]
    categories = ''

    for cat in categoryList:
        categories += '%d,%s,%d\n' % (cat[2], cat[0], cat[1])  # id, name, visible

    #remove final \n
    categories = categories[:-1]

    writeCatFile(categories)


def writeCatFile(categories, filename=None):
    #0,Favourites,1
    #1,24/7,1
    #2,All: Sports,1

    if not categories:
        return

    if isinstance(categories, list):
        cats = '\n'.join(categories)
    else:
        cats = categories

    cats = '~v%d\n%s' % (VERSION, cats)

    if not filename:
        filename = CATFILE

    sfile.write(filename, cats)


def readCatFile():
    cats = []
    for line in sfile.readlines(CATFILE):
        if line and not line.startswith('~'):
            cats.append(line)
    return cats


def createCategoriesFromChannels(channels):
    newcats  = []

    faveCat = dixie.GetFaveCategory()

    for channel in channels:
        categories = channel[2].categories

        for category in categories:
            if category not in newcats and category != faveCat:
                newcats.append(category)

    newcats.sort()

    return ['%s,1' % x for x in newcats] 


def getFromSettings():
    try:    return json.loads(dixie.GetSetting('categories'))
    except: return []


def merge(newCats):
    # returns a dict of the current categories merged with those passed in
    # key - name, value - category integer index
    # also writes out merged list to the CATFILE
    categories = readCatFile()
    current = {}

    newID = 0

    for category in categories: 
        #id, name, visible
        category      = category.split(',')
        id            = int(category[0])
        name          = category[1]
        current[name] = id

        if id > newID:
            newID = id 

    if len(categories) == 0:
        category = 'Favourites'
        categories.append('%d,%s,1' % (newID, category))  # Index, Name, Visible

    # this loop ignores the original indexes
    for category in newCats:
        category = category[1] 
        if category not in current:
            newID += 1 
            current[category] = newID
            categories.append('%d,%s,1' % (newID, category))  # Index, Name, Visible

    writeCatFile(categories)
    return current


def getBuiltIns():
    newChannelList = dixie.loadChannelList() # Read channels.json and return a list. File is downloaded in DB.zip.
    
    newCatIndices = []
    newCatDict = {}
    newCats = []
    unindexed = []
    baseIndex = 9999
    defaultIndex = baseIndex

    max_id = -1
    
    for channel in newChannelList:
        cats = channel[2].split('|')
        for cat in cats:
            index, title = OldStyle(cat)

            if index is None:
                if title in unindexed:
                    continue

                unindexed.append(title)
                defaultIndex += 1
                index = defaultIndex  # these will be corrected once we know 

            elif max_id < index:
                max_id = index

            if index not in newCatIndices:
                newCatIndices.append(index)
                newCatDict[index] = (index, title) 

    # now correct those that were unindexed
    builtins = []
    for index in sorted(newCatIndices):
        if index > baseIndex:
            title   = newCatDict[index][1]
            max_id += 1 
            index   = max_id
            builtins.append((index, title))
        else:
            builtins.append(newCatDict[index])

    return builtins


def convertTextToID(cats, updated_cats):
    if isinstance(cats, list):
        return cats

    try:
        return json.loads(cats)
    except:
        pass

    IDs = []
    cats = cats.split('|')

    for cat in cats:
        index, title = OldStyle(cat)
        if title in updated_cats:
            IDs.append(updated_cats[title])

    return IDs    
