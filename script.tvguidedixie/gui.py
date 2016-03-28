#
#      Copyright (C) 2014 Sean Poyser - With acknowledgement to some original code by twinther (Tommy Winther)
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

import datetime
import threading
import time
import xbmc
import xbmcgui

import source as src
from notification import Notification
from strings import *

import streaming
import xbmcaddon
import xbmc
import os
import shutil
import urllib

import dixie
import deleteDB

import filmon

OTT_CHANNEL = ['Your Channel. Your content.', 'Your Channel. Your Choice.','All day, Every day...', 'Online Radio', 'Android only channel.']


ADDON      = dixie.ADDON
HOME       = dixie.HOME
SKIN       = dixie.SKIN
GMTOFFSET  = dixie.GetGMTOffset()
TRAILERS   = ADDON.getSetting('trailers.addon')
USTV       = ADDON.getSetting('ustv.addon')
IGNORESTRM = ADDON.getSetting('ignore.stream') == 'true'
META_IMAGE = dixie.GetSetting('meta.image')


confirmExit = ADDON.getSetting('confirm.exit').lower() == 'true'
datapath    = dixie.PROFILE
extras      = os.path.join(datapath, 'extras')
skinfolder  = os.path.join(datapath, extras, 'skins')
skinpath    = os.path.join(skinfolder, SKIN)

PATH = skinpath
DSF  = dixie.isDSF()


xml_file = os.path.join('script-tvguide-main.xml')
if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
    XML  = xml_file


MODE_EPG = 'EPG'
MODE_TV = 'TV'
MODE_OSD = 'OSD'

ACTION_LEFT = 1
ACTION_RIGHT = 2
ACTION_UP = 3
ACTION_DOWN = 4
ACTION_PAGE_UP = 5
ACTION_PAGE_DOWN = 6
ACTION_SELECT_ITEM = 7
ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10
ACTION_SHOW_INFO = 11
ACTION_NEXT_ITEM = 14
ACTION_PREV_ITEM = 15

ACTION_MOUSE_WHEEL_UP = 104
ACTION_MOUSE_WHEEL_DOWN = 105
ACTION_MOUSE_MOVE = 107

ACTION_TOUCH_TAP           = 401
ACTION_TOUCH_LONGPRESS     = 411
ACTION_GESTURE_SWIPE_LEFT  = 511
ACTION_GESTURE_SWIPE_RIGHT = 521
ACTION_GESTURE_SWIPE_UP    = 531
ACTION_GESTURE_SWIPE_DOWN  = 541
ACTION_GESTURE_ZOOM        = 502
ACTION_GESTURE_ROTATE      = 503
ACTION_GESTURE_PAN         = 504

KEYZERO = 58

KEY_NAV_BACK = 92
KEY_CONTEXT_MENU = 117
KEY_HOME = 159
KEY_SUPER_SEARCH = 77

CHANNELS_PER_PAGE = 8
TEXT_COLOR = '0xffffffff'
FOCUSED_COLOR = '0xffffffff'
SHADOW_COLOR = 'None'
REMOVE_STRM_FILE    = strings(REMOVE_STRM_FILE)
CHOOSE_STRM_FILE    = strings(CHOOSE_STRM_FILE)
REMIND_PROGRAM      = strings(REMIND_PROGRAM)
DONT_REMIND_PROGRAM = strings(DONT_REMIND_PROGRAM)

HALF_HOUR = datetime.timedelta(minutes = 30)


try:
    #load cfg from file
    f   = open(os.path.join(PATH, 'epg.cfg'))
    cfg = f.readlines()
    f.close()

    for l in cfg:
        l = l.strip()
        #sanity check on text
        pts = l.split('=')
        if len(pts) == 2:
            exec(l)
except:
    pass

def debug(s):
    dixie.log(str(s))

class Point(object):
    def __init__(self):
        self.x = self.y = 0

    def __repr__(self):
        return 'Point(x=%d, y=%d)' % (self.x, self.y)

class EPGView(object):
    def __init__(self):
        self.top = self.left = self.right = self.bottom = self.width = self.cellHeight = 0

class ControlAndProgram(object):
    def __init__(self, control, program):
        self.control = control
        self.program = program

C_CATEGORIES_CTRL = 9000
C_CATEGORIES_LIST = 9001

