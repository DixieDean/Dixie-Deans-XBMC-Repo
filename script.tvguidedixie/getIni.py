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
import dixie
import urllib

ADDON       = dixie.ADDON
FTVINI      = ADDON.getSetting('ftv.ini')
datapath    = dixie.PROFILE
inipath     = os.path.join(datapath, 'ini')
current_ini = os.path.join(datapath, 'addons.ini')


def getIni():
    import extract

    if dixie.isDSF():
        return

    if not os.path.exists(inipath):
        os.makedirs(inipath)
    
    iniurl = dixie.GetExtraUrl() + 'resources/ini.zip'
    inizip = os.path.join(inipath, 'ini.zip')

    try:
        urllib.urlretrieve(iniurl, inizip)
        extract.all(inizip, inipath)
        os.remove(inizip)
    except: pass

    try:
        oldini = os.path.join(inipath, 'uktv.ini')
        if os.path.exists(oldini):
            os.remove(oldini)
        import uktv
        uktv.checkAddons()
    except: pass

    try:
        import livetv
        livetv.checkAddons()
    except: pass

    try:
        import pvr
        pvr.createPVRINI()
    except: pass

    try:
        import hdhr
        hdhr.createHDHRINI()
    except: pass

    try:
        import plugins
        plugins.checkAddons()
        plugins.getPlaylist()
    except: pass


def ftvIni():
    import xbmcaddon

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
    ftvIni()

