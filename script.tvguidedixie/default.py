

import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui

import urllib


import ottplanner_utils as utils
import sfile


ADDON   = utils.ADDON
HOME    = utils.HOME
TITLE   = utils.TITLE
VERSION = utils.VERSION
ICON    = utils.ICON
FANART  = utils.FANART
GETTEXT = utils.GETTEXT


PLAYABLE   = 100
INPROGRESS = 200
FOLDER     = 300
KILL       = 400
DELETE     = 500



def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:
        return

    ADDON.setSetting('VERSION', curr)

    utils.showChangelog()



def GetDeleteFileMenu(title, key):
    menu = []
    menu.append((GETTEXT(31002), 'XBMC.RunPlugin(%s?mode=%d&title=%s&url=%s)' % (sys.argv[0], DELETE, urllib.quote_plus(title), urllib.quote_plus(key))))
    return menu


def Main():
    CheckVersion()

    recordings = utils.LoadRecordings()
    inProgress = False
    titles     = {}
    progress   = {}
    
    for key in recordings:
        recording = recordings[key]
        title     = recording ['title']
        pid       = recording ['pid']
        truncated = recording ['truncated']

        if title not in progress:
            progress[title] = 0

        if pid > 0:
            inProgress = True
            progress[title] = progress[title] + 1
        else:
            if title not in titles:
                titles[title] = []

            titles[title].append(key)

    if inProgress:
        AddDir(GETTEXT(31000), INPROGRESS)

    for title in sorted(titles):
        key       = titles[title][0]
        recording = recordings[key]
        image     = recording['image']
        filename  = recording['filename']
        truncated = recording['truncated']

        nItems = len(titles[title]) + progress[title]

        if nItems > 1:
            AddDir(title, FOLDER, title, image=image, nItems=nItems)
        else:
            AddDir(title, PLAYABLE, filename, image, False, contextMenu=GetDeleteFileMenu(title, key), truncated=truncated)


def InProgess():
    recordings = utils.LoadRecordings()

    for key in recordings:
        recording = recordings[key]
        pid       = recording ['pid']

        if pid > 0:
            title     = recording ['title']
            startDate = recording ['startDate']
            filename  = recording ['filename']
            image     = recording ['image']
            label     = '%s - %s' % (title, str(startDate))

            menu = []
            menu.append((GETTEXT(31001), 'XBMC.RunPlugin(%s?mode=%d&title=%s&url=%d)' % (sys.argv[0], KILL, urllib.quote_plus(title), pid)))
            AddDir(label, PLAYABLE, filename, image, False, contextMenu=menu)


def Folder(title):
    recordings = utils.LoadRecordings()
    
    for key in sorted(recordings):
        recording = recordings[key]
        if title == recording ['title']:
            startDate  = recording ['startDate']
            filename   = recording ['filename']
            image      = recording ['image']
            truncated  = recording ['truncated']
            label      = '%s - %s' % (title, str(startDate))
            inProgress = recording ['pid'] > 0

            AddDir(label, PLAYABLE, filename, image, False, contextMenu=GetDeleteFileMenu(label, key), truncated=truncated, inProgress=inProgress)


def Play(url, title='', image=None):
    if image is None:
        image = ICON

    liz = InitListItem(title, image)
    if url:    
        liz.setPath(url)

    xbmcplugin.setResolvedUrl(int(sys.argv[1]), url is not None, liz)


def DeleteFile(title, key):
    if not utils.DialogYesNo(title, GETTEXT(31004)):
        return False

    recordings = utils.LoadRecordings()
    if key not in recordings:
        utils.DialogOK(GETTEXT(31005))
        return True 

    recording = recordings[key]

    filename  = recording ['filename']

    sfile.remove(filename)

    del recordings[key]

    utils.SaveRecordings(recordings)

    return True


def KillPID(title, pid):
    if not utils.DialogYesNo(title, GETTEXT(31003)):
        return False

    xbmcgui.Window(10000).setProperty('OTT-KILL_RECORDING_%s' % str(pid), 'true')
    return True
        

    
def InitListItem(title, image, truncated, inProgress):
    if image is None:
        image = ICON

    if inProgress:
        title += ' %s' % GETTEXT(31007)

    elif truncated:
        title += ' %s' % GETTEXT(31006)


    liz = xbmcgui.ListItem(title, iconImage=image, thumbnailImage=image)
    liz.setProperty('Fanart_Image', image)
 
    # Jarvis way of setting artwork
    if hasattr(liz, 'setArt'):
        art = {}
        art['landscape'] = image
        art['banner']    = image
        art['poster']    = image
        art['thumb']     = image
        art['fanart']    = image
        liz.setArt(art) 

    return liz


def AddDir(title, mode, url='', image=None, isFolder=True, infoLabels=None, contextMenu=None, truncated=False, inProgress=False, nItems=1):
    if image is None:
        image = ICON

    u  = sys.argv[0] 
    u += '?mode='  + str(mode)
    u += '&title=' + urllib.quote_plus(title)
    u += '&image=' + urllib.quote_plus(image)

    if url != '':     
        u += '&url=' + urllib.quote_plus(url) 

    if nItems > 1:
        title = '%s (%d)' % (title, nItems) 

    liz = InitListItem(title, image, truncated, inProgress)

    if contextMenu:
        liz.addContextMenuItems(contextMenu)

    if infoLabels:
        liz.setInfo(type='Video', infoLabels=infoLabels)

    if not isFolder:
        liz.setProperty('IsPlayable','true')
        u = url
 
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)



def Refresh():
    xbmc.executebuiltin('Container.Refresh')


def GetParams(path):
    params = {}
    path   = path.split('?', 1)[-1]
    pairs  = path.split('&')

    for pair in pairs:
        split = pair.split('=')
        if len(split) > 1:
            params[split[0]] = urllib.unquote_plus(split[1])

    return params


def Go():
    params = GetParams(sys.argv[2])

    try:    mode = int(params['mode'])
    except: mode = None

    try:    title = params['title']
    except: title = None

    try:    url = params['url']
    except: url = None

    try:    image = params['image']
    except: image = None


    if mode == PLAYABLE:
        return Play(url, title, image)

    if mode == FOLDER:
        return Folder(title)

    if mode == INPROGRESS:
        return InProgess()


    if mode == KILL:
        if KillPID(title, url):
            Refresh()
        return


    if mode == DELETE:
        if DeleteFile(title, url):
            Refresh()
        return

    Main()

    
Go()
xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
