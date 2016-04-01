#
#      Copyright (C) 2014 Sean Poyser
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


import xbmcaddon
import notification
import xbmc
import os
import source
import dixie


ADDON = dixie.ADDON
ID    = dixie.ADDONID


datapath   = dixie.PROFILE
cookiepath = os.path.join(datapath,   'cookies')
cookiefile = os.path.join(cookiepath, 'cookie')


class Service(object):
    def __init__(self):
        self.database = source.Database(self)
        self.database.initializeS(self.onInitS)
        


    def onInitS(self, success):
        if success:
            self.database.initializeP(self.onInitP)
        else:
            self.database.close()


    def onInitP(self, success):
        if success:
            self.database.updateChannelAndProgramListCaches(self.onCachesUpdated)
        else:
            self.database.close()


    def onCachesUpdated(self):
        if ADDON.getSetting('notifications.enabled') == 'true':
            n = notification.Notification(self.database, ADDON.getAddonInfo('path'))
            n.scheduleNotifications()
        self.database.close(None)



class MyMonitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)


    def onSettingsChanged(self):
        self.tidySettings()


    def tidySettings(self):
        files = []
        for i in range(10):
            enabled = dixie.GetSetting('INI_%d_E' % i) == 'true'
            if enabled:
                file = dixie.GetSetting('INI_%d' % i)
                files.append(file)

        print files
        
        index = 0

        for file in files:
            if len(file) > 0:
                dixie.SetSetting('INI_%d'   % index, file)
                dixie.SetSetting('INI_%d_E' % index, 'true')
                index += 1

        for i in range(index, 10):
            dixie.SetSetting('INI_%d'   % i, '')
            dixie.SetSetting('INI_%d_E' % index, 'false')


######################################################################
#Functionality

dixie.removeKepmap()
dixie.patchSkins()

if not os.path.exists(cookiepath):
    os.makedirs(cookiepath)

cmd = 'XBMC.RunScript(special://home/addons/script.tvguidedixie/getIni.py)'
xbmc.executebuiltin(cmd)


#legacy tidying up
dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'zOTT.xml')
if os.path.exists(dst):
   os.remove(dst)
   xbmc.sleep(1000)
   xbmc.executebuiltin('Action(reloadkeymaps)')


import update
update.checkForUpdate(silent = True)


if ADDON.getSetting('autoStart') == "true":
    try:
        #workaround Python bug in strptime which causes it to intermittently throws an AttributeError
        import datetime, time
        datetime.datetime.fromtimestamp(time.mktime(time.strptime('2013-01-01 19:30:00'.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
    except:
        pass
    xbmc.executebuiltin('RunScript(%s)' % ID)


monitor = MyMonitor()
monitor.tidySettings()
while (not xbmc.abortRequested):
    xbmc.sleep(1000)