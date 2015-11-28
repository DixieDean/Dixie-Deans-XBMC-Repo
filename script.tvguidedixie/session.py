#
#      Copyright (C) 2014 Richard Dean
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

import xbmc
import xbmcaddon
import os
import dixie

import requests
import cookielib
import urllib
import urllib2
from urllib2 import HTTPError


def getUsername():
    return dixie.GetSetting('username')


def getPassword():
    return dixie.GetSetting('password')

def getAccount():
    return { 'log' : getUsername(), 'pwd' : getPassword(), 'wp-submit' : 'Log In' }


def getPayload():
    return urllib.urlencode(getAccount())

ADDON      = xbmcaddon.Addon(id = 'script.tvguidedixie')
baseurl    = dixie.GetLoginUrl()
datapath   = dixie.PROFILE
cookiepath = os.path.join(datapath, 'cookies')
cookiefile = os.path.join(cookiepath, 'on-tapp.lwp')


urlopen = urllib2.urlopen
Request = urllib2.Request
cj      = cookielib.LWPCookieJar()
opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

urllib2.install_opener(opener)


if not sfile.exists(cookiepath):
    try:    sfile.makedirs(cookiepath)
    except: pass


if sfile.exists(cookiefile):
    cj.load(cookiefile)


def resetCookie():
    try:
        if sfile.exists(cookiefile):
            sfile.remove(cookiefile)
    except:
        pass


def doLogin():
    code = 0
    try:
        payload = getPayload()
        req    = Request(baseurl, payload)
        handle = opener.open(req)
        code   = handle.getcode()

        for index, cookie in enumerate(cj):
            cj.save(cookiefile)
            print cookie
            return code

    except urllib2.HTTPError, error:
        if hasattr(error, 'code'):
            code = error.code
            
    return code


def checkFiles(url):
    url      = dixie.GetDixieUrl() + 'update.txt'
    request  = requests.get(url, allow_redirects=False, auth=(getUsername(), getPassword()))
    response = request.text
    code     = request.status_code
    reason   = request.reason
    
    dixie.log('----- Check OnTapp.TV Files -----')
    dixie.log('---------- status code ----------')
    dixie.Log(code)

    return code


def getFiles(url):
    url      = dixie.GetDixieUrl() + 'update.txt'
    request  = requests.get(url, allow_redirects=False, auth=(getUsername(), getPassword()))
    response = request.text

    return response