

import xbmcaddon
import xbmc
import xbmcgui

id = 'script.tvguidedixie'


ADDON = xbmcaddon.Addon(id = id)
ADDON.openSettings()

#xbmc.executebuiltin('RunScript(%s)' % id)

xbmcgui.Window(10000).setProperty('OTT_LOGIN', 'false')

name   =  'OTT'
script =  os.path.join(ADDON.getAddonInfo('path'), 'launch.py')
args   =  ''
cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0)

xbmc.executebuiltin('CancelAlarm(%s,True)' % name)        
xbmc.executebuiltin(cmd)

