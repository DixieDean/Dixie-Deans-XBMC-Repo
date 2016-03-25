#
#
#      Copyright (C) 2014 Sean Poyser - With acknowledgement to some original code by twinther (Tommy Winther)
#
#  This Program is free software; you can redistribute it and/or modifye
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
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import StringIO
import os
import threading
import datetime
import time
import urllib2
import urllib

from xml.etree import ElementTree

import xbmcaddon
import xbmcplugin
from strings import *
import xbmc
import xbmcgui
import xbmcvfs
import sqlite3

from channel import Channel

import dixie
import settings
import sfile

import re
import io


GMTOFFSET = dixie.GetGMTOffset()

datapath     = dixie.PROFILE
settingsFile = os.path.join(datapath, 'settings.cfg')

USE_DB_FILE = True

SETTINGS_TO_CHECK = ['']

DSF = dixie.isDSF()

channelFolder = dixie.GetChannelFolder()
channelPath   = os.path.join(channelFolder, 'channels')
dixie.log('Channel Folder Setting: %s' % channelPath)

try:    sfile.makedirs(channelPath)
except: pass


def GetLogoType():
    return dixie.GetSetting('logo.type')


def GetLogoFolder():
    CUSTOM = '1'

    logoType = GetLogoType()

    if logoType == CUSTOM:
        logoFolder = dixie.GetSetting('user.logo.folder')
    else:
        logoFolder = dixie.GetSetting('dixie.logo.folder')

    return logoFolder


def CleanFilename(text):
    if DSF:
        return text

    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text


class Program(object):
    def __init__(self, channel, title, startDate, endDate, description, subTitle, imageLarge = None, imageSmall = None, notificationScheduled = None):

        self.channel   = channel
        self.title     = title
        self.startDate = startDate
        self.endDate   = endDate
        self.description = description
        self.subTitle    = subTitle
        self.imageLarge  = imageLarge
        self.imageSmall  = imageSmall
        self.notificationScheduled = notificationScheduled
        

    def __repr__(self):
        return 'Program(channel=%s, title=%s, startDate=%s, endDate=%s, description=%s, subTitle=%s, imageLarge=%s, imageSmall=%s)' % \
            (self.channel, self.title, self.startDate, self.endDate, self.description, self.subTitle, self.imageLarge, self.imageSmall)


class SourceException(Exception):
    pass


class SourceUpdateCanceledException(SourceException):
    pass


class SourceNotConfiguredException(SourceException):
    pass


class DatabaseSchemaException(sqlite3.DatabaseError):
    pass


