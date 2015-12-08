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

import xbmc
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import dixie

def CheckCredentials():
    xbmc.executebuiltin('Dialog.Show(busydialog)')

    response = getResponse()

    xbmc.executebuiltin('Dialog.Close(busydialog)')
    
    if 'login not successful' in response:
        dixie.DialogOK('We failed to verify your credentials', '', 'Please check your settings.')
    else:
        dixie.DialogOK('Your login details are correct.', '', 'Thank you.')

    # dixie.openSettings(focus='0.4')


def getResponse():    
    URL     = dixie.GetVerifyUrl()
    USER    = dixie.GetUser()
    PASS    = dixie.GetPass()
    PAYLOAD = {'username' : USER, 'password' : PASS}
    
    request  = requests.post(URL, data=PAYLOAD)
    response = request.content
    
    dixie.log(response)
    
    return response

if __name__ == '__main__':
    CheckCredentials()