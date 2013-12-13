# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
try:
    import json
except:
    import simplejson as json
    
# external libs
import utils, httplib2, socks, httplib, logging, time    
    
addon = xbmcaddon.Addon('plugin.video.LiveTV')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id='plugin.video.LiveTV')
home = __settings__.getAddonInfo('path')
favorites = xbmc.translatePath( os.path.join( profile, 'favorites' ) )
REV = xbmc.translatePath( os.path.join( profile, 'list_revision') )
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
source_file = xbmc.translatePath( os.path.join( profile, 'source_file') )
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
if os.path.exists(source_file)==True:
    SOURCES = open(source_file).read()
    
# setup cache dir
__scriptname__  = 'LiveTV'
__scriptid__ = "plugin.video.LiveTV"
__addoninfo__ = utils.get_addoninfo(__scriptid__)
__addon__ = __addoninfo__["addon"]
__settings__   = xbmcaddon.Addon(id=__scriptid__)


DIR_USERDATA   = xbmc.translatePath(__addoninfo__["profile"])
SUBTITLES_DIR  = os.path.join(DIR_USERDATA, 'Subtitles')
IMAGE_DIR      = os.path.join(DIR_USERDATA, 'Images')

if not os.path.isdir(DIR_USERDATA):
    os.makedirs(DIR_USERDATA)
if not os.path.isdir(SUBTITLES_DIR):
    os.makedirs(SUBTITLES_DIR)
