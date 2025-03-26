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

import xbmc
import xbmcaddon
import os

import sfile
import dixie
import settings

ADDONID  = 'script.tvguidedixie'
ADDON    =  xbmcaddon.Addon(ADDONID)

ottv     = xbmcaddon.Addon('script.on-tapp.tv')
ottdata  = xbmc.translatePath(ottv.getAddonInfo('profile'))
epgdata  = dixie.PROFILE
hotkey   = xbmc.translatePath('special://profile/keymaps/ottv_hot.xml')

settingsFile = xbmc.translatePath(os.path.join(dixie.PROFILE, 'settings.cfg'))
settingsBAK  = xbmc.translatePath(os.path.join(dixie.PROFILE, 'settings.bak'))

def deleteFiles():
    try:
        sfile.rmtree(ottdata)
        sfile.rmtree(epgdata)
        sfile.remove(hotkey)
        sfile.remove(settingsBAK)

        dixie.DialogOK('On-Tapp.TV successfully reset.', 'PLEASE QUIT AND RESTART [COLOR orange][B]On-Tapp.TV[/B][/COLOR] NOW', '')

    except Exception, e:
        error = str(e)
        dixie.log('%s :: Error resetting OTTV' % error)
        dixie.DialogOK('On-Tapp.TV failed to reset.', error, 'Please restart Kodi and try again.')

def setSettings():
    settings.set    ('ChannelsUpdated', 0, settingsFile)

    ottv.setSetting ('FIRSTRUN',  'false')
    ottv.setSetting ('V4UPGRADE', 'false')
    ottv.setSetting ('LEIAFIX',   'false')
    ottv.setSetting ('SKIN',      'Default Home Skin')


    dixie.SetSetting('epg.date',          '2000-01-01')
    dixie.SetSetting('FIRSTRUN',          'false')
    dixie.SetSetting('dixie.skin',        'Default Skin')
    dixie.SetSetting('dixie.logo.folder', 'Colour Logo Pack')

    dixie.SetSetting('username', '')
    dixie.SetSetting('password', '')

if __name__ == '__main__':
    dixie.DialogOK('IMPORTANT: IF [COLOR orange][B]On-Tapp.TV[/B][/COLOR] IS CURRENTLY OPEN.', 'QUIT AND RESTART THE ADDON AFTER THIS RESET IS COMPLETE.', '')
    deleteFiles()
    setSettings()