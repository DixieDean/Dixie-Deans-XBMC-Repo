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

import os
import xbmc
import xbmcgui
import xbmcaddon

import dixie

datapath = dixie.datapath


def restoreChannels():
    src = os.path.join(datapath, 'channels-backup')
    dst = os.path.join(datapath, 'channels')

    import shutil
    if os.path.isdir(src):
        shutil.rmtree(dst)
        xbmc.sleep(1000)   
        
        shutil.copytree(src, dst)
        shutil.rmtree(src)
        return True
    
    return False

if __name__ == '__main__':
    if restoreChannels() == True:
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Your channels have been successfully restored.', 'This should bring back any customisations', 'that you may have lost.')    
    else:
        d = xbmcgui.Dialog()
        d.ok('OnTapp.TV', 'Sorry, we failed to restore your channels.', '', 'Please restart On-Tapp.TV and try again.')    


