#
#      Copyright (C) 2014 mikey1234
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
ADDON = xbmcaddon.Addon(id='plugin.video.ontapp-player')



def CATEGORIES():
    addDir('iPlayer A-Z','url',3,'','')
    addDir('Live','url',2,'','')


 
       
                                                                      
def char_range(c1, c2):
    
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)
 
    
def GetLive(url):
     
    channel_list = [
                            ('bbc_one_london','bbc_one', 'BBC One'),
                            ('bbc_two_england', 'bbc_two', 'BBC Two'),
                            ('bbc_three','bbc_three', 'BBC Three'),
                            ('bbc_four','bbc_four', 'BBC Four'),
                            ('bbc_four','cbbc', 'CBBC'),
                            ('bbc_three','cbeebies', 'CBeebies'),
                            ('bbc_news24','bbc_news24', 'BBC News Channel'),
                            ('bbc_parliament','bbc_parliament', 'BBC Parliament'),
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
    match=re.compile('<a href="/iplayer/brand/(.+?)".+?<span class="title">(.+?)</span>').findall (link)
    for URL , name in match:
        url='http://www.bbc.co.uk/iplayer/episodes/%s' %URL
        addDir(name,url,4,'','')


def GetEpisodes(url):
    
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
            print name
            print _URL_
            addDir(name,_URL_,5,iconimage.replace('336x189','832x468') ,plot)        



def GetPlayable(name,url,iconimage):

    _NAME_=name
    if 'plugin.video.ontapp-player' in iconimage:

        vpid=url

    else:    
        html = OPEN_URL(url)
      
        vpid=re.compile('"vpid":"(.+?)"').findall(html)[0]
    


    NEW_URL= "http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/pc/vpid/%s" % vpid

    html = OPEN_URL(NEW_URL)

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

    NEW_URL = 'http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/pc/vpid/%s' % url  
    html = OPEN_URL(NEW_URL)

    match=re.compile('application="(.+?)".+?authString="(.+?)".+?identifier="(.+?)".+?protocol="(.+?)".+?server="(.+?)".+?supplier="(.+?)"').findall(html.replace('amp;',''))

    for app,auth , playpath ,protocol ,server,supplier in match:

        port = '1935'
        if protocol == 'rtmpt': port = 80
        if supplier == 'limelight':
            url="%s://%s:%s/ app=%s?%s tcurl=%s://%s:%s/%s?%s playpath=%s live=1" % (protocol,server,port,app,auth,protocol,server,port,app,auth,playpath)

            
        else:
           url="%s://%s:%s/%s?%s playpath=%s?%s live=1" % (protocol,server,port,app,auth,playpath,auth)
           
        
        res=playpath.split('inlet_')[1]
        if '@' in res:
            res=res.split('@')[0]
            
        if int(res) > 1400 :
            TITLE=_NAME_+'- [COLOR white]%s[/COLOR]- [COLOR green][%s kbps][/COLOR]'%(supplier.upper(),res)
        else:
            TITLE=_NAME_+'- [COLOR white]%s[/COLOR] - [COLOR red][%s kbps][/COLOR]'%(supplier.upper(),res)
            
        addDir(TITLE,url,200,iconimage,'') 

            

        #self.AddLiveLink( list, id.replace('_',' ').upper(), url, language = language.title(),host= 'BBC iPLAYER '+supplier,quality=quality_dict.get(res, 'NA'))       
 
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
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

def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        print name + '=' + u
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        if mode ==200:
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
        
elif mode==200:

        PLAY_STREAM(name,url,iconimage)
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
