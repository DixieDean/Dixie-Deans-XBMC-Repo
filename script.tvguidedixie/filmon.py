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


global TheTimer, LoggedIn, SessionID
TheTimer  = None
LoggedIn  = False
SessionID = 0


#http://www.filmon.tv/page/api

ADDON = dixie.ADDON
HOME  = ADDON.getAddonInfo('path')
ICON  = os.path.join(HOME, 'icon.png')
ICON  = xbmc.translatePath(ICON)
TITLE = dixie.TITLE

BASE        = 'http://www.filmon.com/'
INIT_URL    =  BASE + 'api/init/'
LOGIN_URL   =  BASE + 'api/login?session_key=%s&login=%s&password=%s'
LOGOUT_URL  =  BASE + 'api/logout?session_key=%s'
RECORD_URL  =  BASE + 'api/dvr-add?session_key=%s&channel_id=%s&programme_id=%s&start_time=%s'
GUIDE_URL   =  BASE + 'tv/api/tvguide/%s?session_key=%s'

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
    try:
        req  = urllib2.Request(url)
        req.add_header('User-Agent', getUserAgent())
        resp = urllib2.urlopen(req)
        html = resp.read()
        resp.close()
        return html
    except:
        return ''


def initialise():
    if (not USERNAME) or (not PASSWORD):
        print 'No Filmon login details'
        return

    print "IN INITIALISE"
    killTimer()
        
    try:
        global SessionID
        SessionID = 0
        response  = getHTML(INIT_URL)
        SessionID = re.compile('"session_key":"(.+?)"').search(response).group(1)

    except Exception, e:
        print str(e)


def login():
    global TheTimer, LoggedIn, SessionID

    LoggedIn = False

    if SessionID == 0:
        initialise()

    url   = LOGIN_URL % (SessionID, USERNAME, PASSWORD)
    print "LOGIN"
    print url
    login = getHTML(url)

    LoggedIn = len(login) > 0

    if LoggedIn:
        message = 'Logged into Filmon'
    else:
        message = 'Failed to Log into Filmon'

    print message
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
    print "NOW IN LOGOUT"
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

        print "LOGGED OUT RESULT"
        print logout
        print jsn

        if LoggedIn:
            print 'Failed to Logout of Filmon'
        else:
            print 'Logged out of Filmon'
            
    except Exception, e:
        print "EEEEEEEE"
        print str(e)
        pass


def regex_from_to(text, from_string, to_string, excluding=True):
    if excluding:
        r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
    else:
        r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
    return r


def convertToUnixTS(when):
    start   = datetime.datetime(1970, 1, 1)
    delta   = when - start
    seconds = (delta.days * 86400) + delta.seconds
    return seconds


def getGuide(channel):
    global SessionID
    try:

        if SessionID == 0:
            return None

        return getHTML(GUIDE_URL % (channel, SessionID))

    except Exception, e:
        print str(e)
        return None


def getChannel(streamURL):
    try:    return int(re.compile('url=(.+?)&').search(streamURL).group(1))
    except: return None


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

    except Exception, e:
        print "ERROR IN getProgram"
        print str(e)

    return None


    
def record(name, start, streamURL):
    global LoggedIn, SessionID

    if not LoggedIn:
        print "NOT LOGGED IN IN RECORDING"
        login()

    if not LoggedIn:
        dixie.DialogOK('Not logged into Filmon.', 'Please check details and try again.')
        return

    channel = getChannel(streamURL)
    if not channel:
        dixie.DialogOK('No valid channel found in stream.', 'Please edit stream and try again.')
        return

    program = getProgram(channel, start)
    if not program:
        dixie.DialogOK('Program not found in Filmon guide.')
        return

    url     = RECORD_URL % (SessionID, channel, program, convertToUnixTS(start))
    print "RECORDING URL"
    print url
    record  = getHTML(url)
    print record
    success = False

    try:
        jsn = json.loads(record)
        print jsn
        if 'success' in jsn:
           success = jsn['success']
    except:        
        pass

    if success:
        dixie.DialogOK(name, 'has been scheduled to be recorded.')
    else:
        dixie.DialogOK('Failed to schedule recording.')