
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

ADDONID = 'script.tvguidedixie'

def add(params):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % ADDONID) == 1:
        return 'On-Tapp.TV Mini-Guide'
    
    return None


def process(option, params):
    import xbmcaddon
    import os

    addon = xbmcaddon.Addon(ADDONID)
    path  = addon.getAddonInfo('path')

    script = os.path.join(path, 'osd.py')
    cmd    = 'RunScript(%s)' % script

    xbmc.executebuiltin(cmd)