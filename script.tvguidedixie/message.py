#
#      Copyright (C) 2015 Sean Poyser
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

import dixie

import os
import urllib

import urllib2
import json
import datetime


URL = dixie.GetExtraUrl() + 'resources/ottmessage.txt'

def parseDate(dateString):
    try:
        return datetime.datetime.strptime(dateString, '%d/%m/%Y')
    except Exception, e:
        dixie.log('Error in parseDate %s' % str(dateString))
        dixie.log(e)
    return datetime.datetime.now()


def check():
    try:
        return _check()
    except Exception, e:
        dixie.log('Error in message.check %s' % str(e))
        return False


def _check():
    response = urllib2.urlopen(URL).read()

    dixie.log('Response in message._check %s' % str(response))

    response = json.loads(u"" + (response))

    try:
        currentID = dixie.GetSetting('messageID')
        currentID = float(currentID)
    except Exception, e:
        currentID = 0

    newID = float(response['ID'])

    if newID <= currentID:
        return False

    dixie.SetSetting('messageID', str(newID))

    live    = parseDate(response['Live'])
    expires = parseDate(response['Expires'])

    now = datetime.datetime.now()

    if live > now:
        return False

    if now > expires:
        return False

    try:    title = response['Title']
    except: title = getString(1)

    try:    line1 = response['Line1']
    except: line1 = ''

    try:    line2 = response['Line2']
    except: line2 = ''

    try:    line3 = response['Line3']
    except: line3 = ''

    try:    image = response['Image']
    except: image = None

    if image:
        dixie.log('Displaying image announcement %s' % str(newID))

        dixie.log(image)

        import viewer
        url = dixie.GetExtraUrl() + 'resources/' + image
        viewer.show(url)

    else:
        dixie.log('Displaying text announcement %s' % str(newID))

        dixie.log(title)
        dixie.log(line1)
        dixie.log(line2)
        dixie.log(line3)    
        xbmcgui.Dialog().ok(title, line1, line2, line3)

    return True