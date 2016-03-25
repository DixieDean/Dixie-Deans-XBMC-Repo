# -*- coding: utf-8 -*-
#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com) - With acknowledgement to some original code by twinther (Tommy Winther)

import xbmc
import xbmcaddon
import xbmcgui
import os
import dixie

ADDON = xbmcaddon.Addon(id = 'script.tvguidedixie')
HOME  = ADDON.getAddonInfo('path')
ICON  = os.path.join(HOME, 'icon.png')
ICON  = xbmc.translatePath(ICON)


def CheckIdle(maxIdle):
    if maxIdle == 0:
        return
    
    idle = xbmc.getGlobalIdleTime()
    if idle < maxIdle:
        return

    delay = 60
    count = delay
    dp = xbmcgui.DialogProgress()
    dp.create("OnTappTV","Streaming will automatically quit in %d seconds" % count, "Press Cancel to contine viewing")
    dp.update(0)
              
    while xbmc.Player().isPlaying() and count > 0 and not dp.iscanceled():
        xbmc.sleep(1000)
        count -= 1
        perc = int(((delay - count) / float(delay)) * 100)
        if count > 1:
            dp.update(perc,"Streaming will automatically quit in %d seconds" % count, "Press Cancel to contine viewing")
        else:
            dp.update(perc,"Streaming will automatically quit in %d second" % count, "Press Cancel to contine viewing")

    if not dp.iscanceled():
        xbmc.Player().stop()


def get_params(p):
    param=[]
    paramstring=p
    if len(paramstring)>=2:
        params=p
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
           params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param


def playDSF(url, windowed):
    try:
        import urllib
        channel = urllib.quote_plus(url.split(':', 1)[-1])
        url = 'plugin://%s/?channel=%s' % (dixie.DSFID, channel)
        dixie.log('++++++++++++++++++++ playDSF ++++++++++++++++++++')
        dixie.log(url)
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        playlist.add(url, xbmcgui.ListItem(''))
        xbmc.Player().play(playlist, windowed=windowed)
    except:
        return False


def playSF(url):
    launchID = '10025'
    if xbmcgui.Window(10000).getProperty('OTT_LAUNCH_ID') == launchID:
        url = url.replace('ActivateWindow(%s' % launchID, 'ActivateWindow(10501')
        launchID = '10501'

    try:
        if url.startswith('__SF__'):
            url = url.replace('__SF__', '')

        if url.lower().startswith('playmedia'):
            xbmc.executebuiltin(url)
            return True, ''

        if url.lower().startswith('runscript'):
            xbmc.executebuiltin(url)
            return True, ''


        if url.lower().startswith('activatewindow'):
            import sys
            sfAddon = xbmcaddon.Addon(id = 'plugin.program.super.favourites')
            sfPath  = sfAddon.getAddonInfo('path')
            sys.path.insert(0, sfPath)

            import favourite
            import re
            import urllib

            original = re.compile('"(.+?)"').search(url).group(1)

            original = original.replace('%26', 'SF_AMP_SF') #protect '&' within parameters

            cmd = urllib.unquote_plus(original)

            try:    noFanart = favourite.removeFanart(cmd)
            except: pass

            try:    noFanart = favourite.removeSFOptions(cmd)
            except: pass

            if noFanart.endswith(os.path.sep):
               noFanart = noFanart[:-1]

            noFanart = noFanart.replace('+', '%2B')
            noFanart = noFanart.replace(' ', '+')

            url = url.replace(original, noFanart)
            url = url.replace('SF_AMP_SF', '%26') #put '&' back

            xbmc.executebuiltin(url)
            return True, ''

        import urllib
        params = url.split('?', 1)[-1]
        params = get_params(params)

        try:    mode = int(urllib.unquote_plus(params['mode']))
        except: return False, url

        if mode != 400:
            return False, url
        
        try:    path = urllib.unquote_plus(params['path'])
        except: path = None

        dirs = []
        if path:
            try:    current, dirs, files = os.walk(path).next()
            except: pass
            
            if len(dirs) == 0:
                import sys

                path = os.path.join(path, 'favourites.xml')

                sfAddon = xbmcaddon.Addon(id = 'plugin.program.super.favourites')
                sfPath  = sfAddon.getAddonInfo('path')

                sys.path.insert(0, sfPath)

                import favourite
                faves = favourite.getFavourites(path)

                if len(faves) == 1:
                    fave = faves[0][2]
                    if fave.lower().startswith('playmedia'):
                        import re
                        cmd = re.compile('"(.+?)"').search(fave).group(1)
                        return False, cmd

    except Exception, e:
        print str(e)
        pass

    url = 'ActivateWindow(%s,%s)' % (launchID, url)
    xbmc.executebuiltin(url)
    return True, ''


