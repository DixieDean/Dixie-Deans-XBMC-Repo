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

settingsFile = xbmc.translatePath(os.path.join(dixie.PROFILE, 'settings.cfg'))


def deleteDB():
    try:
        import glob
        dixie.log('Deleting database...')
        dbPath  = dixie.PROFILE
        dbFile  = os.path.join(dbPath, 'program.db')
        delete_file(dbFile)

        passed  = not os.path.exists(dbFile)

        if passed: 
            dixie.log('Deleting database...PASSED')
        else:
            dixie.log('Deleting database...FAILED')

        return passed

    except Exception, e:
        dixie.log('Deleting database...EXCEPTION %s' % str(e))
        return False

def delete_file(filename):
    dixie.SetSetting('epg.date', '2000-01-01')
    tries = 10
    while os.path.exists(filename) and tries > 0:
        settings.set('ChannelsUpdated', 0, settingsFile)
        try:
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    dixie.ShowBusy()
    
    if deleteDB():
        dixie.CloseBusy()
        dixie.DialogOK('EPG successfully reset.', 'It will be re-created next time', 'you start the guide')    
    
    else:
        dixie.CloseBusy()
        d = xbmcgui.Dialog()
        dixie.DialogOK('Failed to reset EPG.', 'Database may be locked,', 'please restart Kodi and try again')