class TVGuide(xbmcgui.WindowXML):
    C_MAIN_DATE = 4000
    C_MAIN_TITLE = 4020
    C_MAIN_TIME = 4021
    C_MAIN_DESCRIPTION = 4022
    C_MAIN_IMAGE = 4023
    C_MAIN_LOGO = 4024
    C_MAIN_TIMEBAR = 4100
    C_MAIN_LOADING = 4200
    C_MAIN_LOADING_PROGRESS = 4201
    C_MAIN_LOADING_TIME_LEFT = 4202
    C_MAIN_LOADING_CANCEL = 4203
    C_MAIN_MOUSE_CONTROLS = 4300
    C_MAIN_MOUSE_HOME = 4301
    C_MAIN_MOUSE_LEFT = 4302
    C_MAIN_MOUSE_UP = 4303
    C_MAIN_MOUSE_DOWN = 4304
    C_MAIN_MOUSE_RIGHT = 4305
    C_MAIN_MOUSE_EXIT = 4306
    C_MAIN_BACKGROUND = 4600
    C_MAIN_EPG = 5000
    C_MAIN_EPG_VIEW_MARKER = 5001
    C_MAIN_OSD = 6000
    C_MAIN_OSD_TITLE = 6001
    C_MAIN_OSD_TIME = 6002
    C_MAIN_OSD_DESCRIPTION = 6003
    C_MAIN_OSD_CHANNEL_LOGO = 6004
    C_MAIN_OSD_CHANNEL_TITLE = 6005
    C_MAIN_BLACKOUT = 9999

    def __new__(cls):
        return super(TVGuide, cls).__new__(cls, XML, PATH)

    def __init__(self):
        super(TVGuide, self).__init__()
        self.initialized = False
        self.refresh = False
        self.notification = None
        self.redrawingEPG = False
        self.timebarVisible = False
        self.isClosing = False
        self.controlAndProgramList = list()
        self.ignoreMissingControlIds = [C_CATEGORIES_CTRL, C_CATEGORIES_LIST]
        self.channelIdx = 0
        self.focusPoint = Point()
        self.epgView = EPGView()
        self.streamingService = streaming.StreamsService()
        self.blackout = None
        self.player = xbmc.Player()
        self.database = None
        self.categoriesList = dixie.getCategories()
        if self.categoriesList[0] == '':
            self.categoriesList = []
        self.mode = MODE_EPG
        self.currentChannel = None
        self.highlight      = None

        self.osdEnabled = ADDON.getSetting('enable.osd') == 'true' and ADDON.getSetting('alternative.playback') != 'true'
        self.alternativePlayback = ADDON.getSetting('alternative.playback') == 'true'
        self.osdChannel = None
        self.osdProgram = None
        self.osdWhen    = datetime.datetime.today() - datetime.timedelta(seconds=30) #ie in the past

        self.touch    = False
        self.prevCtrl = -1

        if ADDON.getSetting('enable.touch') == 'true':
            self.touch = True

        # find nearest half hour
        self.viewStartDate = datetime.datetime.today()
        self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)


    def refreshChannelLabels(self, channelStart):
        base = 7001
        for i in range(CHANNELS_PER_PAGE):
            try:
                ctrl = self.getControl(base+i)
                if ctrl:
                    ctrl.setLabel(str(channelStart+i+1))
            except:
                pass


    def getControl(self, controlId):
        try:
            return super(TVGuide, self).getControl(controlId)
        except:
            if controlId in self.ignoreMissingControlIds:
                return None
            if not self.isClosing:
                dixie.DialogOK(strings(SKIN_ERROR_LINE1), strings(SKIN_ERROR_LINE2), strings(SKIN_ERROR_LINE3))
                self.close()
            return None

 
    def resetTimer(self):
        try:
            self.stopTimer()
            self.timer = threading.Timer(1*60, self.onTimer)        
            self.timer.start()
        except Exception, e:
            pass
         
    def stopTimer(self):                   
        try:    self.timer.cancel()        
        except: pass
 
 
    def onTimer(self):
        refresh = 30 * 60 #30 minutes

        timeDelta = datetime.datetime.today() - self.viewStartDate
        secs      = timeDelta.seconds
        days      = timeDelta.days
        inZone    = (days == 0) and (secs < 2*60*60)

        if secs > refresh and inZone:
            self.viewStartDate  = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
        
        self.updateTimebar() 
        self.resetTimer()
 
 
    def close(self):
        dixie.removeKepmap()
        try:
            self.stopTimer()
            del self.timer
        except:
            pass
 
        if not self.isClosing:
            self.isClosing = True
            # if self.player.isPlaying():
            #     self.player.stop()
            if self.database:
                self.database.close(self.final)
            else:
                self.final()

    def final(self):
        xbmcgui.WindowXML.close(self)

    def hideBlackout(self):
        return
        if self.blackout:
            self.removeControl(self.blackout)
            self.blackout = None

    def showBlackout(self):
        return
        img = os.path.join(dixie.RESOURCES, 'blackout.jpg')
        self.hideBlackout()
        self.blackout = xbmcgui.ControlImage(0, 0, 1280, 720, img)
        self.addControl(self.blackout)


    def onInit(self):
        if self.initialized:
            if self.refresh:
                self.refresh = False
                self.database.resetChannels()
                self.onRedrawEPG(self.channelIdx, self.viewStartDate)
                # onInit(..) is invoked again by XBMC after a video addon exits after being invoked by XBMC.RunPlugin(..)
            return

        windowID = xbmcgui.getCurrentWindowId()
        xbmcgui.Window(10000).setProperty('OTT_WINDOW', str(windowID))          

        self.initialized = True
        self._hideControl(self.C_MAIN_MOUSE_CONTROLS, self.C_MAIN_OSD)
        self._showControl(self.C_MAIN_EPG, self.C_MAIN_LOADING)
        self._showControl(self.C_MAIN_BLACKOUT)
        self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(BACKGROUND_UPDATE_IN_PROGRESS))
        self.setFocusId(self.C_MAIN_LOADING_CANCEL)

        control = self.getControl(self.C_MAIN_EPG_VIEW_MARKER)
        if control:
            left, top = control.getPosition()
            self.focusPoint.x = left
            self.focusPoint.y = top
            self.epgView.left = left
            self.epgView.top = top
            self.epgView.right = left + control.getWidth()
            self.epgView.bottom = top + control.getHeight()
            self.epgView.width = control.getWidth()
            self.epgView.cellHeight = (control.getHeight() / CHANNELS_PER_PAGE)

        try:
            self.database = src.Database(CHANNELS_PER_PAGE)
            self.cats = CategoriesMenu1(self.database, self.categoriesList, self)
        except src.SourceNotConfiguredException:
            self.onSourceNotConfigured()
            self.close()
            return

        self.database.initializeS(self.onSourceInitializedS, self.isSourceInitializationCancelled)

        self.resetTimer()


    def onAction(self, action):
        debug('Mode is: %s' % self.mode)

        if self.mode == MODE_TV:
            self.onActionTVMode(action)
        elif self.mode == MODE_OSD:
            self.onActionOSDMode(action)
        elif self.mode == MODE_EPG:
            self.onActionEPGMode(action)

    def onActionTVMode(self, action):
        if action.getId() == ACTION_PAGE_UP:
            self._channelUp()

        elif action.getId() == ACTION_PAGE_DOWN:
            self._channelDown()

        elif not self.osdEnabled:
            pass # skip the rest of the actions

        elif action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK, KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
            self.viewStartDate = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)

        elif action.getId() == ACTION_SHOW_INFO:
            self._showOsd()

    def onActionOSDMode(self, action):
        if action.getId() == ACTION_SHOW_INFO:
            self._hideOsd()

        elif action.getId() in [ACTION_PARENT_DIR, KEY_NAV_BACK, KEY_CONTEXT_MENU, ACTION_PREVIOUS_MENU]:
            self._hideOsd()
            self.viewStartDate = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)

        elif action.getId() == ACTION_SELECT_ITEM:
            if self.playChannel(self.osdChannel):
                self._hideOsd()

        elif action.getId() == ACTION_PAGE_UP:
            self._channelUp()
            self._showOsd()

        elif action.getId() == ACTION_PAGE_DOWN:
            self._channelDown()
            self._showOsd()

        elif action.getId() == ACTION_UP:
            self.osdChannel = self.database.getPreviousChannel(self.osdChannel)
            self.osdProgram = self.database.getCurrentProgram(self.osdChannel)
            self._showOsd()

        elif action.getId() == ACTION_DOWN:
            self.osdChannel = self.database.getNextChannel(self.osdChannel)
            self.osdProgram = self.database.getCurrentProgram(self.osdChannel)
            self._showOsd()

        elif action.getId() == ACTION_LEFT:
            previousProgram = self.database.getPreviousProgram(self.osdProgram)
            if previousProgram:
                self.osdProgram = previousProgram
                self._showOsd()

        elif action.getId() == ACTION_RIGHT:
            nextProgram = self.database.getNextProgram(self.osdProgram)
            if nextProgram:
                self.osdProgram = nextProgram
                self._showOsd()

    def onActionEPGMode(self, action):
        actionId = self.checkTouch(action)
        if actionId == None:
            return

        if actionId in [ACTION_PARENT_DIR, KEY_NAV_BACK, ACTION_PREVIOUS_MENU]:
            if not confirmExit or dixie.DialogYesNo('Are you sure you wish to quit On-Tapp.TV?'):
                self.close()
                return

        elif actionId == ACTION_MOUSE_MOVE:
            self._showControl(self.C_MAIN_MOUSE_CONTROLS)
            return

        elif actionId == KEY_CONTEXT_MENU:
            if self.player.isPlaying():
                self._hideEpg()

        controlInFocus = None
        currentFocus   = self.focusPoint
        try:
            if self.cats.onAction(action):
                return    

            controlInFocus = self.getFocus()

            if controlInFocus in [elem.control for elem in self.controlAndProgramList]:
                (left, top) = controlInFocus.getPosition()
                currentFocus = Point()
                currentFocus.x = left + (controlInFocus.getWidth() / 2)
                currentFocus.y = top + (controlInFocus.getHeight() / 2)
        except Exception, e:
            xbmc.log(str(e))
            control = self._findControlAt(self.focusPoint)
            if control is None and len(self.controlAndProgramList) > 0:
                control = self.controlAndProgramList[0].control
            if control is not None:
                if not self.touch:
                    self.setFocus(control)
                return

        if actionId == ACTION_LEFT:
            self._left(currentFocus)
        elif actionId == ACTION_RIGHT:
            self._right(currentFocus)
        elif actionId == ACTION_UP:
            self._up(currentFocus)
        elif actionId == ACTION_DOWN:
            self._down(currentFocus)
        elif actionId == ACTION_NEXT_ITEM:
            self._nextDay()
        elif actionId == ACTION_PREV_ITEM:
            self._previousDay()
        elif actionId == ACTION_PAGE_UP:
            self._moveUp(CHANNELS_PER_PAGE)
        elif actionId == ACTION_PAGE_DOWN:
            self._moveDown(CHANNELS_PER_PAGE)
        elif actionId == ACTION_MOUSE_WHEEL_UP:
            self._moveUp(scrollEvent = True)
        elif actionId == ACTION_MOUSE_WHEEL_DOWN:
            self._moveDown(scrollEvent = True)
        elif actionId == KEY_HOME:
            self.viewStartDate = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
        elif actionId in [KEY_CONTEXT_MENU] and controlInFocus is not None:
            program = self._getProgramFromControl(controlInFocus)
            if (program is not None) and (not dixie.isLimited()):
                self._showContextMenu(program)
        elif actionId == KEY_SUPER_SEARCH:
            try:
                program = self._getProgramFromControl(controlInFocus)
                xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d&keyword=%s")' % (10025,'plugin.program.super.favourites', 0, urllib.quote_plus(program.title)))
            except:
                pass

        if actionId in range(KEYZERO, KEYZERO+10):
            now = datetime.datetime.today()
            #don't allow 2 OSD to be created
            if (now - self.osdWhen).seconds > 1.5:
                self.osdWhen = now
                key = actionId - KEYZERO
                from osd import OSD
                channel = OSD(str(key), True)
                channel.doModal()  
                selection = channel.channel
                del channel
                try:
                    self.channelIdx = int(selection)-1

                    self.onRedrawEPG(self.channelIdx, self.viewStartDate) 
                    self.resetFocus()

                except Exception, e:
                    pass


    def resetFocus(self):
        try:
            if len(self.controlAndProgramList) < 1:
                return

            title = self.getControl(4010).getLabel()

            for pair in self.controlAndProgramList:
                if pair.program.channel.title == title:
                    self.setFocus(pair.control)
                    return

            self.setFocus(controlAndProgramList[0].control)
        except Exception, e:
            pass


    def resetToChannel(self, channelID):
        channels = self.database.getChannelList(onlyVisible=True)

        index = 0
        for channel in channels:
            if channelID == channel.id:
                self.onRedrawEPG(index, self.viewStartDate)
                return            
            index += 1

        self.onRedrawEPG(0, self.viewStartDate)


    def checkTouch(self,  action):
        id = action.getId()

        if id not in [ACTION_GESTURE_ZOOM, ACTION_GESTURE_ROTATE, ACTION_GESTURE_PAN, ACTION_TOUCH_TAP, ACTION_TOUCH_LONGPRESS, ACTION_GESTURE_SWIPE_LEFT, ACTION_GESTURE_SWIPE_RIGHT, ACTION_GESTURE_SWIPE_UP, ACTION_GESTURE_SWIPE_DOWN]:
            return id

        if id in [ACTION_GESTURE_ZOOM, ACTION_GESTURE_ROTATE]:
            return id

        if id == ACTION_TOUCH_TAP:
            return id

        try:    controlInFocus = self.getFocus()
        except: controlInFocus = None
        if controlInFocus:
            if self._getProgramFromControl(controlInFocus) != None:
                return id

        #never triggered due to back action
        #if id == ACTION_TOUCH_LONGPRESS:
        #    return KEY_HOME

        if id == ACTION_GESTURE_SWIPE_LEFT:
            self.onClick(self.C_MAIN_MOUSE_RIGHT)
            return None

        if id == ACTION_GESTURE_SWIPE_RIGHT:
            self.onClick(self.C_MAIN_MOUSE_LEFT)
            return None

        if id == ACTION_GESTURE_SWIPE_UP:
            #return ACTION_MOUSE_WHEEL_UP
            self.onClick(self.C_MAIN_MOUSE_DOWN)
            return None

        if id == ACTION_GESTURE_SWIPE_DOWN:
            #return ACTION_MOUSE_WHEEL_DOWN
            self.onClick(self.C_MAIN_MOUSE_UP)
            return None

        return id


    def onClick(self, controlId):
        if controlId in [self.C_MAIN_LOADING_CANCEL, self.C_MAIN_MOUSE_EXIT]:
            self.close()
            return

        if self.isClosing:
            return

        if self.cats.onClick(controlId):
            return

        if controlId == self.C_MAIN_MOUSE_HOME:
            self.viewStartDate = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
            return
        elif controlId == self.C_MAIN_MOUSE_LEFT:
            self.viewStartDate -= datetime.timedelta(hours = 2)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
            return
        elif controlId == self.C_MAIN_MOUSE_UP:
            self._moveUp(count = CHANNELS_PER_PAGE)
            return
        elif controlId == self.C_MAIN_MOUSE_DOWN:
            self._moveDown(count = CHANNELS_PER_PAGE)
            return
        elif controlId == self.C_MAIN_MOUSE_RIGHT:
            when = self.viewStartDate + datetime.timedelta(hours = 2)
            if when.date() > self.database.updateLimit:
                return
            self.viewStartDate = when
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
            return

        prevCtrl      = self.prevCtrl
        self.prevCtrl = controlId
        if self.touch:
            if prevCtrl != self.prevCtrl:
                return

        program = self._getProgramFromControl(self.getControl(controlId))
        if program is None:
            return

        if self.touch:
            self._showContextMenu(program)
            return


        self.tryProgram(program)


    def tryProgram(self, program):
        if self.playChannel(program.channel):
            return
        result = self.streamingService.detectStream(program.channel)
        if not result:
            if self.touch:
                return
            # could not detect stream, show context menu
            self._showContextMenu(program)
        elif type(result) == str:
            # one single stream detected, save it and start streaming
            self.database.setCustomStreamUrl(program.channel, result)
            self.playChannel(program.channel)

        else:
            # multiple matches, let user decide
            import detect
            d = detect.StreamAddonDialog(result)
            d.doModal()
            
            if d.stream is not None:
                self.database.setCustomStreamUrl(program.channel, d.stream)
                self.playChannel(program.channel)
                if IGNORESTRM:
                    self.database.deleteCustomStreamUrl(program.channel)

    def _showContextMenu(self, program):
        self.cats.hide()

        self._hideControl(self.C_MAIN_MOUSE_CONTROLS)
        d = PopupMenu(self.database, program, not program.notificationScheduled, self.touch)
        d.doModal()

        buttonClicked = d.buttonClicked
        streamURL     = d.streamURL
        record        = d.record

        del d

        if buttonClicked == PopupMenu.C_POPUP_REMIND:
            if record:
                self.record(program)
                return
            #if program.notificationScheduled:
            #    self.notification.removeNotification(program)
            #else:
            #    self.notification.addNotification(program)
            #self.onRedrawEPG(self.channelIdx, self.viewStartDate)

        elif buttonClicked == PopupMenu.C_POPUP_CHOOSE_STREAM:
            d = StreamSetupDialog(self.database, program.channel)
            d.doModal()
            del d
            self._showContextMenu(program)
            return

        elif buttonClicked == PopupMenu.C_POPUP_PLAY:
            if self.touch:
                self.tryProgram(program)
            else:
                self.playChannel(program.channel)

        elif buttonClicked == PopupMenu.C_POPUP_CHANNELS:
            d = ChannelsMenu(self.database)
            d.doModal()
            del d
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)

        elif buttonClicked == PopupMenu.C_POPUP_CATEGORIES:
            d = CategoriesMenu(self.database, self.categoriesList)
            d.doModal()

            self.categoriesList = d.currentCategories
            del d
            self.cats.updateCategories(self.categoriesList)
            dixie.SetSetting('categories', '|'.join(self.categoriesList))
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)

        elif buttonClicked == PopupMenu.C_POPUP_SETTINGS:
            addonPath = HOME
            script    = os.path.join(addonPath, 'openSettings.py')
            args      = ''
            cmd       = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % ('launch', script, args, 0)
            xbmc.executebuiltin(cmd)
            self.close()

        elif buttonClicked == PopupMenu.C_POPUP_IPLAYER:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.ontapp-player)')

        elif buttonClicked == PopupMenu.C_POPUP_ITVPLAYER:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.itv)')

        elif buttonClicked == PopupMenu.C_POPUP_OTTOOLS:
            self.refresh = True
            xbmc.executebuiltin('XBMC.RunAddon(script.tvguidedixie.tools)')

        elif buttonClicked == PopupMenu.C_POPUP_USTV:
            xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?ch_fanart&mode=%d&name=%s&url=%s",return)' % (10025,'plugin.video.F.T.V', 131, 'My Recordings', 'url'))
            xbmc.executebuiltin("Container.Refresh")
            #xbmc.executebuiltin(ustv)

        elif buttonClicked == PopupMenu.C_POPUP_UKTVPLAY:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.uktvplay)')

        elif buttonClicked == PopupMenu.C_POPUP_SUPERFAVES:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.program.super.favourites)')

        elif buttonClicked == PopupMenu.C_POPUP_VPN:
            xbmc.executebuiltin('XBMC.RunScript(special://home/addons/plugin.program.vpnicity/menu.py,%s)' % self.database.getStreamUrl(program.channel))

        elif buttonClicked == PopupMenu.C_POPUP_SUPER_SEARCH:
            xbmc.executebuiltin('ActivateWindow(%d,"plugin://%s/?mode=%d&keyword=%s",return)' % (10025,'plugin.program.super.favourites', 0, urllib.quote_plus(program.title)))

        self.cats.show()


    def setFocusId(self, controlId):
        control = self.getControl(controlId)
        if control:
            self.setFocus(control)

    def setFocus(self, control):
        debug('setFocus %d' % control.getId())
        if control in [elem.control for elem in self.controlAndProgramList]:
            debug('Focus before %s' % self.focusPoint)
            (left, top) = control.getPosition()
            if left > self.focusPoint.x or left + control.getWidth() < self.focusPoint.x:
                self.focusPoint.x = left
            self.focusPoint.y = top + (control.getHeight() / 2)
            debug('New focus at %s' % self.focusPoint)

        super(TVGuide, self).setFocus(control)


    def onFocus(self, controlId):
        try:
            controlInFocus = self.getControl(controlId)
        except Exception:
            return

        program = self._getProgramFromControl(controlInFocus)
        if program is None:
            return

        title = program.title
        if title in OTT_CHANNEL:
            desc = program.channel.desc
            if desc:
                title = desc

        self.setControlLabel(self.C_MAIN_TITLE, '[B]%s[/B]' % title)
        self.setControlLabel(self.C_MAIN_TIME, '[B]%s - %s[/B]' % (self.formatTime(program.startDate+GMTOFFSET), self.formatTime(program.endDate+GMTOFFSET)))

        if program.description:
            description = program.description
        else:
            description = ''

        self.setControlText(self.C_MAIN_DESCRIPTION, description)

        if program.channel.logo is not None:
            self.setControlImage(self.C_MAIN_LOGO, program.channel.logo)

        imageSmall = os.path.join(dixie.RESOURCES, 'imageSmall.png')

        if not self.touch:
            if program.imageSmall is None:
                self.setControlImage(self.C_MAIN_IMAGE, imageSmall)
            else:
                self.setControlImage(self.C_MAIN_IMAGE, program.imageSmall)

        if ADDON.getSetting('program.background.enabled') == 'true' and program.imageLarge is not None:
            self.setControlImage(self.C_MAIN_BACKGROUND, program.imageLarge)

        if not self.osdEnabled and self.player.isPlaying():
            self.player.stop()

    def _left(self, currentFocus):
        control = self._findControlOnLeft(currentFocus)
        if control is not None:
            self.setFocus(control)
        elif control is None:
            self.viewStartDate -= datetime.timedelta(hours = 2)
            self.focusPoint.x = self.epgView.right
            self.onRedrawEPG(self.channelIdx, self.viewStartDate, focusFunction=self._findControlOnLeft)

    def _right(self, currentFocus):
        control = self._findControlOnRight(currentFocus)
        if control is not None:
            self.setFocus(control)
            return

        when = self.viewStartDate + datetime.timedelta(hours = 2)
        if when.date() > self.database.updateLimit:
            return
        self.viewStartDate = when
        self.focusPoint.x = self.epgView.left
        self.onRedrawEPG(self.channelIdx, self.viewStartDate, focusFunction=self._findControlOnRight)

    def _up(self, currentFocus):
        currentFocus.x = self.focusPoint.x
        control = self._findControlAbove(currentFocus)
        if control is not None:
            self.setFocus(control)
        elif control is None:
            self.cats.setFocus()
            
    def _moveToBottom(self):
        self.focusPoint.y = self.epgView.bottom
        newIndex = self.channelIdx - CHANNELS_PER_PAGE
        if newIndex < 0 and self.channelIdx > 0:
            newIndex = 0
        self.onRedrawEPG(newIndex, self.viewStartDate, focusFunction=self._findControlAbove)

    def _down(self, currentFocus):
        currentFocus.x = self.focusPoint.x
        control = self._findControlBelow(currentFocus)
        if control is not None:
            self.setFocus(control)
        elif control is None:
            self.focusPoint.y = self.epgView.top
            self.onRedrawEPG(self.channelIdx + CHANNELS_PER_PAGE, self.viewStartDate, focusFunction=self._findControlBelow)

    def _nextDay(self):
        self.viewStartDate += datetime.timedelta(days = 1)
        self.onRedrawEPG(self.channelIdx, self.viewStartDate)

    def _previousDay(self):
        self.viewStartDate -= datetime.timedelta(days = 1)
        self.onRedrawEPG(self.channelIdx, self.viewStartDate)

    def _moveUp(self, count = 1, scrollEvent = False):
        if scrollEvent:
            self.onRedrawEPG(self.channelIdx - count, self.viewStartDate)
        else:
            self.focusPoint.y = self.epgView.bottom

            newIndex = self.channelIdx - count
            if newIndex < 0 and self.channelIdx > 0:
                newIndex = 0

            self.onRedrawEPG(newIndex, self.viewStartDate, focusFunction = self._findControlAbove)

    def _moveDown(self, count = 1, scrollEvent = False):
        if scrollEvent:
            self.onRedrawEPG(self.channelIdx + count, self.viewStartDate)
        else:
            self.focusPoint.y = self.epgView.top
            self.onRedrawEPG(self.channelIdx + count, self.viewStartDate, focusFunction=self._findControlBelow)

    def _channelUp(self):
        channel = self.database.getNextChannel(self.currentChannel)
        self.playChannel(channel)

    def _channelDown(self):
        channel = self.database.getPreviousChannel(self.currentChannel)
        self.playChannel(channel)

    def removeHighlight(self):
        if self.highlight:
            self.removeControl(self.highlight)
            self.highlight = None

    def playChannel(self, channel):
        self.removeHighlight()
        control = self.getFocus()
        if control in [elem.control for elem in self.controlAndProgramList]:
            texture = os.path.join(dixie.RESOURCES, 'orange-focus.png')
            x, y    = control.getPosition()
            width   = control.getWidth()
            height  = control.getHeight()
            label   = control.getLabel()
            timeout = 10

            self.highlight = xbmcgui.ControlButton(
                    x,
                    y,
                    width,
                    height,
                    label,
                    noFocusTexture = texture,
                    focusTexture   = texture,
                    textColor      = TEXT_COLOR,
                    focusedColor   = FOCUSED_COLOR,
                    shadowColor    = SHADOW_COLOR
                )

            self.addControl(self.highlight)
            threading.Timer(timeout, self.removeHighlight).start()


        if not DSF:
            if self.prePlayOptions(channel):
                return True

        self.currentChannel = channel
        wasPlaying = self.player.isPlaying()

        if DSF:
            url = 'DSF:%s' % channel.id
        else:
            url = self.database.getStreamUrl(channel)

        if url:
            xbmcgui.Window(10000).setProperty('OTT_CHANNEL', channel.id)
            path = os.path.join(ADDON.getAddonInfo('path'), 'player.py')
            xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d,%s)' % (path, url, False, self.osdEnabled))

            if not wasPlaying:
                self._hideEpg()

        threading.Timer(2, self.waitForPlayBackStopped).start()
        self.osdProgram = self.database.getCurrentProgram(self.currentChannel)

        return url is not None


    def record(self, program):
        dixie.ShowBusy()
        record = filmon.record(program.title, program.startDate, program.endDate, program.channel.streamUrl)
        dixie.CloseBusy()
        return record <> False


    def prePlayOptions(self, channel):
        program = None
        try:    program = self._getProgramFromControl(self.getFocus())
        except: pass

        if not program:
            return False

        if not filmon.isValid(program.channel.streamUrl):
            return False

        now = datetime.datetime.today()

        inPast   = program.endDate   < now
        inFuture = program.startDate > now

        if (not inPast) and (not inFuture):
            return False

        if inPast:
            if dixie.DialogYesNo('Do you want to watch %s' % program.channel.title, 'Or catchup on %s' % program.title, noLabel='Live', yesLabel='Catchup'):
                return self.catchup()

        if inFuture:
            if dixie.DialogYesNo('Do you want to watch %s' % program.channel.title, 'Or set a recording for %s' % program.title, noLabel='Live', yesLabel='Record'):
                return self.record(program)

        return False


    def catchup(self):
        try:
            dixie.ShowBusy()

            controlInFocus = self.getFocus()
            program = self._getProgramFromControl(controlInFocus)
            if program is None:
                dixie.CloseBusy()
                return False

            stream = program.channel.streamUrl.replace('__SF__PlayMedia("', '')

            if not filmon.isValid(stream):
                dixie.CloseBusy()
                return False

            end = program.endDate
            now = datetime.datetime.today()

            if end > now:
                dixie.CloseBusy()
                return False

            name  = program.title
            start = program.startDate

            isRecorded, url = filmon.isRecorded(name, start)
            programID = None

            if not isRecorded:
                programID = filmon.record(name, start, end, stream, showResult=False)

            dixie.CloseBusy()

            if (not isRecorded) and (not programID):                
                dixie.DialogOK('Unable to play %s' % name, 'Catchup requires temporary DVR space on Filmon.', 'Please delete some recordings and try again.')            
                return True


            #now play the stream             
            if not isRecorded:
                url = filmon.getRecording(name, start)

            if not url:
                return False

            wasPlaying = self.player.isPlaying()
            # if not wasPlaying:
            #     self._hideControl(self.C_MAIN_BLACKOUT)
            path = os.path.join(ADDON.getAddonInfo('path'), 'player.py')
            xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d,%s)' % (path, url, self.osdEnabled, name))
            self.showBlackout()

            if not isRecorded:
                filmon.removeRecording(url)

            if not wasPlaying:
                self._hideEpg()

            threading.Timer(5, self.waitForPlayBackStopped).start()
            #self.osdProgram = self.database.getCurrentProgram(self.currentChannel)
          
            return True

        except:
            return False

        return True

    def waitForPlayBackStopped(self):
        for retry in range(0, 100):
            xbmc.sleep(100)
            if self.player.isPlaying():
                break

        retry = 5
        while retry > 0:
            xbmc.sleep(500)
            while self.player.isPlaying() and not xbmc.abortRequested and not self.isClosing:
                xbmc.sleep(500)
                retry = 5
            retry -= 1
        
        xbmc.Player().stop()
        self.onPlayBackStopped()

    def _showOsd(self):
        if not self.osdEnabled:
            return

        if self.mode != MODE_OSD:
            self.osdChannel = self.currentChannel

        if self.osdProgram is not None:
            self.setControlLabel(self.C_MAIN_OSD_TITLE, '[B]%s[/B]' % self.osdProgram.title)
            self.setControlLabel(self.C_MAIN_OSD_TIME, '[B]%s - %s[/B]' % (self.formatTime(self.osdProgram.startDate), self.formatTime(self.osdProgram.endDate)))
            self.setControlText(self.C_MAIN_OSD_DESCRIPTION, self.osdProgram.description)
            self.setControlLabel(self.C_MAIN_OSD_CHANNEL_TITLE, self.osdChannel.title)
            if self.osdProgram.channel.logo is not None:
                self.setControlImage(self.C_MAIN_OSD_CHANNEL_LOGO, self.osdProgram.channel.logo)
            else:
                self.setControlImage(self.C_MAIN_OSD_CHANNEL_LOGO, '')

        self.mode = MODE_OSD
        self._showControl(self.C_MAIN_OSD)

    def _hideOsd(self):
        self.mode = MODE_TV
        self._hideControl(self.C_MAIN_OSD)

    def _hideEpg(self):
        return
        self._hideControl(self.C_MAIN_EPG)
        self.mode = MODE_TV
        self._clearEpg()

    def onRedrawEPG(self, channelStart, startTime, focusFunction = None):
        if self.redrawingEPG or (self.database is not None and self.database.updateInProgress) or self.isClosing:
            debug('onRedrawEPG - already redrawing')
            return # ignore redraw request while redrawing
        debug('onRedrawEPG')

        # self.hideBlackout()

        self.redrawingEPG = True
        self.mode = MODE_EPG
        self._showControl(self.C_MAIN_EPG)
        self.updateTimebar()

        # show Loading screen
        self.setControlLabel(self.C_MAIN_LOADING_TIME_LEFT, strings(CALCULATING_REMAINING_TIME))
        self._showControl(self.C_MAIN_LOADING)
        self.setFocusId(self.C_MAIN_LOADING_CANCEL)
        self.hideTimebar()

        # remove existing controls
        self._clearEpg()

        try:
            self.channelIdx, channels, programs = self.database.getEPGView(channelStart, startTime, clearExistingProgramList = False, categories = self.categoriesList, nmrChannels = CHANNELS_PER_PAGE)
            if len(channels) == 0:
                self.channelIdx, channels, programs = self.database.getEPGView(channelStart, startTime, clearExistingProgramList = False, nmrChannels = CHANNELS_PER_PAGE)
        except src.SourceException:
            self.onEPGLoadError()
            return

        channelsWithoutPrograms = list(channels)
        
        self.refreshChannelLabels(self.channelIdx)

        # date and time row
        self.setControlLabel(self.C_MAIN_DATE, self.formatDate(self.viewStartDate))
        for col in range(1, 5):
            self.setControlLabel(4000 + col, self.formatTime(startTime))
            startTime += HALF_HOUR

        if programs is None:
            self.onEPGLoadError()
            return

        # set channel logo or text
        for idx in range(0, CHANNELS_PER_PAGE):
            if idx >= len(channels):
                self.setControlImage(4110 + idx, ' ')
                self.setControlLabel(4010 + idx, ' ')
            else:
                channel = channels[idx]
                self.setControlLabel(4010 + idx, channel.title)
                if channel.logo is not None:
                    self.setControlImage(4110 + idx, channel.logo)
                else:
                    self.setControlImage(4110 + idx, ' ')

        for program in programs:
            idx = channels.index(program.channel)
            if program.channel in channelsWithoutPrograms:
                channelsWithoutPrograms.remove(program.channel)

            startDelta = program.startDate - self.viewStartDate + GMTOFFSET
            stopDelta  = program.endDate   - self.viewStartDate + GMTOFFSET

            cellStart = self._secondsToXposition(startDelta.seconds)
            if startDelta.days < 0:
                cellStart = self.epgView.left
            cellWidth = self._secondsToXposition(stopDelta.seconds) - cellStart
            if cellStart + cellWidth > self.epgView.right:
                cellWidth = self.epgView.right - cellStart

            if cellWidth > 1:
                if program.notificationScheduled:
                    noFocusTexture = 'tvguide-program-red.png'
                    focusTexture = 'tvguide-program-red-focus.png'
                else:
                    noFocusTexture = 'tvguide-program-grey.png'
                    focusTexture = 'tvguide-program-grey-focus.png'

                if cellWidth < 25:
                    title = '' # Text will overflow outside the button if it is too narrow
                else:
                    title = program.title

                if title in OTT_CHANNEL:
                    desc = program.channel.desc
                    if desc:
                        title = desc

                control = xbmcgui.ControlButton(
                    cellStart,
                    self.epgView.top + self.epgView.cellHeight * idx,
                    cellWidth - 2,
                    self.epgView.cellHeight - 2,
                    title,
                    noFocusTexture = noFocusTexture,
                    focusTexture = focusTexture,
                    textColor = TEXT_COLOR,
                    focusedColor = FOCUSED_COLOR,
                    shadowColor = SHADOW_COLOR
                )

                self.controlAndProgramList.append(ControlAndProgram(control, program))

        for channel in channelsWithoutPrograms:
            description = channel.desc
            if len(description) == 0:
                description = strings(NO_PROGRAM_AVAILABLE)

            idx = channels.index(channel)

            control = xbmcgui.ControlButton(
                self.epgView.left,
                self.epgView.top + self.epgView.cellHeight * idx,
                (self.epgView.right - self.epgView.left) - 2,
                self.epgView.cellHeight - 2,
                description,
                noFocusTexture='tvguide-program-grey.png',
                focusTexture='tvguide-program-grey-focus.png',
                textColor = TEXT_COLOR,
                focusedColor = FOCUSED_COLOR,
                shadowColor = SHADOW_COLOR
            )

            now  = datetime.datetime.today()
            then = now + datetime.timedelta(minutes = 24*60)
            program = src.Program(channel, description, now, then, "", "")
            self.controlAndProgramList.append(ControlAndProgram(control, program))

        # add program controls
        if focusFunction is None:
            focusFunction = self._findControlAt
        focusControl = focusFunction(self.focusPoint)
        controls = [elem.control for elem in self.controlAndProgramList]
        self.addControls(controls)
        if focusControl is not None:
            debug('onRedrawEPG - setFocus %d' % focusControl.getId())
            self.setFocus(focusControl)

        self.ignoreMissingControlIds.extend([elem.control.getId() for elem in self.controlAndProgramList])

        if focusControl is None and len(self.controlAndProgramList) > 0:
            self.setFocus(self.controlAndProgramList[0].control)

        self._hideControl(self.C_MAIN_LOADING)
        self.showTimebar()
        self.redrawingEPG = False

    def _clearEpg(self):
        self.removeHighlight()

        controls = [elem.control for elem in self.controlAndProgramList]
        try:
            self.removeControls(controls)
        except RuntimeError:
            for elem in self.controlAndProgramList:
                try:
                    self.removeControl(elem.control)
                except RuntimeError:
                    pass # happens if we try to remove a control that doesn't exist
        del self.controlAndProgramList[:]

    def onEPGLoadError(self):
        dixie.log('Delete DB OnTapp.TV - onEPGLoadError')
        xbmcgui.Dialog().ok(strings(LOAD_ERROR_TITLE), strings(LOAD_ERROR_LINE1), strings(LOAD_ERROR_LINE2), strings(LOAD_ERROR_LINE3))
        self.close()
        xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.tvguidedixie/deleteDB.py)')
        dixie.log('****** Delete DB complete *******')


    def onSourceNotConfigured(self):
        dixie.log('Delete DB OnTapp.TV - onSourceNotConfigured')
        xbmcgui.Dialog().ok(strings(LOAD_ERROR_TITLE), strings(LOAD_ERROR_LINE1), strings(CONFIGURATION_ERROR_LINE2))
        self.close()
        xbmc.executebuiltin('XBMC.RunScript(special://home/addons/script.tvguidedixie/deleteDB.py)')
        dixie.log('****** Delete DB complete *******')

    def isSourceInitializationCancelled(self):
        return xbmc.abortRequested or self.isClosing


    def onSourceInitializedS(self, success):
        self.database.initializeP(self.onSourceInitializedP, self.isSourceInitializationCancelled)


    def onSourceInitializedP(self, success):
        if success:
            self.notification = Notification(self.database, ADDON.getAddonInfo('path'))
            #first time redraw
            current = xbmcgui.Window(10000).getProperty('OTT_CHANNEL')

            if len(current) == 0:          
                self.onRedrawEPG(0, self.viewStartDate)
            else:
                self.resetToChannel(current)


    def onPlayBackStopped(self):
        if not self.player.isPlaying() and not self.isClosing:
            self._hideControl(self.C_MAIN_OSD)
            self.viewStartDate = datetime.datetime.today()
            self.viewStartDate -= datetime.timedelta(minutes = self.viewStartDate.minute % 30, seconds = self.viewStartDate.second)
            self.onRedrawEPG(self.channelIdx, self.viewStartDate)
            return

    def _secondsToXposition(self, seconds):
        return self.epgView.left + (seconds * self.epgView.width / 7200)


    def _findControlOnRight(self, point):
        distanceToNearest = 10000
        nearestControl = None

        for elem in self.controlAndProgramList:
            control = elem.control
            (left, top) = control.getPosition()
            x = left + (control.getWidth() / 2)
            y = top + (control.getHeight() / 2)

            if point.x < x and point.y == y:
                distance = abs(point.x - x)
                if distance < distanceToNearest:
                    distanceToNearest = distance
                    nearestControl = control

        return nearestControl


    def _findControlOnLeft(self, point):
        distanceToNearest = 10000
        nearestControl = None

        for elem in self.controlAndProgramList:
            control = elem.control
            (left, top) = control.getPosition()
            x = left + (control.getWidth() / 2)
            y = top + (control.getHeight() / 2)

            if point.x > x and point.y == y:
                distance = abs(point.x - x)
                if distance < distanceToNearest:
                    distanceToNearest = distance
                    nearestControl = control

        return nearestControl

    def _findControlBelow(self, point):
        nearestControl = None

        for elem in self.controlAndProgramList:
            control = elem.control
            (leftEdge, top) = control.getPosition()
            y = top + (control.getHeight() / 2)

            if point.y < y:
                rightEdge = leftEdge + control.getWidth()
                if(leftEdge <= point.x < rightEdge
                   and (nearestControl is None or nearestControl.getPosition()[1] > top)):
                    nearestControl = control

        return nearestControl

    def _findControlAbove(self, point):
        nearestControl = None
        for elem in self.controlAndProgramList:
            control = elem.control
            (leftEdge, top) = control.getPosition()
            y = top + (control.getHeight() / 2)

            if point.y > y:
                rightEdge = leftEdge + control.getWidth()
                if(leftEdge <= point.x < rightEdge
                   and (nearestControl is None or nearestControl.getPosition()[1] < top)):
                    nearestControl = control

        return nearestControl

    def _findControlAt(self, point):
        for elem in self.controlAndProgramList:
            control = elem.control
            (left, top) = control.getPosition()
            bottom = top + control.getHeight()
            right = left + control.getWidth()

            if left <= point.x <= right and  top <= point.y <= bottom:
                return control

        return None


    def _getProgramFromControl(self, control):
        for elem in self.controlAndProgramList:
            if elem.control == control:
                return elem.program
        return None

    def _hideControl(self, *controlIds):
        """
        Visibility is inverted in skin
        """
        for controlId in controlIds:
            control = self.getControl(controlId)
            if control:
                control.setVisible(True)

    def _showControl(self, *controlIds):
        """
        Visibility is inverted in skin
        """
        for controlId in controlIds:
            control = self.getControl(controlId)
            if control:
                control.setVisible(False)

    def formatTime(self, timestamp):
        format = xbmc.getRegion('time').replace(':%S', '').replace('%H%H', '%H')
        return timestamp.strftime(format)

    def formatDate(self, timestamp):
        format = xbmc.getRegion('dateshort')
        return timestamp.strftime(format)

    def setControlImage(self, controlId, image):
        control = self.getControl(controlId)
        if not control:
            return
        try:    control.setImage(image.encode('utf-8'), useCache=False)
        except: control.setImage(image.encode('utf-8'))

    def setControlLabel(self, controlId, label):
        control = self.getControl(controlId)
        if control and label:
            control.setLabel(label)

    def setControlText(self, controlId, text):
        control = self.getControl(controlId)
        if control:
            control.setText(text)


    def hideTimebar(self):
        try:
            self.timebarVisible = False
            self.getControl(self.C_MAIN_TIMEBAR).setVisible(self.timebarVisible)
        except:
            pass

    def showTimebar(self):
        try:
            self.timebarVisible = True
            self.getControl(self.C_MAIN_TIMEBAR).setVisible(self.timebarVisible)
        except:
            pass

    def updateTimebar(self):
        try:
            # move timebar to current time
            timeDelta = datetime.datetime.today() - self.viewStartDate
            days      = timeDelta.days
            secs      = timeDelta.seconds
            inZone    = (days == 0) and (secs < 2*60*60)

            control = self.getControl(self.C_MAIN_TIMEBAR)
            if control:
                (x, y) = control.getPosition()
                try:
                    # Sometimes raises:
                    # exceptions.RuntimeError: Unknown exception thrown from the call "setVisible"
                    control.setVisible(inZone)
                except:
                    pass
                control.setPosition(self._secondsToXposition(timeDelta.seconds), y)

            #if scheduleTimer and not xbmc.abortRequested and not self.isClosing:
            #    threading.Timer(1, self.updateTimebar).start()
        except Exception:
            raise


