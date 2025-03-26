
#       Copyright (C) 2013-
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
import xbmcaddon
import os

import utilsTOOLS as utils

ACTION_BACK          = 92
ACTION_PARENT_DIR    = 9
ACTION_PREVIOUS_MENU = 10
ACTION_CONTEXT_MENU  = 117
ACTION_C_KEY         = 122

ACTION_LEFT  = 1
ACTION_RIGHT = 2
ACTION_UP    = 3
ACTION_DOWN  = 4

# FILENAME = 'contextmenu-estuary.xml' if utils.ESTUARY_SKIN else 'contextmenu.xml'
FILENAME = 'contextmenu-estuary.xml'
SKIN     =  utils.getSetting('SKIN')

datapath   = utils.PROFILE
skinfolder = os.path.join(datapath, 'skins')
skinpath   = os.path.join(skinfolder, SKIN)

PATH = skinpath

xml_file = os.path.join(FILENAME)

os.path.join(SKIN, '720p', xml_file)
XML  = xml_file


class ContextMenu(xbmcgui.WindowXMLDialog):
    def __new__(cls, addonID, menu):
        # return super(ContextMenu, cls).__new__(cls, FILENAME, xbmcaddon.Addon(addonID).getAddonInfo('path'))
        return super(ContextMenu, cls).__new__(cls, XML, PATH)


    def __init__(self, addonID, menu):
        super(ContextMenu, self).__init__()
        self.menu = menu


    def onInit(self):
        line   = 38
        spacer = 20
        delta  = 0 

        nItem = len(self.menu)
        if nItem > 16:
            nItem = 16
            delta = 1

        height = (line+spacer) + (nItem*line)

        self.getControl(5001).setHeight(height)

        self.list = self.getControl(3000)
        self.list.reset()
        self.list.setHeight(height-spacer-(delta*line))

        newY = 360 - (height/2)

        self.getControl(5000).setPosition(self.getControl(5000).getX(), newY)

        self.params    = None
        self.paramList = []

        for item in self.menu:
            self.paramList.append(item[1])
            title = item[0]
            liz   = xbmcgui.ListItem(title)
            self.list.addItem(liz)

        self.setFocus(self.list)


    def onAction(self, action):
        actionId = action.getId()

        if actionId in [ACTION_CONTEXT_MENU, ACTION_C_KEY]:
            self.params = 0
            xbmc.sleep(100)
            return self.close()

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_BACK]:
            return self.close()


    def onClick(self, controlId):
        if controlId != 3001:
            index = self.list.getSelectedPosition()
            try:    self.params = self.paramList[index]
            except: self.params = None

        self.close()


    def onFocus(self, controlId):
        pass


def showMenu(addonID, menu, useBuiltin=True):
    useBuiltin=True
    param = -1
    if useBuiltin and hasattr(xbmcgui.Dialog(), 'contextmenu'):
        list = []
        for item in menu:
            list.append(item[0])

        param = xbmcgui.Dialog().contextmenu(list)

        if param > -1:
            param = menu[param][1]

        return param

    menu = ContextMenu(addonID, menu)
    menu.doModal()
    param = menu.params
    del menu

    return param


def selectMenu(title, menu):
    options = []
    for option in menu:
        options.append(option[0])

    option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]