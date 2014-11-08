#
#      Copyright (C) 2014 Mikey1234
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

import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os


#ee3fa
ADDONID = 'plugin.video.ontapp-player'
ADDON   =  xbmcaddon.Addon(ADDONID)



def CATEGORIES():
    addDir('Most Popular','http://www.bbc.co.uk/iplayer/group/most-popular',10,'','')
    addDir('iPlayer A-Z','url',3,'','')
    addDir('Categories','url',7,'','')
    addDir('Search','url',9,'','')
    addDir('Live','url',2,'','')


 
       
                                                                      
def char_range(c1, c2):
    
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)
 
    
def GetLive(url):
     
    channel_list = [
                            ('bbc1','bbc_one', 'BBC One'),
                            ('bbc2', 'bbc_two', 'BBC Two'),
                            ('bbc3','bbc_three', 'BBC Three'),
                            ('bbc4','bbc_four', 'BBC Four'),
                            ('cbbc','cbbc', 'CBBC'),
                            ('cbeebies','cbeebies', 'CBeebies'),
                            ('news_ch','bbc_news24', 'BBC News Channel'),
                            ('parliament','bbc_parliament', 'BBC Parliament'),
                            ('alba','bbc_alba', 'Alba'),
                        ]
    for id, img, name in channel_list :
        iconimage = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.ontapp-player/img',img+'.png'))
        addDir(name,id,6,iconimage,'')       

def GetContent(url):
    nameurl=[]
    urlurl=[]
    for name in char_range('A', 'Z'):
        nameurl.append(name)
        urlurl.append(name.lower())
        
    link=OPEN_URL('http://www.bbc.co.uk/iplayer/a-z/%s'%urlurl[xbmcgui.Dialog().select('Please Select', nameurl)])
    match=re.compile('<a href="/iplayer/brand/(.+?)".+?<span class="title">(.+?)</span>',re.DOTALL).findall (link)
    for url , name in match:
        
        addDir(name,url,4,'','')


def NextPageGenre(url):
    NEW_URL=url
    html=OPEN_URL(NEW_URL)

    match1=re.compile('data-ip-id="(.+?)">.+?href="(.+?)" title="(.+?)".+?img src="(.+?)".+?<p class="synopsis">(.+?)</p>',re.DOTALL).findall (html)
    for IPID ,URL , name , iconimage, plot in match1:
        try:
            getseries=html.split(URL)[1]
            number=re.compile('<em>(.+?)</em>').findall(getseries)[0]

            if not IPID in URL:
                name='%s - [COLOR orange](%s Available)[/COLOR]' % (name,number.strip())
        except:
            name=name    
        _URL_='http://www.bbc.co.uk%s' %URL
        if not IPID in _URL_:
            IPID=IPID
        else:
            IPID=''
        
        addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)    
    try:
        nextpage=re.compile('<span class="next txt"><a href="(.+?)">Next <span').findall (html)[0].replace('amp;','')
        if not nextpage in NEW_URL:
            _URL_='http://www.bbc.co.uk'+nextpage
            addDir('[COLOR blue]>> Next Page >>[/COLOR]',_URL_,8,'' ,'','')
    except:pass


    


def Genre(url):
    nameurl=[]
    urlurl=[]
    link=OPEN_URL('http://www.bbc.co.uk/iplayer').split('Categories</h2>')[1]

    match=re.compile('<a href="(.+?)" class="stat">(.+?)</a>').findall(link)
    for url , name in match:
        import HTMLParser
        h = HTMLParser.HTMLParser()
        nameurl.append(h.unescape(name))
        urlurl.append(url)
    
    NEW_URL='http://www.bbc.co.uk%s/all?sort=dateavailable'%urlurl[xbmcgui.Dialog().select('Please Select Category', nameurl)]    
    html=OPEN_URL(NEW_URL)
    match1=re.compile('data-ip-id="(.+?)">.+?href="(.+?)" title="(.+?)".+?img src="(.+?)".+?<p class="synopsis">(.+?)</p>',re.DOTALL).findall (html)
    for IPID ,URL , name , iconimage, plot in match1:
        try:
            getseries=html.split(URL)[1]
            number=re.compile('<em>(.+?)</em>').findall(getseries)[0]

            if not IPID in URL:
                name='%s - [COLOR orange](%s Available)[/COLOR]' % (name,number.strip())
        except:
            name=name    
        _URL_='http://www.bbc.co.uk%s' %URL
        if not IPID in _URL_:
            IPID=IPID
        else:
            IPID=''
        
        addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)    
    try:
        nextpage=re.compile('<span class="next txt"><a href="(.+?)">Next <span').findall (html)[0].replace('amp;','')
        if not nextpage in NEW_URL:
            _URL_='http://www.bbc.co.uk'+nextpage
            addDir('[COLOR blue]>> Next Page >>[/COLOR]',_URL_,8,'' ,'','')
    except:pass          
         

def POPULAR(url):
    NEW_URL=url
    html=OPEN_URL(NEW_URL)

    match1=re.compile('data-ip-id="(.+?)">.+?href="(.+?)" title="(.+?)".+?img src="(.+?)".+?<p class="synopsis">(.+?)</p>',re.DOTALL).findall (html)
    for IPID ,URL , name , iconimage, plot in match1:
        try:
            getseries=html.split(URL)[1]
            number=re.compile('<em>(.+?)</em>').findall(getseries)[0]

            if not IPID in URL:
                name='%s - [COLOR orange](%s Available)[/COLOR]' % (name,number.strip())
        except:
            name=name    
        _URL_='http://www.bbc.co.uk%s' %URL
        if not IPID in _URL_:
            IPID=IPID
        else:
            IPID=''
        
        addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot,IPID)