class PopupMenu(xbmcgui.WindowXMLDialog):
    C_POPUP_PLAY = 4000
    C_POPUP_CHOOSE_STREAM = 4001
    C_POPUP_REMIND = 4002
    C_POPUP_CHANNELS = 4003
    C_POPUP_QUIT = 4004
    C_POPUP_CHANNEL_LOGO = 4100
    C_POPUP_CHANNEL_TITLE = 4101
    C_POPUP_PROGRAM_TITLE = 4102
    C_POPUP_CATEGORIES = 4005
    C_POPUP_SETTINGS = 4007
    C_POPUP_IPLAYER = 4008
    C_POPUP_ITVPLAYER = 4010
    C_POPUP_OTTOOLS = 4014
    C_POPUP_UKTVPLAY = 4015
    C_POPUP_USTV = 4011
    C_POPUP_SUPER_SEARCH = 4009
    C_POPUP_SUPERFAVES = 4012
    C_POPUP_VPN = 4013
    C_POPUP_HOME = 4006


    def __new__(cls, database, program, showRemind, touch):
        xml_file = os.path.join('script-tvguide-menu.xml')
        if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
            XML = xml_file

        return super(PopupMenu, cls).__new__(cls, XML, PATH)


    def __init__(self, database, program, showRemind, touch):
        """

        @type database: source.Database
        @param program:
        @type program: source.Program
        @param showRemind:
        """
        super(PopupMenu, self).__init__()
        self.database = database
        self.program = program
        self.showRemind = showRemind
        self.buttonClicked = None
        self.touch = touch


    def onInit(self):
        # self.getControl(self.C_POPUP_OTTOOLS).setVisible(False) RD -Temporary hide of the 4oD button until a new use is found for it.

        programTitleControl = self.getControl(self.C_POPUP_PROGRAM_TITLE)
        programTitleControl.setLabel(self.program.title)

        playControl = self.getControl(self.C_POPUP_PLAY)
        playControl.setLabel('Watch Channel')

        #isPlayable = self.program.channel.isPlayable()
        isPlayable = self.database.isPlayable(self.program.channel)

        if not isPlayable:
            playControl.setEnabled(False)
            self.setFocusId(self.C_POPUP_REMIND)
            # self.getControl(self.C_POPUP_REMIND).setVisible(False)
            # self.setFocusId(self.C_POPUP_CHOOSE_STREAM)

        if self.touch or self.program.title == strings(NO_PROGRAM_AVAILABLE):
            playControl.setEnabled(True)
            self.setFocusId(self.C_POPUP_PLAY)

        channelLogoControl  = self.getControl(self.C_POPUP_CHANNEL_LOGO)
        channelTitleControl = self.getControl(self.C_POPUP_CHANNEL_TITLE)

        if self.program.channel.logo is not None:
            channelLogoControl.setImage(self.program.channel.logo)
            channelTitleControl.setVisible(False)
        else:
            channelLogoControl.setVisible(False)
            channelTitleControl.setLabel(self.program.channel.title)

        if self.database.getCustomStreamUrl(self.program.channel):
            try:    self.getControl(self.C_POPUP_CHOOSE_STREAM).setLabel(REMOVE_STRM_FILE)
            except: pass
            xbmcgui.Window(10000).setProperty('TVG_CHOOSE', REMOVE_STRM_FILE)
        else:
            try:    self.getControl(self.C_POPUP_CHOOSE_STREAM).setLabel(CHOOSE_STRM_FILE)
            except: pass
            xbmcgui.Window(10000).setProperty('TVG_CHOOSE', CHOOSE_STRM_FILE)

        #if self.showRemind:
        #    try:    self.getControl(self.C_POPUP_REMIND).setLabel(REMIND_PROGRAM)
        #    except: pass
        #    xbmcgui.Window(10000).setProperty('TVG_REMIND', REMIND_PROGRAM)
        #else:
        #    try:    self.getControl(self.C_POPUP_REMIND).setLabel(DONT_REMIND_PROGRAM)
        #    except: pass
        #    xbmcgui.Window(10000).setProperty('TVG_REMIND', DONT_REMIND_PROGRAM)

        self.getControl(self.C_POPUP_REMIND).setLabel('Set Recording')
        self.streamURL = self.program.channel.streamUrl.replace('__SF__PlayMedia("', '')
        if filmon.isValid(self.streamURL):
            self.record = True
            self.getControl(self.C_POPUP_REMIND).setEnabled(True)
        else:
            self.record = False
            self.getControl(self.C_POPUP_REMIND).setEnabled(False)
            if isPlayable:
                self.setFocusId(self.C_POPUP_PLAY)
            else:
                self.setFocusId(self.C_POPUP_CHOOSE_STREAM)

        try:
            ctrl = self.getControl(5000)
            self.setFocusId(5000)
        except:
            pass

        xbmcgui.Window(10000).clearProperty('TVG_popup_id')


    def onAction(self, action):
        try:
            id = int(xbmcgui.Window(10000).getProperty('TVG_popup_id'))
            self.buttonClicked = id
            self.close()
        except:
            pass

        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
            self.close()
            return

    def onClick(self, controlId):
        if controlId == self.C_POPUP_CHOOSE_STREAM and self.database.getCustomStreamUrl(self.program.channel):

            self.database.deleteCustomStreamUrl(self.program.channel)

            chooseStrmControl = self.getControl(self.C_POPUP_CHOOSE_STREAM)
            chooseStrmControl.setLabel(CHOOSE_STRM_FILE)

            if not self.database.isPlayable(self.program.channel):
                playControl = self.getControl(self.C_POPUP_PLAY)
                playControl.setEnabled(False)

        else:
            self.buttonClicked = controlId
            self.close()

    def onFocus(self, controlId):
        pass

