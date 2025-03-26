#
#      Copyright (C) 2014 Sean Poyser
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

import platform
try:    original_ps = platform.system
except: original_ps = None

def platform_system():
    if original_ps:
        return original_ps()

    import sys
    if sys.platform.lower().startswith('win'):
        return 'Windows'

    return 'Other OSes to be determined'

platform.system = platform_system

import requests

platform.system = original_ps

import dixie


def download(url, dest, dp=None):
    import session
    session = session.loadSession()
    request = session.get(url, stream=True)

    code = request.status_code
    #dixie.log('========== download login code ==========')
    dixie.log(code)

    if dixie.isCF(code):
        dixie.log('===== DOWNLOAD: SERVER ISSUE CF ACTIVE =====')
        return

    try:
        length = int(request.headers['Content-Length'])
    except:
        length = 15000000

    chunkSize  = 512
    currLength = float(0)

    with open(dest, 'wb') as f:
        for chunk in request.iter_content(chunkSize):
            f.write(chunk)
            if dp:
                currLength += chunkSize
                percent     = currLength /  length * 100
                dp.update(int(percent))
