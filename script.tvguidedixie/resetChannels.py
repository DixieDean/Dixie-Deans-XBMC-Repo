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
import xbmcgui
import xbmcaddon
import os
import sfile

import dixie


def resetChannels():
    path = dixie.GetChannelFolder()
    chan = os.path.join(path, 'channels')

    if sfile.exists(chan):
        xbmc.executebuiltin('Dialog.Show(busydialog)')

        sfile.rmtree(chan)

        xbmc.executebuiltin('Dialog.Close(busydialog)')

        d = xbmcgui.Dialog()
        d.ok('On-Tapp.TV', 'On-Tapp.TV Channels successfully reset.', 'They will be re-created next time', 'you start the guide')

    else:
        pass


if __name__ == '__main__':
    resetChannels()
