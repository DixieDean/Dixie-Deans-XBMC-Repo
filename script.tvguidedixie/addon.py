#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
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
import xbmcgui
import os
import dixie

dixie.migrateDSF()

def main():
    windowID = xbmcgui.Window(10000).getProperty('OTT_WINDOW')
    try:
        windowID = int(windowID)
        xbmc.executebuiltin('ActivateWindow(%d)' % windowID)  
        return
    except:
        pass

    name   = dixie.TITLE + ' Launcher'
    script = os.path.join(dixie.HOME, 'launch.py')
    args   = ''
    cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)        
    xbmc.executebuiltin(cmd)


if __name__ == '__main__':
    try:    main()
    except: pass
