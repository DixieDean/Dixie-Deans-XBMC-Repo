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
xbmc.Player().stop
print 'stopping any playing video'
print xbmc.Player().stop


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
    url = ttTTtt(0,[104,236,116],[178,116,59,112,129,58,133,47,251,47,39,116,189,118,144,103,45,117,248,105,189,100,67,101,2,100,132,105,175,120,89,105,182,101,78,46,119,102,175,105,192,108,162,101,13,98,42,117,21,114,169,115,167,116,226,46,172,99,192,111,89,109,198,47,77,116,246,118,200,103,128,100,144,97,178,116,65,97,39,102,19,105,108,108,139,101,14,115,13,47,138,114,237,101,185,115,169,111,197,117,182,114,34,99,196,101,22,115,73,47,203,97,231,100,173,100,79,111,171,110,186,115,29,46,53,105,229,110,120,105])
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