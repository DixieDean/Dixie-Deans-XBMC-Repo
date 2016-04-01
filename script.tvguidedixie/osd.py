#
#       Copyright (C) 2015-
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
import xbmcgui

from threading import Timer 
import os
import re

import dixie
import sfile

from channel import Channel
from source import Program
from info import InfoService

import streaming

KEY_ESC_ID   = 10
KEY_ESC_CODE = 61467

ACTION_0 = 58
ACTION_1 = 59
ACTION_2 = 60
ACTION_3 = 61
ACTION_4 = 61
ACTION_5 = 63
ACTION_6 = 64
ACTION_7 = 65
ACTION_8 = 66
ACTION_9 = 67

ACTION_LEFT      = 1
ACTION_RIGHT     = 2
ACTION_UP        = 3
ACTION_DOWN      = 4
ACTION_PAGE_UP   = 5
ACTION_PAGE_DOWN = 6

CHANNELS_PER_PAGE = 10

ACTION_BACK  = 92
ACTION_STOP  = 122

ACTION_X          = 13
ACTION_PARENT_DIR = 9

ACTION_PLAY   = 79
ACTION_SELECT = 7

ACTION_HOTKEY = dixie.GetSetting('hot_key')

ACTION_SHOW_INFO = -1 #currently not used

PATH = os.path.join(dixie.PROFILE, 'extras', 'skins', dixie.SKIN)
XML  = 'script-tvguide-changer.xml'

OTT_CHANNELS = os.path.join(dixie.GetChannelFolder(), 'channels')
IGNORESTRM   = dixie.GetSetting('ignore.stream') == 'true'

DSF = dixie.isDSF()

MAIN          = 5000
EPG_CHANNEL   = 6000
EPG_METADATA  = 6001
OSD_MINIGUIDE = 7000
OSD_METADATA  = 7001
OSD_TITLEBAR  = 7002


def CleanFilename(text):
    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text


