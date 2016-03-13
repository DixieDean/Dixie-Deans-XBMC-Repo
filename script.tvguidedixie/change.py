#
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

import xbmcgui
import xbmcaddon
import sys
import datetime

import dixie

from sqlite3        import dbapi2 as sqlite3
from osd import OSD


def action(key):
    dixie.log('Key pressed %s' % key)

    if not key in ['SELECT', 'PGUP', 'PGDOWN', 'UP', 'DOWN', 'LEFT', 'RIGHT', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'G']:
        dixie.log('Input not recognised')
        return

    xbmcgui.Window(10000).setProperty('OTT_CHANGE_SCRIPT', 'TRUE')

    if key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        channel = OSD(key)
        channel.doModal()
        del channel
        return


    if key == 'LEFT':
        channel = OSD('PREV')
        channel.doModal()
        del channel
        return

    if key in ['RIGHT', 'G']:
        channel = OSD()
        channel.doModal()
        del channel
        return

    if key == 'SELECT':
        channel = OSD()
        channel.doModal()
        del channel
        return

    channel = OSD()
    channel.doModal()
    del channel
    return


if xbmcgui.Window(10000).getProperty('OTT_CHANGE_SCRIPT') == 'TRUE':
    dixie.log('Change script already running')    
else:
    try:
        action(sys.argv[1].upper())
    except Exception, e:
        dixie.log('Error in change script %s' % str(e))    

xbmcgui.Window(10000).clearProperty('OTT_CHANGE_SCRIPT')