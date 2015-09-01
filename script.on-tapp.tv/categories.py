
#       Copyright (C) 2015
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
import re

import utilsOTT as utils

ADDONID = 'script.tvguidedixie'
ADDON   = xbmcaddon.Addon(ADDONID)
PROFILE = ADDON.getAddonInfo('profile')
PATH    = xbmc.translatePath(os.path.join(PROFILE, 'cats.xml'))
SKIN    = utils.getSetting('SKIN')

datapath   = utils.PROFILE
skinfolder = os.path.join(datapath, 'skins')
skinpath   = os.path.join(skinfolder, SKIN)
xml_file   = os.path.join('categories.xml')

if os.path.join(SKIN, 'skins', 'Default', '720p', xml_file):
    XML  = xml_file

ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10

KEY_NAV_BACK = 92


def getSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


def setSetting(param, value):
    if xbmcaddon.Addon(ADDONID).getSetting(param) == value:
        return
    xbmcaddon.Addon(ADDONID).setSetting(param, value)


def getAllCategories():    
    if os.path.exists(PATH):
        f = open(PATH)
        xml = f.read()
        f.close()
    
        items = re.findall('<category>(.+?)</category', xml)
        items = '|'.join(items)
        names = items.split('|')

        allCategories = []
    
        for name in names:
            if name not in allCategories:
                allCategories.append(name)
                allCategories.sort()
                
    return allCategories


def getCurrentCategories():
    currentCategories = getSetting('categories').split('|')
    return currentCategories


class CategoriesMenu(xbmcgui.WindowXMLDialog):
    C_CATEGORIES_LIST = 7000
    C_CATEGORIES_SELECTION = 7001
    C_CATEGORIES_SAVE = 7002
    C_CATEGORIES_CANCEL = 7003


    def __new__(cls, categoriesList):
        return super(CategoriesMenu, cls).__new__(cls, XML, skinpath)


    def __init__(self, categoriesList):
        # get categories list from cats.xml and current categories from settings
        super(CategoriesMenu, self).__init__()
        self.allCategories  = getAllCategories()
        self.categoriesList = getCurrentCategories()
        if categoriesList:
            self.currentCategories = list(categoriesList)
        else:
            self.currentCategories = list()

        self.workingCategories = list(self.currentCategories)
        

    def onInit(self):
        # display categories list
        self.updateCategoriesList()
        self.setFocusId(self.C_CATEGORIES_LIST)


    def onAction(self, action):
        # close categories list
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK]:
            self.close()
            return


    def onClick(self, controlId):
        # navigate, turn on/off, save/cancel
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

            item = xbmcgui.ListItem(' %s' % (category), iconImage = iconImage)
            item.setProperty('idx', str(idx))
            listControl.addItem(item)        
