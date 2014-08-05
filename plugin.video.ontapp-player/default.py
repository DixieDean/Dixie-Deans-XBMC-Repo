import xbmc
import xbmcgui

class Main:
    def __init__(self):
        # playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
        # playlist.clear()
        # playlist.add('E:\\movies\\300.VOB')
        xbmc.Player().play
        
m = Main()