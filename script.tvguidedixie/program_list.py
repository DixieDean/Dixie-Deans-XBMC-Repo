#
#       Copyright (C) 2017
#       OTT Networks Ltd
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


import xbmc
import xbmcgui
import xbmcaddon
import os

import datetime
import time

import dixie

from source import Channel

KEY_NAV_BACK = 92
KEY_ESC_ID   = 10
KEY_ESC_CODE = 61467

ACTION_BACK          = 92
ACTION_PARENT_DIR    = 9
ACTION_PREVIOUS_MENU = 10

ACTION_UP         = 3
ACTION_DOWN       = 4
ACTION_PAGE_UP    = 5
ACTION_PAGE_DOWN  = 6
ACTION_SELECT     = 7
ACTION_MOUSE_MOVE = 107


C_DIALOG_BOX   = 4300
C_DIALOG_TITLE = 4302
C_DIALOG_TEXT  = 4303
C_DIALOG_YES   = 4301
C_DIALOG_NO    = 4304
C_DIALOG_ICON  = 4305
C_DIALOG_OKAY  = 4306

THEPAST   = -1
THENOW    =  0
THEFUTURE =  1

class DialogList(xbmcgui.WindowXMLDialog):

    def __new__(cls, programs, channels, term , showHits):
        xml = 'script-tvguide-program-list.xml'
        return super(DialogList, cls).__new__(cls, xml, dixie.getSkinPath(xml))

    def __init__(self, programs, channels, term , showHits):
        super(DialogList, self).__init__()
        self.programs = programs
        self.term     = term
        self.channels = channels
        self.showHits = showHits


    def onInit(self):
        try:
            self.prune()

            nHits   = len(self.programs)
            hitText = 'hit'
            if nHits > 1: hitText = hitText + 's'

            if self.showHits:
                self.getControl(4001).setLabel('%s (%d %s)' % (self.term, len(self.programs), hitText))
            else:
                self.getControl(4001).setLabel(self.term)

            self.programDesc     = self.getControl(4002)
            self.programImage    = self.getControl(4007)
            self.selectedProgram = None

            self.list = self.getControl(4003)

            self.listID       = self.list.getId()
            self.currentIndex = -1

            try:    self.populateList()
            except: pass

            if len(self.programs) < 1:
                self.setFocus(self.getControl(4005))
            else:
                self.setFocus(self.list)
                self.updateDetails()
        except:
            raise

    def populateList(self):
        nHits    = len(self.programs)
        colStart = '[COLOR=FF808080]'
        colEnd   = '[/COLOR]'
        when     = THEPAST

        count    = 0
        progress = 10

        for p in self.programs:
            if when != THEFUTURE:
                when = self.isOnWhen(p)
                if when == THEPAST:
                    colStart = '[COLOR=FF17CFF9]'
                    airTime  = 'Aired '
                    at       = '@ '
                elif when == THENOW:
                    colStart = '[COLOR=FF00FF00]'
                    airTime  = 'Live Now! '
                    day      = ''
                    at       = ''
                elif when == THEFUTURE:
                    airTime  = 'Airing '
                    at       = '@ '
                    colStart = ''
                    colEnd   = ''

            title = '%s%s%s' % (colStart, p[0], colEnd)

            startDate = self.parseDate(p[3])
            day       = dixie.getDayAsString(startDate.date())
            when      = dixie.formatTime(startDate)
            time      = '%s%s  %s%s' % (colStart, day, when, colEnd)

            logo = p[6]
            if logo:
                liz = xbmcgui.ListItem(title, time, iconImage=logo)
            else:
                liz = xbmcgui.ListItem(title, time)
            self.list.addItem(liz)


    def prune(self):
        localChannels = {}
        for c in self.channels:
            localChannels[c.id] = c.logo

        localPrograms = []
        for p in self.programs:
            if p[2] in localChannels:
                #update channel logo
                p[6] = localChannels[p[2]]
                localPrograms.append(p)

        self.programs = localPrograms


    def parseDate(self, dateString):
        if type(dateString) in [str, unicode]:
            dt = dateString.split(' ')
            d  = dt[0]
            t  = dt[1]
            ds = d.split('-')
            ts = t.split(':')
            return datetime.datetime(int(ds[0]), int(ds[1]) ,int(ds[2]), int(ts[0]), int(ts[1]), int(ts[2]))

        return dateString


    def isOnWhen(self, program):
        now   = datetime.datetime.today()
        start = program[3]
        end   = program[4]

        start = self.parseDate(start)
        end   = self.parseDate(end)

        if now < start:
            return THEFUTURE

        if now >= end:
            return THEPAST

        return THENOW
               
 
    def onAction(self, action):
        try:
            actionID = action.getId()
            if actionID in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK, ACTION_BACK, KEY_ESC_ID]:
                self.close()
                return

            if actionID in [ACTION_UP, ACTION_DOWN, ACTION_PAGE_UP, ACTION_PAGE_DOWN, ACTION_MOUSE_MOVE]:
                self.updateDetails()

            if actionID in [ACTION_SELECT]:
                if self.currentIndex > -1:
                    self.selectedProgram = self.programs[self.currentIndex]
                self.close()
                return
        except:
            pass


    def onClick(self, controlId):
        if controlId == self.listID:
            self.selectedProgram = self.programs[self.currentIndex]
        else:
            self.currentIndex = -1
        self.close()
 
 
    def onFocus(self, controlId):
        if controlId == self.listID:
            self.updateDetails()


    def updateDetails(self):
        try:
            index = self.list.getSelectedPosition()
            if self.currentIndex == index:
                return
            self.currentIndex = index

            self.programImage.setImage(self.programs[self.currentIndex][5], useCache=False)

            self.programDesc.setText(self.programs[self.currentIndex][1])
            self.programDesc.setVisible(self.programs[self.currentIndex][1] != '')

        except:
            self.programDesc.setVisible(False)


def show(programs, channels, term=None, showHits=False):
    list = DialogList(programs, channels, term, showHits)
    list.doModal()
    selected = list.selectedProgram 
    del list
    return selected
