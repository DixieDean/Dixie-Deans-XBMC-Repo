#
#      Copyright (C) 2016 Richard Dean (write2dixie@gmail.com)
#

import os
import xbmc
import dixie
import resources

from resources.pastebin_python import PastebinPython
from resources.pastebin_python.pastebin_exceptions   import PastebinBadRequestException, PastebinNoPastesException, PastebinFileException
from resources.pastebin_python.pastebin_constants    import PASTE_PUBLIC, EXPIRE_10_MIN, EXPIRE_1_DAY, EXPIRE_1_MONTH, EXPIRE_1_WEEK, PASTE_UNLISTED
from resources.pastebin_python.pastebin_formats      import FORMAT_NONE, FORMAT_PYTHON, FORMAT_HTML


def LogUploader():
    kodilogs = getLogfiles()
    ottvlog  = getOTTVfile()

    try:
        for log in kodilogs:
            doPaste(log)

        logcode = doPaste(ottvlog)
        dixie.DialogOK('This is your log code: [COLOR orange][B]' + logcode + '[/B][/COLOR]', 'Write it down and send it to us via our forum.', 'Or email it to us with your support question: support@on-tapp.tv')

    except: pass


def doPaste(logfile):
    pastebin = PastebinPython(api_dev_key='82ab1f8053f13f84beea0d1c933f48f2')

    try:
        dixie.log('------------ UPLOAD LOG ------------')
        dixie.log(logfile)

        pastebin.createAPIUserKey('OnTappNetworks', 'ontapp123')
        paste   = pastebin.createPasteFromFile(logfile, 'On-Tapp-Networks Logfiles', FORMAT_HTML, PASTE_UNLISTED, EXPIRE_1_DAY)
        logcode = paste.rsplit('/', 1)[-1]

        dixie.log(logcode)
        dixie.log(paste)

    except PastebinBadRequestException as e:
        showError(e.message)
        return ''
    except PastebinFileException as e:
        showError(e.message)
        return ''

    return logcode


def showError(error):
    dixie.log(error)
    dixie.DialogOK('Sorry, the following error occurred:', '[COLOR orange][B]' + error + '[/B][/COLOR]', 'Restart Kodi and try again.')


def getOTTVfile():
    ottv = os.path.join(dixie.PROFILE, 'log.txt')

    if os.path.isfile(ottv):
        dixie.log('======= On-Tapp.TV log.txt path is =======')
        dixie.log(ottv)
        return ottv

    return ''


def getLogfiles():
    path = xbmc.translatePath('special://logpath')
    old  = os.path.join(path, 'xbmc.log')
    kodi = os.path.join(path, 'kodi.log')
    spmc = os.path.join(path, 'spmc.log')

    logfiles = []

    if os.path.isfile(old):
        dixie.log('======= XBMC log path is =======')
        dixie.log(old)
        oldlog = os.path.join(path, 'xbmc.old.log')
        logfiles.append(old)
        logfiles.append(oldlog)

        return logfiles

    if os.path.isfile(kodi):
        dixie.log('======= KODI log path is =======')
        dixie.log(kodi)
        oldlog = os.path.join(path, 'kodi.old.log')
        logfiles.append(kodi)
        logfiles.append(oldlog)

        return logfiles

    if os.path.isfile(spmc):
        dixie.log('======= SPMC log path is =======')
        dixie.log(spmc)
        oldlog = os.path.join(path, 'spmc.old.log')
        logfiles.append(spmc)
        logfiles.append(oldlog)

        return logfiles

    return ''


if __name__ == '__main__':
    dixie.ShowBusy()
    LogUploader()
    dixie.CloseBusy()
