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
import xbmcaddon
import os

import dixie

import zipfile

ROOT  = dixie.PROFILE 
# ROOT  = '/'
LINE1 = 'Now restoring from backup'
LINE2 = 'Please wait, this may take a while.'


def doRestore():
    try:
        filename = getFile('Please select backup file', 'zip')

        if not filename:
            return False

        dp = dixie.Progress(LINE1, LINE2, hide=True)

        success = extractAll(filename, dp)

        dp.close()

        if success: 
            dixie.DialogOK('Backup successfully restored')

        return True

    except Exception, e:
        dixie.log(e)

    return False


def extractAll(filename, dp):
    zin = zipfile.ZipFile(filename, 'r')

    folder = ROOT.rsplit('script.tvguidedixie', 1)[0]

    try:
        nItem = float(len(zin.infolist()))
        index = 0
        for item in zin.infolist():
            index += 1

            percent  = int(index / nItem *100)
            dp.update(percent, LINE1, LINE2)

            if item.filename.startswith('script.tvguidedixie'):
                zin.extract(item, folder)
            else:
                zin.extract(item, ROOT)

    except Exception, e:
        dixie.log('Error whilst unzipping %s' % zin.filename)
        dixie.log(e)
        return False

    return True


def getFile(title, ext):
    filename = xbmcgui.Dialog().browse(1, title, 'files', '.'+ext, False, False, os.sep)

    if filename == 'NO FILE':
        return None

    return filename


if __name__ == '__main__':
    try:    doRestore()
    except: pass

    xbmcaddon.Addon(dixie.ADDONID).openSettings()
