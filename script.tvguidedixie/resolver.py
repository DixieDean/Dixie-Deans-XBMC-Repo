import urllib
import xbmc
import xbmcaddon

PREFIXES = ['VDRTV', 'ANOVA', 'VIPSS', 'LIM2', 'NATH', 'NICE', 'SHUB', 'PREM', 'GIZ', 'GSPRTS', 'GEH', 'TVK', 'MTXIE', 'XTC', 'SCTV', 'SUP', 'UKT', 'LIMIT', 'FAB', 'ACE', 'HORIZ', 'ROOT2', 'FREE', 'MEGA', 'IPTS', 'JINX2', 'ROOT', 'IPLAY', 'MAXI', 'END', 'SPRM', 'MCKTV', 'TWIST', 'PREST', 'MATS', 'BLKI']

import dixie

def resolve(url, recording=False):
    # dixie.log('==== RESOLVER INITIAL URL ====')
    # dixie.log(url)

    if not url:
        return  None, None

    if url.startswith('http:'):
        # dixie.log('==== PLAYLIST URL ====')
        # dixie.log(url)
        stream = url
        if recording:
            stream = '?url=' + urllib.quote_plus(url)
            # dixie.log('==== PLAYLIST RECORD URL ====')
            # dixie.log(url)
        play = True
        return stream, play

    for prefix in PREFIXES:
        if url.startswith(prefix):
            import linkloader
            stream = linkloader.getURL(url)
            if (prefix == 'VDRTV') or (prefix == 'SUP'):
                if recording:
                    stream = '?url=' + urllib.quote_plus(stream)
            play = 'IPLAYD' not in url
            return stream, play

    stream = None
    play   = None

    if url.startswith('HDTV'):
        import smh
        stream = smh.getURL(url)
        play   = True

    if url.startswith('LIVETV'):
        import livetv
        stream = livetv.getLIVETV(url)
        play   = True

    if url.startswith('FLA'):
        ADDONID = 'plugin.video.FlawlessTv'
        ADDON   =  xbmcaddon.Addon(ADDONID)

        path    =  ADDON.getAddonInfo('path')

        import sys
        sys.path.insert(0, path)

        import iptv2
        url    = url.split(':', 1)[-1]


        url = url.replace('BBC 1',   'BBC ONE')
        url = url.replace('BBC One', 'BBC ONE')
        url = url.replace('BBC 2',   'BBC TWO')
        url = url.replace('BBC Two', 'BBC TWO')

        stream = iptv2.GetStreamURLByChannelID(url)
        if recording:
            stream = '?url=' + stream
        play = True

    return stream, play