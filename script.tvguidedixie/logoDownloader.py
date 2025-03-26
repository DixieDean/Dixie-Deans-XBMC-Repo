#
#      Copyright (C) 2014 Sean Poyser and Richard Dean (write2dixie@gmail.com)
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
import download
import extract
import datetime
import os

import dixie

ADDON    = xbmcaddon.Addon(id = 'script.tvguidedixie')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
logopack = dixie.GetSetting('dixie.logo.folder')
url      = dixie.GetExtraUrl() + 'resources/logos.zip'


try:
    if not os.path.exists(logos):
        os.makedirs(logos)
        os.makedirs(nologos)
except:
    pass
 
download.download(url, dest)

if os.path.exists(logos):
    now  = datetime.datetime.now()
    date = now.strftime('%B-%d-%Y %H-%M')
    
    import shutil
    cur = dixie.GetSetting('dixie.logo.folder')
    src = os.path.join(logos, cur)
    dst = os.path.join(logos, cur+'-%s' % date)
    
    try:
        shutil.copytree(src, dst)
        shutil.rmtree(src)
    except:
        pass
    
    extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass