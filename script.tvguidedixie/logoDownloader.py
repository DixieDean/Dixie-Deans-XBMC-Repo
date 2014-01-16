import urllib,dxmnew,xbmc,xbmcaddon
ADDON     = xbmcaddon.Addon(id = 'script.tvguidedixie')
xbmc.executebuiltin("XBMC.Notification(TV Guide Dixie,Please Wait!,2000)")

datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
Path=os.path.join(datapath,'extras')
try: os.makedirs(Path)
except: pass
Url = 'https://raw.github.com/DixieDean/Dixie-Deans-XBMC-Repo/master/logos.zip'
LocalName = 'logos.zip'
LocalFile = xbmc.translatePath(os.path.join(Path, LocalName))
try: urllib.urlretrieve(Url,LocalFile)
except:xbmc.executebuiltin("XBMC.Notification(TV Guide Dixie,Logo download failed,3000)")
if os.path.isfile(LocalFile):
    extractFolder = Path
    pluginsrc =  xbmc.translatePath(os.path.join(extractFolder))
    dxmnew.unzipAndMove(LocalFile,extractFolder,pluginsrc)
    xbmc.executebuiltin("XBMC.Notification(TV Guide Dixie,Logo download complete,3000)")
try:os.remove(LocalFile)
except:pass
