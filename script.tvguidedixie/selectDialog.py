
#       Copyright (C) 2013-2014
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
import threading

            
class MainGui(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__( self )
        self.title      = kwargs.get('title')
        self.options    = kwargs.get('options')
        self.icons      = kwargs.get('icons')
        self.selected   = kwargs.get('selected')
        self.option     = -1


    def onInit(self):
        try:
            self.list = self.getControl(6)
            self.getControl(3).setVisible(False)
        except:
            self.list = self.getControl(3)

        self.getControl(5).setVisible(False)
        self.getControl(1).setLabel(self.title)
        #self.getControl(1).setVisible(False) #Confluence hack to get title to set correctly

        for idx, item in enumerate(self.options):
            listitem = xbmcgui.ListItem(item)                        
            listitem.setIconImage(self.icons[idx])
            self.list.addItem(listitem) 

        self.setFocus(self.list)
        self.list.selectItem(self.selected)


    def onAction(self, action):
        actionID = action.getId()

        if actionID == 1: #left
            self.setFocus(self.list)

        if actionID in (9, 10, 92, 216, 247, 257, 275, 61467, 61448):
            self.option = -1
            self.close()


    def onClick(self, controlID):
        if controlID in [7, 99]: #cancel buttons Krypton(7) / Pre-Krypton(99)
            self.option = -1
            return self.close()
        
        if controlID == 6 or controlID == 3:
            self.option = self.list.getSelectedPosition()
            self.close()


    def onFocus(self, controlID):
        pass


def doSelect(title, options, icons, selectedIndex):
    menu = MainGui('DialogSelect.xml', '', title=title, options=options, icons=icons, selected=selectedIndex)    
    menu.doModal()
    option = menu.option
    del menu
    return option


def selectItem(index):
    if index < 0:
        return

    dlg = None
    while not dlg:
        try:
            dlg = xbmcgui.Window(12000)
        except:
            xbmc.sleep(50)

    list = None
    while not list:
        try:
            list = dlg.getControl(3)
        except:
            xbmc.sleep(50)

    xbmc.sleep(150)
    list.selectItem(index)


def select(title, menu, selection=None):
    selectedIndex = -1
    if selection:
        for idx, option in enumerate(menu):
            if selection == option[0]:
                selectedIndex = idx
                break

    options = []
    icons   = []
    for idx, option in enumerate(menu):
        label = option[0]
        if idx == selectedIndex:
            label = '[COLOR selected]%s[/COLOR]' % label
        options.append(label)
        if len(option) > 2:
            icons.append(option[2])

    if len (icons) > 0:
        option = doSelect(title, options, icons, selectedIndex)
    else:
        if selectedIndex > -1:
            threading.Timer(0, selectItem, [selectedIndex]).start()

        option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]