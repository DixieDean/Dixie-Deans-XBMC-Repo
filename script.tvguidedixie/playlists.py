 
import os
import requests
import urllib
import json
import io

import dixie
import mapping

PROFILE = dixie.PROFILE
PATH = os.path.join(PROFILE, 'plists')

inipath  = os.path.join(PROFILE, 'ini')

MAPFILE    = os.path.join(inipath, 'mappings.json')
MAPSFILE   = os.path.join(inipath, 'maps.json')
LABELFILE  = os.path.join(inipath, 'labels.json')
PREFIXFILE = os.path.join(inipath, 'prefixes.json')

try:
    mappings  = json.load(open(MAPFILE))
    maps      = json.load(open(MAPSFILE))
    labelmaps = json.load(open(LABELFILE))
    prefixes  = json.load(open(PREFIXFILE))
except:
    pass

def loadPlaylists():
    dixie.log('============= PLAYLISTS ============')
    try:
        if not os.path.exists(PATH):
            generatePlaylists()
        
        return json.load(io.open(PATH, encoding='utf-8'))

    except Exception as e:
        dixie.log('==== Playlist load error ====')
        dixie.log(e)
        return []

def generatePlaylists():
    source = dixie.GetSetting('iptv.source')
    if source == '0':
        return iptv_account()

    if source == '1':
        return manual_setup()

    raise Exception('Invalid value of %r for iptv.source setting' % source)

def iptv_account():
    the_list = []

    for i in range(0, 2):
        if dixie.GetSetting('IPTV_%d' % i) == 'true':
            IPTV_URL  = dixie.GetSetting('IPTV_%d_URL'  % i)
            IPTV_PORT = dixie.GetSetting('IPTV_%d_PORT' % i)
            IPTV_TYPE = dixie.GetSetting('IPTV_%d_TYPE' % i)
            IPTV_USER = dixie.GetSetting('IPTV_%d_USER' % i)
            IPTV_PASS = dixie.GetSetting('IPTV_%d_PASS' % i)
        
            if len(IPTV_URL) > 0:
                value = function8(IPTV_URL, IPTV_PORT, IPTV_TYPE, IPTV_USER, IPTV_PASS)
                the_list.append((value, 'IPTV%d: ' % (i+1)))
            
    return function4('URLS', the_list)

def manual_setup():
    the_list = []
    if dixie.GetSetting('playlist.type') == '0':
        if dixie.GetSetting('URL_O') == 'true':
            value = dixie.GetSetting('playlist.url')
            if value:
                the_list.append((value, 'URL1: '))
                
        if dixie.GetSetting('URL_1') == 'true':
            value = dixie.GetSetting('playlist.url1')
            if value:
                the_list.append((value, 'URL2: '))
                
        if dixie.GetSetting('URL_2') == 'true':
            value = dixie.GetSetting('playlist.url2')
            if value:
                the_list.append((value, 'URL3: '))

        dixie.log(the_list)
        
        return function4('URLS', the_list)

    if dixie.GetSetting('playlist.type') == '1':
        if dixie.GetSetting('FILE_0') == 'true':
            value = dixie.GetSetting('playlist.file')
            if value:
                the_list.append((value, 'FILE1: '))
                
        if dixie.GetSetting('FILE_1') == 'true':
            value = dixie.GetSetting('playlist.file1')
            if value:
                the_list.append((value, 'FILE2: '))
                
        if dixie.GetSetting('FILE_2') == 'true':
            value = dixie.GetSetting('playlist.file2')
            if value:
                the_list.append((value, 'FILE3: '))
                
        dixie.log(the_list)
        
        return function4('FILES', the_list)


def function3():  # doesn't appear to be called from anywhere
    urls = ['http://x.co/HEZ5ZyiJeW']

    is_playlist = False
    
    for url in urls:
        request = requests.get(url)
        content = request.content

        try:
            is_playlist = '#EXTM3U' in content
        except TypeError:
            try:
                is_playlist = '#EXTM3U' in content.decode()
            except:
                pass
        
        if is_playlist:
            return function4('CLOUD', [(url, '')])
        
def function4(playlist_type, plist):
    dixie.log(playlist_type)
    # dixie.log(plist)
    
    playlists = []
    
    for item in plist:
        url  = item[0]
        var2 = item[1]
        value = function5(playlist_type, url, var2)
        playlists.extend(value)
        
    json.dump(playlists, open(PATH, 'w'))
    
def function5(playlist_type, url, var2):
    content = function7(playlist_type, url)
    pairs   = []
    
    for i in range(1,len(content), 2):
        if is_valid(content[i+1]):
            var3 = content[i]
            var4 = content[i+1].rstrip()  # TODO no rstrip in other version??
            pairs.append([var3, var4])
            
    the_list = list()
    
    for item in pairs:
        item0 = item[0]
        item1 = item[1]
        
        var5 = item0.split(',')[-1].strip().upper()
        # var6 = dixie.cleanLabel(var5)
        # var7 = dixie.cleanPrefix(var6)
        # var8 = dixie.mapChannelName(var7)
        cleanlabel = mapping.cleanLabel(var5)
        tmplabel   = mapping.editPrefix(prefixes, cleanlabel)
        epglabel   = mapping.mapEPGLabel(prefixes, maps, tmplabel)
        
        value = item1.replace('rtmp://$OPT:rtmp-raw=', '').strip()
        # the_list.append((var2, var8, value))
        the_list.append((var2, epglabel, value))
        
    return the_list

def is_valid(link):
    if not link:
        return False

    link = link.strip()

    invalid = ['#EXT-X-ENDLIST', '/movie/', '/series/', '.mp4']

    for item in invalid:
        if item in link.lower():
            return False

    return True

def function7(playlist_type, url):
    if playlist_type == 'URLS' or playlist_type == 'CLOUD':
        response = requests.get(url)
        content  = io.StringIO(response.text)
        return content.readlines()

    if playlist_type == 'FILES':
        with io.open(url, encoding='utf-8') as content:
            return content.readlines()

def function8(url, port, ttype, user, password):
    if not url.startswith('http://'):
        url = 'http://' + url
        
    url += function9(port)
    url += '/get.php?username=%s' % user
    url += '&password=%s' % password
    url += '&type=m3u_plus&output='
    url += function10(ttype)
    
    return url

def function9(port):
    if port == '':
        return port

    return ':' + port

def function10(ttype):
    if ttype == '0':
        return 'm3u8'

    if ttype == '1':
        return 'mpegts'

if __name__ == '__main__':
    generatePlaylists()
