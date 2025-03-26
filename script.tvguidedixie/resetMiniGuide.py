#
#      Copyright (C) 2016 On-Tapp-Networks Limited
#

import xbmc
import os

import sfile
import dixie

settingsFile = xbmc.translatePath(os.path.join(dixie.PROFILE, 'settings.cfg'))

def resetMiniGuide():
    sfile.remove(settingsFile)
    dixie.DialogOK('On-Tapp.TV Mini-Guide successfully reset.', '', '')

if __name__ == '__main__':
    resetMiniGuide()