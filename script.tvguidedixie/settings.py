#
#       Copyright (C) 2014
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


import xbmc
import xbmcaddon
import os

import dixie
import sfile


ADDON = dixie.ADDONID

ORIGINAL = 'settings.xml'
BACKUP   = 'settings.bak'


def validate():
    if checkSettings():
        backupSettings()
    else:
        restoreSettings()
        

def checkSettings():
    validator = dixie.GetSetting('validator')

    return validator != '0'


def backupSettings():
    path  = dixie.PROFILE
    src   = os.path.join(path, ORIGINAL)
    dst   = os.path.join(path, BACKUP)

    try:
        sfile.remove(dst)
        sfile.copy(src, dst)
        dixie.SetSetting('validator', 1)
    except Exception, e:
        pass


def restoreSettings():
    path  = dixie.PROFILE
    dst   = os.path.join(path, ORIGINAL)
    src   = os.path.join(path, BACKUP)

    if not sfile.exists(src):
        return backupSettings()

    try:
        sfile.remove(dst)
        sfile.copy(src, dst)
        dixie.SetSetting('validator', 1)
        xbmc.sleep(500)
    except Exception, e:
        pass


def get(param, file):
    try:    config = sfile.readlines(file)
    except: return None

    for line in config:
        if line.startswith(param):
            return line.split(param, 1)[-1].split('=', 1)[-1].strip()

    return None


def clear(param, file):
    setParam(param, '', file)


def set(param, value, file):
    config = []
    try:
        param  = param + '='
        config = sfile.readlines(file)
    except:
        pass
        
    copy = []
    for line in config:
        line = line.strip()
        if (len(line) > 0) and (not line.startswith(param)):
            copy.append(line)

    copy.append(param + str(value))

    f = sfile.file(file, 'w')

    for line in copy:
        f.write(line)
        f.write('\n')
    f.close()


def getAll(file):
    try:    lines = sfile.readlines(file)
    except: return []

    config = []
    for line in lines:
        try:                 
            line = line.split('=', 1)
            if len(line) == 1:
                config.append([line[0].strip(), ''])
            else:
                config.append([line[0].strip(), line[1].strip()])
        except:
            pass

    return config