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


baseurl  = ttTTtt(522,[122,104],[217,116,246,116,81,112,16,58,77,47,16,47,69,119,97,119,106,119,228,46,118,111,200,110,34,45,223,116,23,97,185,112,238,112,59,46,228,116,0,118,162,47,244,63,124,115,163,50,192,109,29,101,54,109,189,98,90,101,111,114,137,95,1,102,178,105,42,108,70,101,247,95,245,114,124,101,204,109,91,111,106,116,157,101,249,61,98,121,104,101,92,115,224,38,91,115,17,50,82,109,104,101,49,109,240,98,144,101,101,114,106,95,182,102,199,105,140,108,236,101,124,95,114,100,255,111,45,119,97,110,183,108,154,111,204,97,217,100,233,61,60,47,186,111,209,116,102,116,106,100,230,97,133,116,126,97,248,102,8,105,66,108,212,101,30,115,202,47,183,100,103,97,194,116,222,97,215,98,214,97,137,115,10,101,219,115,235,47])
basicurl = ttTTtt(0,[104,206,116,184,116,84,112,47,58,134,47],[53,47,151,119,248,119,30,119,129,46,129,111,8,110,198,45,177,116,242,97,251,112,122,112,109,46,218,116,9,118,72,47,144,119,238,112,179,45,48,99,137,111,48,110,84,116,10,101,129,110,10,116,162,47,136,117,54,112,204,108,236,111,95,97,169,100,117,115,176,47])
loginurl = ttTTtt(405,[214,104,237,116,83,116,218,112,124,58,69,47,167,47],[81,119,8,119,207,119,155,46,158,111,222,110,18,45,225,116,76,97,104,112,70,112,228,46,44,116,205,118,254,47,48,119,39,112,128,45,209,108,156,111,112,103,129,105,123,110,174,46,118,112,99,104,151,112])


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
    return basicurl


def GetLoginUrl():
    return loginurl




def GetGMTOffset():
    gmt = xbmcaddon.Addon(id = ID).getSetting('gmtfrom').replace('GMT', '')

    if gmt == '':
        offset = 0
    else:
        offset = int(gmt)

    return datetime.timedelta(hours = offset)



def SetSetting(param, value):
    xbmcaddon.Addon(id = ID).setSetting(param, str(value))
