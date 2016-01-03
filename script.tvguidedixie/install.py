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

filename  = 'OTTV Mini-Guide.py'

sfaves = xbmcaddon.Addon('plugin.program.super.favourites')
path   = sfaves.getAddonInfo('profile')
file   = os.path.join(path, 'Plugins', filename)


def miniGuide():
        try:
            install_file(filename)
        
            passed = (sfile.exists(file))
        
            if passed: 
                dixie.log('Installing Mini-Guide Plugin...PASSED')
            else:
                dixie.log('Installing Mini-Guide Plugin...FAILED')
        
            dixie.SetSetting('MINIGUIDE', 'true')
        
            return passed
        
        except Exception, e:
            dixie.log('Installing Mini-Guide Plugin...EXCEPTION %s' % str(e))
        
        return False


def install_file(filename):
    ottv = dixie.HOME
    src  = os.path.join(ottv, 'resources', filename)
    
    if not os.path.exists(path):
        sfile.makedirs(path)
        sfile.copy(src, file)


if __name__ == '__main__':
    xbmc.executebuiltin('Dialog.Show(busydialog)')
    
    if miniGuide():
        xbmc.executebuiltin('Dialog.Close(busydialog)')
        
        if dixie.DialogYesNo('Would you like to assign a button ', 'on your remote control or keybord', 'to activate the On-Tapp.TV Mini-Guide?'):
            xbmc.executebuiltin('RunScript(special://home/addons/script.tvguidedixie/keyProgrammer.py)')
        
    else:
        xbmc.executebuiltin('Dialog.Close(busydialog)')
        dixie.DialogOK('On-Tapp.TV Mini-Guide failed to install.', 'Ensure you have Super Favourites installed.', 'Thank you.')