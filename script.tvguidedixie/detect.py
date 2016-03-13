#
#       Copyright (C) 2015
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
import xbmcaddon
import xbmcgui
import os

import dixie
import settings


SKIN = dixie.SKIN

datapath   = dixie.PROFILE
extras     = os.path.join(datapath, 'extras')
skinfolder = os.path.join(datapath, extras, 'skins')
skinpath   = os.path.join(skinfolder, SKIN)

PATH = skinpath

xml_file = os.path.join('script-tvguide-main.xml')
if os.path.join(SKIN, 'extras', 'skins', 'Default', '720p', xml_file):
    XML  = xml_file

ACTION_PARENT_DIR = 9
ACTION_PREVIOUS_MENU = 10

KEY_NAV_BACK = 92



class StreamAddonDialog(xbmcgui.WindowXMLDialog):
    C_SELECTION_LIST = 1000

    def __new__(cls, addons):
        xml_file = os.path.join('script-tvguide-streamaddon.xml')
        if os.path.join(SKIN, skinfolder, 'Default', '720p', xml_file):
            XML = xml_file

        return super(StreamAddonDialog, cls).__new__(cls, XML, PATH)

    def __init__(self, addons):
        super(StreamAddonDialog, self).__init__()
        self.addons = addons
        self.stream = None

    def onInit(self):
        try:
            SUPERFAVES = 'plugin.program.super.favourites'
            SF_ICON    = xbmcaddon.Addon(id=SUPERFAVES).getAddonInfo('icon')
            
        except:
            SF_ICON   = ''

        items = list()
        for id, label, url in self.addons:
            try:
                if id.startswith('SF_'):
                    dir  = id.split('SF_', 1)[-1]
                    cfg  = os.path.join(dir, 'folder.cfg')
                    icon = settings.get('ICON', cfg)

                    if not icon:
                        icon = SF_ICON

                    name = ''
                
                elif id == 'kodi-favourite':
                    icon = os.path.join(dixie.RESOURCES, 'kodi-favourite.png')
                    name = ''

                elif id == 'iptv-playlist':
                    icon = os.path.join(dixie.RESOURCES, 'iptv-playlist.png')
                    name = ''

                elif id == 'script.on-tapp.tv':
                    icon = os.path.join(dixie.RESOURCES, 'kodi-pvr.png')
                    name = ''

                else:
                    addon = xbmcaddon.Addon(id)
                    icon  = addon.getAddonInfo('icon')
                    name  = addon.getAddonInfo('name')

                if not name:
                    name = label
                if not icon:
                    icon = ''
                
                item = xbmcgui.ListItem(label, name, icon)
                item.setProperty('stream', url)
                items.append(item)

            except:
                pass

                item = xbmcgui.ListItem(label, '', id)
                item.setProperty('stream', url)
                items.append(item)        

        listControl = self.getControl(StreamAddonDialog.C_SELECTION_LIST)
        listControl.addItems(items)

        self.setFocus(listControl)

    def onAction(self, action):
        if action.getId() in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, KEY_NAV_BACK]:
            self.close()

    def onClick(self, controlId):
        if controlId == StreamAddonDialog.C_SELECTION_LIST:
            listControl = self.getControl(StreamAddonDialog.C_SELECTION_LIST)
            self.stream = listControl.getSelectedItem().getProperty('stream')
            self.close()

    def onFocus(self, controlId):
        pass
