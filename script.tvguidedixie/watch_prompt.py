#
#      Copyright (C) On-Tapp-Networks Limited 2017-
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
import os
import urllib
import re

import dixie
import sfile
import streaming

from channel import Channel
from source import Program
from info import InfoService

ADDON = dixie.ADDON

OTT_CHANNELS = os.path.join(dixie.GetChannelFolder(), 'channels')
IGNORESTRM   = dixie.GetSetting('ignore.stream') == 'true'
OPEN_OTT     = dixie.OPEN_OTT
CLOSE_OTT    = dixie.CLOSE_OTT

DSF = dixie.isDSF()

program  = sys.argv[1]
filename = sys.argv[2]
text     = sys.argv[3]


def showDialog():
    PROGRAM  = '[COLOR orange][B]' + program + '[/B][/COLOR]'

    line1    =  PROGRAM + ' ' + text
    line2    = 'Would you like to watch it?'
    noLabel  = 'Ignore'
    yesLabel = 'Watch'

    if not dixie.DialogYesNo(line1, line2, noLabel=noLabel, yesLabel=yesLabel):
        return
    playChannel(filename)


def playChannel(filename):
    channel = getChannelFromFile(filename)
    if not channel:
        return

    if DSF:
        streamUrl = 'DSF:%s' % channel.id
    else:
        streamUrl = channel.streamUrl

    if not streamUrl:
        streamUrl = detectStream(channel)

    if streamUrl:
        if not DSF:
            import plugins
            streamUrl = plugins.selectStream(channel.streamUrl, channel.title)

            while streamUrl == 'addMore':
                result = streaming.StreamsService().detectStream(channel)

                import detect
                d = detect.StreamAddonDialog(result)
                d.doModal()

                if d.stream is not None:
                    setCustomStreamUrl(channel, d.stream, d.label)

                if DSF:
                    streamUrl = 'DSF:%s' % channel.id
                else:
                    streamUrl = channel.streamUrl

                streamUrl = plugins.selectStream(channel.streamUrl, channel.title)

    if not streamUrl:
        return

    path = os.path.join(dixie.HOME, 'player.py')
    xbmc.executebuiltin('XBMC.RunScript(%s,%s,%d)' % (path, streamUrl, False))


def detectStream(channel):
    result = streaming.StreamsService().detectStream(channel)

    if type(result) == str:
        setCustomStreamUrl(channel, result)
        return result

    if len(result) < 1:
        dixie.DialogOK('Sorry, we could not detect a stream.', '', 'Please allocate a stream for this channel.')
        return None

    import detect

    d = detect.StreamAddonDialog(result)
    d.doModal()

    if not d.stream:
        return None

    setCustomStreamUrl(channel, d.stream, d.label)
    return d.stream


def removeCleanChannel(id):
    path = os.path.join(OTT_CHANNELS, id)
    if sfile.exists(path):
        try:    sfile.remove(path)
        except: pass


def addCleanChannel(channel, id):
    path = os.path.join(OTT_CHANNELS, id) 

    if not sfile.exists(path): 
        channel.writeToFile(path)


def setCustomStreamUrl(channel, stream_url, label=''):
    id = CleanFilename(channel.id)


    if len(channel.streamUrl) > 0:
        newStream = channel.streamUrl + '|' + OPEN_OTT + label + CLOSE_OTT + stream_url

    else:
        newStream = OPEN_OTT + label + CLOSE_OTT + stream_url
        newStream = newStream .replace(OPEN_OTT + CLOSE_OTT, '')

    channel.streamUrl = newStream

    removeCleanChannel(id)
    addCleanChannel(channel, id)


def CleanFilename(text):
    text = text.replace('*', '_star')
    text = text.replace('+', '_plus')
    text = text.replace(' ', '_')

    text = re.sub('[:\\/?\<>|"]', '', text)
    text = text.strip()
    try:    text = text.encode('ascii', 'ignore')
    except: text = text.decode('utf-8').encode('ascii', 'ignore')

    return text


def getChannelFromFile(id):
    path = os.path.join(OTT_CHANNELS, id)

    if not sfile.exists(path):
        return None

    cfg = sfile.readlines(path)

    return Channel(cfg)


if __name__ == '__main__':
    showDialog()