class ChannelsMenu(xbmcgui.WindowXMLDialog):
    C_CHANNELS_LIST = 6000
    C_CHANNELS_SELECTION_VISIBLE = 6001
    C_CHANNELS_SELECTION = 6002
    C_CHANNELS_SAVE = 6003
    C_CHANNELS_CANCEL = 6004



    def __new__(cls, database):
        xml_file = os.path.join('script-tvguide-channels.xml')
        if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
            XML = xml_file

        return super(ChannelsMenu, cls).__new__(cls, XML, PATH)

    def __init__(self, database):
        """

        @type database: source.Database
        """
        super(ChannelsMenu, self).__init__()
        self.database = database
        self.channelList = database.getChannelList(onlyVisible = False)
        self.swapInProgress = False


    def onInit(self):
        self.updateChannelList()
        self.setFocusId(self.C_CHANNELS_LIST)
        self.move = False


    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
            self.close()
            return

        if (self.getFocusId() == self.C_CHANNELS_LIST and action.getId() in [ACTION_LEFT]) or (action.getId() in [ACTION_GESTURE_SWIPE_LEFT]):
            listControl = self.getControl(self.C_CHANNELS_LIST)
            idx = listControl.getSelectedPosition()
            buttonControl = self.getControl(self.C_CHANNELS_SELECTION)
            buttonControl.setLabel('[B]%s[/B]' % self.channelList[idx].title)
            self.move = True

            self.getControl(self.C_CHANNELS_SELECTION_VISIBLE).setVisible(False)
            self.setFocusId(self.C_CHANNELS_SELECTION)

        elif (self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() in [ACTION_RIGHT, ACTION_SELECT_ITEM]) or (action.getId() in [ACTION_GESTURE_SWIPE_RIGHT]):
            self.getControl(self.C_CHANNELS_SELECTION_VISIBLE).setVisible(True)
            xbmc.sleep(350)
            self.setFocusId(self.C_CHANNELS_LIST)
            self.move = False

        elif (self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() in [ACTION_UP]) or (self.move and action.getId() in [ACTION_GESTURE_SWIPE_UP]):
            listControl = self.getControl(self.C_CHANNELS_LIST)
            idx = listControl.getSelectedPosition()
            if idx > 0:
                self.swapChannels(idx, idx - 1)

        elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() == ACTION_PAGE_UP:
            listControl = self.getControl(self.C_CHANNELS_LIST)
            idx = listControl.getSelectedPosition()
            for i in range(0, 8):
                if idx == 0:
                    return
                self.swapChannels(idx, idx - 1)
                idx -= 1

        elif (self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() in [ACTION_DOWN, ACTION_GESTURE_SWIPE_DOWN]) or (self.move and action.getId() in [ACTION_GESTURE_SWIPE_DOWN]):
            listControl = self.getControl(self.C_CHANNELS_LIST)
            idx = listControl.getSelectedPosition()
            if idx < listControl.size() - 1:
                self.swapChannels(idx, idx + 1)

        elif self.getFocusId() == self.C_CHANNELS_SELECTION and action.getId() == ACTION_PAGE_DOWN:
            listControl = self.getControl(self.C_CHANNELS_LIST)
            idx = listControl.getSelectedPosition()
            for i in range(0,8):
                if idx == listControl.size()-1:
                    return
                self.swapChannels(idx, idx + 1)
                idx += 1


    def onClick(self, controlId):
        if controlId == self.C_CHANNELS_LIST:
            listControl = self.getControl(self.C_CHANNELS_LIST)
            item = listControl.getSelectedItem()
            channel = self.channelList[int(item.getProperty('idx'))]
            channel.visible = 0 if channel.visible else 1

            if channel.visible:
                iconImage = 'tvguide-channel-visible.png'
            else:
                iconImage = 'tvguide-channel-hidden.png'
            item.setIconImage(iconImage)

        elif controlId == self.C_CHANNELS_SAVE:
            self.database.saveChannelList(self.close, self.channelList)

        elif controlId == self.C_CHANNELS_CANCEL:
            self.close()


    def onFocus(self, controlId):
        pass

    def updateChannelList(self):
        listControl = self.getControl(self.C_CHANNELS_LIST)
        listControl.reset()
        for idx, channel in enumerate(self.channelList):
            if channel.visible:
                iconImage = 'tvguide-channel-visible.png'
            else:
                iconImage = 'tvguide-channel-hidden.png'

            item = xbmcgui.ListItem('%3d. %s' % (idx+1, channel.title), iconImage = iconImage)
            item.setProperty('idx', str(idx))
            listControl.addItem(item)

    def updateListItem(self, idx, item):
        channel = self.channelList[idx]
        item.setLabel('%3d. %s' % (idx+1, channel.title))

        if channel.visible:
            iconImage = 'tvguide-channel-visible.png'
        else:
            iconImage = 'tvguide-channel-hidden.png'
        item.setIconImage(iconImage)
        item.setProperty('idx', str(idx))

    def swapChannels(self, fromIdx, toIdx):
        if self.swapInProgress:
            return
        self.swapInProgress = True

        c = self.channelList[fromIdx]
        self.channelList[fromIdx] = self.channelList[toIdx]
        self.channelList[toIdx] = c

        # recalculate weight
        for idx, channel in enumerate(self.channelList):
            channel.weight = idx

        listControl = self.getControl(self.C_CHANNELS_LIST)
        self.updateListItem(fromIdx, listControl.getListItem(fromIdx))
        self.updateListItem(toIdx, listControl.getListItem(toIdx))

        listControl.selectItem(toIdx)
        #xbmc.sleep(50)
        self.swapInProgress = False



