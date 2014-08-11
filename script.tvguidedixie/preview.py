#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
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

def play(url, windowed):
    if checkForAlternateStreaming(url):
        return

    xbmc.Player().play(item = url, windowed = windowed)
    print '****** Attempt 1 ******'
    print url
    xbmc.sleep(100)
    if not xbmc.Player().isPlaying():
        xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
        print '****** Attempt 2 ******'
        print url

def checkForAlternateStreaming(url):
    if "plugin.video.ntv" in url:
        print '****** Alternate NTV ******'
        print url
        return alternateStream(url)

    if 'plugin.video.expattv' in url:
        print '****** Alternate  ExPat ******'
        print url
        return alternateStream(url)

    if 'plugin.video.filmon' in url:
        print '****** Alternate  FilmOn ******'
        print url
        return alternateStream(url)

    if 'plugin.video.notfilmon' in url:
        print '****** Alternate NotFilmOn ******'
        print url
        return alternateStream(url)
        
    if 'plugin.video.itv' in url:
        print '****** Alternate ITV ******'
        print url
        return alternateStream(url)
        
    if 'plugin.video.iplayer' in url:
        print '****** Alternate iPlayer ******'
        print url
        return alternateStream(url)
        
    if 'plugin.video.musicvideojukebox' in url:
        print '****** Alternate JukeBox ******'
        print url
        return alternateStream(url)
        
    if 'plugin.video.muzu.tv' in url:
        print '****** Alternate Muzu ******'
        print url
        return alternateStream(url)
        
    if 'plugin.audio.ramfm' in url:
        print '****** Alternate RAM FM ******'
        print url
        return alternateStream(url)
        
    if 'plugin.video.movie25' in url:
        print '****** Alternate MashUp ******'
        print url
        return alternateStream(url)
        
    return False

def alternateStream(url):
    xbmc.executebuiltin('XBMC.RunPlugin(%s)' % url)
    print '****** Alternate Method ******'
    print url
    return True


if __name__ == '__main__': 
    play(sys.argv[1], sys.argv[2] == 1)


# expattv
# static.filmon.com
# notfilmon
# plugin.video.iplayer
# plugin.video.itv
# plugin.video.youtube
# plugin.video.musicvideojukebox
# plugin.video.muzu.tv
# plugin.audio.ramfm
# plugin.video.tgun
# plugin.video.movie25