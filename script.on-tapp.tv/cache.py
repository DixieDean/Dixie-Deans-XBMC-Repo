
#       Copyright (C) 2013
#       Sean Poyser (seanpoyser@gmail.com)
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

import os
import time
import glob
import urllib2

import utilsOTT as utils
import xbmc


CacheDir  = xbmc.translatePath(os.path.join(utils.PROFILE, 'c'))
CacheSize = 100


def clearCache():
    try:
        import shutil
        shutil.rmtree(CacheDir)
        while os.path.isdir(CacheDir):
            xbmc.sleep(50)
        checkCacheDir()
    except: pass


def checkCacheDir():
    try:
        if not os.path.isdir(CacheDir):
            os.makedirs(CacheDir)
    except:
        pass


def getURLNoCache(url, agent=None, tidy=True):
    req = urllib2.Request(url)
    if agent:
        req.add_header('User-Agent', agent)

    response = urllib2.urlopen(req)
    html     = response.read()
    response.close()

    if tidy:
        html = html.replace('\r', '').replace('\n', '').replace('\t', '')

    return html


def getURL(url, maxSec=0, agent=None, tidy=True):
    purgeCache()
    
    if url == None:
        return None

    if maxSec > 0:
        timestamp = getTimestamp(url)
        if timestamp > 0:
            if (time.time() - timestamp) <= maxSec:
                return getCachedData(url)
			
    try:    data = getURLNoCache(url, agent, tidy)
    except: data = ''

    addToCache(url, data)
    return data


def getTimestamp(url):
    cacheKey  = createKey(url)
    cachePath = os.path.join(CacheDir, cacheKey)

    if os.path.isfile(cachePath):
        try:    return os.path.getmtime(cachePath)
        except: pass

    return 0


def getCachedData(url):
    cacheKey  = createKey(url)
    cachePath = os.path.join(CacheDir, cacheKey)
    f         = file(cachePath, 'r')

    data = f.read()
    f.close()

    return data


def addToCache(url, data):
    if len(data) < 100:
        return

    checkCacheDir()

    cacheKey  = createKey(url)
    cachePath = os.path.join(CacheDir, cacheKey)
    f         = file(cachePath, 'w')

    f.write(data)
    f.close()

    purgeCache()


def createKey(url):
    try:
        from hashlib import md5
        return md5(url).hexdigest()
    except:
        import md5
        return md5.new(url).hexdigest()

        
def purgeCache():
    files  = glob.glob(os.path.join(CacheDir, '*'))
    nFiles = len(files)

    try:
        while nFiles > gCacheSize:            
            oldestFile = getOldestFile(files)
            path       = os.path.join(CacheDir, oldestFile)
 
            while os.path.exists(path):
                try:    os.remove(path)
                except: pass

            files  = glob.glob(os.path.join(CacheDir, '*'))
            nFiles = len(files)
    except:
        pass


def getOldestFile(files):
    if not files:
        return None
    
    now    = time.time()
    oldest = files[0], now - os.path.getctime(files[0])

    for f in files[1:]:
        age = now - os.path.getctime(f)
        if age > oldest[1]:
            oldest = f, age

    return oldest[0]