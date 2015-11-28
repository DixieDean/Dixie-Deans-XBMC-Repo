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

import os
import dixie
import urllib

ADDON       = dixie.ADDON
FTVINI      = ADDON.getSetting('ftv.ini')
datapath    = dixie.PROFILE
inipath     = os.path.join(datapath, 'ini')
current_ini = os.path.join(datapath, 'addons.ini')


ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
 t = ooOOOoo
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0  
 for c in t2:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t


def getIni():
    import extract
    import download
    
    path = current_ini

    if dixie.GetSystem():
        url = dixie.GetExtraUrl() + 'resources/other/addons.ini'
        try:
            urllib.urlretrieve(url, path)
        except: pass
        return
    
    
    url = dixie.GetExtraUrl() + 'resources/addons.ini'
    try:
        urllib.urlretrieve(url, path)
    except: pass

    if not os.path.exists(inipath):
        os.makedirs(inipath)
    
    iniurl = dixie.GetExtraUrl() + 'resources/ini.zip'
    inizip = os.path.join(inipath, 'ini.zip')

    try:
        urllib.urlretrieve(iniurl, inizip)
        extract.all(inizip, inipath)
        os.remove(inizip)
    except: pass
    
    try:
        url1 = ttTTtt(303,[193,104,0,116,159,116,5,112,161,115,105,58],[228,47,159,47,235,114,0,97,177,119,39,46,34,103,214,105,97,116,4,104,145,117,9,98,89,117,85,115,217,101,83,114,47,99,32,111,20,110,24,116,24,101,170,110,221,116,19,46,147,99,37,111,17,109,168,47,213,82,236,101,244,110,101,101,187,103,194,97,83,100,19,101,29,115,84,84,214,86,224,47,215,114,5,101,167,112,129,111,78,115,158,105,141,116,152,111,77,114,62,121,56,46,251,114,55,101,153,110,24,101,215,103,37,97,251,100,190,101,46,115,122,116,150,118,249,47,131,109,85,97,190,115,248,116,89,101,224,114,85,47,55,97,36,100,111,100,120,111,241,110,111,115,251,50,89,46,94,105,74,110,17,105])
        url2 = ttTTtt(688,[232,104,228,116],[74,116,16,112,252,58,81,47,50,47,101,116,250,101,222,99,140,98,236,111,56,120,148,46,63,116,5,118,119,47,199,114,242,101,160,112,63,111,40,47,242,116,182,101,230,99,60,105,111,112,97,116,189,118,172,103,179,117,44,105,103,100,223,101,67,47,238,97,165,100,152,100,96,111,171,110,184,115,101,46,170,105,238,110,182,105])
    
        temp1 = os.path.join(inipath, 'temp1')
        temp2 = os.path.join(inipath, 'temp2')
        temp3 = os.path.join(inipath, 'temp3')
        temp4 = os.path.join(inipath, 'temp4')

        ini1 = os.path.join(inipath, 'ini1.ini')
        ini2 = os.path.join(inipath, 'ini2.ini')
    
        urllib.urlretrieve(url1, temp1)    
    
        with open(temp1, 'r') as f:
            lines = f.readlines()

        with open(temp2, 'w') as f:
            for line in lines:
                if not 'plugin.video.expattv' in line:
                    f.write(line)

        with open(temp2, 'r') as f:
            lines = f.readlines()
    
        with open(temp3, 'w') as f:
            for line in lines:
                if not 'plugin.video.F.T.V' in line:
                    f.write(line)

        with open(temp3, 'r') as f:
            lines = f.readlines()
    
        with open(temp4, 'w') as f:
            for line in lines:
                if not 'plugin.video.ccloudtv' in line:
                    f.write(line)

        with open(temp4, 'r') as f:
            lines = f.readlines()
    
        with open(ini1, 'w') as f:
            for line in lines:
                if not '*' in line:
                    f.write(line)
                
        os.remove(temp1)
        os.remove(temp2)
        os.remove(temp3)
        os.remove(temp4)

        urllib.urlretrieve(url2, temp1)
    
        with open(temp1, 'r') as f:
            lines = f.readlines()

        with open(temp2, 'w') as f:
            for line in lines:
                if not 'plugin.video.expattv' in line:
                    f.write(line)

        with open(temp2, 'r') as f:
            lines = f.readlines()
    
        with open(temp3, 'w') as f:
            for line in lines:
                if not 'plugin.video.F.T.V' in line:
                    f.write(line)

        with open(temp3, 'r') as f:
            lines = f.readlines()
    
        with open(temp4, 'w') as f:
            for line in lines:
                if not 'plugin.video.ccloudtv' in line:
                    f.write(line)

        with open(temp4, 'r') as f:
            lines = f.readlines()
    
        with open(ini2, 'w') as f:
            for line in lines:
                if not 'plugin.video.ntv' in line:
                    f.write(line)
                
        os.remove(temp1)
        os.remove(temp2)
        os.remove(temp3)
        os.remove(temp4)
    except: pass


def ftvIni():
    import xbmcaddon

    if FTVINI == 'UK Links':
        ftv = 'uk.ini'
    else:
        ftv = 'nongeo.ini'

    path = os.path.join(datapath, ftv)

    try:
        url = dixie.GetExtraUrl() + 'resources/' + ftv
        urllib.urlretrieve(url, path)
    except:
        pass
    
    AVAILABLE = False
    if not AVAILABLE:
        try:
            addon = xbmcaddon.Addon('plugin.video.F.T.V')
            if FTVINI == 'Non-Geolocked UK Links':
                BASE      = addon.setSetting('root_channel', '3092')
                AVAILABLE = BASE
            else:
                BASE      = addon.setSetting('root_channel', '689')
                AVAILABLE = BASE
        except:
            AVAILABLE = False

    

if __name__ == '__main__':
    getIni()
    dixie.DialogOK('Built-in Addon links updated.', 'Always manually update your channel links', 'via "Choose Stream" if they are not working.')
    ftvIni()

