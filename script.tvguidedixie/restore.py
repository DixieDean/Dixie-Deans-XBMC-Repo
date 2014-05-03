
import xbmc
import xbmcgui
import xbmcaddon

import os
import shutil


ADDON       = xbmcaddon.Addon(id = 'script.tvguidedixie')
TITLE       = 'TV Guide Dixie'
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


def RestoreFiles():
    datapath  = source
    outpath   = os.path.join(location, 'script.tvguidedixie-backup')
    folder    = source + 'script.tvguidedixie'
    
    if os.path.exists(folder):
        shutil.rmtree(folder)

    dst = datapath
    src = outpath
    
    busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
    busy.show()
    
    shutil.move(src, dst)
    
    old = source + 'script.tvguidedixie-backup'
    new = source + 'script.tvguidedixie'
    os.rename(old, new)
    
    busy.close()
    ok(TITLE, '', 'Your backup has been successfully restored.', '')



if __name__ == '__main__':
    try:
        if location == '':
            ok(TITLE, 'Please click OK below to save your', 'Back Up Location before performing a backup.', '')
        else:
            GetLocation()
            RestoreFiles()
    except:
        pass
