#
#      Copyright (C) 2014-15 Sean Poyser and Richard Dean (write2dixie@gmail.com)
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

import xbmcgui
import os

import dixie
import sfile

import zipfile

ROOT     = dixie.PROFILE 
FILENAME = 'OTT-backup.zip'

LINE1 = 'Backup file now being created.'
LINE2 = 'Please wait, this may take a while.'


def doBackup():
    CUSTOM = '1'

    chanType = dixie.GetSetting('chan.type')
    logoType = dixie.GetSetting('logo.type')
    
    dixie.log('Backup: Channel setting is %s' % chanType)
    dixie.log('Backup: Logo setting is %s' % logoType)

    if (chanType == CUSTOM) or (logoType == CUSTOM):
        dixie.DialogOK('It appears you are using a custom location', 'for your channels or logos (Home Networking).', 'Please back-up On-Tapp.TV manually.')
        return

    try:
        folder = getFolder('Please select backup folder location')

        if not folder:
            return False

        filename = os.path.join(folder, FILENAME)

        dp = dixie.Progress(LINE1, LINE2)

        success = doZipfile(filename, dp)

        dp.close()

        if success: 
            dixie.DialogOK('Backup successfully created')
        else:
            dixie.DeleteFile(filename)

        return True

    except Exception, e:
        dixie.log(e)

    return False


def doZipfile(outputFile, dp):
    zip = None

    source  = ROOT
    relroot = os.path.abspath(os.path.join(source, os.pardir))
    cookies = os.path.join(dixie.ADDONID, 'cookies')

    total = float(0)
    index = float(0)

    for root, dirs, files in os.walk(source):
        total += 1
        for file in files:
            total += 1

    for root, dirs, files in os.walk(source):  
        if zip == None:
            zip = zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED)

        index   += 1
        percent  = int(index / total * 100)
        if not updateProgress(dp, percent):
            return False

        local = os.path.relpath(root, relroot)       
        if local == cookies:
            continue

        for file in files:
            index   += 1
            percent  = int(index / total * 100)
            if not updateProgress(dp, percent):
                return False

            arcname  = os.path.join(local, file)
            filename = os.path.join(root, file)           
            zip.write(filename, arcname)

    return True


def updateProgress(dp, percent):
    dp.update(percent, LINE1, LINE2)
    if not dp.iscanceled():
        return True

    return False


def getFolder(title):
    folder = xbmcgui.Dialog().browse(3, title, 'files', '', False, False, os.sep)

    return xbmc.translatePath(folder)



if __name__ == '__main__':
    try:    doBackup()
    except: pass

    dixie.ADDON.openSettings()