class Database(object):
    PROGRAM_DB = 'program.db'

    def __init__(self, nChannel):
        self.connP = None

        self.eventQueue = list()
        self.event = threading.Event()
        self.eventResults = dict()

        self.categoriesList = None

        self.source = instantiateSource()

        self.updateInProgress = False
        self.updateFailed = False
        self.settingsChanged = None

        self.channelList = []
        self.channelDict = {}

        profilePath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
        if not os.path.exists(profilePath):
            os.makedirs(profilePath)

        self.programPath = os.path.join(profilePath, Database.PROGRAM_DB)

        threading.Thread(name='Database Event Loop', target=self.eventLoop).start()


    def eventLoop(self):
        dixie.log('Database.eventLoop() >>>>>>>>>> starting...')
        while True:
            self.event.wait()
            self.event.clear()

            event = self.eventQueue.pop(0)

            command = event[0]
            callback = event[1]

            dixie.log('Database.eventLoop() >>>>>>>>>> processing command: %s' % command.__name__)

            try:
                result = command(*event[2:])
                self.eventResults[command.__name__] = result

                if callback:
                    if self._initializeS == command:
                        threading.Thread(name='Database callback', target=callback, args=[result]).start()
                    elif self._initializeP == command:
                        threading.Thread(name='Database callback', target=callback, args=[result]).start()
                    else:
                        threading.Thread(name='Database callback', target=callback).start()

                if self._close == command:
                    del self.eventQueue[:]
                    break

            except Exception, e:
                dixie.log('Database.eventLoop() >>>>>>>>>> exception! %s' % str(e))
                raise

        dixie.log('Database.eventLoop() >>>>>>>>>> exiting...')


    def _invokeAndBlockForResult(self, method, *args):
        event = [method, None]
        event.extend(args)
        self.eventQueue.append(event)
        self.event.set()

        while not self.eventResults.has_key(method.__name__):
            time.sleep(0.1)

        result = self.eventResults.get(method.__name__)
        del self.eventResults[method.__name__]
        return result


    def initializeS(self, callback, cancel_requested_callback=None):
        self.eventQueue.append([self._initializeS, callback, cancel_requested_callback])
        self.event.set()                


    def initializeP(self, callback, cancel_requested_callback=None):
        self.eventQueue.append([self._initializeP, callback, cancel_requested_callback])
        self.event.set()


    def _initializeS(self, cancel_requested_callback):
        return self.initializeChannels()


    def initializeChannels(self):
        channels = self.getAllChannels()

        if len(channels) == 0:
            dixie.SetSetting('PREVLOGO', '')
            return

        BUILTIN = '0'
        CUSTOM  = '1'

        logoFolder = GetLogoFolder()
        logoType   = GetLogoType()

        if logoType == CUSTOM:
            logoPath = ''
        else:
            logoPath = 'special://profile/addon_data/script.tvguidedixie/extras/logos/'

        dixie.log('Logo Path Setting:   %s' % logoPath)
        dixie.log('Logo Folder Setting: %s' % logoFolder)
        dixie.log('Logo Type:           %s' % logoType)

        prevLogoFolder = dixie.GetSetting('PREVLOGO')
        currLogoFolder = logoFolder

        if currLogoFolder == prevLogoFolder:
           return True

        dixie.SetSetting('PREVLOGO', currLogoFolder)
        
        for ch in channels:
            channel  = self.getChannelFromFile(ch)
            chtitle = channel.title
            if DSF:
                chtitle = urllib.quote_plus(channel.title)

            if channel == None:
                continue

            logoFile = os.path.join(logoPath, logoFolder, chtitle + '.png')

            if channel.logo <> logoFile:
                channel.logo = logoFile
                self.replaceChannel(channel)

        return True


    def _initializeP(self, cancel_requested_callback):
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime)
        sqlite3.register_converter('timestamp', self.convert_datetime)

        self.alreadyTriedUnlinking = False
        while True:
            if cancel_requested_callback is not None and cancel_requested_callback():
                break

            try:
                self.openP()

                # create and drop dummy table to check if database is locked
                c = self.connP.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS database_lock_check(id TEXT PRIMARY KEY)')
                c.execute('DROP TABLE database_lock_check')
                c.close()

                self._createTable()
                self.settingsChanged = self._wasSettingsChanged(ADDON)
                break

            except sqlite3.OperationalError:
                if cancel_requested_callback is None:
                    sfile.log('EPG Database is locked, bailing out...')
                    break
                else:  # ignore 'database is locked'
                    dixie.log('EPG Database is locked, retrying...')

            except sqlite3.DatabaseError:
                self.connP = None
                if self.alreadyTriedUnlinking:
                    dixie.log('EPG Database is broken and unlink() failed')
                    break
                else:
                    try:
                        os.unlink(self.programPath)
                    except OSError:
                        pass
                    self.alreadyTriedUnlinking = True
                    xbmcgui.Dialog().ok(ADDON.getAddonInfo('name'), strings(DATABASE_SCHEMA_ERROR_1),
                                        strings(DATABASE_SCHEMA_ERROR_2), strings(DATABASE_SCHEMA_ERROR_3))

        return self.connP is not None


    def close(self, callback=None):
        self.eventQueue.append([self._close, callback])
        self.event.set()


    def _close(self):
        self.closeS()
        self.closeP()


    def closeS(self):
        return


    def closeP(self):
        #try:
        #    # rollback any non-commit'ed changes to avoid database lock
        #    if self.connP:
        #        self.connP.rollback()
        #except sqlite3.OperatiaonalError:
        #    pass  # no transaction is active
        if self.connP:
            self.connP.close()
            del self.connP


    def openP(self):
        self.connP = sqlite3.connect(self.programPath, detect_types=sqlite3.PARSE_DECLTYPES)
        #self.connP.execute('PRAGMA foreign_keys = ON')
        self.connP.row_factory = sqlite3.Row
        self.calcUpdateLimit()


    def parseDate(self, dateString):
        try:
            if type(dateString) in [str, unicode]:
                dt = dateString.split('-')
                return datetime.date(int(dt[0]), int(dt[1]) ,int(dt[2]))
        except:
            pass
        return datetime.date(1900, 1, 1)


    def calcUpdateLimit(self):
        self.updateLimit = datetime.date(1900, 1, 1)
        try:
            c = self.connP.cursor()
            c.execute('SELECT date FROM updates WHERE source=?', [self.source.KEY])
            for row in c:
                when = self.parseDate(row['date'])
                if when > self.updateLimit:
                    self.updateLimit = when
        except:
            pass
        c.close()


    def removeProgramDB(self):
        self.closeP()
        try:
            os.remove(self.programPath)
        except Exception, e:
            pass


    def _wasSettingsChanged(self, addon):
        settingsChanged = False
        count           = 0
        
        params = settings.getAll(settingsFile)
        
        for pair in params:
            param = pair[0]
            if param in SETTINGS_TO_CHECK:
                count += 1
                if pair[1] != addon.getSetting(param):
                    settingsChanged = True

        if count != len(SETTINGS_TO_CHECK):
            settingsChanged = True

        #update (or create) file
        if settingsChanged or len(params) == 0:
            for param in SETTINGS_TO_CHECK:
                value = addon.getSetting(param).decode('utf-8', 'ignore')
                settings.set(param, value, settingsFile)

        dixie.log('Settings changed: ' + str(settingsChanged))
        return settingsChanged


    def _isCacheExpired(self, date):
        # return True
        if self.settingsChanged:
            return True

        channelsLastUpdated = datetime.datetime.fromtimestamp(0)
        programsLastUpdated = datetime.datetime.fromtimestamp(0)

        try:
            when = settings.get('ChannelsUpdated', settingsFile)
            channelsLastUpdated = datetime.datetime.fromtimestamp(float(when))
        except:
            channelsLastUpdated = datetime.datetime.fromtimestamp(0)        

        try:
            dateStr = date.strftime('%Y-%m-%d')
            c = self.connP.cursor()
            c.execute('SELECT programs_updated FROM updates WHERE source=? AND date=?', [self.source.KEY, dateStr])
            row = c.fetchone()
            if row:
                programsLastUpdated = row['programs_updated']
        except:
            pass        
        c.close()

        return self.source.isUpdated(channelsLastUpdated, programsLastUpdated)


    def updateChannelAndProgramListCaches(self, callback, date = datetime.datetime.now(), progress_callback = None, clearExistingProgramList = True):
        self.eventQueue.append([self._updateChannelAndProgramListCaches, callback, date, progress_callback, clearExistingProgramList])
        self.event.set()


    def _updateChannelAndProgramListCaches(self, date, progress_callback, clearExistingProgramList):
        sqlite3.register_adapter(datetime.datetime, self.adapt_datetime)
        sqlite3.register_converter('timestamp', self.convert_datetime)

        if not self._isCacheExpired(date):
            return
        
        self.updateInProgress = True
        self.updateFailed = False
        dateStr = date.strftime('%Y-%m-%d')

        if len(self.channelDict) == 0:
            channels = self.getAllChannels()
            for channel in channels:
                theChannel = self.getChannelFromFile(channel)
                if theChannel:
                    self.channelDict[channel] = theChannel

        try:
            dixie.log('Updating caches...')
            if progress_callback:
                progress_callback(0)

            if self.settingsChanged:
                self.source.doSettingsChanged()

            self.settingsChanged = False # only want to update once due to changed settings

            toDelete = self.getAllChannels()

            weight = 0

            imported = imported_channels = imported_programs = 0
            for item in self.source.getDataFromExternal(date, progress_callback):
                imported += 1

                if isinstance(item, Channel):
                    imported_channels += 1
                    channel = item

                    clean = CleanFilename(channel.id)
                    if clean in toDelete:
                        toDelete.remove(clean)

                    weight += 1
                    channel.weight = weight
                    self.createChannel(channel)

            #channels updated
            try:    settings.set('ChannelsUpdated', self.adapt_datetime(datetime.datetime.now()), settingsFile)
            except: pass

            self.deleteOldChannels(toDelete)

            if imported_channels == 0:
                self.updateFailed = True
            if imported_programs == 0:
                self.updateFailed = (not USE_DB_FILE)
  
        except SourceUpdateCanceledException:
            # force source update on next load
            try:    settings.set('ChannelsUpdated', 0, settingsFile)
            except: pass

        except Exception:
            import traceback as tb
            import sys
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)

            try:
                # invalidate cached data
                try:    settings.set('ChannelsUpdated', 0, settingsFile)
                except: pass
               
            except:
                pass

            self.updateFailed = True

        update = dixie.GetSetting('updated.channels')
        if int(update) < 0:
            dixie.SetSetting('updated.channels', 0)
            dixie.SetSetting('current.channels', 0)
        else:
            dixie.SetSetting('current.channels', update)
            self.channelDict = {}
            self.updateInProgress = False

        self.initializeChannels()

        self.updateInProgress = False


    def deleteOldChannels(self, toDelete):
        dixie.log('START deleteOldChannels')

        dixie.log('Pass 1')
        dixie.log(toDelete)
        for i in xrange(len(toDelete), 0, -1):
            id = toDelete[i-1]
            try:
                channel = self.getChannelFromFile(id)
                dixie.log(channel)

                if channel.isClone == 1:
                    original = id.split('_clone_')[0]
                    dixie.log('Clone of %s' % original)
                    if original not in toDelete:
                        dixie.log('NOT removing clone %s' % id)
                        toDelete.remove(id)

                if channel.userDef == 1:
                    dixie.log('NOT removing userdef %s' % id)
                    toDelete.remove(id)

            except Exception, e:
                dixie.log('ERROR in deleteOldChannels %s' % str(e))

        dixie.log('Pass 2')
        dixie.log(toDelete)
        for id in toDelete:
            try:                
                dixie.log('Channel %s no longer available' % id)
                self.removeCleanChannel(id)
            except:
                pass

        dixie.log('END deleteOldChannels')




    def getAllChannels(self):
        channels = []

        try:
            current, dirs, files = sfile.walk(channelPath)
        except Exception, e:
            dixie.log('Error in getAllChannels' % str(e))
            return channels

        for file in files:
            channels.append(file)

        return channels


    def removeCleanChannel(self, id):
        try:    del self.channelDict[id]
        except: pass

        path = os.path.join(channelPath, id)
        if sfile.exists(path):
            try:    sfile.remove(path)
            except: pass


    def addChannel(self, channel):
        self.addCleanChannel(channel, CleanFilename(channel.id))


    def addCleanChannel(self, channel, id):
        path = os.path.join(channelPath, id) 

        if id not in self.channelDict:
            self.channelDict[id] = channel.clone()

        if not sfile.exists(path): 
            channel.writeToFile(path)


    def replaceChannel(self, channel):
        clean = CleanFilename(channel.id)

        if clean in self.channelDict: 
            if self.channelDict[clean].compare(channel):
                return  

        self.removeCleanChannel(clean)
        self.addCleanChannel(channel, clean)


    def createChannel(self, channel):
        path = os.path.join(channelPath, CleanFilename(channel.id))

        if sfile.exists(path):
            # TODO self.updateChannel(channel)
            return

        self.addChannel(channel)


    def updateChannel(self, channel):
        toUpdate = self.getChannelFromFile(CleanFilename(channel.id))

        if not toUpdate:
            xbmc.log("WE SHOULD NOT SEE THIS TEXT IN THE LOG")
            return 

        #once we know this works, we can do it more intelligently
        toUpdate.categories = channel.categories
        # toUpdate.title = channel.title

        self.replaceChannel(toUpdate)


    def getChannelFromFile(self, id):
        path = os.path.join(channelPath, id)

        if not sfile.exists(path):
            return None

        cfg = sfile.readlines(path)
        
        return Channel(cfg)

        ch = Channel(cfg[0], cfg[1], cfg[2], cfg[3], cfg[4], cfg[5], cfg[6])

        return ch


    def getEPGView(self, channelStart, date = datetime.datetime.now(), progress_callback = None, clearExistingProgramList = True, categories = None, nmrChannels=9):

        date  -= GMTOFFSET
        result = self._invokeAndBlockForResult(self._getEPGView, channelStart, date, progress_callback, clearExistingProgramList, categories, nmrChannels)

        if self.updateFailed:
            raise SourceException('No channels or programs imported')

        return result


    def _getEPGView(self, channelStart, date, progress_callback, clearExistingProgramList, categories, nmrChannels):
        update = xbmcgui.Window(10000).getProperty('OTT_UPDATE')
        if len(update) > 0:
            self.removeProgramDB()
            import update
            update.newEPGAvailable()
            self.openP()            

        self._updateChannelAndProgramListCaches(date, progress_callback, clearExistingProgramList)
        
        channels  = []
        _channels = self._getChannelList(onlyVisible = True, categories = categories)

        isProtected = dixie.isProtected()

        for channel in _channels:
            if isProtected or (dixie.ADULT not in channel.categories):
                channels.append(channel)

        if channelStart < 0:
            channelStart = len(channels) - 1
        elif channelStart > len(channels) - 1:
            channelStart = 0
        channelEnd = channelStart + nmrChannels

        channelsOnPage = channels[channelStart:channelEnd]
        programs = self._getProgramList(channelsOnPage, date)

        return [channelStart, channelsOnPage, programs]


    def getNextChannel(self, currentChannel):
        channels = self.getChannelList()
        idx = channels.index(currentChannel)
        idx += 1
        if idx > len(channels) - 1:
            idx = 0
        return channels[idx]


    def getPreviousChannel(self, currentChannel):
        channels = self.getChannelList()
        idx = channels.index(currentChannel)
        idx -= 1
        if idx < 0:
            idx = len(channels) - 1
        return channels[idx]


    def saveChannelList(self, callback, channelList):
        self.eventQueue.append([self._saveChannelList, callback, channelList])
        self.event.set()


    def _saveChannelList(self, channelList):
        for idx, channel in enumerate(channelList):
            self.replaceChannel(channel)

        self.channelList = None


    def getChannelList(self, onlyVisible = True):
        if not self.channelList or not onlyVisible:
            result = self._invokeAndBlockForResult(self._getChannelList, onlyVisible)

            if not onlyVisible:
                return result

            self.channelList = result

        return self.channelList


    def _getChannelList(self, onlyVisible, categories = None):
        if categories and len(categories) > 0:
            return self._getChannelListFilteredByCategory(onlyVisible, categories)

        channelList = []

        if len(self.channelDict) == 0:
            channels = self.getAllChannels()
        else:
            channels = self.channelDict.keys()

        for channel in channels:
            if channel in self.channelDict:
                theChannel = self.channelDict[channel]
            else:
                theChannel = self.getChannelFromFile(channel)
                if theChannel:
                    self.channelDict[channel] = theChannel

            add = False
            if theChannel:
                if onlyVisible:
                    add = theChannel.visible
                else:
                    add = True

            if add:
                channelList.append(theChannel.clone())

        channelList.sort(key=lambda x: x.weight)
        return channelList
 

    def _getChannelListFilteredByCategory(self, onlyVisible, categories):
        channelList = []

        if len(self.channelDict) == 0:
            channels = self.getAllChannels()
        else:
            channels = self.channelDict.keys()

        for channel in channels:
            if channel in self.channelDict:
                theChannel = self.channelDict[channel]
            else:
                theChannel = self.getChannelFromFile(channel)
                if theChannel:
                    self.channelDict[channel] = theChannel

            add = False
            if theChannel:
                if onlyVisible:
                    add =  theChannel.visible
                else:
                    add = True

                if add:
                    channelCats = theChannel.categories.split('|')
                    for category in channelCats:
                        if category in categories:
                            channelList.append(theChannel.clone())
                            break

        channelList.sort(key=lambda x: x.weight)
        return channelList


    def getCategoriesList(self):
        if not self.categoriesList:
           self.categoriesList = self._invokeAndBlockForResult(self._getCategoriesList)
        return self.categoriesList


    def _getCategoriesList(self):
        if len(self.channelDict) == 0:
            channels = self.getAllChannels()
        else:
            channels = self.channelDict.keys()

        categoriesList = []

        for channel in channels:
            if channel in self.channelDict:
                theChannel = self.channelDict[channel]
            else:
                theChannel = self.getChannelFromFile(channel)

            categories = theChannel.categories.split('|')
            for category in categories:
                if category not in categoriesList:
                    categoriesList.append(category)

        categoriesList.sort()

        try:
            if not dixie.isProtected():
                categoriesList.remove(dixie.ADULT)
        except:
            pass

        return categoriesList


    def isPlayable(self, channel):
        id = CleanFilename(channel.id)
        if id in self.channelDict:
            theChannel = self.channelDict[id]
        else:
            theChannel = self.getChannelFromFile(id)

        if theChannel == None:
            return False

        if theChannel.streamUrl == None:
            return False

        return len(theChannel.streamUrl) > 1


    def getCurrentProgram(self, channel):
        return self._invokeAndBlockForResult(self._getCurrentProgram, channel)

    def _getCurrentProgram(self, channel):       
        channelMap = {}
        channelMap[channel.id] = channel

        strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

        program = None

        now = datetime.datetime.now()
        c = self.connP.cursor()
        c.execute('SELECT * FROM programs WHERE channel IN ' + strCh  + ' AND source=? AND start_date <= ? AND end_date >= ?', [self.source.KEY, now, now])
        row = c.fetchone()
        if row:
            program = Program(channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
        c.close()

        return program


    def getNextProgram(self, channel):
        return self._invokeAndBlockForResult(self._getNextProgram, channel)


    def _getNextProgram(self, program):
        channel = ''
        channelMap = {}
        channelMap[program.channel.id] = channel

        strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

        nextProgram = None
        c = self.connP.cursor()
        c.execute('SELECT * FROM programs WHERE channel IN ' + strCh + ' AND source=? AND start_date >= ? ORDER BY start_date ASC LIMIT 1', [self.source.KEY, program.endDate])
        row = c.fetchone()
        if row:
            nextProgram = Program(program.channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
        c.close()

        return nextProgram


    def getPreviousProgram(self, channel):
        return self._invokeAndBlockForResult(self._getPreviousProgram, channel)


    def _getPreviousProgram(self, program):
        channel = ''
        channelMap = {}
        channelMap[program.channel.id] = channel

        strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

        previousProgram = None
        c = self.connP.cursor()
        c.execute('SELECT * FROM programs WHERE channel IN ' + strCh + ' AND source=? AND end_date <= ? ORDER BY start_date DESC LIMIT 1', [self.source.KEY, program.startDate])
        row = c.fetchone()
        if row:
            previousProgram = Program(program.channel, row['title'], row['start_date'], row['end_date'], row['description'], row['subTitle'], row['image_large'], row['image_small'])
        c.close()

        return previousProgram


    def _locateChannel(self, id, channels):
        theList = []
        for ch in channels:
            if ch.id.split('_clone_')[0] == id:
                theList.append(ch)
        return theList


    def _getProgramList(self, channels, startTime): #TODO Notifications
        endTime = startTime + datetime.timedelta(hours = 2)
        programList = []

        channelMap = {}
        for ch in channels:
            if ch.id:
                id = ch.id.split('_clone_')[0]
                channelMap[id] = ch

        if not channels:
            return []

        c = self.connP.cursor()
        strCh = '(\'' + '\',\''.join(channelMap.keys()) + '\')'

        c.execute('SELECT channel, title, start_date, end_date, description, subTitle, image_large, image_small FROM programs WHERE channel IN ' + strCh + ' AND end_date > ? AND start_date < ? AND source = ?', (startTime, endTime, self.source.KEY))    
        for row in c:         
            channel = self._locateChannel(row['channel'].encode('utf-8'), channels)
            for ch in channel:
                program = Program(ch, row["title"], row["start_date"], row["end_date"], row["description"], row["subTitle"], row['image_large'], row['image_small'])
                #program.notificationScheduled = self._isNotificationRequiredForProgram(program)
                programList.append(program)  
        return programList


    def setCustomStreamUrl(self, channel, stream_url):
        if stream_url is not None:
            self._invokeAndBlockForResult(self._setCustomStreamUrl, channel, stream_url)


    def _setCustomStreamUrl(self, channel, stream_url):
        id = CleanFilename(channel.id)
        if id in self.channelDict:
            theChannel = self.channelDict[id]
        else:
            theChannel = self.getChannelFromFile(id)
 
        if stream_url == theChannel.streamUrl:
            return

        theChannel.streamUrl = stream_url

        self.removeCleanChannel(id)
        self.addCleanChannel(theChannel, id)


    def getCustomStreamUrl(self, channel):
        return self._invokeAndBlockForResult(self._getCustomStreamUrl, channel)


    def _getCustomStreamUrl(self, channel):
        id = CleanFilename(channel.id)
        if id in self.channelDict:
            theChannel = self.channelDict[id]
        else:
            theChannel = self.getChannelFromFile(id)

        return theChannel.streamUrl


    def deleteCustomStreamUrl(self, channel):
        return self._invokeAndBlockForResult(self._deleteCustomStreamUrl, channel)


    def _deleteCustomStreamUrl(self, channel):
        self._setCustomStreamUrl(channel, '')


    def getStreamUrl(self, channel):
        customStreamUrl = self.getCustomStreamUrl(channel)
        if customStreamUrl:
            customStreamUrl = customStreamUrl.encode('utf-8', 'ignore')
            return customStreamUrl

        elif self.isPlayable(channel):
            streamUrl = channel.streamUrl.encode('utf-8', 'ignore')
            return streamUrl

        return None


    def adapt_datetime(self, ts):
        # http://docs.python.org/2/library/sqlite3.html#registering-an-adapter-callable
        return time.mktime(ts.timetuple())


    def convert_datetime(self, ts):
        try:
            return datetime.datetime.fromtimestamp(float(ts))
        except ValueError:
            return None


    def _createTable(self):
        self._createTableP()


    def _createTableS(self):
        return


    def _createTableP(self):
        c = self.connP.cursor()
        try:
            c.execute('SELECT major, minor, patch FROM version')
            (major, minor, patch) = c.fetchone()
            version = [major, minor, patch]
        except sqlite3.OperationalError:
            version = [0, 0, 0]

        try:
            if version < [1, 4, 0]:
                c.execute('CREATE TABLE version (major INTEGER, minor INTEGER, patch INTEGER)')
                c.execute('INSERT INTO version(major, minor, patch) VALUES(1, 4, 0)')

                c.execute('CREATE TABLE updates(id INTEGER PRIMARY KEY, source TEXT, date TEXT, programs_updated TIMESTAMP)')

                c.execute('CREATE TABLE programs(channel TEXT, title TEXT, start_date TIMESTAMP, end_date TIMESTAMP, description TEXT, image_large TEXT, image_small TEXT, source TEXT, subTitle TEXT)')

            self.connP.commit()
            c.close()

        except sqlite3.OperationalError, ex:
            raise DatabaseSchemaException(ex)


    def addNotification(self, program):
        self._invokeAndBlockForResult(self._addNotification, program)
        # no result, but block until operation is done


    def _addNotification(self, program):  #TODO
        return
        c = self.connS.cursor()
        c.execute("INSERT INTO notifications(channel, program_title, source) VALUES(?, ?, ?)", [program.channel.id, program.title, self.source.KEY])
        self.connS.commit()
        c.close()


    def removeNotification(self, program):
        self._invokeAndBlockForResult(self._removeNotification, program)


    def _removeNotification(self, program):  #TODO
        return
        c = self.connS.cursor()
        c.execute("DELETE FROM notifications WHERE channel=? AND program_title=? AND source=?", [program.channel.id, program.title, self.source.KEY])
        self.connS.commit()
        c.close()


    def getNotifications(self, daysLimit = 2):
        return self._invokeAndBlockForResult(self._getNotifications, daysLimit)

    def _getNotifications(self, daysLimit): #TODO
        start = datetime.datetime.now() - GMTOFFSET
        end   = start + datetime.timedelta(days = daysLimit)
        c     = self.connS.cursor()
        c.execute("SELECT DISTINCT c.title, p.title, p.start_date FROM notifications n, channels c, programs p WHERE n.channel = c.id AND p.channel = c.id AND n.program_title = p.title AND n.source=? AND p.start_date >= ? AND p.end_date <= ?", [self.source.KEY, start, end])
        programs = c.fetchall()
        c.close()

        return programs


    def isNotificationRequiredForProgram(self, program):
        return self._invokeAndBlockForResult(self._isNotificationRequiredForProgram, program)


    def _isNotificationRequiredForProgram(self, program):  #TODO
        c = self.connS.cursor()
        c.execute("SELECT 1 FROM notifications WHERE channel=? AND program_title=? AND source=?", [program.channel.id, program.title, self.source.KEY])
        result = c.fetchone()
        c.close()

        return result


    def clearAllNotifications(self):
        self._invokeAndBlockForResult(self._clearAllNotifications)
        # no result, but block until operation is done


    def _clearAllNotifications(self):  #TODO
        return
        c = self.connS.cursor()
        c.execute('DELETE FROM notifications')
        self.connS.commit()
        c.close()


    def resetChannels(self):
        self._invokeAndBlockForResult(self._resetChannels)


    def _resetChannels(self):
        self.channelDict = {}


class Source(object):
    def getDataFromExternal(self, date, progress_callback = None):
        """
        Retrieve data from external as a list or iterable. Data may contain both Channel and Program objects.
        The source may choose to ignore the date parameter and return all data available.

        @param date: the date to retrieve the data for
        @param progress_callback:
        @return:
        """
        return None


    def doSettingsChanged(self):
        return


    def isUpdated(self, channelsLastUpdated, programsLastUpdated):
        today = datetime.datetime.now()
        if channelsLastUpdated is None or channelsLastUpdated.day != today.day:
            return True

        if programsLastUpdated is None or programsLastUpdated.day != today.day:
            return True
        return False


class XMLTVSource(Source):
    KEY = 'xmltv'

    def __init__(self, addon):
        self.logoFolder = addon.getSetting('xmltv.logo.folder')
        self.xmltvFile = addon.getSetting('xmltv.file')

        if not self.xmltvFile or not xbmcvfs.exists(self.xmltvFile):
            raise SourceNotConfiguredException()

    def getDataFromExternal(self, date, progress_callback = None):
        f = FileWrapper(self.xmltvFile)
        context = ElementTree.iterparse(f, events=("start", "end"))
        return parseXMLTV(context, f, f.size, self.logoFolder, progress_callback)

    def isUpdated(self, channelsLastUpdated, programLastUpdate):
        if channelsLastUpdated is None or not xbmcvfs.exists(self.xmltvFile):
            return True

        stat = xbmcvfs.Stat(self.xmltvFile)
        fileUpdated = datetime.datetime.fromtimestamp(stat.st_mtime())
        return fileUpdated > channelsLastUpdated


class DIXIESource(Source):
    KEY = 'dixie'

    def isUpdated(self, channelsLastUpdated, programsLastUpdated):
        zero = datetime.datetime.fromtimestamp(0)
        if channelsLastUpdated is None or channelsLastUpdated == zero:
            return True

        current = int(dixie.GetSetting('current.channels'))
        update  = int(dixie.GetSetting('updated.channels'))

        #dixie.log('current = %d' % current)
        #dixie.log('update  = %d' % update)

        if update == -1:
            dixie.SetSetting('updated.channels', current)
            return True

        return current != update


    def __init__(self, addon):
        self.KEY += '.' + dixie.GetKey()
        self.xml = None

        gmt = addon.getSetting('gmtfrom').replace('GMT', '')
        if gmt == '':
            self.offset = 0
        else:
            self.offset = int(gmt)


    def getDataFromExternal(self, date, progress_callback = None):
        categoryPath = os.path.join(datapath, 'cats.xml')
        channels     = os.path.join(datapath, 'chan.xml')

        categories   = dixie.getCategoryList(categoryPath)

        xml = None
        
        try:
            if sfile.exists(channels):
                xml = sfile.read(channels)
        except:
            dixie.log('Error reading chan.xml')

        if not xml:
            return []
            
        
        if not self.xml:
            self.xml = xml
            
        io = StringIO.StringIO(self.xml)
        
        context = ElementTree.iterparse(io, events=("start", "end"))
        return parseXMLTV(context, io, len(self.xml), progress_callback, self.offset, categories)


    def doSettingsChanged(self):
        return


def parseXMLTVDate(dateString, offset):
    if dateString is not None:
        if dateString.find(' ') != -1:
            # remove timezone information
            dateString = dateString[:dateString.find(' ')]
        t = time.strptime(dateString, '%Y%m%d%H%M%S')
        d = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
        d += datetime.timedelta(hours = offset)
        return d
    else:
        return None


def parseXMLTV(context, f, size, progress_callback, offset=0, categories=None):
    event, root = context.next()
    elements_parsed = 0

    for event, elem in context:
        if event == "end":
            result = None
            if elem.tag == "programme":
                channel = elem.get("channel")
                title = elem.findtext("title")
                subTitle = elem.findtext("sub-title")
                category = elem.findtext("category")
                description = elem.findtext("desc")
                mergeTitle = elem.findtext("sub-title")
                if not description:
                    description = subTitle
                    
                result = Program(channel, title, parseXMLTVDate(elem.get('start'), offset), parseXMLTVDate(elem.get('stop'), offset), description, elem.findtext("sub-title"))

            elif elem.tag == "channel":
                id     = elem.get("id")
                title  = elem.findtext("display-name")
                result = Channel(id, title)

                if categories:
                    try:
                        category = categories[title]
                        result.categories = category
                        # dixie.log('The category for %s is %s' % (title, category))
                    except:
                        dixie.log('Couldnt find %s in the categories' % (title))

            if result:
                elements_parsed += 1
                if progress_callback and elements_parsed % 500 == 0:
                    if not progress_callback(100.0 / size * f.tell()):
                        raise SourceUpdateCanceledException()
                yield result

        root.clear()
    f.close()
    

class FileWrapper(object):
    def __init__(self, filename):
        self.vfsfile = xbmcvfs.File(filename)
        self.size = self.vfsfile.size()
        self.bytesRead = 0


    def close(self):
        self.vfsfile.close()


    def read(self, bytes):
        self.bytesRead += bytes
        return self.vfsfile.read(bytes)


    def tell(self):
        return self.bytesRead



def instantiateSource():
    activeSource = DIXIESource
    return activeSource(ADDON)