def Search(url):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Search iPlayer')
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText() .replace(' ','%20')  # sometimes you need to replace spaces with + or %20
            if search_entered == None:
                return False  
        NEW_URL='http://www.bbc.co.uk/iplayer/search?q=%s'%search_entered
        NextPageGenre(NEW_URL)


def GetEpisodes(url):

    url='http://www.bbc.co.uk/iplayer/episodes/%s' %url
    link=OPEN_URL(url)

    match=re.compile('data-ip-id=".+?">.+?<a href="(.+?)" title="(.+?)".+?data-ip-src="(.+?)">.+?class="synopsis">(.+?)</p>',re.DOTALL).findall (link)
    if len(match)==1:
        _URL_='http://www.bbc.co.uk/%s' %match[0][0]
        name=match[0][1]
        iconimage=match[0][2].replace('336x189','832x468')      

        GetPlayable(name,_URL_,iconimage)
    else:    
        for URL , name , iconimage, plot in match:
            _URL_='http://www.bbc.co.uk/%s' %URL

            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot)        



def GetPlayable(name,url,iconimage):

    _NAME_=name
    if 'plugin.video.ontapp-player' in iconimage:

        vpid=url

    else:    
        html = OPEN_URL(url)
      
        vpid=re.compile('"vpid":"(.+?)"').findall(html)[0]
    


    NEW_URL= "http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/pc/vpid/%s" % vpid

    html = OPEN_URL(NEW_URL,True)

    match=re.compile('application="(.+?)".+?String="(.+?)".+?identifier="(.+?)".+?protocol="(.+?)".+?server="(.+?)".+?supplier="(.+?)"').findall(html.replace('amp;',''))
    for app,auth , playpath ,protocol ,server,supplier in match:

        port = '1935'
        if protocol == 'rtmpt': port = 80
        if supplier == 'limelight':
            url="%s://%s:%s/ app=%s?%s tcurl=%s://%s:%s/%s?%s playpath=%s" % (protocol,server,port,app,auth,protocol,server,port,app,auth,playpath)
            res=playpath.split('secure_auth/')[1]
            
        else:
           url="%s://%s:%s/%s?%s playpath=%s?%s" % (protocol,server,port,app,auth,playpath,auth)
           
        if supplier == 'akamai':
            res=playpath.split('secure/')[1]
            
        if supplier == 'level3':
            res=playpath.split('mp4:')[1]
            
        resolution=res.split('kbps')[0]
        if int(resolution) > 1400 :
            TITLE=_NAME_+'- [COLOR white]%s[/COLOR]- [COLOR green][%s kbps][/COLOR]'%(supplier.upper(),resolution)
        else:
            TITLE=_NAME_+'- [COLOR white]%s[/COLOR] - [COLOR red][%s kbps][/COLOR]'%(supplier.upper(),resolution)
        addDir(TITLE,url,200,iconimage,'') 



def GetLivePlayable(name,url,iconimage):

    _NAME_=name

    NEW_URL = 'http://a.files.bbci.co.uk/media/live/manifests/hds/pc/llnw/%s.f4m' % url  
    html = OPEN_URL(NEW_URL,True)

    match=re.compile('href="(.+?)"').findall(html.replace('amp;',''))
    item=len(match)-1
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(match[item].replace('f4m','m3u8'))
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

            

        #self.AddLiveLink( list, id.replace('_',' ').upper(), url, language = language.title(),host= 'BBC iPLAYER '+supplier,quality=quality_dict.get(res, 'NA'))       
 
def OPEN_URL(url,resolve=False):
    if ADDON.getSetting('proxy')=='false':
        req = urllib2.Request(url)
    else:
        if resolve==True:
            import base64
            print 'RESOLVING'
            req = urllib2.Request('http://www.justproxy.co.uk/index.php?q='+base64.b64encode(url))
        else:
            req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    dp = xbmcgui.DialogProgress()
    dp.create('On-Tapp.TV Player', 'Opening ' + name.upper())
    return link
    
    
    
def PLAY_STREAM(name,url,iconimage):
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
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

def addDir(name,url,mode,iconimage,description,IPID=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)+"&IPID="+urllib.quote_plus(IPID)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        menu=[]
        if not IPID == '':
            menu.append(('[COLOR orange]Grab All Episodes[/COLOR]','XBMC.Container.Update(%s?mode=4&url=%s)'% (sys.argv[0],IPID)))  
            liz.addContextMenuItems(items=menu, replaceItems=False)
        if mode ==200 or mode ==6:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
        
 
        
def setView(content, viewType):
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
IPID=None

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
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
try:
        IPID=urllib.unquote_plus(params["IPID"])
except:
        pass    

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        GetMain(url)

elif mode==2:
        print ""+url
        GetLive(url)        
        
elif mode==3:
        print ""+url
        GetContent(url)
     
elif mode==4:
        print ""+url
        GetEpisodes(url)

elif mode==5:
        GetPlayable(name,url,iconimage)

elif mode==6:
        GetLivePlayable(name,url,iconimage)

elif mode==7:
        Genre(url)


elif mode==8:
        NextPageGenre(url)  


elif mode==9:
        Search(url)

elif mode==10:
        POPULAR(url)         
        
elif mode==200:

        PLAY_STREAM(name,url,iconimage)
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
