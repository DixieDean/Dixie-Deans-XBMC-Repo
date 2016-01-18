#
#      Copyright (C) 2014 Richard Dean (write2dixie@gmail.com)
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
import requests

import vpn_utils as utils


def Network():
    try:
        getIP()
        address = xbmcgui.Window(10000).getProperty('VPNICITY_ADDR')
        country = xbmcgui.Window(10000).getProperty('VPNICITY_LABEL')

        message = 'IP Address: %s  Country: %s' % (address, country)

        utils.notify(message)
        utils.log('VPNicity location is: ' + message)
    except: pass

def getIP():
    response = requests.get('https://api.ipify.org').text
    xbmcgui.Window(10000).setProperty('VPNICITY_ADDR', response)
    #
    # return response
    