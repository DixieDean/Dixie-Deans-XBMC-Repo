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

import os
import xbmc
import xbmcgui
import xbmcaddon

def deleteCookie():
    try:
        xbmc.log("[script.tvguidedixie] Deleting database...", xbmc.LOGDEBUG)
        addonPath  = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidedixie').getAddonInfo('profile'))
        cookiePath = os.path.join(addonPath, 'cookies')
        cookieFile = os.path.join(cookiePath, 'on-tapp.lwp')

        delete_file(cookieFile)
        
        passed = not os.path.exists(cookieFile)

        if passed: 
            xbmc.log("[script.tvguidedixie] Deleting database...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvguidedixie] Deleting database...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvguidedixie] Deleting database...EXCEPTION', xbmc.LOGDEBUG)
        return False

def delete_file(filename):
    tries = 10
    while os.path.exists(filename) and tries > 0: 
        try:             
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    if deleteCookie():
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Cookie file successfully deleted.', 'It will be re-created next time', 'you start the guide')    
    else:
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Failed to delete cookie file.', 'The file may be locked,', 'please restart XBMC and try again')    


