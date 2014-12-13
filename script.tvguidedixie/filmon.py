#
#      Copyright (C) 2014 Sean Poyser
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


import xbmc
import xbmcgui
import xbmcaddon

import dixie

import urllib2
import re
import json
import os
import datetime
from hashlib import md5

from threading import Timer


global TheTimer, LoggedIn, SessionID, GMTOFFSET
TheTimer  = None
LoggedIn  = False
SessionID = 0
GMTOFFSET = 0


#http://www.filmon.tv/page/api

ADDON = dixie.ADDON
HOME  = ADDON.getAddonInfo('path')
ICON  = os.path.join(HOME, 'icon.png')
ICON  = xbmc.translatePath(ICON)
TITLE = dixie.TITLE

BASE           = 'http://www.filmon.com/'
INIT_URL       =  BASE + 'api/init/'
LOGIN_URL      =  BASE + 'api/login?session_key=%s&login=%s&password=%s'
LOGOUT_URL     =  BASE + 'api/logout?session_key=%s'
RECORD_URL     =  BASE + 'api/dvr-add?session_key=%s&channel_id=%s&programme_id=%s&start_time=%s'
RECORDINGS_URL =  BASE + 'api/dvr-list?session_key=%s'
GUIDE_URL      =  BASE + 'tv/api/tvguide/%s?session_key=%s'

INTERVAL = 275 #Filmon timeout is actually 300

try:
    ftv      = xbmcaddon.Addon('plugin.video.F.T.V')
    USERNAME = ftv.getSetting('filmon_user')
    PASSWORD = ftv.getSetting('filmon_pass')
    PASSWORD = md5(PASSWORD).hexdigest()

    AVAILABLE = len(USERNAME) > 0 and len(PASSWORD) > 0
except:
    AVAILABLE = False


def notify(message, length=5000):
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)


def getUserAgent():
    return ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'


def getHTML(url):
    global GMTOFFSET
    try:
        req  = urllib2.Request(url)
        req.add_header('User-Agent', getUserAgent())
        resp = urllib2.urlopen(req, timeout=10)
  
        headers = resp.headers
        gmt     = headers['Date'].split(', ')[-1]
        gmt     = datetime.datetime.strptime(gmt, '%d %b %Y %H:%M:%S GMT')

        GMTOFFSET = gmt - datetime.datetime.today()
        GMTOFFSET = ((GMTOFFSET.days * 86400) + (GMTOFFSET.seconds + 1800)) / 3600        
        GMTOFFSET *= -3600

        html = resp.read()
        resp.close()
        return html
    except:
        return ''


def initialise():
    if (not USERNAME) or (not PASSWORD):
        return

    killTimer()
        
    try:
        global SessionID
        SessionID = 0
        response  = getHTML(INIT_URL)
        SessionID = re.compile('"session_key":"(.+?)"').search(response).group(1)
    except:
        pass


def login():
    global TheTimer, LoggedIn, SessionID

    LoggedIn = False

    if SessionID == 0:
        initialise()

    url   = LOGIN_URL % (SessionID, USERNAME, PASSWORD)
    login = getHTML(url)

    LoggedIn = len(login) > 0

    if LoggedIn:
        message = 'Logged into Filmon'
    else:
        message = 'Failed to Log into Filmon'

    #notify(message)

    if LoggedIn:
        TheTimer = Timer(INTERVAL, logout)
        TheTimer.start()


def killTimer():
    global TheTimer
    if TheTimer:
        TheTimer.cancel()
        del TheTimer
        TheTimer = None


def logout():
    killTimer()

    global LoggedIn, SessionID
    if not LoggedIn:
        return

    id = SessionID

    LoggedIn  = False
    SessionID = 0

    try:
        url    = LOGOUT_URL % id
        logout = getHTML(url)

        jsn  = json.loads(logout)
        if 'success' in jsn:
            LoggedIn = not jsn['success']

        if LoggedIn:
            print 'Failed to Logout of Filmon'
        else:
            print 'Logged out of Filmon'
            
    except:
        pass


def convertToUnixTS(when):
    global GMTOFFSET
    start   = datetime.datetime(1970, 1, 1)
    delta   = when - start
    seconds = (delta.days * 86400) + delta.seconds
    return seconds - GMTOFFSET


def getGuide(channel):
    global SessionID
    try:

        if SessionID == 0:
            return None

        return getHTML(GUIDE_URL % (channel, SessionID))

    except:
        return None


def getChannel(streamURL):
    try:    
        return int(re.compile('url=(.+?)&').search(streamURL).group(1))
    except:
        pass

    try:
        chID = streamURL.rsplit('ch_fanart=', 1)[-1]
        chID = int(chID.split('<>', 1)[0])
        return chID
    except:
        return None


def getProgram(channel, start):
    try:
        startTS = convertToUnixTS(start)

        guide = getGuide(channel)
        if not guide:
            return None

        text  = '","startdatetime":"%s"' % startTS
        guide = guide.split(text)[0]
        guide = guide.rsplit('{"programme":"', 1)[-1]

        return guide

    except:
        pass

    return None


def verifyLogin():
    global LoggedIn

    if not LoggedIn:
        login()

    if not LoggedIn:
        dixie.DialogOK('Not logged into Filmon.', 'Please check details and try again.')
        return False

    return True

    
def record(name, start, end, streamURL, showResult=True):
    if not verifyLogin():
        return False

    global SessionID

    channel = getChannel(streamURL)
    if not channel:
        dixie.DialogOK('No valid channel found in stream.', 'Please edit stream and try again.')
        return False

    program = getProgram(channel, start)
    if not program:
        dixie.DialogOK('Program not found in Filmon guide.')
        return False

    url     = RECORD_URL % (SessionID, channel, program, convertToUnixTS(start))
    record  = getHTML(url)
    success = False

    try:
        jsn = json.loads(record)

        if 'success' in jsn:
           success = jsn['success']
    except:        
        pass

    if not showResult:
        return program

    if success:
        if end < datetime.datetime.today():
            dixie.DialogOK(name, 'Has been recorded.')
        else:
            dixie.DialogOK(name, 'Has been scheduled to be recorded.')
    else:
        dixie.DialogOK('Failed to schedule recording.')

    return program


def getRecording(programID):
    if not verifyLogin():
        return False

    global SessionID

    url        = RECORDINGS_URL % SessionID
    recordings = getHTML(url)
    recordings = json.loads(recordings)
    recordings = recordings['recordings']
    
    for recording in recordings:
        images = recording['images']
        poster = images['poster']
        if programID in poster:
            return recording['download_url']

    return None