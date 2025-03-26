#
#  Copyright (C) 2016
#  On-Tapp-Networks
#


import xbmc
import sfile
import dixie
import channel
import os


def getList(url, query, result):
    import session
    session  = session.loadSession()
    request  = session.get(url).json()
    response = request[query]

    # dixie.log('=== extras getList ===')
    # dixie.log(request)
    # dixie.log(response)

    return response[result]


def install(url, path, zipfile):
    import download
    import extract

    dp = dixie.Progress('Downloading files.', 'Please Wait.')

    download.download(url, zipfile, dp)
    # dixie.log('----------- FIRSTRUN DOWNLOAD LINEUP ------------')
    # dixie.log(url)
    # dixie.log(zipfile)

    extract.all(zipfile, path)
    sfile.remove(zipfile)


def installSF(sfZip):
    sfData  = os.path.join('special://profile', 'addon_data', 'plugin.program.super.favourites')
    sfDir   = xbmc.translatePath(sfData)
    path    = os.path.join(sfDir, 'Super Favourites')
    zipfile = os.path.join(path, 'sfZip.zip')

    if not os.path.isdir(path):
        sfile.makedirs(path)

    install(sfZip, path, zipfile)


def installLineup(option):
    label = option[0]
    url   = option[1]
    isSF  = option[2]
    sfZip = option[3]
    # dixie.log('----------- FIRSTRUN getLineups ------------')
    # dixie.log(label)
    # dixie.log(url)
    # dixie.log(isSF)
    # dixie.log(sfZip)

    path    = dixie.PROFILE
    zipfile = os.path.join(path, 'lineups.zip')
    chandir = os.path.join(path, 'channels')
    # catfile = os.path.join(path, 'catfile')
    # cfgfile = os.path.join(path, 'settings.cfg')

    # if dixie.DialogYesNo('Would you like to install ' + label, 'and make it your active channel line-up?', 'It will be downloaded and installed into your system.'):

    if isSF == 'true':
        dixie.DialogOK(label + ' requires some links added to your Super Favourites', 'We will install these first and then install your line-up', 'Thank you.')
        installSF(sfZip)

    # if os.path.isdir(chandir):
    #     sfile.rmtree(chandir)

    install(url, path, zipfile)
    dixie.DialogOK(label + ' line-up has been installed successfully.', '', 'It is now set as your active channel line-up.')

    # if sfile.exists(catfile):
    #     sfile.remove(catfile)
    #     sfile.remove(catfile)
    #     dixie.DialogOK(label + ' catfile deleted', 'settings.cfg deleted', '')