if not os.path.isdir(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def get_proxy():
    proxy_server = None
    proxy_type_id = 0
    proxy_port = 8080
    proxy_user = None
    proxy_pass = None
    try:
        proxy_server = __settings__.getSetting('proxy_server')
        proxy_type_id = __settings__.getSetting('proxy_type')
        proxy_port = int(__settings__.getSetting('proxy_port'))
        proxy_user = __settings__.getSetting('proxy_user')
        proxy_pass = __settings__.getSetting('proxy_pass')
    except:
        pass

    if   proxy_type_id == '0': proxy_type = socks.PROXY_TYPE_HTTP_NO_TUNNEL
    elif proxy_type_id == '1': proxy_type = socks.PROXY_TYPE_HTTP
    elif proxy_type_id == '2': proxy_type = socks.PROXY_TYPE_SOCKS4
    elif proxy_type_id == '3': proxy_type = socks.PROXY_TYPE_SOCKS5

    proxy_dns = True
    
    return (proxy_type, proxy_server, proxy_port, proxy_dns, proxy_user, proxy_pass)

def get_httplib():
    http = None
    try:
        if __settings__.getSetting('proxy_use') == 'true':
            (proxy_type, proxy_server, proxy_port, proxy_dns, proxy_user, proxy_pass) = get_proxy()
            logging.info("Using proxy: type %i rdns: %i server: %s port: %s user: %s pass: %s", proxy_type, proxy_dns, proxy_server, proxy_port, "***", "***")
            http = httplib2.Http(proxy_info = httplib2.ProxyInfo(proxy_type, proxy_server, proxy_port, proxy_dns, proxy_user, proxy_pass))
        else:
          logging.info("No Proxy\n")
          http = httplib2.Http()
    except:
        raise
        logging.error('Failed to initialize httplib2 module')

    return http

http = get_httplib()


       
# what OS?        
environment = os.environ.get( "OS", "xbox" )

def getSources():
        if os.path.exists(favorites)==True:
            addDir('Favorites','url',4,xbmc.translatePath(os.path.join(home, 'resources', 'favorite.png')),fanart,'','','',False)
        if os.path.exists(source_file)==False:
            xbmc.executebuiltin("XBMC.Notification(LiveTV,Choose type source and then select Add Source.,15000,"+icon+")")
            __settings__.openSettings()
            return
        sources = json.loads(open(source_file,"r").read())
        if len(sources) > 1:
            for i in sources:
                addDir(i[0],i[1],1,icon,fanart,'','','')
        else:
            getData(sources[0][1],fanart)


def addSource(url=None):
        if url is None:
            if not __settings__.getSetting("new_file_source") == "":
               source = __settings__.getSetting('new_file_source')
            if not __settings__.getSetting("new_url_source") == "":
               source = __settings__.getSetting('new_url_source')
        else:
            source = url
        if source == '' or source is None:
            return
        if '/' in source:
            nameStr = source.split('/')[-1].split('.')[0]
        if '\\' in source:
            nameStr = source.split('\\')[-1].split('.')[0]
        if '%' in nameStr:
            nameStr = urllib.unquote_plus(nameStr)
        keyboard = xbmc.Keyboard(nameStr,'Displayed Name, Rename?')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newStr = keyboard.getText()
        if len(newStr) == 0:
            return
        source_list = []
        source = (newStr, source)
        if os.path.exists(source_file)==False:
            source_list.append(source)
            b = open(source_file,"w")
            b.write(json.dumps(source_list))
            b.close()
        else:
            sources = json.loads(open(source_file,"r").read())
            sources.append(source)
            b = open(source_file,"w")
            b.write(json.dumps(sources))
            b.close()
        __settings__.setSetting('new_url_source', "")
        __settings__.setSetting('new_file_source', "")
        xbmc.executebuiltin("XBMC.Notification(LiveTV,New source added.,5000,"+icon+")")

def rmSource(name):
        sources = json.loads(open(source_file,"r").read())
        for index in range(len(sources)):
            try:
                if sources[index][0] == name:
                    del sources[index]
                b = open(source_file,"w")
                b.write(json.dumps(sources))
                b.close()
            except:
                pass


def getCommunitySources():
        req = urllib2.Request('http://live-tv-stream.googlecode.com/svn/trunk/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        files = soup('ul')[0]('li')[1:]
        for i in files:
            name = i('a')[0]['href']
            url = 'http://live-tv-stream.googlecode.com/svn/trunk/'+name
            addDir(name,url,11,icon,fanart,'','','',False)

                
def getCommunitySources():
        req = urllib2.Request('http://home.no/chj191/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        files = re.compile('<a href="(.+?)">LiveTV.xml</a>').findall
        name = 'LiveTV.xml'
        url = 'http://home.no/chj191/'+name
        addDir(name,url,11,icon,fanart,'','','',False)

                
def getUpdate():
        req = urllib2.Request('http://home.no/chj191/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        files = re.compile('<a href="(.+?)">LiveTV.xml</a>').findall
        name = 'LiveTV.xml'
        url = 'http://home.no/chj191/'+name
        addDir(name,url,11,icon,fanart,'','','',False)
        if not xbmcvfs.exists(__settings__.getSetting('save_location')):
                success = xbmcvfs.mkdir(__settings__.getSetting('save_location'))
                save_location = __settings__.getSetting('save_location')
        if 'smb:' in save_location:
                file_name = xbmc.makeLegalFilename(os.path.join( profile, 'temp', name))
                f = open(os.path.join( profile, 'temp', name),"w")
                f.write(link)
                f.close()
                copy = xbmcvfs.copy(os.path.join( profile, 'temp', name), os.path.join( save_location, name))
                if copy:
                    xbmcvfs.delete( xbmc.translatePath(os.path.join( profile, 'temp', name)))
                else:
                    print '------ Error smb: makeLegalFilename -----'
        else:
                try:
                    file_name = xbmc.makeLegalFilename(os.path.join(save_location, name))
                    f = open(os.path.join(save_location, name),"w")
                    f.write(link)
                    f.close()
                except:
                    print "there was a problem writing to save location."
                    return
        xbmc.executebuiltin("XBMC.Notification(LiveTV,LiveTV Updated,5000,"+icon+")")


def checkForUpdate():
        req = urllib2.Request('http://home.no/chj191/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        files = re.compile('<a href="(.+?)">LiveTV.xml</a>').findall
        name = 'LiveTV.xml'
        url = 'http://home.no/chj191/'+name
        getUpdate()


if __settings__.getSetting('LiveTv') == "true":
    if __settings__.getSetting('save_location') == "":
        xbmc.executebuiltin("XBMC.Notification('LiveTV','Choose a location to save files and select OK to save.',15000,"+icon+")")
        __settings__.openSettings()
    else:
        try:
            checkForUpdate()
        except urllib2.URLError, e:
            errorStr = str(e.read())
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code


def getSoup(url):
        print 'getSoup(): '+url
        if url.startswith('http://'):
            try:
                req = urllib2.Request(url)
                response = urllib2.urlopen(req)
                data = response.read()
                response.close()
            except urllib2.URLError, e:
                # errorStr = str(e.read())
                if hasattr(e, 'code'):
                    print 'We failed with error code - %s.' % e.code
                    xbmc.executebuiltin("XBMC.Notification(LiveTV,We failed with error code - "+str(e.code)+",10000,"+icon+")")
                elif hasattr(e, 'reason'):
                    print 'We failed to reach a server.'
                    print 'Reason: ', e.reason
                    xbmc.executebuiltin("XBMC.Notification(LiveTV,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")
        else:
            if xbmcvfs.exists(url):
                if url.startswith("smb://"):
                    copy = xbmcvfs.copy( url, xbmc.translatePath(os.path.join(profile, 'temp', 'sorce_temp.txt')))
                    if copy:
                        data = open( xbmc.translatePath(os.path.join(profile, 'temp', 'sorce_temp.txt')), "r").read()
                        xbmcvfs.delete( xbmc.translatePath(os.path.join(profile, 'temp', 'sorce_temp.txt')) )
                    else:
                        print "--- failed to copy from smb: ----"
                else:
                    data = open(url, 'r').read()
            else:
                print "---- Soup Data not found! ----"
                return
        soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        return soup


def getData(url,fanart):
        soup = getSoup(url)
        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
                name = channel('name')[0].string
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    thumbnail = ''
                    
                try:    
                    if not channel('fanart'):
                        if __settings__.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart
                    
                try:
                    desc = channel('info')[0].string
                    if desc == None:
                        raise
                except:
                    desc = ''

                try:
                    genre = channel('genre')[0].string
                    if genre == None:
                        raise
                except:
                    genre = ''

                try:
                    date = channel('date')[0].string
                    if date == None:
                        raise
                except:
                    date = ''
                try:
                    addDir(name.encode('utf-8', 'ignore'),url,2,thumbnail,fanArt,desc,genre,date)
                except:
                    print 'There was a problem adding directory from getData(): '+name.encode('utf-8', 'ignore')
        else:
            getItems(soup('item'),fanart)


def getChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('channel', attrs={'name' : name})
        items = channel_list('item')
        try:
            fanArt = channel_list('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:    
                if not channel('fanart'):
                    if __settings__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                else:
                    fanArt = channel('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
                if desc == None:
                    raise
            except:
                desc = ''

            try:
                genre = channel('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = channel('date')[0].string
                if date == None:
                    raise
            except:
                date = ''
            try:
                addDir(name.encode('utf-8', 'ignore'),url,3,thumbnail,fanArt,desc,genre,date)
            except:
                print 'There was a problem adding directory - '+name.encode('utf-8', 'ignore')
        print fanArt
        getItems(items,fanArt)


def getSubChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('subchannel', attrs={'name' : name})
        items = channel_list('subitem')
        getItems(items,fanart)


def getItems(items,fanart):
        for item in items:
            try:
                name = item('title')[0].string
            except:
                print '-----Name Error----'
                name = ''
            try:
                if item('epg'):
                    if item('epg')[0].string > 1:
                        name += getepg(item('epg')[0].string)
            except:
                print '----- EPG Error ----'
            try:                  
                if item('epg3'):
                    if item('epg3')[0].string > 1:
                       name += getepg3(item('epg3')[0].string)
                else:
                    pass
            except:
                print '----- EPG Error ----' 

            try:
                if __settings__.getSetting('mirror_link') == "true":
                    try:
                        url = item('link')[1].string    
                    except:
                        url = item('link')[0].string
                if __settings__.getSetting('mirror_link_low') == "true":
                    try:
                        url = item('link')[2].string    
                    except:
                        try:
                            url = item('link')[1].string
                        except:
                            url = item('link')[0].string
                else:
                    url = item('link')[0].string
            except:
                print '---- URL Error Passing ----'+name
                pass

            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:    
                if not item('fanart'):
                    if __settings__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                    else:
                        fanArt = fanart
                else:
                    fanArt = item('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                fanArt = fanart
            try:
                desc = getepg2(item('epg2')[0].string)
                if desc == None:
                    raise
            except:               
                try:
                    desc = getepg4(item('epg4')[0].string)
                    if desc == None:
                        raise                                        
                except:
                    desc = ''

            try:
                genre = item('genre')[0].string
                if genre == None:
                    raise
            except:
                genre = ''

            try:
                date = item('date')[0].string
                if date == None:
                    raise
            except:
                date = ''
            try:
                addLink(url,name.encode('utf-8', 'ignore'),thumbnail,fanArt,desc,genre,date,True)
            except:
                print 'There was a problem adding link - '+name.encode('utf-8', 'ignore')


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
            params=sys.argv[2]
            cleanedparams=params.replace('?','')
            if (params[len(params)-1]=='/'):
                params=params[0:len(params)-2]
            pairsofparams=cleanedparams.split('&')
            param={}
            for i in range(len(pairsofparams)):
                splitparams={}
                splitparams=pairsofparams[i].split('=')
                if (len(splitparams))==2:
                    param[splitparams[0]]=splitparams[1]
        return param


def getFavorites():
        for i in json.loads(open(favorites).read()):
            name = i[0]
            url = i[1]
            iconimage = i[2]
            try:
                fanArt = i[3]
                if fanArt == None:
                    raise
            except:
                if __settings__.getSetting('use_thumb') == "true":
                    fanArt = iconimage
                else:
                    fanArt = fanart
            addLink(url,name,iconimage,fanArt,'','','')


def addFavorite(name,url,iconimage,fanart):
        favList = []
        if os.path.exists(favorites)==False:
            print 'Making Favorites File'
            favList.append((name,url,iconimage,fanart))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            print 'Appending Favorites'
            a = open(favorites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart))
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()


def rmFavorite(name):
        print 'Remove Favorite'
        a = open(favorites).read()
        data = json.loads(a)
        for index in range(len(data)):
            try:
                if data[index][0]==name:
                    del data[index]
                    b = open(favorites, "w")
                    b.write(json.dumps(data))
                    b.close()
            except:
                pass


def addDir(name,url,mode,iconimage,fanart,description,genre,date,showcontext=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "Date": date } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext == True:
            try:
                if name in str(SOURCES):
                    contextMenu = [('Remove from Sources','XBMC.Container.Update(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
                    liz.addContextMenuItems(contextMenu, True)
            except:
                pass
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addLink(url,name,iconimage,fanart,description,genre,date,showcontext=True):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "Date": date } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            try:
                if name in FAV:
                    contextMenu = [('Remove from LiveTV Favorites','XBMC.Container.Update(%s?mode=6&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
                else:
                    contextMenu = [('Add to LiveTV Favorites','XBMC.Container.Update(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart)))]
            except:
                contextMenu = [('Add to LiveTV Favorites','XBMC.Container.Update(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart)))]
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


  # Thanks to mikey1234, an epg scraper 
def getepg(link):
    req = urllib2.Request(link+'=&desc=1&day=0&from=now')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('"><b>(.+?)</b> <b>(.+?)</b>(.+?)</div>').findall(link)
    nowtime = match[0][0]
    nowtitle = match[0][1]
    nowdesc = match [0][2]
    nexttime = match[1][0]
    nexttitle = match[1][1]
    nextdesc = match [1][2]
    return "   -   %s" %(nowtitle)    
    
def getepg2(link):
    req = urllib2.Request(link+'=&desc=1&day=0&from=now')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('"><b>(.+?)</b> <b>(.+?)</b>(.+?)</div>').findall(link)
    nowtime = match[0][0]
    nowtitle = match[0][1]
    nowdesc = match [0][2]
    nexttime = match[1][0]
    nexttitle = match[1][1]
    nextdesc = match [1][2]
    return "[B][NOW] - %s[/B]\n%s\n\n[B][NEXT] - %s[/B]\n%s" %(nowtitle, nowdesc, nexttitle, nextdesc)    
    
def getepg3(link):
    req = urllib2.Request(link+'=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&desc=1&align=1&day=0&from=now')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('<b>(.+?)</b> <b><a href="http://uk.imdb.com/find(.+?)>(.+?)</a></b> <i>Film</i>\n(.+?)</div>').findall(link)
    nowtime = match[0][0]
    nowtitle = match[0][2]
    nowdesc = match [0][3]
    return "   -   %s" %(nowtitle)    
    
def getepg4(link):
    req = urllib2.Request(link+'=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&c=&desc=1&align=1&day=0&from=now')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    match=re.compile('<b>(.+?)</b> <b><a href="http://uk.imdb.com/find(.+?)>(.+?)</a></b> <i>Film</i>\n(.+?)</div>').findall(link)
    nowtitle = match[0][2]
    nowdesc = match [0][3]
    nexttime = match[1][0]
    nexttitle = match[1][2]
    nextdesc = match [1][3]
    return "[B][NOW] - %s[/B]\n%s\n\n[B][NEXT] - %s[/B]\n%s" %(nowtitle, nowdesc, nexttitle, nextdesc)    




xbmcplugin.setContent(int(sys.argv[1]), 'movies')
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass

params=get_params()

url=None
name=None
mode=None

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
    print "getSources"
    getSources()

elif mode==1:
    print "getData"
    getData(url,fanart)

elif mode==2:
    print "getChannelItems"
    getChannelItems(name,url,fanart)

elif mode==3:
    print ""
    getSubChannelItems(name,url,fanart)

elif mode==4:
    print ""
    getFavorites()

elif mode==5:
    print ""
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart)

elif mode==6:
    print ""
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
    
elif mode==7:
    print "addSource"
    addSource(url)

elif mode==8:
    print "rmSource"
    rmSource(name)

elif mode==9:
    print "getUpdate"
    getUpdate()
    
elif mode==10:
    print "getCommunitySources"
    getCommunitySources()
    
elif mode==11:
    print ""
    addSource(url)
    
elif mode==12:
    print ""

xbmcplugin.endOfDirectory(int(sys.argv[1]))