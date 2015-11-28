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


import os
import subprocess
import xbmcgui
import xbmc
import vpn_utils as utils


def KillVPN(): 
    print '************  in netkill.py kill vpn  ************'
    
    xbmcgui.Window(10000).clearProperty('VPNICITY_LABEL')
    xbmcgui.Window(10000).clearProperty('VPNICITY_ABRV')
    xbmcgui.Window(10000).clearProperty('VPNICITY_SERVER')
    xbmcgui.Window(10000).clearProperty('VPNICITY_CONNECTED')

    if os.name == 'nt':
        try:
            si = subprocess.STARTUPINFO
            si.dwFlags |= subprocess._subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = subprocess._subprocess.SW_HIDE

            ps  = subprocess.Popen('TASKKILL /F /IM openvpn.exe', shell=True, stdout=subprocess.PIPE, startupinfo=None)
            ps.wait()
        except:
            pass
        return

    # Android
    if utils.platform() == "android" :
        print '************  in netkill.py kill android vpn  ************'
        xbmc.executebuiltin( "StartAndroidActivity(%s,%s)" % ( "com.vpnicity.openvpn.control", "com.vpnicity.openvpn.control.DISCONNECT") )
        return

    #LINUX
    try:
        cmd = utils.getSudo() + 'killall -9 openvpn'

        print '************  in netkill.py cmd  ************'
        ps  = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        ps.wait()
    except:
        pass

if __name__ == '__main__':
    KillVPN()