
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
import xbmcaddon
import xbmcgui

import utilsOTT as utils


ADDON = utils.ADDON


if ADDON.getSetting('autoStart') == "true":
    try:
        #workaround Python bug in strptime which causes it to intermittently throws an AttributeError
        import datetime, time
        datetime.datetime.fromtimestamp(time.mktime(time.strptime('2013-01-01 19:30:00'.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
    except:
        pass
    xbmc.executebuiltin('RunScript(%s)' % utils.ADDONID)


#------------------------------------------------------------------------


class MyMonitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)

        self.settings = {}
        self.settings['SKIN'] = ''        

        self._onSettingsChanged(init=True)


    def onSettingsChanged(self):
        self._onSettingsChanged()


    def _onSettingsChanged(self, init=False):
        relaunch = False

        for key in self.settings:
            value = utils.getSetting(key)
            if value <> self.settings[key]:
                relaunch           = True
                self.settings[key] = value

        if init:
            return

        if relaunch:
            utils.Log('Settings changed - relaunching')
            self.relaunch()

    def relaunch(self):
        xbmcgui.Window(10000).setProperty('OTT_RELAUNCH', 'true')
        
#------------------------------------------------------------------------


monitor = MyMonitor()

while (not xbmc.abortRequested):
    xbmc.sleep(1000)   

del monitor
