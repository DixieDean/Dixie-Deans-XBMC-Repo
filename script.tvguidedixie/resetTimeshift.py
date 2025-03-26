#
#      Copyright (C) 2017 On-Tapp-Networks Limited
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


def resetTimeshift():
    if dixie.isDSF():
        return # resetAllChannels()

    from channel import GetChannelFromFile
    path = dixie.GetChannelFolder()
    src  = os.path.join(path, 'channels')

    toReset = []

    current, dirs, files = sfile.walk(src)
    for file in files:
        filename = os.path.join(src, file)
        toReset.append(file)

    if len(toReset) == 0:
        return

    channels = []
    # shifted  = []
    titles   = []

    for file in toReset:
        channel = GetChannelFromFile(os.path.join(src, file))
        offset  = channel.offset
        if channel:
            channels.append(channel)
            titles.append(channel.title + ' [COLOR orange]' + str(offset) + ' minutes[/COLOR]')

    # dixie.log(channels)
    # dixie.log(titles)

    import xbmcgui

    selections = xbmcgui.Dialog().multiselect('Please select the channels you would like to reset', titles)

    if not selections:
        selections = []

    resetAll = 0 in selections

    for idx, channel in enumerate(channels):
        
        notimeshift = channel.offset
        if idx in selections: # +1 to account for 'All Channels' item
            notimeshift = '0'

        channel.offset = notimeshift
        channel.writeToFile(os.path.join(src, toReset[idx]))

    d = xbmcgui.Dialog()
    d.ok('On-Tapp.TV', 'Your selected timeshifts have been reset.', 'They will be re-created next time', 'you start the guide')


if __name__ == '__main__':
    resetTimeshift()