class StreamSetupDialog(xbmcgui.WindowXMLDialog):
    C_STREAM_STRM_TAB = 101
    C_STREAM_FAVOURITES_TAB = 102
    C_STREAM_ADDONS_TAB = 103
    C_STREAM_SUPERFAVE_TAB = 104
    C_STREAM_PLAYLIST_TAB = 105
    C_STREAM_STRM_BROWSE = 1001
    C_STREAM_STRM_FILE_LABEL = 1005
    C_STREAM_STRM_PREVIEW = 1002
    C_STREAM_STRM_OK = 1003
    C_STREAM_STRM_CANCEL = 1004
    C_STREAM_FAVOURITES = 2001
    C_STREAM_FAVOURITES_PREVIEW = 2002
    C_STREAM_FAVOURITES_OK = 2003
    C_STREAM_FAVOURITES_CANCEL = 2004
    C_STREAM_ADDONS = 3001
    C_STREAM_ADDONS_STREAMS = 3002
    C_STREAM_ADDONS_NAME = 3003
    C_STREAM_ADDONS_DESCRIPTION = 3004
    C_STREAM_ADDONS_PREVIEW = 3005
    C_STREAM_ADDONS_OK = 3006
    C_STREAM_ADDONS_CANCEL = 3007

    C_STREAM_PLAYLIST = 4001
    C_STREAM_PLAYLIST_PREVIEW = 4002
    C_STREAM_PLAYLIST_OK = 4003
    C_STREAM_PLAYLIST_CANCEL = 4004

    C_STREAM_SUPERFAVE_BROWSE = 5001
    C_STREAM_SUPERFAVE_PREVIEW = 5002
    C_STREAM_SUPERFAVE_OK = 5003
    C_STREAM_SUPERFAVE_CANCEL = 5004
    C_STREAM_SUPERFAVE_LABEL = 5005


    C_STREAM_VISIBILITY_MARKER = 100

    VISIBLE_STRM = 'strm'
    VISIBLE_FAVOURITES = 'favourites'
    VISIBLE_ADDONS = 'addons'
    VISIBLE_PLAYLIST = 'playlist'
    VISIBLE_SUPERFAVE = 'superfave'

    def __new__(cls, database, channel):
        xml_file = os.path.join('script-tvguide-streamsetup.xml')

        if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
            XML = xml_file

        return super(StreamSetupDialog, cls).__new__(cls, XML, PATH)

    def __init__(self, database, channel):
        """
        @type database: source.Database
        @type channel:source.Channel
        """
        super(StreamSetupDialog, self).__init__()
        self.database = database
        self.channel = channel
        self.player = xbmc.Player()
        self.previousAddonId = None
        self.previousProvider = None
        self.strmFile = None
        self.streamingService = streaming.StreamsService()

    def close(self):
        if self.player.isPlaying():
            self.player.stop()
        super(StreamSetupDialog, self).close()

    def onInit(self):
        self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_STRM)

        favourites = self.streamingService.loadFavourites()
        items  = list()  
        for label, value in favourites:
            item = xbmcgui.ListItem(label)
            item.setProperty('stream', value)
            items.append(item)

        listControl = self.getControl(StreamSetupDialog.C_STREAM_FAVOURITES)
        listControl.addItems(items)

        items = list()
        for id in self.streamingService.getAddons():
            try:
                addon = xbmcaddon.Addon(id) # raises Exception if addon is not installed
                item = xbmcgui.ListItem(addon.getAddonInfo('name'), iconImage=addon.getAddonInfo('icon'))
                item.setProperty('addon_id', id)
                if id == 'script.on-tapp.tv':
                    item = xbmcgui.ListItem('Kodi PVR', iconImage=os.path.join(dixie.RESOURCES, 'kodi-pvr.png'))
                    item.setProperty('addon_id', id)
                items.append(item)
            except Exception:
                pass
        listControl = self.getControl(StreamSetupDialog.C_STREAM_ADDONS)
        listControl.addItems(items)
        self.updateAddonInfo()

        playlist = self.streamingService.loadPlaylist()
        items = list()
        for label, value in playlist:
            item = xbmcgui.ListItem(label)
            item.setProperty('stream', value)
            items.append(item)

        listControl = self.getControl(StreamSetupDialog.C_STREAM_PLAYLIST)
        listControl.addItems(items)


    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
            self.close()
            return

        elif self.getFocusId() == self.C_STREAM_ADDONS:
            self.updateAddonInfo()


    def onClick(self, controlId):
        if controlId == self.C_STREAM_STRM_BROWSE:
            stream = xbmcgui.Dialog().browse(1, ADDON.getLocalizedString(30304), 'video', mask='.xsp|.strm')
            if stream:
                self.database.setCustomStreamUrl(self.channel, stream)
                self.getControl(self.C_STREAM_STRM_FILE_LABEL).setText(stream)
                self.strmFile = stream

        elif controlId == self.C_STREAM_ADDONS_OK:
            listControl = self.getControl(self.C_STREAM_ADDONS_STREAMS)
            item = listControl.getSelectedItem()
            if item:
                stream = item.getProperty('stream')
                self.database.setCustomStreamUrl(self.channel, stream)
            self.close()

        elif controlId == self.C_STREAM_FAVOURITES_OK:
            listControl = self.getControl(self.C_STREAM_FAVOURITES)
            item = listControl.getSelectedItem()
            if item:
                stream = item.getProperty('stream')
                self.database.setCustomStreamUrl(self.channel, stream)
            self.close()

        elif controlId == self.C_STREAM_SUPERFAVE_BROWSE:
            import sys
            sfAddon = xbmcaddon.Addon(id = 'plugin.program.super.favourites')
            sfPath  = sfAddon.getAddonInfo('path')
            sys.path.insert(0, sfPath)
            import chooser

            if chooser.GetFave('OTT'):
                path  = xbmc.getInfoLabel('Skin.String(OTT.Path)')
                label = xbmc.getInfoLabel('Skin.String(OTT.Label)')

                if path.lower().startswith('playmedia'):
                    import re
                    path = re.compile('"(.+?)"').search(path).group(1)
                else:             
                    path = '__SF__' + path

                self.database.setCustomStreamUrl(self.channel, path)
                self.getControl(self.C_STREAM_SUPERFAVE_LABEL).setText(label)
                self.strmFile = path

        elif controlId == self.C_STREAM_PLAYLIST_OK:
            listControl = self.getControl(self.C_STREAM_PLAYLIST)
            item = listControl.getSelectedItem()
            if item:
                stream = item.getProperty('stream')
                self.database.setCustomStreamUrl(self.channel, stream)
            self.close()

        elif controlId == self.C_STREAM_STRM_OK:
            self.database.setCustomStreamUrl(self.channel, self.strmFile)
            self.close()

        elif controlId == self.C_STREAM_SUPERFAVE_OK:
            self.database.setCustomStreamUrl(self.channel, self.strmFile)
            self.close()

        elif controlId in [self.C_STREAM_ADDONS_CANCEL, self.C_STREAM_FAVOURITES_CANCEL, self.C_STREAM_STRM_CANCEL, self.C_STREAM_SUPERFAVE_CANCEL, self.C_STREAM_PLAYLIST_CANCEL]:
            self.close()

        elif controlId in [self.C_STREAM_ADDONS_PREVIEW, self.C_STREAM_FAVOURITES_PREVIEW, self.C_STREAM_STRM_PREVIEW, self.C_STREAM_SUPERFAVE_PREVIEW, self.C_STREAM_PLAYLIST_PREVIEW]:
            if self.player.isPlaying():
                self.player.stop()
                self.getControl(self.C_STREAM_ADDONS_PREVIEW).setLabel(strings(PREVIEW_STREAM))
                self.getControl(self.C_STREAM_FAVOURITES_PREVIEW).setLabel(strings(PREVIEW_STREAM))
                self.getControl(self.C_STREAM_SUPERFAVE_PREVIEW).setLabel(strings(PREVIEW_STREAM))
                self.getControl(self.C_STREAM_STRM_PREVIEW).setLabel(strings(PREVIEW_STREAM))
                self.getControl(self.C_STREAM_PLAYLIST_PREVIEW).setLabel(strings(PREVIEW_STREAM))
                return

            stream = None
            windowed = None
            visible = self.getControl(self.C_STREAM_VISIBILITY_MARKER).getLabel()
            if visible == self.VISIBLE_ADDONS:
                listControl = self.getControl(self.C_STREAM_ADDONS_STREAMS)
                item = listControl.getSelectedItem()
                if item:
                    stream = item.getProperty('stream')
            elif visible == self.VISIBLE_FAVOURITES:
                listControl = self.getControl(self.C_STREAM_FAVOURITES)
                item = listControl.getSelectedItem()
                if item:
                    stream = item.getProperty('stream')
            elif visible == self.VISIBLE_SUPERFAVE:
                stream = self.strmFile
            elif visible == self.VISIBLE_PLAYLIST:
                listControl = self.getControl(self.C_STREAM_PLAYLIST)
                item = listControl.getSelectedItem()
                if item:
                    stream = item.getProperty('stream')
            elif visible == self.VISIBLE_STRM:
                stream = self.strmFile

            if stream is not None:
                path = os.path.join(ADDON.getAddonInfo('path'), 'player.py')
                xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d)' % (path, stream, 1))
                retries = 10
                while retries > 0 and not self.player.isPlaying():
                    retries -= 1
                    xbmc.sleep(1000)
                if self.player.isPlaying():
                    self.getControl(self.C_STREAM_PLAYLIST_PREVIEW).setLabel(strings(STOP_PREVIEW))
                    self.getControl(self.C_STREAM_ADDONS_PREVIEW).setLabel(strings(STOP_PREVIEW))
                    self.getControl(self.C_STREAM_FAVOURITES_PREVIEW).setLabel(strings(STOP_PREVIEW))
                    self.getControl(self.C_STREAM_SUPERFAVE_PREVIEW).setLabel(strings(STOP_PREVIEW))
                    self.getControl(self.C_STREAM_STRM_PREVIEW).setLabel(strings(STOP_PREVIEW))


    def onFocus(self, controlId):
        if controlId == self.C_STREAM_STRM_TAB:
            self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_STRM)
        elif controlId == self.C_STREAM_FAVOURITES_TAB:
            self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_FAVOURITES)
        elif controlId == self.C_STREAM_ADDONS_TAB:
            self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_ADDONS)
        elif controlId == self.C_STREAM_SUPERFAVE_TAB:
            self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_SUPERFAVE)
        elif controlId == self.C_STREAM_PLAYLIST_TAB:
            self.getControl(self.C_STREAM_VISIBILITY_MARKER).setLabel(self.VISIBLE_PLAYLIST)

    def updateAddonInfo(self):
        listControl = self.getControl(self.C_STREAM_ADDONS)
        item = listControl.getSelectedItem()
        if item is None:
            return

        if item.getProperty('addon_id') == self.previousAddonId:
            return

        self.previousAddonId = item.getProperty('addon_id')
        addon = xbmcaddon.Addon(id = item.getProperty('addon_id'))
        self.getControl(self.C_STREAM_ADDONS_NAME).setLabel('[B]%s[/B]' % addon.getAddonInfo('name'))
        self.getControl(self.C_STREAM_ADDONS_DESCRIPTION).setText(addon.getAddonInfo('description'))

        streams = self.streamingService.getAddonStreams(item.getProperty('addon_id'))
        items = list()
        for (label, stream) in streams:
            item = xbmcgui.ListItem(label)
            item.setProperty('stream', stream)
            items.append(item)
        listControl = self.getControl(StreamSetupDialog.C_STREAM_ADDONS_STREAMS)
        listControl.reset()
        listControl.addItems(items)


