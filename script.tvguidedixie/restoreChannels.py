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

import dixie
import sfile

datapath = dixie.GetChannelFolder()


def restoreChannels():
    src = os.path.join(datapath, 'channels-backup')
    dst = os.path.join(datapath, 'channels')

    if not sfile.exists(src):
        return False
    
    try:
        current, dirs, files = sfile.walk(src)
        for file in files:
            full = os.path.join(current, file)
            sfile.copy(full,  dst)
    except Exception, e:
        print str(e)
        return False
    
    return True


if __name__ == '__main__':
    if restoreChannels():
        dixie.DialogOK('Your channels have been successfully restored.', 'This should bring back any customisations', 'that you may have lost.')
    else:
        dixie.DialogOK('Sorry, we failed to restore your channels.', '', 'Please restart On-Tapp.TV and try again.')    


