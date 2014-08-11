#
#      Copyright (C) 2014 Richard Dean
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


baseurl  = ttTTtt(0,[104],[128,116,233,116,39,112,137,58,87,47,190,47,150,119,9,119,172,119,212,46,41,111,17,110,181,45,46,116,32,97,122,112,209,112,193,46,150,116,127,118,118,47,127,63,244,115,228,50,178,109,40,101,249,109,151,98,205,101,83,114,65,95,94,102,136,105,63,108,54,101,233,95,107,114,94,101,225,109,165,111,97,116,44,101,95,61,219,121,239,101,144,115,133,38,245,115,175,50,161,109,51,101,118,109,123,98,207,101,30,114,245,95,246,102,250,105,133,108,40,101,20,95,100,100,210,111,90,119,255,110,98,108,109,111,55,97,77,100,19,61,183,47,8,97,101,99,40,99,176,101,217,115,130,115,63,45,170,115,1,50,233,109,146,101,146,109,76,98,119,101,217,114,140,45,68,108,196,101,236,118,58,101,205,108,95,49,49,47])
resource = ttTTtt(780,[190,104,148,116,210,116,205,112],[191,58,177,47,147,47,90,119,222,119,146,119,115,46,212,111,185,110,224,45,4,116,112,97,179,112,138,112,63,46,246,116,183,118,57,47,129,119,107,112,19,45,208,99,252,111,242,110,143,116,79,101,182,110,134,116,127,47,236,117,22,112,36,108,120,111,61,97,57,100,174,115,186,47])
loginurl = ttTTtt(405,[214,104,237,116,83,116,218,112,124,58,69,47,167,47],[81,119,8,119,207,119,155,46,158,111,222,110,18,45,225,116,76,97,104,112,70,112,228,46,44,116,205,118,254,47,48,119,39,112,128,45,209,108,156,111,112,103,129,105,123,110,174,46,118,112,99,104,151,112])


def GetDixieUrl(DIXIEURL):
    if DIXIEURL == 'ALL CHANNELS':
        return baseurl + 'all/'

    if DIXIEURL == 'DIXIE':
        return baseurl + 'dixie/'

    if DIXIEURL == 'BASIC CHANNELS':
        return basicurl + 'basic/'

    if DIXIEURL == 'INTERNATIONAL':
        return baseurl + 'inter/'

    if DIXIEURL == 'NORTH AMERICA':
        return baseurl + 'na/'

def GetExtraUrl():
    return resource


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


def GetSetting(param):
    return xbmcaddon.Addon(id = ID).getSetting(param)
