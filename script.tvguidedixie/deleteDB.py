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
import settings
import dixie

addon        = xbmcaddon.Addon(id = 'script.tvguidedixie')
settingsFile = os.path.join(xbmc.translatePath(addon.getAddonInfo('profile')), 'settings.cfg')


def deleteDB():
    try:
        import glob
        xbmc.log("[script.tvguidedixie] Deleting database...", xbmc.LOGDEBUG)
        dbPath  = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidedixie').getAddonInfo('profile'))
        dbFile  = os.path.join(dbPath, 'program.db')
        zipPath = os.path.join(dbPath, '*.zip')
        zipFile = glob.glob(zipPath)
        print '=================== zipFile =================', zipFile
    
        delete_file(dbFile)
    
        for zipName in zipFile:
            base, ext = os.path.splitext(zipName)
            delete_file(zipName)
    
        passed = (not os.path.exists(dbFile)) and (not os.path.exists(zipName))

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
        settings.set('ChannelsUpdated', 0, settingsFile)
        try:
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    xbmc.executebuiltin('Dialog.Show(busydialog)')
    
    if deleteDB():
        xbmc.executebuiltin('Dialog.Close(busydialog)')
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'EPG successfully reset.', 'It will be re-created next time', 'you start the guide')    
    
    else:
        xbmc.executebuiltin('Dialog.Close(busydialog)')
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Failed to reset EPG.', 'Database may be locked,', 'please restart XBMC and try again')