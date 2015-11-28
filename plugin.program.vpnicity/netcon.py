#
#       Copyright (C) 2015
#       Sean Poyser (seanpoyser@gmail.com) and Richard Dean (write2dixie@gmail.com)
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


import vpn
import browser
import vpn_utils as utils
import xbmc
import xbmcgui

utils.dialogOK('Please choose a country to connect to.', '', 'Netflix will start after we are connected.')
country = browser.getCountry(utils.ADDONID, vpn.GetCountries())

print '************  in netcon.py country chosen, trying VPN  ************'

vpn.BestVPN(country)

if xbmcgui.Window(10000).getProperty('VPNICITY_CONNECTED') == 'True':
    utils.dialogOK('VPN connected.', '', 'We will now log you into your Netflix account.')
    xbmc.executebuiltin('StartAndroidActivity("com.netflix.mediaclient"),return')
