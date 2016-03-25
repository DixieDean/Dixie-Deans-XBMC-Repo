#
#      Copyright (C) 2015 Richard Dean
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
import xbmc
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import json
import os

import sfile
import utilsOTT as utils


ADDON   = utils.ADDON
HOME    = utils.HOME
PROFILE = utils.PROFILE

AddonID = utils.AddonID
Addon   = utils.Addon
epghome = utils.epghome
epgpath = utils.epgpath
extras  = utils.extras
logos   = utils.logos

URL      = utils.getBaseURL() + 'ott-update.txt'
FIRSTRUN = utils.getSetting('FIRSTRUN') == 'true'


def checkUpdate():
    if utils.isDSF():
        import dsf
        try:    dsf.checkUpdate()
        except: pass
        return
    
    if not FIRSTRUN:
        BASEURL = utils.getBaseURL()
        utils.doBackup()
        utils.downloadDefaults(BASEURL)
        return

    response   = getResponse()
    ottskin    = response['OTTSkin']
    epgskin    = response['EPGSkin']
    logocolour = response['LogoColour']
    logowhite  = response['LogoWhite']
    ottupdate  = response['OTTUpdate']
    epgupdate  = response['EPGUpdate']


    curr = ottskin
    prev = utils.getSetting('OTTSKIN')

    if not prev == curr:
        url     = utils.getBaseURL() + response['OTT Skin Link']
        path    = xbmc.translatePath(PROFILE) 
        path    = os.path.join(path, 'skins')
        zipfile = os.path.join(path, 'skin-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        utils.downloadSkins(url, path, zipfile)
        utils.setSetting('OTTSKIN', curr)


    curr = epgskin
    prev = utils.getSetting('EPGSKIN')

    if not prev == curr:
        url     = utils.getBaseURL() + response['EPG Skin Link']
        path    = os.path.join(extras, 'skins')
        zipfile = os.path.join(path,   'skin-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        utils.downloadSkins(url, path, zipfile)
        utils.setSetting('EPGSKIN', curr)


    curr = logocolour
    prev = utils.getSetting('LOGOCOLOUR')

    if not prev == curr:
        url     = utils.getBaseURL() + response['Logo Colour']
        path    = os.path.join(logos, 'Colour Logo Pack')
        zipfile = os.path.join(path,  'logo-colour-update.zip')

        if not sfile.exists(path):
            sfile.makedirs(path)

        utils.downloadLogos(url, path, zipfile)
        utils.setSetting('LOGOCOLOUR', curr)


    curr = logowhite
    prev = utils.getSetting('LOGOWHITE')

    if not prev == curr:
        url     = utils.getBaseURL() + response['Logo White']
        path    = os.path.join(logos, 'White Logo Pack')
        zipfile = os.path.join(path,  'logo-white-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        utils.downloadLogos(url, path, zipfile)
        utils.setSetting('LOGOWHITE', curr)


    curr = ottupdate
    prev = utils.getSetting('OTTUPDATE')

    if not prev == curr:
        url     = utils.getBaseURL() + response['OTT Update']
        path    = xbmc.translatePath(HOME)
        zipfile = os.path.join(path, 'python-update.zip')
        
        utils.doOTTUpdate(url, path, zipfile, ottupdate)
        utils.setSetting('OTTUPDATE', curr)


    curr = epgupdate
    prev = utils.getSetting('EPGUPDATE')

    if not prev == curr:
        url     = utils.getBaseURL() + response['EPG Update']
        path    = xbmc.translatePath(epghome)
        zipfile = os.path.join(path, 'python-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        utils.doEPGUpdate(url, path, zipfile, epgupdate)
        utils.setSetting('EPGUPDATE', curr)
    return


def getResponse():
    request  = requests.get(URL, verify=False)
    response = request.content

    utils.Log('Response in checkUpdate %s' % str(response))

    return json.loads(u"" + (response))