def play(url, windowed, name=None):
    dixie.SetSetting('streamURL', url)
    handled = False
    
    getIdle = int(ADDON.getSetting('idle').replace('Never', '0'))
    maxIdle = getIdle * 60 * 60

    dixie.loadKepmap()
    
    if url.startswith('HDTV'):
        import hdtv
        delay  = 5
        stream = hdtv.getURL(url)

        if not playAndWait(stream, windowed, maxIdle, delay=delay):
            dixie.SetSetting('LOGIN_HDTV', '2001-01-01 00:00:00')
            stream = hdtv.getURL(url)
            playAndWait(stream, windowed, maxIdle, delay=delay)
        return

    if url.startswith('IPLAYD'):
        import iplayer
        stream = iplayer.getURL(url)
        dixie.log(stream)
        xbmc.executebuiltin('XBMC.RunPlugin(%s)' % stream)
        return

    if url.startswith('IPLAY'):
        import iplayer
        stream = iplayer.getURL(url)
        playAndWait(stream, windowed, maxIdle)
        return

    if url.startswith('LIVETV'):
        import livetv
        stream = livetv.getLIVETV(url)
        dixie.log(stream)
        playAndWait(stream, windowed, maxIdle)
        return

    if url.startswith('IPTV'):
        import iptv
        url = iptv.getURL(url)
        dixie.log(url)
        xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
        return

    if url.isdigit():
        command = ('{"jsonrpc": "2.0", "id":"1", "method": "Player.Open","params":{"item":{"channelid":%s}}}' % url)
        xbmc.executeJSONRPC(command)
        return
    
    if (url.startswith('__SF__')) or ('plugin://plugin.program.super.favourites' in url.lower()):
        handled, url = playSF(url)
        if handled:
            return

    if url.lower().startswith('dsf'):
        if playDSF(url, windowed):
            wait(maxIdle)
        return

    # if url.lower().startswith('upnp:'):
    #     playAndWait(url, windowed, maxIdle)
    #     return

    if not checkForAlternateStreaming(url):
        playAndWait(url, windowed, maxIdle)

        xbmc.sleep(3000)
        if not xbmc.Player().isPlaying():
            xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
            wait(maxIdle)

def playAndWait(url, windowed, maxIdle, delay=0):
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    playlist.add(url, xbmcgui.ListItem(''))
    try:
        xbmc.Player().play(playlist, windowed=windowed)
    except: pass

    if delay == 0:
        wait(maxIdle)
        return True

    delay *= 4
    while (delay >= 0) and (not xbmc.Player().isPlaying()):
        delay -= 1
        xbmc.sleep(250)

    if not xbmc.Player().isPlaying():
        return False
    
    wait(maxIdle)
    return True


def wait(maxIdle):
    while xbmc.Player().isPlaying():
        xbmc.sleep(1000)
        CheckIdle(maxIdle)


def checkForAlternateStreaming(url):
    if 'plugin.video.expattv' in url:
        return alternateStream(url)

    if 'plugin.video.filmon' in url:
        return alternateStream(url)

    if 'plugin.video.notfilmon' in url:
        return alternateStream(url)

    if 'plugin.video.iplayerwww' in url:
        return alternateStream(url)

    if 'plugin.video.SportsDonkey' in url:        
        return alternateStream(url)

    if 'plugin.audio.ramfm' in url:        
        return alternateStream(url)

    if 'plugin.video.movie25' in url:
        return alternateStream(url)

    if 'plugin.video.irishtv' in url:
        return alternateStream(url)

    if 'plugin.video.F.T.V' in url:        
        return alternateStream(url)

    if 'plugin.video.sportsaholic' in url:        
        return alternateStream(url)

    if 'plugin.video.navi-x' in url:        
        return alternateStream(url)

    if 'plugin.video.mxnews' in url:        
        return alternateStream(url)

    if 'plugin.program.skygo.launcher' in url:        
        return alternateStream(url)

    if 'plugin.program.advanced.launcher' in url:        
        return alternateStream(url)

    if 'plugin.video.iplayer' in url:        
        return alternateStream(url)

    if 'plugin.video.stalker' in url:
        return alternateStream(url)

    if 'plugin.video.dex' in url:
        return alternateStream(url)

    return False

def alternateStream(url):
    xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
    print '***** ottv alternateStream *****', url
    
    retries = 10
    while retries > 0 and not xbmc.Player().isPlaying():
        retries -= 1
        xbmc.sleep(1000)
        
    return True



if __name__ == '__main__': 
    name = None
    if len(sys.argv) > 3:
        name = sys.argv[3]
    
    play(sys.argv[1], sys.argv[2] == 1, name)
