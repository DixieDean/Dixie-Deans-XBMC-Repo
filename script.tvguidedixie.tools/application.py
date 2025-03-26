
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

import main
functionality = main

import xbmc
import xbmcgui
import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import json

import utilsTOOLS as utils


ACTION_SELECT     = 7
ACTION_PARENT_DIR = 9
ACTION_BACK       = 92
ACTION_LCLICK     = 100
ACTION_RCLICK     = 101
ACTION_CONTEXT    = 117

ESC = 61467

MAINLIST  = 69
ALLLISTS  = [49, 69]
MAINGROUP = 100
LISTBACK  = -999
SKIN      = utils.getSetting('SKIN')

datapath    = utils.PROFILE
skinfolder  = os.path.join(datapath, 'skins')
skinpath    = os.path.join(skinfolder, SKIN)

PATH = skinpath

xml_file = os.path.join('main.xml')

os.path.join(SKIN, 'skins', 'Default', '720p', xml_file)
XML  = xml_file


class Application(xbmcgui.WindowXML):
    def __new__(cls, addonID):
        return super(Application, cls).__new__(cls, XML, PATH)

# class Application(xbmcgui.WindowXML):
#     def __new__(cls, addonID):
#         skin = 'Default'
#         path = os.path.join(xbmcaddon.Addon(addonID).getAddonInfo('path'), 'resources', 'skins', skin)
#         return super(Application, cls).__new__(cls, 'main.xml', path)


    def __init__(self, addonID):
        super(Application, self).__init__()
        self.ADDONID         = addonID
        self.properties      = {}
        self.lists           = []
        self.context         = False
        self.busy            = None
        self.showBack        = False
        self.timer           = None
        self.counter         = 0
        self.activeList      = MAINLIST
        self.refreshLists()

    def onInit(self):
        self.clearList()

        if len(self.lists) < 1:
            self.onParams('init')
            return

        #add new list so we can just call onBack
        self.newList()
        self.onBack()


    def run(self, param=''):
        self.doModal()


    def close(self):
        self.stopTimer()
        xbmcgui.WindowXML.close(self)


    def resetTimer(self):
        try:
            self.stopTimer()
            self.timer = threading.Timer(1, self.onTimer) 
            self.timer.start()
        except Exception, e:
            pass


    def stopTimer(self):
        if not self.timer:
            return

        try:
            self.timer.cancel()
            del self.timer
            self.timer = None
        except Exception, e:
            pass


    def onTimer(self):
        self.counter += 1
        self.resetTimer()


    def doRefresh(self):
        self.newList()
        self.onBack()


    def onFocus(self, controlId):
        utils.Log('onFocus %d' % controlId)


    def openSettings(self, addonID):
        functionality.ShowSettings(addonID)


    def onAction(self, action):
        #see here https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h for the full list

        actionId = action.getId()
        buttonId = action.getButtonCode()

        if actionId != 107:
            utils.Log('onAction actionID %d' % actionId)
            utils.Log('onAction buttonID %d' % buttonId)

        if actionId in [ACTION_CONTEXT, ACTION_RCLICK]:
            return self.onContextMenu()

        if actionId in [ACTION_PARENT_DIR, ACTION_BACK] or buttonId in [ESC]:
            return self.onBack()

        try:    id = self.getFocus().getId()
        except: id = 0

        select = (actionId == ACTION_SELECT) or (actionId == ACTION_LCLICK)

        if not select:
            return

        if id == self.activeList:   
            liz        = self.getSelectedItem()
            param      = liz.getProperty('Param')
            image      = liz.getProperty('Image')
            mode       = int(liz.getProperty('Mode'))
            isFolder   = liz.getProperty('IsFolder')   == 'true'
            isPlayable = liz.getProperty('IsPlayable') == 'true'

            if mode == LISTBACK:
                return self.onBack()

            if param:
                self.stopTimer()
                self.onParams(param, isFolder)
                self.resetTimer()


    def onClick(self, controlId):
        utils.Log('onClick %d' % controlId)


    def onBack(self): 
        try:    self.lists.pop()
        except: pass

        if len(self.lists) == 0:
            self.close()
            return

        self.list = self.lists[-1]

        if len(self.list) == 0:
            #addon must have originally been started with a
            #parameter therefore reset to initial position
            self.lists = []
            self.onInit()
            return

        if hasattr(functionality, 'onBack'):
           functionality.onBack(self, self.list[0])

        self.addItems(self.list)


    def onContextMenu(self):
        if self.context:
            return

        #liz   = self.getSelectedItem()
        #index = int(liz.getProperty('Index'))
        #item  = self.list[index]
        #menu  = item['ContextMenu']

        id     = self.getFocus().getId()
        ctrl   = self.getControl(id)
        liz    = ctrl.getSelectedItem()
        menu   = liz.getProperty('ContextMenu')
        menu   = json.loads(menu)

        replaceItems = liz.getProperty('ReplaceItems') == 'true'

        if not replaceItems:
            menu = list(menu + self.getSTDMenu(liz))

        if len(menu) < 1:
            return

        import contextmenus
        self.context = True
        params       = contextmenus.showMenu(self.ADDONID, menu, False)
        self.context = False

        if not params or params < 0:
            return

        if self.trySTDMenu(params):
            return

        self.onParams(params, isFolder=False)


    def showControl(self, id, show):
        try:    self.getControl(id).setVisible(show)
        except: pass


    def getProgress(self):
        try:    return self.busy.getControl(10)
        except: return None


    def showBusy(self):
        self.busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        self.busy.show()
        progress = self.getProgress()
        if progress:
            progress.setVisible(False)


    def closeBusy(self):
        if self.busy:
            self.busy.close()
            self.busy = None


    def newList(self):
        self.list = []
        self.lists.append(self.list)


    def getSelectedItem(self):
        try:    return self.getActiveList().getSelectedItem()
        except: return None


    def setControlImage(self, id, image):
        if image == None:
            return

        control = self.getControl(id)
        if not control:
            return

        if 'http' in image:
            image = image.replace(' ', '%20')

        try:    control.setImage(image)
        except: pass


    def clearList(self):
        self.getActiveList().reset()


    def getSTDMenu(self, liz):
        param = liz.getProperty('Param')

        std = []

        std.append(('Settings', 'STD:SETTINGS'))
        return std


    def trySTDMenu(self, params):
        if params == 'STD:SETTINGS':
            self.addonSettings()
            return True

        return False


    def addonSettings(self):
        xbmcaddon.Addon(self.ADDONID).openSettings()
        return True


    def setProperty(self, property, value):
        self.properties[property] = value
        #xbmcgui.Window(xbmcgui.getCurrentWindowId()).setProperty(property, value)
        xbmcgui.Window(10000).setProperty(property, value)


    def clearProperty(self, property):
        del self.properties[property]
        xbmcgui.Window(10000).clearProperty(property)


    def clearAllProperties(self):
        for property in self.properties:
            xbmcgui.Window(10000).clearProperty(property)

        self.properties = {}


    def addDir(self, name, mode, url='', image=None, isFolder=True, isPlayable=False, totalItems=0, contextMenu=[], replaceItems=False, infoLabels={}, listID=None):
        if not image:
            image = ''

        if not contextMenu:
            contextMenu=[]

        if not infoLabels:
            infoLabels={}

        if listID is None:
            listID = MAINLIST

        item = {}
        item['Name']         = name
        item['Mode']         = mode
        item['Url']          = url
        item['Image']        = image
        item['IsFolder']     = isFolder
        item['IsPlayable']   = isPlayable
        item['ContextMenu']  = contextMenu
        item['ReplaceItems'] = replaceItems
        item['ListID']       = listID
        item['InfoLabels']   = dict(infoLabels)

        self.list.append(item)

        progress = self.getProgress()
        if not progress:
            return
            
        if totalItems == 0:
            progress.setVisible(False)
        else:
            progress.setVisible(True)
            nItems = float(len(self.list) - 1) # subtract params'
            if self.showBack:
                nItems -= 1 # subtract params' and 'back' items
            perc   = 100 * nItems / totalItems
            progress.setPercent(perc)


    def getActiveList(self):
        return self.getControl(self.activeList)


    def refreshLists(self):
        for id in ALLLISTS:
            # subtracting one will hide the whole group
            self.showControl(id-1, id == self.activeList)


    def setActiveList(self, listID):
        listID = int(listID)

        if listID == self.activeList:
            return

        self.activeList = listID
        self.refreshLists()



    def addItems(self, theList):
        listID = self.activeList

        self.clearList()

        #index  = 1 #not '0' because first item in list is the params item

        listItems = []

        for item in theList[1:]:
            name         = item['Name']
            mode         = item['Mode']
            url          = item['Url']
            image        = item['Image']
            isFolder     = item['IsFolder']
            isPlayable   = item['IsPlayable']
            contextMenu  = item['ContextMenu']
            replaceItems = item['ReplaceItems']
            listID       = item['ListID'] 
            infoLabels   = item['InfoLabels']

            liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)

            #liz.setProperty('Index',        str(index))
            liz.setProperty('Mode',         str(mode))
            liz.setProperty('Param',        url)
            liz.setProperty('Image',        image)
            liz.setProperty('ListID',       str(listID))
            liz.setProperty('IsFolder',     'true'  if isFolder     else 'false')
            liz.setProperty('IsPlayable',   'true'  if isPlayable   else 'false')
            liz.setProperty('ReplaceItems', 'true'  if replaceItems else 'false')
            liz.setProperty('ContextMenu',   json.dumps(contextMenu))

            #index += 1
  
            if infoLabels and (len(infoLabels) > 0):
                liz.setInfo(type='', infoLabels=infoLabels)
                #each infolabel is set as a property, this allow user-defined infoLabels
                #that can be accessed in the skin xml via: $INFO[Window.Property(USERDEFINED)]
                for item in infoLabels:     
                    liz.setProperty(item, infoLabels[item])

            listItems.append(liz)

        self.setActiveList(listID)
        self.getActiveList().addItems(listItems)

        try:    self.setFocus(self.getActiveList())
        except: pass

        if self.timer == None:
            self.resetTimer()


    def onParams(self, params, isFolder=True):
        if isFolder:
            self.newList() 
            #store params as first item in list
            self.list.append(params)
            if self.showBack:
                #add the '..' item
                self.addDir('Previous menu', LISTBACK, image='DefaultFolderBack.png', contextMenu=[('Add-on settings', 'STD:SETTINGS')], replaceItems=True)

        #call into the "real" addon
        if isFolder:
            self.showBusy()
        functionality.onParams(self, params)
        self.closeBusy()

        if isFolder:
            self.addItems(self.list)


    def containerRefresh(self):
        self.lists.pop()
        self.onParams(self.list[0], True)
