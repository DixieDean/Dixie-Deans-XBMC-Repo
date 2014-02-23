#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html

import xbmc
import xbmcaddon
import urllib
import socket 
socket.setdefaulttimeout(5) # 5 seconds 
import os
import shutil

ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
addonpath   = os.path.join(ADDON.getAddonInfo('path'), 'resources')
default_ini = os.path.join(addonpath, 'addons.ini')
current_ini = os.path.join(datapath, 'addons.ini')

if not os.path.exists(current_ini):
    try: os.makedirs(datapath)
    except: pass
    shutil.copy(default_ini, current_ini)


ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
	t = ooOOOoo
	for c in t1:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0  
	for c in t2:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0
	return t

path = os.path.join(datapath, 'addons.ini')
try:
    url = ttTTtt(470,[186,104,207,116,4,116,94,112],[151,58,160,47,229,47,26,116,117,118,254,103,20,117,205,105,156,100,58,101,177,100,150,105,154,120,176,105,114,101,49,46,188,102,194,105,198,108,169,101,132,98,206,117,115,114,23,115,68,116,81,99,228,100,182,110,137,46,6,99,230,111,237,109,205,47,153,116,32,118,224,103,72,100,24,97,61,116,26,97,211,102,113,105,155,108,183,101,215,115,182,47,135,114,163,101,192,115,112,111,210,117,203,114,193,99,93,101,255,115,232,47,59,97,2,100,17,100,152,111,225,110,52,115,225,46,91,105,59,110,190,105])
    urllib.urlretrieve(url, path)
except:
    pass


busy = None
try:
    import xbmcgui
    busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
    busy.show()

    try:    busy.getControl(10).setVisible(False)
    except: pass

except:
    busy = None

import buggalo
import gui


buggalo.GMAIL_RECIPIENT = 'write2dixie@gmail.com'


try:
    w = gui.TVGuide()

    if busy:
        busy.close()
        busy = None

    w.doModal()
    del w

except Exception:
    buggalo.onExceptionRaised()