#
#      Copyright (C) 2014 Richard Dean
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
import os

import dixie
import sfile

hotkey = xbmc.translatePath('special://profile/keymaps/ottv_hot.xml')


def resetHotkey():
    deleteFiles()
    dixie.CloseBusy()


def deleteFiles():
    try:
        sfile.remove(hotkey)
                
        dixie.DialogOK('On-Tapp.TV Hot Key successfully reset.', 'Please restart Kodi for this to take affect.', 'Thank you.')
        
    except Exception, e:
        error = str(e)
        dixie.log('%s :: Error resetting OTTV' % error)
        dixie.DialogOK('On-Tapp.TV Hot Key failed to reset.', error, 'Please restart Kodi and try again.')


if __name__ == '__main__':
    dixie.ShowBusy()
    resetHotkey()