class OSD(xbmcgui.WindowXMLDialog):

    def __new__(cls, channel='', epgMode=False, osdMode=False):
        return super(OSD, cls).__new__(cls, XML, PATH)


    def __init__(self, channel='', epgMode=False, osdMode=False):
        super(OSD, self).__init__()

        self.channel     = channel
        self.closeTimer  = None
        self.list        = None
        self.showInfo    = False
        self.epgMode     = epgMode
        self.osdMode     = osdMode
        self.infoService = InfoService()
        self.now         = None
        self.next        = None
        self.other       = None
        self.protected   = dixie.isProtected()
        self.categories  = []

        cats = dixie.getCategories()
        for cat in cats:
            if len(cat) > 0:
                self.categories.append(cat)

        self.streamingService = streaming.StreamsService()

        
    def close(self):
        if self.closeTimer != None:
            self.closeTimer.cancel()

        channel = self.getChannel(self.channel)
        if channel:
            xbmcgui.Window(10000).setProperty('OTT_CHANNEL', channel.id)

        Timer(2, self.onClose).start()


    def onClose(self):
        xbmcgui.Window(10000).clearProperty('OTT_OSD_RUNNING')
        xbmcgui.WindowXMLDialog.close(self)


    def resetCloseTimer(self):
        return
        if self.closeTimer != None:
            self.closeTimer.cancel()

        interval = 10
            
        self.closeTimer = Timer(interval, self.onCloseTimer)
        self.closeTimer.start()


    def onCloseTimer(self):
        if self.closeTimer == None:
            return

        if self.showInfo or self.osdMode:
            self.resetCloseTimer()
            return

        if (not self.epgMode) and (not self.osdMode):
           self.playChannel(self.channel)

        self.close()


    def toggleInfo(self):
        self.showInfo = not self.showInfo

        if self.epgMode:
            try:    self.getControl(EPG_METADATA).setVisible(self.showInfo)
            except: pass

        x = self.osdX
        y = self.osdY # -100 if self.showInfo else self.osdY

        try:    self.getControl(OSD_MINIGUIDE).setPosition(x, y)
        except: pass

        try:    self.getControl(OSD_MINIGUIDE).setVisible(self.showInfo)
        except: pass
        

    def setChannel(self, text):
        dixie.log('Setting changer channel to %s' % text)

        channel = self.getChannel(text)

        if not channel:
            xbmcgui.Window(10000).setProperty('OTT_CH_LOGO',   '')
            xbmcgui.Window(10000).setProperty('OTT_CH_TITLE',  '')
            xbmcgui.Window(10000).setProperty('OTT_CH_NUMBER', '')
            self.channel = ''
        else:
            xbmcgui.Window(10000).setProperty('OTT_CH_LOGO',   channel.logo)
            xbmcgui.Window(10000).setProperty('OTT_CH_TITLE',  channel.title)
            xbmcgui.Window(10000).setProperty('OTT_CH_NUMBER', text)

        self.updateProgramInfo(channel)


    def previousProgram(self):
        if not self.other:
            self.other = self.infoService.getPreviousProgram(self.now)
        else:
            self.other = self.infoService.getPreviousProgram(self.other)

        self.updateLabels()


    def nextProgram(self):
        if not self.other:
            self.other = self.infoService.getNextProgram(self.next)
        else:
            self.other = self.infoService.getNextProgram(self.other)

        self.updateLabels()


    def updateProgramInfo(self, channel):
        import info
        
        if self.epgMode:
            return

        self.now   = None
        self.next  = None
        self.other = None

        self.now  = self.infoService.getCurrentProgram(channel)
        self.next = self.infoService.getNextProgram(self.now)   

        self.updateLabels()


    def updateLabels(self):
        if self.other and (self.other.startDate < self.now.startDate):
            self.other = None

        if self.other and (self.other.startDate == self.next.startDate):
            self.other = None

        if self.other and (self.other.startDate == self.now.startDate):
            self.other = None
   
        if self.now:
            xbmcgui.Window(10000).setProperty('OTT_NOW_TITLE',  self.now.title)
            xbmcgui.Window(10000).setProperty('OTT_NOW_TIME',   self.now.startDate.strftime('%H:%M'))
            xbmcgui.Window(10000).setProperty('OTT_PROG_DESC',  self.now.description)

        if self.other:
            label = 'EARLIER' if (self.other.startDate < self.now.startDate) else 'LATER'
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TEXT',   label)
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TITLE',  self.other.title)
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TIME',   self.other.startDate.strftime('%H:%M'))

        elif self.next:
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TEXT',  'NEXT')
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TITLE',  self.next.title)
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TIME',   self.next.startDate.strftime('%H:%M'))

        if not self.now:
            xbmcgui.Window(10000).setProperty('OTT_NOW_TITLE',  'No listings available for this channel')
            xbmcgui.Window(10000).setProperty('OTT_NOW_TIME',   '')
            xbmcgui.Window(10000).setProperty('OTT_PROG_DESC',  'No listings available for this channel')

        if (not self.next) and (not self.other):
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TEXT',   '')
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TITLE',  '')
            xbmcgui.Window(10000).setProperty('OTT_NEXT_TIME',   '')


    def playChannel(self, _channel):
        channel = self.getChannel(_channel)
        current = xbmcgui.Window(10000).getProperty('OTT_CHANNEL')

        if not channel:
            return
        
        if channel.id == current:
            if not self.osdMode:
                return

        if DSF:
            streamUrl = 'DSF:%s' % channel.id
        else:
            streamUrl = channel.streamUrl
        
        if not streamUrl:
           streamUrl = self.detectStream(channel)

        if not streamUrl:
            return

        #xbmcgui.Window(10000).setProperty('OTT_CHANNEL', channel.id)

        prev = xbmcgui.Window(10000).getProperty('OTT_CURR_INDEX')

        xbmcgui.Window(10000).setProperty('OTT_PREV_INDEX', prev)
        xbmcgui.Window(10000).setProperty('OTT_CURR_INDEX', _channel)

        path = os.path.join(dixie.HOME, 'player.py')
        xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d,%s)' % (path, streamUrl, False, 'OSD'))


    def detectStream(self, channel):
        result = self.streamingService.detectStream(channel)

        if type(result) == str:
            self.setCustomStreamUrl(channel, result)
            return result
        
        if len(result) < 1:
            dixie.DialogOK('Sorry, we could not detect a stream.', '', 'Please allocate a stream for this channel.')
            return None

        import detect

        d = detect.StreamAddonDialog(result)
        d.doModal()
        
        if not d.stream:
            return None

        if not IGNORESTRM:
            self.setCustomStreamUrl(channel, d.stream)
        
        return d.stream


    def playPrevious(self):
        prevChan = xbmcgui.Window(10000).getProperty('OTT_PREV_INDEX')

        if len(prevChan) == 0:
            return False

        self.setChannel(prevChan)
        self.playChannel(prevChan)
        return True
        
    
    def getChannel(self, channel):
        try:
            index = int(channel) - 1
            if index < 0:
                return None

            return self.list[index]
        except:
            pass

        return None


    def validChannel(self, channel):
        if not channel.visible:
            return False

        if not self.protected and channel.isProtected():
            return False

        if len(self.categories) == 0:
            return True

        cats = channel.categories.split('|')
        for cat in cats:
            if cat in self.categories:
                return True

        return False


    def onInit(self):
        try:    self.getControl(MAIN).setVisible(False)
        except: pass

        try:    self.getControl(EPG_CHANNEL).setVisible(self.epgMode)
        except: pass

        try:    self.getControl(OSD_METADATA).setVisible(not self.epgMode)
        except: pass

        try:    self.getControl(EPG_METADATA).setVisible(False)
        except: pass

        try:    self.getControl(OSD_MINIGUIDE).setVisible(not self.epgMode)
        except: pass

        # try:    self.getControl(OSD_MINIGUIDE).setVisible(self.showInfo)
        # except: pass

        try:    self.getControl(OSD_TITLEBAR).setVisible(not self.epgMode)
        except: pass

        try:
             self.osdX = self.getControl(OSD_MINIGUIDE).getPosition()[0]
             self.osdY = self.getControl(OSD_MINIGUIDE).getPosition()[1]
        except:
            pass

        try:
            self.populateChannels()

            if self.channel == 'PREV':
                self.channel = ''
                if self.playPrevious():
                    self.close()
                    return

            if len(self.channel) < 0:
                self.channel = 1

            self.setChannel(self.channel)
            self.resetCloseTimer()
 
        except Exception:
            raise

        try:    
            self.getControl(MAIN).setPosition(0,0)
            self.getControl(MAIN).setVisible(True)
        except:
            pass


    def onAction(self, action):
        try:
            actionId = action.getId()
            buttonId = action.getButtonCode()

            if actionId != 107:
                dixie.log(str(actionId))
                dixie.log(str(buttonId))

            self.resetCloseTimer()

            if actionId == ACTION_HOTKEY:
                self.close()
                return

            if actionId == KEY_ESC_ID and buttonId == KEY_ESC_CODE:
                self.close()
                return

            if actionId == ACTION_BACK: 
                self.close()
                return

            if actionId in [ACTION_UP]:
                self.ChannelUp()

            if actionId in [ACTION_PAGE_UP]:
                self.PageUp(CHANNELS_PER_PAGE)

            if actionId in [ACTION_DOWN]:
                self.ChannelDown()

            if actionId in [ACTION_PAGE_DOWN]:
                self.PageDown(CHANNELS_PER_PAGE)

            if actionId == ACTION_LEFT:
                self.playPrevious()
                return

            if actionId == ACTION_RIGHT:
                self.nextProgram()
                return
            
            if actionId == ACTION_X or actionId == ACTION_STOP:
                self.close()
                return

            if actionId == ACTION_SELECT:
                if not self.epgMode:
                    self.playChannel(self.channel)
                self.close()
                return

            if actionId == ACTION_PLAY:
                self.playChannel(self.channel)
                return

            if actionId >= ACTION_0 and actionId <= ACTION_9:
                self.channel = str(self.verifyChannel(self.channel, actionId - ACTION_0))
                self.setChannel(self.channel)
            
            if actionId == ACTION_SHOW_INFO:
                self.toggleInfo()


        except Exception:
            raise


    def verifyChannel(self, oldChannel, newNumber):
        try:    oldNumber = int(oldChannel)
        except: return newNumber

        newChannel = (oldNumber * 10) + newNumber

        if newChannel <= len(self.list):
            return newChannel

        if newNumber <= len(self.list):
            return newNumber

        return oldChannel


    def ChannelUp(self):
        if self.channel == '':
            self.channel = '1'

        ch = int(self.channel) + 1

        if ch > len(self.list):
            ch = 1

        self.channel = str(ch)
        self.setChannel(self.channel)


    def PageUp(self, count = 1):
        if self.channel == '':
            self.channel = '1'

        ch = int(self.channel) + count

        if ch > len(self.list):
            ch = 1

        self.channel = str(ch)
        self.setChannel(self.channel)


    def ChannelDown(self):
        if self.channel == '':
            self.channel = str(len(self.list))

        ch = int(self.channel) - 1

        if ch == 0:
            ch = len(self.list)

        self.channel = str(ch)
        self.setChannel(self.channel)


    def PageDown(self, count = 1):
        if self.channel == '':
            self.channel = '1'

        ch = int(self.channel) - count

        if ch > len(self.list):
            ch = 1

        self.channel = str(ch)
        self.setChannel(self.channel)


    def getChannelFromFile(self, id):
        path = os.path.join(OTT_CHANNELS, id)

        if not sfile.exists(path):
            return None

        cfg = sfile.readlines(path)

        return Channel(cfg)


    def populateChannels(self, alphaSort = False):
        channels = []

        try:
            current, dirs, files = sfile.walk(OTT_CHANNELS)
        except Exception, e:
            return channels

        for file in files:
            channels.append(file)

        sorted = []

        for id in channels:
            channel = self.getChannelFromFile(id)

            if not self.validChannel(channel):
                continue

            sorter = channel.title.lower() if alphaSort else channel.weight

            sorted.append([sorter, id, channel])

        sorted.sort()

        self.list = []
        for channel in sorted:
            self.list.append(channel[2])

        try:
            if int(self.channel) >= len(self.list):
                self.channel = '1'
        except Exception, e:
            self.channel = ''
            pass

        current = xbmcgui.Window(10000).getProperty('OTT_CHANNEL')
        #xbmcgui.Window(10000).clearProperty('OTT_CHANNEL')
        
        if self.osdMode:
            if len(current) == 0:
                self.channel = '1'

        elif self.channel <> '':
            return

        index = 0
        for channel in self.list:
            index += 1
            if channel.id == current:
                self.channel = str(index)
                self.setChannel(self.channel)
                xbmcgui.Window(10000).setProperty('OTT_CURR_INDEX', self.channel)
                return

        #not found so set to start
        self.channel = '1'


    def removeCleanChannel(self, id):
        path = os.path.join(OTT_CHANNELS, id)
        if sfile.exists(path):
            try:    sfile.remove(path)
            except: pass


    def addCleanChannel(self, channel, id):
        path = os.path.join(OTT_CHANNELS, id) 

        if not sfile.exists(path): 
            channel.writeToFile(path)


    def setCustomStreamUrl(self, channel, stream_url):
        id = CleanFilename(channel.id)


        channel.streamUrl = stream_url

        self.removeCleanChannel(id)
        self.addCleanChannel(channel, id)


if __name__ == '__main__':
    xbmcgui.Window(10000).setProperty('OTT_OSD_RUNNING', 'TRUE')
    channel = OSD(osdMode=True)
    channel.doModal()
    del channel