class ChooseStreamAddonDialog(xbmcgui.WindowXMLDialog):
    C_SELECTION_LIST = 1000

    def __new__(cls, addons):
        xml_file = os.path.join('script-tvguide-streamaddon.xml')
        if os.path.join(SKIN, skinfolder, 'Default', '720p', xml_file):
            XML = xml_file

        return super(ChooseStreamAddonDialog, cls).__new__(cls, XML, PATH)

    def __init__(self, addons):
        super(ChooseStreamAddonDialog, self).__init__()
        self.addons = addons
        self.stream = None


    def onInit(self):
        items = list()
        for id, label, url in self.addons:
            try:
                addon = xbmcaddon.Addon(id)
                item = xbmcgui.ListItem(label, addon.getAddonInfo('name'), addon.getAddonInfo('icon'))
                item.setProperty('stream', url)
                items.append(item)
            except:
                item = xbmcgui.ListItem(label, '', id)
                item.setProperty('stream', url)
                items.append(item)

        listControl = self.getControl(ChooseStreamAddonDialog.C_SELECTION_LIST)
        listControl.addItems(items)

        self.setFocus(listControl)

    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK]:
            self.close()

    def onClick(self, controlId):
        if controlId == ChooseStreamAddonDialog.C_SELECTION_LIST:
            listControl = self.getControl(ChooseStreamAddonDialog.C_SELECTION_LIST)
            self.stream = listControl.getSelectedItem().getProperty('stream')
            self.close()

    def onFocus(self, controlId):
        pass


