
import os
import xbmc
import xbmcgui
import xbmcaddon

def resetAll():
    try:
        xbmc.log("[script.tvguidedixie] Deleting userdata files...", xbmc.LOGDEBUG)
        allPath  = xbmc.translatePath(xbmcaddon.Addon(id = 'script.tvguidedixie').getAddonInfo('profile'))
        prgPath  = os.path.join(allPath, 'program.db')
        srcPath = os.path.join(allPath, 'source.db')
        setPath = os.path.join(allPath, 'settings.xml')

        delete_file(prgPath)
        delete_file(srcPath)
        delete_file(setPath)
        
        passed = not os.path.exists(setPath)

        if passed: 
            xbmc.log("[script.tvguidedixie] Deleting userdata files...PASSED", xbmc.LOGDEBUG)
        else:
            xbmc.log("[script.tvguidedixie] Deleting userdata files...FAILED", xbmc.LOGDEBUG)

        return passed

    except Exception, e:
        xbmc.log('[script.tvguidedixie] Deleting userdata files...EXCEPTION', xbmc.LOGDEBUG)
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
    if resetAll():
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'OnTapp.TV successfully reset.', 'Everything will be re-created next time', 'you start the guide')    
    else:
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Failed to reset OnTapp.TV.', 'Some files may be locked,', 'please restart XBMC and try again')    


