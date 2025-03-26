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

import dixie


ACTION_MOVE_LEFT          = 1
ACTION_MOVE_RIGHT         = 2
ACTION_MOVE_UP            = 3
ACTION_MOVE_DOWN          = 4
ACTION_SELECT_ITEM        = 7
ACTION_MOUSE_LEFT_CLICK   = 100
ACTION_MOUSE_DOUBLE_CLICK = 103
ACTION_MOUSE_MOVE         = 107

ACTION_PARENT_DIR         = 9
ACTION_PREVIOUS_MENU      = 10
ACTION_NAV_BACK           = 92

KEY_CONTEXT_MENU          = 117

TIMEOUT = 10

class KeyListener(xbmcgui.WindowXMLDialog):

    def __new__(cls, text):
        try: 
            ret = super(KeyListener, cls).__new__(cls, 'DialogProgress.xml', '')
        except:
            ret   = super(KeyListener, cls).__new__(cls, 'DialogConfirm.xml', '')
        return ret 


    def __init__(self, text):
        self.key     = 0
        self.timeout = TIMEOUT
        self.text    = text
        self.setTimer()


    def close(self):
        self.timer.cancel()
        xbmcgui.WindowXML.close(self)


    def onInit(self):
        try:
            self.getControl(20).setVisible(False)
            self.getControl(10).setLabel(xbmc.getLocalizedString(222))
            self.setFocus(self.getControl(10))
            self.getControl(11).setVisible(False)
            self.getControl(12).setVisible(False)
        except:
            pass


        self.onUpdate()


    def onUpdate(self):
        text  = 'Press a key to assign it to %s[CR]' % self.text
        text += 'Timeout in %d seconds...' % self.timeout

        self.getControl(9).setText(text)


    def onAction(self, action):
        actionId = action.getId()

        if actionId in [ACTION_MOVE_LEFT, ACTION_MOVE_RIGHT, ACTION_MOVE_UP, ACTION_MOVE_DOWN, ACTION_SELECT_ITEM, ACTION_MOUSE_LEFT_CLICK, ACTION_MOUSE_DOUBLE_CLICK , ACTION_MOUSE_MOVE, KEY_CONTEXT_MENU]:
            return

        if actionId in [ACTION_PARENT_DIR, ACTION_PREVIOUS_MENU, ACTION_NAV_BACK]:
            return self.close()
       
        self.key = action.getButtonCode()
        self.close()


    def onClick(self, controlId):
        self.close()


    def onTimer(self):
        self.timeout -= 1
        if self.timeout < 0:
            return self.close()

        self.onUpdate()
        self.setTimer()


    def setTimer(self):
        self.timer = Timer(1, self.onTimer)
        self.timer.start()


def recordKey(text):
    dialog  = KeyListener(text)

    dialog.doModal()

    key = dialog.key

    del dialog
    return key


def main(filename, cmd, setting, text):
    key = recordKey(text)
    if key < 1:
        dixie.DialogOK('On-Tapp.TV Hot Key assignment cancelled')
        return

    start = 'key id="%d"' % key
    end   = 'key'

    if dixie.WriteKeymap(start, end, filename, cmd):
        dixie.log('OTTV %s HotKey assigned: %s' % (text, key))
        if len(setting) > 0:
            dixie.SetSetting(setting, key)
        dixie.DialogOK('On-Tapp.TV Hot Key successfully set up.', '', 'Thank you.')

        xbmc.executebuiltin('Action(reloadkeymaps)')  


if __name__ == '__main__':
    filename = sys.argv[1]
    cmd      = sys.argv[2]
    setting  = sys.argv[3]
    text     = sys.argv[4]
    main(filename, cmd, setting, text)