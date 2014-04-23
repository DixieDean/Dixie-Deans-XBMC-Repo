

import xbmcaddon

id = 'script.tvguidedixie'


ADDON = xbmcaddon.Addon(id = id)
ADDON.openSettings()

xbmc.executebuiltin('RunScript(%s)' % id)

