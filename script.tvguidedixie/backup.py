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
import xbmcaddon

import os
import shutil


ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
TITLE       = 'OnTapp.TV'
source      = xbmc.translatePath('special://profile/addon_data/')
folder      = source + 'script.tvguidedixie'
location    = ADDON.getSetting('backup.location')
datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))


def ok(title, line1, line2 = '', line3 = ''):
    dlg = xbmcgui.Dialog()
    dlg.ok(title, line1, line2, line3)


def GetLocation():
    try:
        if os.path.exists(source):
            return source
            
        if os.path.exists(location):
            return location
        
    except Exception, e:
        print str(e)


def BackupFiles():
    datapath = os.path.join(source, folder)
    outpath = os.path.join(location, 'script.tvguidedixie-backup')
    
    src = datapath
    dst = outpath
    
    busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
    busy.show()
    
    shutil.copytree(src, dst, symlinks=False, ignore=None)
    
    busy.close()
    ok(TITLE, '', 'Your setup has been successfully backed up.', '')
    


if __name__ == '__main__':
    try:
        if location == '':
            ok(TITLE, 'Please click OK below to save your', 'Back Up Location before performing a backup.', '')
        else:
            GetLocation()
            BackupFiles()
    except:
        pass
