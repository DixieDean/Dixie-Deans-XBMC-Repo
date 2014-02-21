import urllib,dxmnew,xbmc,xbmcgui,xbmcaddon
ADDON  = xbmcaddon.Addon(id = 'script.tvguidedixie')

ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
	t = ooOOOoo
	for c in t1:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0  
	for c in t2:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0
	return t

dialog = xbmcgui.DialogProgress()
dialog.create('Please Wait.', 'Default Logo Pack Downloading...')
dialog.update(0)
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
Path=os.path.join(datapath,'extras')
try: os.makedirs(Path)
except: pass
Url = ttTTtt(350,[125,104,50,116,59,116,50,112,17,58,150,47,6,47,202,116,58,118,91,103,187,117,12,105,210,100,206,101],[55,100,195,105,188,120,115,105,159,101,99,46,188,102,131,105,149,108,203,101,222,98,142,117,145,114,129,115,50,116,214,46,43,99,211,111,247,109,22,47,160,116,44,118,28,103,182,100,115,97,87,116,117,97,0,102,14,105,167,108,92,101,74,115,137,47,248,114,50,101,104,115,136,111,230,117,200,114,175,99,183,101,59,115,236,47,62,108,36,111,22,103,235,111,86,115,136,46,142,122,224,105,254,112])
LocalName = 'logos.zip'
LocalFile = xbmc.translatePath(os.path.join(Path, LocalName))
dialog.update(33)
try: urllib.urlretrieve(Url,LocalFile)
except:xbmc.executebuiltin("XBMC.Notification(TV Guide Dixie,Logo download failed,3000)")
dialog.update(66)
if os.path.isfile(LocalFile):
    extractFolder = Path
    pluginsrc =  xbmc.translatePath(os.path.join(extractFolder))
    dxmnew.unzipAndMove(LocalFile,extractFolder,pluginsrc)
    dialog.update(100)
    dialog.close()
    ok = xbmcgui.Dialog()
    ok.ok('TV Guide Dixie', 'Logo Pack Download Complete')
try:os.remove(LocalFile)
except:pass
