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


def GetDixieUrl(DIXIEURL):
    baseurl = ttTTtt(430,[68,104,212,116,20,116,176,112,118,58],[43,47,51,47,34,116,226,118,180,103,44,117,211,105,159,100,10,101,52,100,87,105,106,120,43,105,90,101,16,46,83,102,165,105,206,108,31,101,197,98,242,117,13,114,127,115,84,116,84,99,135,100,46,110,65,46,218,99,171,111,29,109,84,47,144,116,189,118,187,103,229,100,126,97,121,116,87,97,37,102,6,105,211,108,21,101,144,115,209,47,17,100,97,97,179,116,84,97,181,98,252,97,101,115,42,101,51,115,220,47])

    if DIXIEURL == 'DIXIE':
        return baseurl + 'dixie/'

    if DIXIEURL == 'BASIC CHANNELS':
        return baseurl + 'basic/'

    if DIXIEURL == 'INTERNATIONAL':
        return baseurl + 'inter/'

    if DIXIEURL == 'NORTH AMERICA':
        return baseurl + 'na/'

    if DIXIEURL == 'XPAT PLANET':
        return baseurl + 'xpat/'

    if DIXIEURL == 'TEST':
        return baseurl + 'test/'

    if DIXIEURL == 'G-BOX MIDNIGHT MX2':
        return baseurl + 'mx2/'


def GetExtraUrl():
    return ttTTtt(0,[104,165,116,218,116,153,112,18,58,229,47,69,47],[27,116,10,118,102,103,79,117,206,105,41,100,247,101,214,100,12,105,150,120,8,105,118,101,236,46,182,102,41,105,152,108,234,101,253,98,55,117,90,114,146,115,107,116,137,99,154,100,132,110,137,46,38,99,232,111,62,109,17,47,220,116,88,118,129,103,227,100,22,97,215,116,237,97,111,102,137,105,134,108,70,101,0,115,69,47,152,114,218,101,251,115,250,111,107,117,86,114,140,99,210,101,170,115,68,47])




def GetGMTOffset():
    gmt = xbmcaddon.Addon(id = ID).getSetting('gmtfrom').replace('GMT', '')

    if gmt == '':
        offset = 0
    else:
        offset = int(gmt)

    return datetime.timedelta(hours = offset)



def SetSetting(param, value):
    xbmcaddon.Addon(id = ID).setSetting(param, str(value))
