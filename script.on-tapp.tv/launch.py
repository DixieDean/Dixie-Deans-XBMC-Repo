
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

import utils

def main(addonID, param=None):
    try:        
        import application
        app = application.Application(addonID)
        app.run(param)
        del app
    except Exception, e:
        utils.Log('******************* ERROR IN MAIN *******************')
        utils.Log(str(e))
        raise


if __name__ == '__main__':
    addonID  = sys.argv[1]

    while xbmc.getCondVisibility('Window.IsActive(okdialog)') <> 0:
        xbmc.sleep(100)
   
    if len(sys.argv) == 2:
        main(addonID)
    else:
        main(addonID, sys.argv[2])