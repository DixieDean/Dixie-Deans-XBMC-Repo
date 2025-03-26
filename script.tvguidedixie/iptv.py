#
# Copyright (C) 2015 Sean Poyser and Richard Dean

import xbmc
import xbmcaddon
import json
import time
import datetime
import urllib
import os

import dixie

PATH    = os.path.join(dixie.PROFILE, 'iptv_channels')
SETTING = 'LOGIN_IPTV'

def getURL(url):
    if dixie.validTime(SETTING, 60 * 60 * 24): #24 hours
        response = json.load(open(PATH))
    else:
        response = getIPTVJSON()
        setTimeToNow(SETTING)
    
    stream = url.split(':', 1)[-1].lower()
    
    try:
        result = response['result']
        files  = result['files']

    except Exception as e:
        catchException(e)
        return None


    for file in files:
        label = file['label']

        if stream == label.lower():
            return file['file']

    return None


def getIPTVJSON():
    AddonID = 'plugin.video.stalker'
    Addon   =  xbmcaddon.Addon(AddonID)
    
    MAC   =  Addon.getSetting('portal_mac_1')
    root  = 'plugin://plugin.video.stalker/?genre_name=All&portal='
    query = ('{"name": "NFPS", "parental": "false", "url": "http://portal.iptvprivateserver.tv", "mac": "%s", "serial": {"custom": false}, "password": "0000"}' % MAC)
    url   =  urllib.quote_plus(query)
    param =  root + url + '&mode=channels&genre_id=*'
    login    = ('{"jsonrpc":"2.0", "method":"Files.GetDirectory", "params":{"directory":"plugin://plugin.video.stalker"}, "id": 1}')
    jsonrpc  = ('{"jsonrpc":"2.0", "method":"Files.GetDirectory", "params":{"directory":"%s"}, "id": 1}' % param)
    

    try:
        message = 'Logging into server. One moment please.'
        dixie.notify(message)
        dixie.ShowBusy()
        xbmc.executeJSONRPC(login)
        response = xbmc.executeJSONRPC(jsonrpc)
        
        dixie.CloseBusy()
    
        content = json.loads(response.decode('utf-8', 'ignore'))
    
        json.dump(content, open(PATH,'w'))

        return content
    
    except Exception as e:
        catchException(e)
        return {'Error' : 'Plugin Error'}


def setTimeToNow(setting):
    now = datetime.datetime.today()
    dixie.SetSetting(setting, str(now))


def catchException(e):
    line1 = 'Sorry, an error occured: JSON Error: %s'  %e
    line2 = 'Please re-link this channel and try again.'
    line3 = 'Use: Context Menu => Remove Stream'
    
    dixie.log(e)
    dixie.DialogOK(line1, line2, line3)    
    dixie.SetSetting(SETTING, '')