class CategoriesMenu(xbmcgui.WindowXMLDialog):
    C_CATEGORIES_LIST = 7000
    C_CATEGORIES_SELECTION = 7001
    C_CATEGORIES_SAVE = 7002
    C_CATEGORIES_CANCEL = 7003

    def __new__(cls, database, categoriesList):
        xml_file = os.path.join('script-tvguide-categories.xml')
        if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
            XML = xml_file

        return super(CategoriesMenu, cls).__new__(cls, XML, PATH)


    def __init__(self, database, categoriesList):
        """

        @type database: source.Database
        """
        super(CategoriesMenu, self).__init__()
        self.database = database

        self.allCategories = database.getCategoriesList()
        if categoriesList:
            self.currentCategories = list(categoriesList)
        else:
            self.currentCategories = list()

        self.workingCategories = list(self.currentCategories)

        self.swapInProgress = False


    def onInit(self):
        self.updateCategoriesList()
        self.setFocusId(self.C_CATEGORIES_LIST)


    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
            self.close()
            return

    def onClick(self, controlId):
        if controlId == self.C_CATEGORIES_LIST:
            listControl = self.getControl(self.C_CATEGORIES_LIST)
            item        = listControl.getSelectedItem()
            category    = self.allCategories[int(item.getProperty('idx'))]
            if category in self.workingCategories:
                self.workingCategories.remove(category)
            else:
                self.workingCategories.append(category)

            if category in self.workingCategories:
                iconImage = 'tvguide-categories-visible.png'
            else:
                iconImage = 'tvguide-categories-hidden.png'
            item.setIconImage(iconImage)

        elif controlId == self.C_CATEGORIES_SAVE:
            self.currentCategories = self.workingCategories
            self.close()

        elif controlId == self.C_CATEGORIES_CANCEL:
            self.close()


    def onFocus(self, controlId):
        pass


    def updateCategoriesList(self):
        listControl = self.getControl(self.C_CATEGORIES_LIST)
        listControl.reset()
        for idx, category in enumerate(self.allCategories):
            if category in self.workingCategories:
                iconImage = 'tvguide-categories-visible.png'
            else:
                iconImage = 'tvguide-categories-hidden.png'
            
            category = urllib.unquote_plus(category)
            
            item = xbmcgui.ListItem(category, iconImage = iconImage)
            item.setProperty('idx', str(idx))
            listControl.addItem(item)


