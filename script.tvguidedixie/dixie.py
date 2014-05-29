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

import xbmcaddon
import datetime

ID = 'script.tvguidedixie'


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


baseurl  = ttTTtt(0,[104,9,116,248,116,217,112],[88,58,36,47,236,47,104,116,225,118,115,103,166,117,222,105,77,100,124,101,98,102,29,105,198,108,241,101,202,115,158,46,65,115,239,51,128,46,199,97,239,109,63,97,147,122,227,111,196,110,87,97,221,119,92,115,104,46,239,99,15,111,30,109,100,47,237,100,208,97,83,116,127,97,171,98,219,97,196,115,66,101,83,115,175,47])
basicurl = ttTTtt(428,[9,104,150,116,126,116,221,112,92,58,166,47,71,47,239,116,124,118,180,103,179,117,196,105,179,100,71,101,214,102,171,105,199,108,239,101,243,115,136,46,93,115,43,51,48,46],[39,97,210,109,2,97,156,122,144,111,155,110,153,97,197,119,255,115,232,46,108,99,153,111,235,109,123,47])

def GetDixieUrl(DIXIEURL):
    if DIXIEURL == 'DIXIE':
        return baseurl + 'dixie/'

    if DIXIEURL == 'BASIC CHANNELS':
        return basicurl + 'basic/'

    if DIXIEURL == 'INTERNATIONAL':
        return baseurl + 'inter/'

    if DIXIEURL == 'NORTH AMERICA':
        return baseurl + 'na/'

    if DIXIEURL == 'TEST':
        return baseurl + 'test/'


def GetExtraUrl():
    return basicurl + 'resources/'



def GetGMTOffset():
    gmt = xbmcaddon.Addon(id = ID).getSetting('gmtfrom').replace('GMT', '')

    if gmt == '':
        offset = 0
    else:
        offset = int(gmt)

    return datetime.timedelta(hours = offset)



def SetSetting(param, value):
    xbmcaddon.Addon(id = ID).setSetting(param, str(value))
