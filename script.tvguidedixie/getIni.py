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

import download
import extract

ADDON    = dixie.ADDON
FTVINI   = ADDON.getSetting('ftv.ini')
datapath = dixie.PROFILE
inipath  = os.path.join(datapath, 'ini')


def getIni():
    #dixie.log('====== CF getIni.py ======')
    if dixie.isDSF():
        return

    if not os.path.exists(inipath):
        os.makedirs(inipath)

    iniurl = dixie.GetExtraUrl() + 'resources/ini.zip'
    inizip = os.path.join(inipath, 'ini.zip')

    try:
        download.download(iniurl, inizip)
        extract.all(inizip, inipath)
        os.remove(inizip)
    except: pass

###################################################################

    cacheFiles = ['anovatemp', 'vipsstemp', 'lim2temp', 'nathotemp', 'nicetemp', 'shubtamp', 'premtemp', 'giztemp', 'gsprtstemp', 'getemp', 'mtxtemp', 'tvktemp', 'mtxtemp', 'tvktemp', 'xtemp', 'ro2temp', 'megatmp', 'freetmp', 'dtemp', 'ftemp', 'maxtemp', 'etemp', 'shtemp', 'rutemp', 'rotemp', 'j2temp', 'iptstmp', 'vdtemp', 'sprtemp', 'mcktemp', 'twitemp', 'prestemp', 'matstmp', 'blkitemp', 'hortemp', 'acetemp', 'fabtemp', 'limitemp', 'ukttemp', 'suptemp', 'sctemp']

    for cacheFile in cacheFiles:
        path = os.path.join(datapath, cacheFile)
        if os.path.exists(path):
            os.remove(path)

    # try:
    #     import playini
    #     playini.checkAddons()
    # except: pass

    try:
        import iptvini
        iptvini.checkAddons()
    except: pass

    try:
        import iplayer
        iplayer.checkAddons()
    except: pass

    try:
        import smh
        smh.checkAddons()
    except: pass

    try:
        import hdtv
        hdtv.checkAddons()
    except: pass

    try:
        import uktv
        uktv.checkAddons()
    except: pass

    try:
        import livetv
        livetv.checkAddons()
    except: pass

    try:
        import plugins
        plugins.checkAddons()
    except: pass

    try:
        import pvr
        pvr.createPVRINI()
    except: pass

    try:
        import hdhr
        hdhr.createHDHRINI()
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
        download.download(url, path)
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


def checkRuya():
    import xbmcaddon
    import dixie

    datapath =  dixie.PROFILE
    inipath  =  os.path.join(datapath, 'ini')
    RUYA     = 'plugin.video.ruyaiptv'


    if xbmc.getCondVisibility('System.HasAddon(%s)' % RUYA) == 1:
        try:
            if xbmcaddon.Addon('plugin.video.ruyaiptv').getAddonInfo('name') == 'IPTV Subs':
                files = ['ruyaiptv.ini', 'ruyaiptv-sw.ini']

            else:
                files = ['iptvsubs.ini']

                for file in files:
                    path = os.path.join(inipath, file)
                    if os.path.exists(path):
                        os.remove(path)
        except: pass

    files2 = ['smarthub-sw.ini']

    for file in files2:
        path = os.path.join(inipath, file)
        if os.path.exists(path):
            os.remove(path)


def setAlarm(url):
    #set script to run again in x minutes
    name   = dixie.TITLE + ' INI Files Update'
    script = os.path.join(dixie.HOME, 'getIni.py')
    args   = url
    cmd    = 'AlarmClock(%s, RunScript(%s, %s), %d, True)' % (name, script, args, INTERVAL)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)
    xbmc.executebuiltin(cmd)


def setTimeToNow(setting):
    now = datetime.datetime.today()
    dixie.SetSetting(setting, str(now))



if __name__ == '__main__':
    getIni()
    # ftvIni()
    # checkRuya()
