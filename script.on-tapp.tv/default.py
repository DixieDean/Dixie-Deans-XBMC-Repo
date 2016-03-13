
#       Copyright (C) 2013-
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

import xbmc
import utilsOTT as utils
import update

NOHOME = utils.getSetting('NOHOME') == 'true'

update.checkUpdate()

if __name__ == '__main__':
    if NOHOME:
        xbmc.executebuiltin('RunScript(script.tvguidedixie)')

    else:
        param = None

        if len(sys.argv) > 1:
            param = sys.argv[1]

        xbmc.executebuiltin('Dialog.Close(busydialog)')
        utils.Launch(param)
