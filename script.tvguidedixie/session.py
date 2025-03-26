#
#      Copyright (C) 2018 On-Tapp-Networks Limited.
#

import dixie
import sfile

import platform
try:    original_ps = platform.system
except: original_ps = None

def platform_system():
    if original_ps:
        return original_ps()

    import sys
    if sys.platform.lower().startswith('win'):
        return 'Windows'

    return 'Other OSes to be determined'

platform.system = platform_system

import requests

platform.system = original_ps

import requests.utils
import pickle
import os

ADDON      = dixie.ADDON
datapath   = dixie.PROFILE
cookiepath = os.path.join(datapath, 'cookies')
cookiefile = os.path.join(cookiepath, 'cookies.txt')


import sys
path = dixie.RESOURCES
sys.path.insert(0, path)

import cfscrape

sfile.makedirs(cookiepath)


def getSession(silent=False):
    resetCookies()

    session = loadSession()

    if not silent:
        message = 'Logging into On-Tapp.TV'
        dixie.notify(message)
        #dixie.log(message)
    try:
        session.get(dixie.GetLoginUrl(), verify=False)
    except:
        return False

    PAYLOAD  = { 'log' : dixie.GetUser(), 'pwd' : dixie.GetPass(), 'wp-submit' : 'Log In' }
    response = 'login_error'
    code     =  0

    try:
        login    = session.post(dixie.GetLoginUrl(), data=PAYLOAD, verify=False)
        cookies  = session.cookies

        response = login.content
        code     = login.status_code

        saveCookies(cookies, cookiefile)

        #dixie.log('===== login code =====')
        #dixie.log(code)

        return code, response

    except:
        return False, False


def loadSession():
    status = checkStatus()

    if status == 503:
        #dixie.log('======== USING CFSCRAPE ========')
        return cfscrape.create_scraper()

    #dixie.log('======== USING REQUESTS ========')
    return requests.Session()


def resetSession():
    #dixie.log('************** RESET SESSION **************')
    getSession(silent=False)


def checkStatus():
    url = 'https://www.on-tapp.tv'
    request = requests.head(url)

    #dixie.log('======== checkStatus ========')
    #dixie.log(request.status_code)
    return request.status_code


def resetCookies():
    #dixie.log('======== session - reset cookies ========')
    sfile.remove(cookiefile)


def saveCookies(cookies, filename):
    try:
        with open(filename, 'w') as f:
            pickle.dump(requests.utils.dict_from_cookiejar(cookies), f)
    except Exception, e:
        #dixie.log('******* SAVE COOKIES EXCEPTION *******')
        dixie.log(e)


def loadCookies(filename):
    #dixie.log('******* LOAD COOKIES *******')

    if not os.path.isfile(cookiefile):
        #dixie.log('******* COOKIE MISSING *******')
        getSession(silent=False)

    try:
        with open(filename) as f:
            return requests.utils.cookiejar_from_dict(pickle.load(f))
    except Exception, e:
        #dixie.log('******* LOAD COOKIES EXCEPTION *******')
        dixie.log(e)