class CategoriesMenu(xbmcgui.WindowXMLDialog):
    C_CATEGORIES_LIST = 7000
    C_CATEGORIES_SELECTION = 7001
    C_CATEGORIES_SAVE = 7002
    C_CATEGORIES_CANCEL = 7003

    def __new__(cls, database, categoriesList):
        xml_file = os.path.join('script-tvguide-categories.xml')
        if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
            XML = xml_file

        return super(CategoriesMenu, cls).__new__(cls, XML, PATH)


    def __init__(self, database, categoriesList):
        """

        @type database: source.Database
        """
        super(CategoriesMenu, self).__init__()
        self.database = database

        self.allCategories = database.getCategoriesList()
        if categoriesList:
            self.currentCategories = list(categoriesList)
        else:
            self.currentCategories = list()

        self.workingCategories = list(self.currentCategories)

        self.swapInProgress = False

        xbmc.log(str(categoriesList)) 
        xbmc.log(str(self.currentCategories))


    def onInit(self):
        self.updateCategoriesList()
        self.setFocusId(self.C_CATEGORIES_LIST)


    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, KEY_CONTEXT_MENU]:
            self.close()
            return

    def onClick(self, controlId):
        if controlId == self.C_CATEGORIES_LIST:
            listControl = self.getControl(self.C_CATEGORIES_LIST)
            item        = listControl.getSelectedItem()
            category    = self.allCategories[int(item.getProperty('idx'))]
            if category in self.workingCategories:
                self.workingCategories.remove(category)
            else:
                self.workingCategories.append(category)

            if category in self.workingCategories:
                iconImage = 'tvguide-categories-visible.png'
            else:
                iconImage = 'tvguide-categories-hidden.png'
            item.setIconImage(iconImage)

        elif controlId == self.C_CATEGORIES_SAVE:
            self.currentCategories = self.workingCategories
            self.close()

        elif controlId == self.C_CATEGORIES_CANCEL:
            self.close()


    def onFocus(self, controlId):
        pass


    def updateCategoriesList(self):
        listControl = self.getControl(self.C_CATEGORIES_LIST)
        listControl.reset()
        for idx, category in enumerate(self.allCategories):
            if category in self.workingCategories:
                iconImage = 'tvguide-categories-visible.png'
            else:
                iconImage = 'tvguide-categories-hidden.png'
            
            category = urllib.unquote_plus(category)
            
            item = xbmcgui.ListItem(category, iconImage = iconImage)
            item.setProperty('idx', str(idx))
            listControl.addItem(item)


class CategoriesMenu1(object):
    def __init__(self, database, categories, parent):
        self.database = database
        self.parent   = parent

        self.isVisible     = False
        self.allCategories = database.getCategoriesList()

        try:
            self.updateCategories(categories)
            self.show()
        except:
            pass

    def show(self):
        try:
            if (dixie.isLimited()) or (dixie.GetSetting('hide.cats') == 'true'):
                return self.hide()

            self.isVisible = True
            self.parent.getControl(C_CATEGORIES_CTRL).setVisible(self.isVisible)
        except:
            self.hide()

    def hide(self):
        try:
            self.isVisible = False
            self.parent.getControl(C_CATEGORIES_CTRL).setVisible(self.isVisible)
        except:
            pass
        

    def onAction(self, action):
        controlInFocus = self.parent.getFocus()
        if controlInFocus <> self.parent.getControl(C_CATEGORIES_LIST):
            return False

        actionId = action.getId()

        if actionId in [ACTION_UP]:
            self.parent._moveToBottom()

        if actionId in [ACTION_DOWN]:
            self.parent._down(Point())
            
        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK]:
            self.parent.close()

        return True

    def onClick(self, controlId):
        if controlId <> C_CATEGORIES_LIST:
            return False

        listControl = self.parent.getControl(C_CATEGORIES_LIST)
        item        = listControl.getSelectedItem()
        category    = self.allCategories[int(item.getProperty('idx'))]

        if category in self.categories:
            self.categories.remove(category)
        else:
            self.categories.append(category)

        if category in self.categories:
            iconImage = 'ontapp-category-visible.png'
        else:
            iconImage = 'ontapp-category-hidden.png'

        item.setIconImage(iconImage)

        self.parent.categoriesList = self.categories
        dixie.SetSetting('categories', '|'.join(self.parent.categoriesList))
        self.onRedrawEPG()

        return True


    def updateCategories(self, categories):
        if categories:
            self.categories = list(categories)
        else:
            self.categories = list()

        self.updateCategoriesList()


    def updateCategoriesList(self):
        try:
            listControl = self.parent.getControl(C_CATEGORIES_LIST)
            listControl.reset()

            for idx, category in enumerate(self.allCategories):
                if category in self.categories:
                    iconImage = 'ontapp-category-visible.png'
                else:
                    iconImage = 'ontapp-category-hidden.png'

                category = urllib.unquote_plus(category)

                item = xbmcgui.ListItem(category, iconImage = iconImage)
                item.setProperty('idx', str(idx))
                listControl.addItem(item)
        except:
            self.isVisible = False


    def setFocus(self):
        if not self.isVisible:
            return self.parent._moveToBottom()

        ctrl = self.parent.getControl(C_CATEGORIES_LIST)
        if ctrl:
            self.parent.setFocus(ctrl)


    def onRedrawEPG(self):       
        self.parent.onRedrawEPG(self.parent.channelIdx, self.parent.viewStartDate)
        self.setFocus()