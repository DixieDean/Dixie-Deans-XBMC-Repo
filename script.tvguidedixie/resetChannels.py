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


def resetChannels():
    from channel import GetChannelFromFile
    path = dixie.GetChannelFolder()
    src  = os.path.join(path, 'channels')

    if dixie.isDSF():
        return resetAllChannels(src)

    toDelete = []

    current, dirs, files = sfile.walk(src)
    for file in files:
        filename = os.path.join(src, file)
        toDelete.append(file)

    if len(toDelete) == 0:
        return

    channels = []
    titles   = ['[B][I]Reset ALL Channels[/I][/B]']

    for file in toDelete:
        channel = GetChannelFromFile(os.path.join(src, file))
        if channel:
            channels.append(channel)
            titles.append(channel.title)

    # dixie.log(channels)
    # dixie.log(titles)

    import xbmcgui

    selections = xbmcgui.Dialog().multiselect('Please select the channels you would like to reset', titles)

    if not selections:
        selections = []

    resetAll = 0 in selections
    if resetAll:
        return resetAllChannels(src)

    for idx, channel in enumerate(channels):
        nostreams = channel.streamUrl
        if idx+1 in selections: # +1 to account for 'All Channels' item
            nostreams = ''

        channel.streamUrl = nostreams
        channel.writeToFile(os.path.join(src, toDelete[idx]))

    d = xbmcgui.Dialog()
    d.ok('On-Tapp.TV', 'Your selected channels have been successfully reset.', 'They will be re-created next time', 'you start the guide')


def resetAllChannels(src):
    dixie.log('======= resetAllChannels =======')
    if os.path.exists(src):
        xbmc.executebuiltin('Dialog.Show(busydialog)')

        path = dixie.GetChannelFolder()
        cats = os.path.join(path, 'catfile')

        sfile.rmtree(src)
        sfile.remove(cats)

        import download
        import extract
        src = 'https://raw.githubusercontent.com/DixieDean/Dixie-Deans-XBMC-Repo/master/files/lineups/default/Default Line-up.zip'
        dst =  os.path.join(dixie.datapath, 'zipfile.zip')
        dp  =  dixie.Progress('Resetting All Channels.', 'Please Wait.')

        download.download(src, dst, dp)
        extract.all(dst, path)
        sfile.remove(dst)

        xbmc.executebuiltin('Dialog.Close(busydialog)')

        d = xbmcgui.Dialog()
        d.ok('On-Tapp.TV', 'All channels successfully reset.', 'They will be re-created next time', 'you start the guide')


if __name__ == '__main__':
    resetChannels()
