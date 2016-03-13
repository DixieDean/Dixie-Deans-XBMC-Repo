#
#       Copyright (C) 2014
#       Sean Poyser (seanpoyser@gmail.com)
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
#  KeyListener class based on XBMC Keymap Editor by takoi


import xbmc
import xbmcgui
from threading import Timer

import os
import dixie

XML  = 'KeyListener.xml'

ICON = dixie.ICON

TIMEOUT = 10

class KeyListener(xbmcgui.WindowXMLDialog):

    def __new__(cls):
        return super(KeyListener, cls).__new__(cls, XML, dixie.HOME)


    def __init__(self):
        self.key = 0


    def onInit(self):
        timeout = 'Timeout in %d seconds...' % TIMEOUT
        label   = 'Press a key to assign it to Toggle Full Screen now'

        self.getControl(401).addLabel(label)
        self.getControl(402).addLabel(timeout)
        self.getControl(400).setImage(ICON)
        

    def onAction(self, action):
        self.key = action.getButtonCode()
        self.close()


def recordKey():
    dialog  = KeyListener()
    timeout = Timer(TIMEOUT, dialog.close)

    timeout.start()

    dialog.doModal()

    timeout.cancel()

    key = dialog.key

    del dialog
    return key


def main():
    key = recordKey()
    if key < 1:
        return

    start = 'key id="%d"' % key
    end   = 'key'

    if dixie.WriteFSKeymap(start, end):
        dixie.log('OTTV HotKey assigned: %s' % key)
        dixie.DialogOK('On-Tapp.TV Hot Key successfully set up.', '', 'Thank you.')
        xbmc.sleep(1000)
        xbmc.executebuiltin('Action(reloadkeymaps)')


main()
