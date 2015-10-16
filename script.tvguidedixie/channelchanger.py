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

ACTION_BACK  = 92
ACTION_STOP  = 122

ACTION_X          = 13
ACTION_PARENT_DIR = 9

ACTION_PLAY   = 79
# ACTION_SELECT = 7


PATH = os.path.join(dixie.PROFILE, 'extras', 'skins', dixie.SKIN)
XML  = 'script-tvguide-changer.xml'

OTT_CHANNELS = os.path.join(dixie.GetChannelFolder(), 'channels')
IGNORESTRM   = dixie.GetSetting('ignore.stream') == 'true'

CHANNELS_PER_PAGE = 8


def CleanFilename(text):
    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text


class ChannelChanger(xbmcgui.WindowXMLDialog):
    C_CHANNEL = 6000
    C_TITLE   = 6001
    C_LOGO    = 6002

    def __new__(cls, channel, epgMode=False):
        return super(ChannelChanger, cls).__new__(cls, XML, PATH)


    def __init__(self, channel, epgMode=False):
        super(ChannelChanger, self).__init__()

        self.channel     = channel
        self.closeTimer  = None
        self.list        = None
        self.epgMode     = True if epgMode else False
        
        self.streamingService = streaming.StreamsService()


    def close(self):         
        if self.closeTimer != None:
            self.closeTimer.cancel()

        xbmcgui.WindowXMLDialog.close(self) 


    def resetCloseTimer(self):
        if self.closeTimer != None:
            self.closeTimer.cancel()
            
        self.closeTimer = Timer(2, self.onCloseTimer)
        self.closeTimer.start()


    def onCloseTimer(self):
        if self.closeTimer == None:
            return

        if not self.epgMode:
           self.playChannel(self.channel)

        self.close()


    def setChannel(self, text):
        ctrl  = self.getControl(self.C_CHANNEL)
        title = self.getControl(self.C_TITLE)
        logo  = self.getControl(self.C_LOGO)

        dixie.log('Setting changer channel to %s' % text)

        channel = self.getChannel(text)

        if not channel:
            ctrl.setLabel('')
            title.setLabel('')
            logo.setVisible(False)
            self.channel = ''
            return

        ctrl.setLabel(text)
        title.setLabel(channel.title)
        logo.setVisible(True)
        logo.setImage(channel.logo)


    def playChannel(self, _channel):
        channel = self.getChannel(_channel)
        current = xbmcgui.Window(10000).getProperty('OTT_CHANNEL')

        if not channel:
            return
        
        if channel.id == current:
            return

        streamUrl = channel.streamUrl
        
        if not streamUrl:
           streamUrl = self.detectStream(channel)

        if not streamUrl:
            return

        xbmcgui.Window(10000).setProperty('OTT_CHANNEL', channel.id)

        prev = xbmcgui.Window(10000).getProperty('OTT_CURR_INDEX')

        xbmcgui.Window(10000).setProperty('OTT_PREV_INDEX', prev)
        xbmcgui.Window(10000).setProperty('OTT_CURR_INDEX', _channel)

        path = os.path.join(dixie.HOME, 'player.py')
        xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d,%s)' % (path, streamUrl, False, 'ChannelChanger'))


    def detectStream(self, channel):
        result = self.streamingService.detectStream(channel)
        
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
            return None


    def onInit(self):
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


    def onAction(self, action):
        try:
            actionId = action.getId()
            buttonId = action.getButtonCode()         

            if actionId == 107:
                return

            #dixie.log('************* channelchanger onAction *********************')
            #dixie.log(str(actionId))
            #dixie.log(str(buttonId))

            self.resetCloseTimer()        

            if actionId == KEY_ESC_ID and buttonId == KEY_ESC_CODE:
                self.close()
                return

            if actionId == ACTION_BACK: 
                if self.channel == '':
                    self.close()
                    return
                self.channel = self.channel[:-1]
                self.setChannel(self.channel)

            if actionId in [ACTION_UP, ACTION_PAGE_UP]:
                self.ChannelUp()

            if actionId in [ACTION_DOWN, ACTION_PAGE_DOWN]:
                self.ChannelDown();

            if actionId in [ACTION_LEFT, ACTION_RIGHT]:
                self.playPrevious()
                return
            
            if actionId == ACTION_X or actionId == ACTION_STOP:
                self.close()
                return

            # if actionId == ACTION_SELECT and self.epgMode:
            #     self.close()
            #     return

            if actionId == ACTION_PLAY:
                self.playChannel(self.channel)
                return                   

            if actionId >= ACTION_0 and actionId <= ACTION_9:
                self.channel = str(self.verifyChannel(self.channel, actionId - ACTION_0))

            self.setChannel(self.channel)
          
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


    def ChannelDown(self):
        if self.channel == '':
            self.channel = str(len(self.list))

        ch = int(self.channel) - 1        

        if ch == 0:
            ch = len(self.list)

        self.channel = str(ch)


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

            if not channel.visible:
                continue

            sorter  = channel.title.lower() if alphaSort else channel.weight

            sorted.append([sorter, id, channel])

        sorted.sort()

        self.list = []
        for channel in sorted:
            self.list.append(channel[2])

        if self.channel <> '':
            return

        current = xbmcgui.Window(10000).getProperty('OTT_CHANNEL')
        index = 0
        for channel in self.list:
            index += 1            
            if channel.id == current:
                self.channel = str(index)
                self.setChannel(self.channel)     
                xbmcgui.Window(10000).setProperty('OTT_CURR_INDEX', self.channel)
                return


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
    channel = ChannelChanger('')
    channel.doModal()     
    del channel