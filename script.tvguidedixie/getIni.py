#
#      Copyright (C) 2014 Richard Dean
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

import os
import xbmc
import xbmcgui
import xbmcaddon
import urllib

import dixie

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
FTVINI      = ADDON.getSetting('ftv.ini')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
current_ini = os.path.join(datapath, 'addons.ini')

def getIni():
    path = current_ini
    try:
        url = dixie.GetExtraUrl() + 'resources/addons.ini'
        urllib.urlretrieve(url, path)
    except:
        pass

def ftvIni():
    if FTVINI == 'UK Links':
        ftv = 'uk.ini'
    else:
        ftv = 'nongeo.ini'

    path = os.path.join(datapath, ftv)

    try:
        url = dixie.GetExtraUrl() + 'resources/' + ftv
        urllib.urlretrieve(url, path)
    except:
        pass
    
    AVAILABLE = False
    if not AVAILABLE:
        try:
            addon = xbmcaddon.Addon('plugin.video.F.T.V')
            if FTVINI == 'Non-Geolocked UK Links':
                BASE      = addon.setSetting('root_channel', '3092')
                AVAILABLE = BASE
            else:
                BASE      = addon.setSetting('root_channel', '689')
                AVAILABLE = BASE
        except:
            AVAILABLE = False

    

if __name__ == '__main__':
    getIni()
    d = xbmcgui.Dialog()
    d.ok('TV Guide Dixie', 'Built-in Addon links updated.', 'Always manually update your channel links', 'via "Choose Stream" if they are not working.')
    ftvIni()

