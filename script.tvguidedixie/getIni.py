
import os
import xbmc
import xbmcgui
import xbmcaddon
import urllib

import dixie

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
current_ini = os.path.join(datapath, 'addons.ini')



def getIni():
    path = current_ini
    try:
        url = dixie.GetExtraUrl() + 'addons.ini'
        urllib.urlretrieve(url, path)
    except:
        pass


if __name__ == '__main__':
    getIni()
    d = xbmcgui.Dialog()
    d.ok('TV Guide Dixie', 'Built-in Addon links updated.', 'Always manually update your channel links', 'via "Choose Stream" if they are not working.')

