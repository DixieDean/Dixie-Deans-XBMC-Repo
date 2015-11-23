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


ADDON   =  utils.ADDON
HOME    =  utils.HOME
PROFILE =  utils.PROFILE


AddonID = 'script.tvguidedixie'
Addon   =  xbmcaddon.Addon(AddonID)
epghome =  Addon.getAddonInfo('path')
epgpath =  xbmc.translatePath(Addon.getAddonInfo('profile'))
extras  =  os.path.join(epgpath, 'extras')
logos   =  os.path.join(extras, 'logos')

OTTURL   = utils.getSetting('ottv.url').upper()
URL      = utils.getBaseURL(OTTURL) + '/ott-update.txt'
FIRSTRUN = utils.getSetting('FIRSTRUN') == 'true'


def checkUpdate():
    if not FIRSTRUN:
        BASEURL = utils.getBaseURL(OTTURL)
        utils.DialogOK('Welcome to On-Tapp.TV 3.0', 'We will now do a back-up of any', 'existing files before installation.')
        utils.doBackup()
        
        if OTTURL == 'OTHER':
            Addon.setSetting('dixie.url', 'Other')
            Addon.setSetting('dixie.skin', 'EPG-Skin')
            utils.setSetting('SKIN', 'OTT-Skin')
        
        utils.downloadDefaults(BASEURL)
    
    else:
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
            url     = utils.getBaseURL(OTTURL) + response['OTT Skin Link']
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
            url     = utils.getBaseURL(OTTURL) + response['EPG Skin Link']
            path    = os.path.join(extras, 'skins')
            zipfile = os.path.join(path,   'skin-update.zip')
            
            if not sfile.exists(path):
                sfile.makedirs(path)
            
            utils.downloadSkins(url, path, zipfile)
            utils.setSetting('EPGSKIN', curr)

    
        curr = logocolour
        prev = utils.getSetting('LOGOCOLOUR')

        if not prev == curr:
            url     = utils.getBaseURL(OTTURL) + response['Logo Colour']
            path    = os.path.join(logos, 'Colour Logo Pack')
            zipfile = os.path.join(path,  'logo-colour-update.zip')
            
            if not sfile.exists(path):
                sfile.makedirs(path)
            
            utils.downloadLogos(url, path, zipfile)
            utils.setSetting('LOGOCOLOUR', curr)
    

        curr = logowhite
        prev = utils.getSetting('LOGOWHITE')

        if not prev == curr:
            url     = utils.getBaseURL(OTTURL) + response['Logo White']
            path    = os.path.join(logos, 'White Logo Pack')
            zipfile = os.path.join(path,  'logo-white-update.zip')
            
            if not sfile.exists(path):
                sfile.makedirs(path)
            
            utils.downloadLogos(url, path, zipfile)
            utils.setSetting('LOGOWHITE', curr)


        curr = ottupdate
        prev = utils.getSetting('OTTUPDATE')

        if not prev == curr:
            url     = utils.getBaseURL(OTTURL) + response['OTT Update']
            path    = xbmc.translatePath(HOME)
            zipfile = os.path.join(path, 'python-update.zip')
            
            utils.doOTTUpdate(url, path, zipfile, ottupdate)
            utils.setSetting('OTTUPDATE', curr)


        curr = epgupdate
        prev = utils.getSetting('EPGUPDATE')

        if not prev == curr:
            url     = utils.getBaseURL(OTTURL) + response['EPG Update']
            path    = xbmc.translatePath(epghome)
            zipfile = os.path.join(path, 'python-update.zip')
            
            if not sfile.exists(path):
                sfile.makedirs(path)
            
            utils.doEPGUpdate(url, path, zipfile, epgupdate)
            utils.setSetting('EPGUPDATE', curr)


def getResponse():
    request  = requests.get(URL, verify=False)
    response = request.content

    utils.Log('Response in checkUpdate %s' % str(response))

    return json.loads(u"" + (response))