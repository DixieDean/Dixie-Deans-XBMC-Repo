#
#      Copyright (C) 2016 On-Tapp-Networks Limited
#

import xbmc
import xbmcaddon
import dixie

ottv = xbmcaddon.Addon('script.on-tapp.tv')

def getVersion():
    OTTV  = ottv.getAddonInfo('version')
    OTEPG = dixie.ADDON.getAddonInfo('version')

    dixie.DialogOK('You are currently running the following versions', 'On-Tapp.TV: ' + '[COLOR orange][B]' + OTTV + '[/B][/COLOR]', 'On-Tapp.EPG: ' + '[COLOR orange][B]' + OTEPG + '[/B][/COLOR]')

    if dixie.DialogYesNo('Would you like to force Kodi to check', 'for any updates right now?', ''):
        xbmc.executebuiltin('UpdateAddonRepos')


if __name__ == '__main__':
    getVersion()
