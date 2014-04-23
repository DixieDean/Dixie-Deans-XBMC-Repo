import xbmc
import xbmcaddon
import download
import extract

import dixie

ADDON    = xbmcaddon.Addon(id = 'script.tvguidedixie')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
url      = dixie.GetExtraUrl() + 'logos.zip'


try:
    os.makedirs(logos)
    os.makedirs(nologos)
except:
    pass
 
download.download(url, dest)
extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass