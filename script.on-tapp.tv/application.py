
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

import ott
functionality = ott

import xbmc
import xbmcgui
import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import re
import urllib
import threading


import sfile
import utilsOTT as utils
import favourites
import categories
import rss


ACTION_SELECT     = 7
ACTION_PARENT_DIR = 9
ACTION_BACK       = 92
ACTION_LCLICK     = 100
ACTION_RCLICK     = 101
ACTION_CONTEXT    = 117

ESC = 61467

MAINLIST    = 59
MAINGROUP   = 100
CATEGORIES  = 2000
SETTINGS    = 2001
TOOLS       = 2002
VPN         = 2003
TVGUIDE     = 3000
MOVIES      = 3001
TVSHOWS     = 3002
NETFLIX     = 3003
MOVIEANDTV  = 3004
WORLDTV     = 3005
ANDROID     = 3006
ADULT       = 3007
KID         = 3008
VIDEOWINDOW = 3010

LISTBACK  = -999

GETTEXT  = utils.GETTEXT
FRODO    = utils.FRODO
SKIN     = utils.getSetting('SKIN')
FIRSTRUN = utils.getSetting('FIRSTRUN') == 'true'
DSF      = utils.isDSF()


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


    def __init__(self, addonID):        
        super(Application, self).__init__()
        self.ADDONID         = addonID
        self.skin            = utils.getSetting('SKIN')
        self.properties      = {}        
        self.lists           = []
        self.start           = None        
        self.context         = False
        self.busy            = None
        self.showBack        = False
        self.timer           = None
        self.faves           = str(favourites.getFavourites())
        self.counter         = 0
        self.listSize        = -1
        self.rss             = None

        self.setProperty('LB_FOOTER',  'Powered by SWIFT')
        self.setProperty('LB_TITLE',    GETTEXT(30000))
        self.setProperty('LB_MAINDESC', GETTEXT(30002))


    def onInit(self):
        if (not self.rss) and (DSF) and (utils.DSFVER > '1.0.3'):
            # try:
            winID    = xbmcgui.getCurrentWindowId()
            self.rss = rss.RSS(winID, 925, 120, 315, 315, 'http://nearscreen.gvax.tv/webtoprint/rss?id=1')
            self.updateDisplay()
            # except: pass

        self.clearList()

        xbmcgui.Window(10000).clearProperty('DSF_LIMITED')

        if self.start:            
            self.lists.append([]) 
            start      = self.start
            self.start = None
            self.onParams(start)
            return
            
        if len(self.lists) < 1:            
            self.onParams('init')
            return

        #add new list so we can just call onBack        
        self.newList()
        self.onBack()


    def run(self, param=''):        
        self.start = param

        if self.start and self.start.startswith('_Playable'):
            #this will be a Playable item called from Favourites menu
            self.newList()
            self.windowed = False
            self.onParams(self.start.replace('_Playable', ''), isFolder=False)
            return

        #self.resetTimer()
        self.doModal()

              
    def close(self):
        self.stopTimer()
        del self.rss
        xbmcgui.Window(10000).clearProperty('DSF_LIMITED')
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

        if self.counter == 5:
            self.clearProperty('LB_FOOTER')

        self.updateDisplay()

        #if self.relaunch:
        #    self.doRelaunch()
        #    return


        if xbmcgui.Window(10000).getProperty('OTT_RELAUNCH') == 'true':
            xbmcgui.Window(10000).setProperty('OTT_RELAUNCH', 'false')
            if not FIRSTRUN:
                self.doRelaunch()

        if self.listSize <> self.getListSize():
            self.containerRefresh()

        self.resetTimer()


    def doRefresh(self):
        self.newList()
        self.onBack()


    def doRelaunch(self):
        self.stopTimer()
        #self.relaunch = False
        utils.Launch()
        self.close()


    def onFocus(self, controlId):
        utils.Log('onFocus %d' % controlId)
        
        if controlId == SETTINGS:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Edit your GVAx settings')
            
        if controlId == VPN:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Use the VPN to connect to different countries')

        if controlId == TVGUIDE:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Open the TV Guide to show what is on TV')

        if controlId == MOVIES:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Open your Movie Library')

        if controlId == TVSHOWS:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Open your TV Show Library')

        if controlId == NETFLIX:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Watch content from Netflix')

        if controlId == MOVIEANDTV:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Browse and search for TV Shows and Movies')

        if controlId == WORLDTV:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Browse and search for TV Shows and Movies')

        if controlId == ANDROID:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Open your Android Apps')

        if controlId == ADULT:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Adult Section')

        if controlId == KID:
            return xbmcgui.Window(10000).setProperty('GVAX_DESC', 'Ninos Section')
        
        xbmcgui.Window(10000).setProperty('GVAX_DESC', '')


    def getDSFSetting(self, setting):
        return utils.getDSFSetting(setting)


    def updateVPN(self):
        try:
            self.status  = self.getControl(2004)
            self.country = ''

            address =  xbmcgui.Window(10000).getProperty('VPNICITY_ADDR')
            country =  xbmcgui.Window(10000).getProperty('VPNICITY_LABEL')
            if country == '':
                country = 'VPNicity not active'
    
            status = '[COLOR orange]IP Address:[/COLOR] [CR]%s [CR][COLOR orange]Country:[/COLOR] [CR]%s ' % (address, country)
            self.status.setLabel(status)
        except:
            pass


    def updateAdult(self):
        try:
            isAdult = self.getDSFSetting('PROTECTED').lower() == 'true'
            text    = 'Adultos' if isAdult else 'Ninos'

            self.setProperty('GVAX_ADULT', text)
            self.getControl(ADULT).setVisible(isAdult)
            self.getControl(KID).setVisible(not isAdult)
        except:
            pass

    def updateDisplay(self):
        if DSF:
            self.updateVPN()
            self.updateAdult()
            # try:
            self.rss.update()
            # except: pass

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

        if id == MAINLIST:   
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

        if id == CATEGORIES:
            categoriesList = categories.getSetting('categories').split('|')
            if categoriesList[0] == '':
                categoriesList = []
               
            functionality.ShowCategories(categoriesList)

        if id == SETTINGS:
            if DSF:
                addonID = utils.DSFID
            else:
                addonID = 'script.tvguidedixie'

            self.openSettings(addonID)

        
        if id == TOOLS:
            functionality.OpenTools()    

        if id == MOVIES:
            if utils.getSetting('KodiLib') == 'true':
                xbmc.executebuiltin('ActivateWindow(10501,plugin://plugin.video.genesis/?action=movieNavigator,return)')
            else:
                xbmc.executebuiltin('ActivateWindow(10025,videodb://1/2,return)')
        
        if id == TVSHOWS:
            if utils.getSetting('KodiLib') == 'true':
                xbmc.executebuiltin('ActivateWindow(10501,plugin://plugin.video.genesis/?action=tvNavigator,return)')
            else:
                xbmc.executebuiltin('ActivateWindow(10025,videodb://2/2,return)')
        
        if id == NETFLIX:
            xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.vpnicity/netcon.py,return)')
        
        if select and id == MOVIEANDTV:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.genesis)')
        
        if id == WORLDTV:
            xbmc.executebuiltin('XBMC.RunAddon(plugin.video.alluc.api)')
        
        if id == ANDROID:
            xbmc.executebuiltin('ActivateWindow(10025,androidapp://sources/apps,return)')
        
        if id == ADULT:
            xbmc.executebuiltin('ActivateWindow(10501,plugin://plugin.program.super.favourites/?label=Adult&mode=400&path=special://userdata/addon_data/plugin.program.super.favourites/Super Favourites/Adult/,return)')
        
        if id == VPN:
            xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.vpnicity/manual.py,return)')
        
        if id == VIDEOWINDOW:   
            xbmc.executebuiltin('Action(fullscreen)')  

        if id == KID:
            xbmcgui.Window(10000).setProperty('DSF_LIMITED', 'true')
            id = TVGUIDE

        if id == TVGUIDE:
            if xbmcgui.Window(10000).getProperty('VPNICITY_CONNECTED') == 'True':
                xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.vpnicity/netkill.py,return)')
            xbmc.executebuiltin('RunScript(script.tvguidedixie)')
        
                                 
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
        
        liz   = self.getSelectedItem()        
        index = int(liz.getProperty('Index'))
        item  = self.list[index]
        menu  = item['ContextMenu']

        replaceItems = liz.getProperty('ReplaceItems') == 'true'
        
        if not replaceItems:
            menu = list(menu + self.getSTDMenu(liz))            

        if len(menu) < 1:
            return

        import contextmenu
        self.context = True
        params       = contextmenu.showMenu(self.ADDONID, menu)
        self.context = False

        if not params:
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
        #xbmc.executebuiltin('Dialog.Show(busydialog)')
        self.busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        self.busy.show()
        progress = self.getProgress()
        if progress:
            progress.setVisible(False)        
        
        
    def closeBusy(self):    
        #xbmc.executebuiltin('Dialog.Close(busydialog)')
        if self.busy:
            self.busy.close()
            self.busy = None


    def newList(self):
        self.list = []
        self.lists.append(self.list)        


    def getSelectedItem(self):
        try:    return self.getListItem(self.getCurrentListPosition())
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
        if FRODO:
            #calling xbmcgui.WindowXML.clearList(self)
            #sometimes crashes XBMC
            #see http://trac.xbmc.org/ticket/14780
            self.showControl(MAINGROUP, False)      
            for i in range(self.getListSize(), 0, -1):            
                self.removeItem(i-1)
            self.showControl(MAINGROUP, True)
            return

        xbmcgui.WindowXML.clearList(self)  


    def getSTDMenu(self, liz):
        param = liz.getProperty('Param')

        std = []

        #if param in self.faves:
        #    std.append(('Remove from favourites', 'STD:REMOVEFAVOURITE'))
        #else:
        #    std.append(('Add to favourites',      'STD:ADDFAVOURITE'))

        std.append((GETTEXT(30001), 'STD:SETTINGS'))
        return std


    def trySTDMenu(self, params):

        if params == 'STD:SETTINGS':
            self.addonSettings()
            return

        if params == 'STD:ADDFAVOURITE':
            return self.addFavourite()

        if params == 'STD:REMOVEFAVOURITE':
            return self.removeFavourite()

        return False


    def addFavourite(self):
        liz        = self.getSelectedItem()
        name       = liz.getLabel()
        param      = liz.getProperty('Param')
        thumb      = liz.getProperty('Image')
        isPlayable = liz.getProperty('IsPlayable') == 'true'

        self.faves += param

        if isPlayable:
            param = '_Playable' + param
 
        cmd = 'RunScript(%s,%s)' % (self.ADDONID, param)

        favourites.add(name, cmd, thumb)

        return True


    def removeFavourite(self):
        liz   = self.getSelectedItem()
        param = liz.getProperty('Param')

        self.faves = self.faves.replace(param, '')

        return True


    def addonSettings(self):
        xbmcaddon.Addon(self.ADDONID).openSettings()
        #self.relaunch = True
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


    def addDir(self, name, mode, url='', image=None, isFolder=True, isPlayable=False, totalItems=0, contextMenu=[], replaceItems=False, infoLabels={}):
        if not image:
            image = ''

        if not contextMenu:
            contextMenu=[]

        if not infoLabels:
            infoLabels={}

        item = {}
        item['Name']         = name
        item['Mode']         = mode
        item['Url']          = url
        item['Image']        = image
        item['IsFolder']     = isFolder
        item['IsPlayable']   = isPlayable
        item['ContextMenu']  = contextMenu
        item['ReplaceItems'] = replaceItems
        item['InfoLabels']   = infoLabels

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
        

    def addItems(self, theList):  
        self.clearList()
        self.showControl(MAINGROUP, False)   
                        
        ignore = True
        index  = 1 #not '0' because first item in list is the params item
        
        for item in theList:
            if ignore:
                ignore = False
                continue
                
            name         = item['Name']
            mode         = item['Mode']
            url          = item['Url']
            image        = item['Image']
            isFolder     = item['IsFolder']
            isPlayable   = item['IsPlayable']
            contextMenu  = item['ContextMenu']
            replaceItems = item['ReplaceItems']
            infoLabels   = item['InfoLabels']

            liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)

            liz.setProperty('Index',        str(index))
            liz.setProperty('Mode',         str(mode))
            liz.setProperty('Param',        url)
            liz.setProperty('Image',        image)
            liz.setProperty('IsFolder',     'true'  if isFolder     else 'false')
            liz.setProperty('IsPlayable',   'true'  if isPlayable   else 'false')
            liz.setProperty('ReplaceItems', 'true'  if replaceItems else 'false')

            index += 1

            if contextMenu and (len(contextMenu) > 0):
                #doesn't seem to work for script plugins??
                #but we'll set it anyway
                liz.addContextMenuItems(contextMenu)
  
            if infoLabels and (len(infoLabels) > 0):
                liz.setInfo(type='', infoLabels=infoLabels)
                #each infolabel is set as a property, this allow user-defined infoLabels
                #that can be accessed in the skin xml via: $INFO[Window.Property(USERDEFINED)]
                for item in infoLabels:     
                    liz.setProperty(item, infoLabels[item])

            self.addItem(liz)  

        self.showControl(MAINGROUP, True)

        self.listSize = self.getListSize()

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

            
    def setResolvedUrl(self, url, success=True, listItem=None, windowed=False):
        if not success or len(url) == 0:
            return

        if not listItem:
            listItem = xbmcgui.ListItem(url)

        if self.skin == 'Thumbnails':
            windowed = False
        if self.skin == 'Thumbnails + Zoom':
            windowed = False

        type = xbmc.PLAYER_CORE_AUTO

        pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        pl.clear()
        pl.add(url, listItem)
        xbmc.Player(type).play(pl, windowed=windowed)