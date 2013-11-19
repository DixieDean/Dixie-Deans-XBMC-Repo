import xbmc
import os
import xbmcaddon
import glob
import re
import datetime
import xbmcgui
import urllib
import time
import xbmcplugin
import urllib2
if 64 - 64: i11iIiiIii
from sqlite3 import dbapi2 as sqlite3
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
def o0OO00 ( text0 , text1 , text2 = None ) :
 oo = ''
 for i1iII1IiiIiI1 in text1 :
  if not text0 :
   oo += chr ( i1iII1IiiIiI1 )
  text0 = not text0
  if 40 - 40: ooOoO0O00 * IIiIiII11i
 if not text2 :
  return oo
  if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 for i1iII1IiiIiI1 in text2 :
  if not text0 :
   oo += chr ( i1iII1IiiIiI1 )
  text0 = not text0
  if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
 return oo
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
O0oOO0o0 = o0OO00 ( 22 , [ 102 , 115 , 49 , 99 , 51 , 114 , 35 , 105 , 55 , 112 , 47 , 116 , 56 , 46 , 44 , 109 , 78 , 111 , 49 , 100 , 119 , 117 , 71 , 108 , 86 , 101 , ] , [ 55 , 46 , 49 , 120 , 101 , 98 , 112 , 109 , 119 , 99 , 34 , 46 , 62 , 97 , 90 , 100 , 43 , 115 , ] )
if 9 - 9: o0o - OOO0o0o
Ii1iI = o0OO00 ( 10 , [ 71 , 118 , 107 , 105 , 86 , 115 , 59 , 105 , 73 , 116 , 36 , 111 , 42 , 114 , ] , [ 94 , 95 , 93 , 103 , 53 , 97 , ] )
if 100 - 100: i1IIi . o0o / o00O0oo * OoooooooOO + IiII * Ii1I
O0IiiiIiI1iIiI1 = xbmcaddon . Addon ( id = O0oOO0o0 )
if 85 - 85: I1ii11iIi11i
iIi1IIii11I = o0OO00 ( 7 , [ 88 , 118 , 63 , 101 , 118 , 114 , 121 , 115 , 110 , 105 , 65 , 111 , 68 , 110 , ] )
if 84 - 84: iIii1I11I1II1 . o00O0oo / o00O0oo % o00O0oo
i11 = [ o0OO00 ( 9 , [ 81 , 120 , 90 , 98 , 75 , 109 , 38 , 99 , 95 , 97 , 57 , 100 , 72 , 100 , 111 , 111 , 92 , 110 , ] ) , o0OO00 ( 6 , [ 108 , 117 , 51 , 114 , 72 , 108 , 110 , 108 , 77 , 105 , 45 , 98 , ] ) , o0OO00 ( 7 , [ 43 , 117 , 49 , 114 , 121 , 108 , 80 , 108 , 93 , 105 , 103 , 98 , 56 , 50 , ] ) ]
if 41 - 41: o0o . OOO0o0o * o00O0oo % i11iIiiIii
class o000o0o00o0Oo ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . shut = kwargs [ 'close_time' ]
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
  if 80 - 80: OoooooooOO . IIiIiII11i
 def onInit ( self ) :
  while self . shut > 0 :
   xbmc . sleep ( 1000 )
   self . shut -= 1
  xbmc . Player ( ) . stop ( )
  self . _close_dialog ( )
  return
  if 87 - 87: Ii1I / OOO0o0o + o0o - OOO0o0o . OOO0o0o / ooOoO0O00
 def onFocus ( self , controlID ) : pass
 if 11 - 11: IIiIiII11i % OOooOOo - oOo0O0Ooo
 def onClick ( self , controlID ) :
  if controlID == 12 :
   self . shut = 0
   if 58 - 58: i11iIiiIii % o0o
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] :
   self . shut = 0
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  time . sleep ( .4 )
  self . close ( )
  return
  if 54 - 54: iII111i % O0 + IIiIiII11i - ooOoO0o / IiII
iIiiI1 = o0OO00 ( 16 , [ 110 , 117 , 78 , 114 , 54 , 108 , 45 , 105 , 109 , 110 , 70 , 115 , 58 , 116 , 37 , 97 , 63 , 108 , 53 , 108 , 126 , 101 , 57 , 114 , ] , [ 83 , 46 , 108 , 99 , 120 , 111 , 122 , 109 , ] )
OoOooOOOO = o0OO00 ( 4 , [ 105 , 103 , 58 , 111 , ] , [ 37 , 111 , 123 , 103 , ] )
if 45 - 45: o0o + I1Ii111
iII111ii = O0IiiiIiI1iIiI1 . getSetting ( Ii1iI )
if 3 - 3: ooOoO0o + O0
I1Ii = o0OO00 ( 14 , [ 86 , 88 , 63 , 66 , 75 , 77 , 97 , 67 , 63 , 65 , 46 , 68 , 116 , 83 , ] , [ 71 , 67 , 42 , 76 , 97 , 73 , 111 , 69 , 91 , 78 , 98 , 84 , 97 , ] )
if 66 - 66: I1Ii111
if iII111ii == None or iII111ii == '' :
 from random import randint
 iII111ii = str ( randint ( 0 , 0x7fffffff ) )
 O0IiiiIiI1iIiI1 . setSetting ( Ii1iI , iII111ii )
 if 78 - 78: I1ii11iIi11i
Iii1I111 = o0OO00 ( 7 , [ 124 , 120 , 40 , 98 , 116 , 109 , ] , [ 83 , 99 , 98 , 97 , 68 , 100 , 47 , 115 , ] )
OO0O0O00OooO = map ( __import__ , i11 )
OoooooOoo = o0OO00 ( 7 , [ 79 , 108 , 46 , 101 , 44 , 45 , 72 , 97 , 77 , 110 , 63 , 97 , 92 , 108 , ] , )
if 70 - 70: I1ii11iIi11i . I1ii11iIi11i - I1ii11iIi11i / I11i * iII111i
def OoO000 ( dateString ) :
 try :
  return datetime . datetime . fromtimestamp ( time . mktime ( time . strptime ( dateString . encode ( 'utf-8' , 'replace' ) , "%Y-%m-%d %H:%M:%S" ) ) )
 except :
  return datetime . datetime . today ( ) - datetime . timedelta ( days = 1 )
  if 42 - 42: Ii1I - i1IIi / i11iIiiIii + iII111i + I1ii11iIi11i
iIi = Iii1I111 + o0OO00 ( 8 , [ 101 , 45 , 102 , 115 , 89 , 101 , 72 , 114 , ] , [ 40 , 118 , 59 , 105 , 48 , 99 , 90 , 101 , ] )
II = o0OO00 ( 5 , [ 51 , 121 , 113 , 116 , 59 , 105 , 58 , 99 , 119 , 115 , ] , )
if 14 - 14: oOo0O0Ooo . IIiIiII11i / I1Ii111
def IiiiI1II1I1 ( time_setting_id = 'ga_time' , hour_threshold = 2 ) :
 ooIi11iI1i = 60 * 60
 Ooo = hour_threshold * ooIi11iI1i
 if 68 - 68: IiII + iII111i . iIii1I11I1II1 - o00O0oo % iIii1I11I1II1 - OOO0o0o
 oOOO00o = datetime . datetime . today ( )
 if 97 - 97: IiII % IiII + ooOoO0O00 * ooOoO0o
 o0o00o0 = O0IiiiIiI1iIiI1 . getSetting ( time_setting_id )
 if not o0o00o0 or o0o00o0 == '' :
  o0o00o0 = '2000-01-01 00:00:00'
 o0o00o0 = OoO000 ( o0o00o0 )
 if 25 - 25: oOo0O0Ooo - o00O0oo . OoooooooOO
 I11ii1 = oOOO00o - o0o00o0
 I11II1i = I11ii1 . days
 IIIII = I11ii1 . seconds
 if 75 - 75: ooOoO0O00 % ooOoO0O00
 iI1 = ( I11II1i > 0 ) or ( IIIII > Ooo )
 if 19 - 19: IiII + OOO0o0o
 if not iI1 :
  return False
  if 53 - 53: OoooooooOO . i1IIi
 O0IiiiIiI1iIiI1 . setSetting ( time_setting_id , str ( oOOO00o ) . split ( '.' ) [ 0 ] )
 if 18 - 18: OOooOOo
 return True
 if 28 - 28: iII111i - o00O0oo . o00O0oo + oO0o - OoooooooOO + O0
oOoOooOo0o0 = o0OO00 ( 7 , [ 89 , 70 , 52 , 97 , 81 , 105 , 92 , 108 , ] , [ 59 , 117 , 84 , 114 , 108 , 101 , ] )
def OOOO ( utm_url ) :
 OOO00 = o0OO00 ( 90 , [ 51 , 77 , 86 , 111 , 100 , 122 , 105 , 105 , 125 , 108 , 42 , 108 , 43 , 97 , 47 , 47 , 126 , 53 , 115 , 46 , 126 , 48 , 68 , 32 , 106 , 40 , 60 , 87 , 102 , 105 , 35 , 110 , 110 , 100 , 42 , 111 , 58 , 119 , 93 , 115 , 120 , 59 , 99 , 32 , 32 , 85 , 93 , 59 , 101 , 32 , 96 , 87 , 57 , 105 , 50 , 110 , 40 , 100 , 107 , 111 , 68 , 119 , 54 , 115 , 39 , 32 , 126 , 78 , 81 , 84 , 55 , 32 , 115 , 53 , 103 , 46 , 50 , 49 , 34 , 59 , 60 , 32 , 83 , 101 , 36 , 110 , 98 , 45 , 50 , 71 , 55 , 66 , 82 , 59 , 121 , 32 , 115 , 114 , 96 , 118 , 111 , 58 , 53 , 49 , 33 , 46 , 75 , 57 , 89 , 46 , 114 , 48 , 49 , 46 , 122 , 51 , 86 , 41 , ] , [ 95 , 32 , 57 , 71 , 114 , 101 , 42 , 99 , 94 , 107 , 81 , 111 , 113 , 47 , 87 , 50 , 61 , 48 , 114 , 48 , 109 , 56 , 120 , 48 , 118 , 57 , 71 , 50 , 94 , 52 , 54 , 49 , 33 , 55 , 120 , 32 , 118 , 70 , 119 , 105 , 87 , 114 , 113 , 101 , 92 , 102 , 67 , 111 , 60 , 120 , 60 , 47 , 115 , 51 , 65 , 46 , 95 , 48 , 121 , 46 , 111 , 51 , ] )
 import urllib2
 try :
  iiiiiIIii = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOO00 }
 )
  O000OO0 = urllib2 . urlopen ( iiiiiIIii ) . read ( )
 except :
  print ( oOoOooOo0o0 + ": %s" % utm_url )
 return O000OO0
 if 43 - 43: o0o - O0 % IIiIiII11i . IiII
o00 = o0OO00 ( 28 , [ 115 , 104 , 62 , 116 , 68 , 116 , 119 , 112 , 64 , 58 , 59 , 47 , 43 , 47 , 55 , 119 , 54 , 119 , 58 , 119 , 57 , 46 , ] , [ 52 , 117 , 112 , 114 , 100 , 108 , 48 , 105 , 119 , 110 , 62 , 115 , 109 , 116 , 91 , 97 , 123 , 108 , 84 , 108 , 87 , 101 , 76 , 114 , 78 , 46 , 114 , 99 , 120 , 111 , 95 , 109 , 112 , 47 , ] )
if 95 - 95: O0 + I1ii11iIi11i . ooOoO0O00 / O0
def O000oo0O ( url ) :
 iiiiiIIii = OO0O0O00OooO [ 2 ] . Request ( url , headers = { 'User-Agent' : "Magic Browser" } )
 OOOOi11i1 = OO0O0O00OooO [ 2 ] . urlopen ( iiiiiIIii )
 IIIii1II1II = OOOOi11i1 . read ( )
 return IIIii1II1II
 if 42 - 42: I1Ii111 + Ii1I
o0O0o0Oo = o0OO00 ( 28 , [ 81 , 120 , 60 , 98 , 103 , 109 , 108 , 99 , 72 , 97 , 95 , 100 , 58 , 115 , 51 , 47 , 123 , 120 , 124 , 98 , 73 , 109 , 94 , 99 , ] , [ 102 , 97 , 105 , 100 , 106 , 115 , 117 , 45 , 79 , 98 , 71 , 108 , 100 , 111 , 89 , 99 , 58 , 107 , 81 , 101 , 126 , 114 , 46 , 115 , 33 , 46 , 85 , 112 , 89 , 104 , 42 , 112 , ] )
Ii11Ii1I = o0OO00 ( 4 , [ 111 , 85 , ] , [ 35 , 65 , 74 , 45 , 114 , 52 , ] ) + o0OO00 ( 9 , [ 44 , 52 , 46 , 51 , 105 , 48 , 113 , 49 , ] , [ 110 , 50 , 37 , 52 , 74 , 57 , 92 , 45 , 47 , 49 , ] )
if 72 - 72: ooOoO0o / i1IIi * oOo0O0Ooo - o0o
def Oo0O0O0ooO0O ( dev_addon_visitor , path , group , name ) :
 try :
  IIIIii = dev_addon_visitor
  if IIIIii == None or IIIIii == '' :
   IIIIii = iII111ii
   if 70 - 70: I1Ii111 / IiII . ooOoO0o % oOo0O0Ooo
  OOoOO00OOO0OO = iII111ii
  iI1I111Ii111i = O0IiiiIiI1iIiI1 . getAddonInfo ( iIi1IIii11I )
  I1Ii = path
  if 7 - 7: OOO0o0o * I1ii11iIi11i % Ii1I . o00O0oo
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  if 45 - 45: i11iIiiIii * ooOoO0O00 % iIii1I11I1II1 + I11i - I1Ii111
  iIi1iIiii111 = "http://www." + OoOooOOOO + OoooooOoo + II + ".com/__utm.gif"
  if not group == "None" :
   iIIIi1 = iIi1iIiii111 + "?" + "utmwv=" + iI1I111Ii111i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmt=" + "event" + "&utme=" + quote ( "5(" + I1Ii + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( I1Ii ) + "&utmac=" + Ii11Ii1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , IIIIii , OOoOO00OOO0OO , OOoOO00OOO0OO , OOoOO00OOO0OO , "2" ] )
   if 20 - 20: i1IIi + I11i - OOO0o0o
   if 30 - 30: ooOoO0O00 - iII111i - i11iIiiIii % oO0o - ooOoO0O00 * I1Ii111
   if 61 - 61: Ii1I - IiII % iII111i
   if 84 - 84: Ii1I * I1ii11iIi11i / IiII - O0
   if 30 - 30: iIii1I11I1II1 / OOO0o0o - o0o - ooOoO0O00 % ooOoO0o
   if 49 - 49: IIiIiII11i % OOO0o0o . OOO0o0o . IiII * OOO0o0o
   if 97 - 97: I1Ii111 + OOooOOo . iII111i + I11i % ooOoO0o
   if 95 - 95: i1IIi
   OOOO ( iIIIi1 )
   if 3 - 3: o0o - O0 / o0o % I1ii11iIi11i / o0o . IIiIiII11i
  if name == "None" :
   iiI111I1iIiI = iIi1iIiii111 + "?" + "utmwv=" + iI1I111Ii111i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1Ii ) + "&utmac=" + Ii11Ii1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , IIIIii , OOoOO00OOO0OO , OOoOO00OOO0OO , OOoOO00OOO0OO , "2" ] )
   if 41 - 41: oOo0O0Ooo . OOO0o0o + O0 * OOooOOo % oOo0O0Ooo * oOo0O0Ooo
   if 19 - 19: ooOoO0o
   if 46 - 46: I11i - I1Ii111 . iIii1I11I1II1 / I11i
   if 7 - 7: i1IIi / IIiIiII11i * o0o . o00O0oo . iIii1I11I1II1
   if 13 - 13: iII111i / i11iIiiIii
  else :
   if group == "None" :
    iiI111I1iIiI = iIi1iIiii111 + "?" + "utmwv=" + iI1I111Ii111i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1Ii + "/" + name ) + "&utmac=" + Ii11Ii1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , IIIIii , OOoOO00OOO0OO , OOoOO00OOO0OO , OOoOO00OOO0OO , "2" ] )
    if 2 - 2: IIiIiII11i / O0 / OOooOOo % oO0o % I1Ii111
    if 52 - 52: OOooOOo
    if 95 - 95: I1Ii111
    if 87 - 87: OOO0o0o + oO0o . iII111i + oO0o
    if 91 - 91: O0
   else :
    iiI111I1iIiI = iIi1iIiii111 + "?" + "utmwv=" + iI1I111Ii111i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1Ii + "/" + group + "/" + name ) + "&utmac=" + Ii11Ii1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , IIIIii , OOoOO00OOO0OO , OOoOO00OOO0OO , OOoOO00OOO0OO , "2" ] )
    if 61 - 61: ooOoO0O00
    if 64 - 64: OOO0o0o / oO0o - O0 - IiII
    if 86 - 86: IiII % oO0o / IIiIiII11i / oO0o
    if 42 - 42: I1ii11iIi11i
    if 67 - 67: o0o . ooOoO0o . O0
    if 10 - 10: I11i % I11i - iIii1I11I1II1 / iII111i + I1Ii111
  OOOO ( iiI111I1iIiI )
  if 87 - 87: Ii1I * I11i + iII111i / iIii1I11I1II1 / ooOoO0o
 except :
  print oOoOooOo0o0
  if 37 - 37: ooOoO0o - OOO0o0o * Ii1I % i11iIiiIii - o0o
o0oO = o0OO00 ( 10 , [ 59 , 97 , 123 , 100 , 76 , 118 , 71 , 101 , 79 , 114 , 38 , 116 , ] , [ 84 , 46 , 75 , 120 , 59 , 109 , 109 , 108 , ] )
if 1 - 1: I1ii11iIi11i - Ii1I . IiII . I1ii11iIi11i / oOo0O0Ooo + IiII
def OooOOOOo ( ) :
 if 76 - 76: I1ii11iIi11i
 I1iIIii = False
 if 22 - 22: ooOoO0O00
 try :
  import simplejson as json
 except :
  import json
  if 33 - 33: IiII
 iI11i1ii11 = o00 + o0O0o0Oo
 OOooo0O00o = O000oo0O ( iI11i1ii11 )
 oOOoOooOo = json . loads ( OOooo0O00o )
 if 51 - 51: IiII + ooOoO0o % iIii1I11I1II1 / Ii1I / iII111i % OoooooooOO
 o0O0OOO0Ooo = O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' )
 #user_data_path = xbmc.translatePath(ADDON.getAddonInfo('profile'))
 if 45 - 45: O0 / OOooOOo
 i1 = len ( oOOoOooOo )
 if 8 - 8: Ii1I * oO0o - I1Ii111 - I1ii11iIi11i * iII111i % IIiIiII11i
 ii = 0
 if 90 - 90: OOooOOo % i1IIi / I1ii11iIi11i
 for IIi in oOOoOooOo :
  i1Iii1i1I = IIi [ 'id' ]
  OOoO00 = re . sub ( O0oOO0o0 , i1Iii1i1I , o0O0OOO0Ooo )
  if 40 - 40: IIiIiII11i * I1Ii111 + iII111i % ooOoO0o
  if os . path . exists ( OOoO00 ) :
   ii = ii + 1
   if 74 - 74: Ii1I - oOo0O0Ooo + OoooooooOO + o0o / oO0o
 if ii > 0 :
  I1iIIii = True
  if 23 - 23: O0
 return I1iIIii
 if 85 - 85: I1Ii111
 if 84 - 84: IIiIiII11i . iIii1I11I1II1 % OoooooooOO + I1Ii111 % OoooooooOO % I1ii11iIi11i
IIi1 = o0OO00 ( 11 , [ 112 , 97 , 77 , 100 , 80 , 118 , 74 , 101 , 49 , 114 , 117 , 116 , 94 , 49 , ] , [ 103 , 46 , 69 , 120 , 76 , 109 , 65 , 108 , ] )
if 45 - 45: ooOoO0o / ooOoO0o + o0o + OOO0o0o
def iI111i ( ) :
 if xbmc . getCondVisibility ( 'system.platform.ios' ) :
  if not xbmc . getCondVisibility ( 'system.platform.atv' ) :
   IIi11i1i1iI1 = o000o0o00o0Oo ( IIi1 , O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) )
 elif xbmc . getCondVisibility ( 'system.platform.android' ) :
  IIi11i1i1iI1 = o000o0o00o0Oo ( IIi1 , O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) )
 else :
  IIi11i1i1iI1 = o000o0o00o0Oo ( o0oO , O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 , logo_path = '%s/resources/skins/DefaultSkin/media/Logo/' % O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' ) )
  if 23 - 23: i11iIiiIii + OOooOOo . i1IIi
 IIi11i1i1iI1 . doModal ( )
 del IIi11i1i1iI1
 if 100 - 100: o0o . Ii1I * I1Ii111
i1i1Iiii1I1 = o0OO00 ( 11 , [ 94 , 88 , 64 , 66 , 59 , 77 , 86 , 67 , 44 , 65 , 74 , 68 , 97 , 83 , ] , [ 80 , 68 , 55 , 69 , 109 , 86 , 117 , 83 , ] )
if 53 - 53: ooOoO0O00
def i1Ii1Ii ( dev_addon_visitor , ad_id = '' , ad_num = '' , dev_addon_id = '' ) :
 if 52 - 52: I1ii11iIi11i . Ii1I
 ii1iII1II = ''
 Iii1I1I11iiI1 = ''
 if dev_addon_id != '' :
  ii1iII1II = xbmcaddon . Addon ( id = dev_addon_id )
  Iii1I1I11iiI1 = ii1iII1II . getAddonInfo ( 'author' )
  if 18 - 18: iII111i + ooOoO0o - I1Ii111 . ooOoO0O00 + i11iIiiIii
 try :
  import simplejson as json
 except :
  import json
  if 20 - 20: o0o
 Oo0oO00o = o0OO00 ( 11 , [ 103 , 104 , 91 , 116 , 78 , 116 , 111 , 112 , 48 , 58 , 90 , 47 , 116 , 47 , ] , [ 53 , 119 , 96 , 119 , 65 , 119 , 41 , 46 , ] )
 i11I1II1I11i = Oo0oO00o + iIiiI1 + '/' + Iii1I111 + '/' + iIi + o0OO00 ( 8 , [ 47 , 46 , 54 , 112 , 94 , 104 , 102 , 112 , 33 , 63 , ] , [ 125 , 105 , 82 , 100 , 44 , 61 , ] ) + ad_id
 OOooo0O00o = O000oo0O ( i11I1II1I11i )
 oOOoOooOo = json . loads ( OOooo0O00o )
 if 61 - 61: IIiIiII11i - iII111i . Ii1I / iII111i + oOo0O0Ooo
 I1i11i = '' ;
 try :
  I1i11i = oOOoOooOo [ 'message' ]
 except :
  I1i11i = ''
  if 64 - 64: iII111i % iIii1I11I1II1 * Ii1I
 if I1i11i == 'no-ads' :
  return ad_id
  if 79 - 79: O0
 oOO00O = oOOoOooOo [ 'AdNum' ]
 OOOoo0OO = oOOoOooOo [ 'ClientId' ]
 oO0o0 = oOOoOooOo [ 'AdId' ]
 iI1Ii11iIiI1 = oOOoOooOo [ 'AdType' ]
 OO0Oooo0oOO0O = oOOoOooOo [ 'Ad' ]
 if 62 - 62: IIiIiII11i
 if ad_num == '-1' :
  Oo0O0O0ooO0O ( dev_addon_visitor , I1Ii , OOOoo0OO , oO0o0 )
  if dev_addon_id != '' :
   Oo0O0O0ooO0O ( dev_addon_visitor , i1i1Iiii1I1 , Iii1I1I11iiI1 , dev_addon_id )
   if 100 - 100: I1Ii111 - O0 % Ii1I * iII111i + IIiIiII11i
  from random import randint
  import threading
  for Oo0O0oooo in range ( 0 , 4 ) :
   I111iI = str ( randint ( 0 , 0x7fffffff ) )
   threading . Thread ( target = Oo0O0O0ooO0O , args = ( I111iI , I1Ii , OOOoo0OO , oO0o0 ) ) . start ( )
   if dev_addon_id != '' :
    threading . Thread ( target = Oo0O0O0ooO0O , args = ( I111iI , i1i1Iiii1I1 , Iii1I1I11iiI1 , dev_addon_id ) ) . start ( )
    if 56 - 56: IIiIiII11i
  return
  if 54 - 54: o0o / iII111i . Ii1I % ooOoO0o
 if iI1Ii11iIiI1 == 'IMAGE' :
  Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/script.module.xbmc.ads/resources/skins/DefaultSkin/media' , '' ) )
  O0OOOOo0O = os . path . join ( Oo , 'advert.jpg' )
  urllib . urlretrieve ( OO0Oooo0oOO0O , O0OOOOo0O )
  iI111i ( )
 elif iI1Ii11iIiI1 == 'YOUTUBE' :
  OooOO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'plugin.video.youtube' ) )
  if os . path . exists ( OooOO ) == True :
   I1111 = 'plugin://plugin.video.youtube/?path=root/video&action=play_video&videoid=%s' % OO0Oooo0oOO0O
   iiIiiiiI = xbmcgui . ListItem ( 'ADVERT' , iconImage = "DefaultVideo.png" , thumbnailImage = '' )
   iiIiiiiI . setInfo ( type = "Video" , infoLabels = { "Title" : 'ADVERT' } )
   iiIiiiiI . setProperty ( "IsPlayable" , "true" )
   oooOo0OOOoo0 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
   oooOo0OOOoo0 . clear ( )
   oooOo0OOOoo0 . add ( I1111 , iiIiiiiI )
   xbmc . Player ( xbmc . PLAYER_CORE_MPLAYER ) . play ( oooOo0OOOoo0 )
 elif iI1Ii11iIiI1 == 'TEXT' :
  OOoO = re . compile ( 'TITLE\:(.+?)\|' ) . findall ( OO0Oooo0oOO0O ) [ 0 ]
  OO0O000 = re . compile ( 'MESSAGE1\:(.+?)\|' ) . findall ( OO0Oooo0oOO0O ) [ 0 ]
  iiIiI1i1 = re . compile ( 'MESSAGE2\:(.+?)\|' ) . findall ( OO0Oooo0oOO0O ) [ 0 ]
  oO0O00oOOoooO = re . compile ( 'MESSAGE3\:(.+?)\|' ) . findall ( OO0Oooo0oOO0O ) [ 0 ]
  IiIi11iI = xbmcgui . Dialog ( )
  IiIi11iI . ok ( OOoO , OO0O000 , iiIiI1i1 , oO0O00oOOoooO )
  if 83 - 83: ooOoO0O00 % oOo0O0Ooo % OOO0o0o % I11i
 Oo0O0O0ooO0O ( dev_addon_visitor , I1Ii , OOOoo0OO , oO0o0 )
 if dev_addon_id != '' :
  Oo0O0O0ooO0O ( dev_addon_visitor , i1i1Iiii1I1 , Iii1I1I11iiI1 , dev_addon_id )
  if 80 - 80: i11iIiiIii % OOO0o0o + I1Ii111 % IiII - I11i
 from random import randint
 import threading
 for Oo0O0oooo in range ( 0 , 4 ) :
  I111iI = str ( randint ( 0 , 0x7fffffff ) )
  threading . Thread ( target = Oo0O0O0ooO0O , args = ( I111iI , I1Ii , OOOoo0OO , oO0o0 ) ) . start ( )
  if dev_addon_id != '' :
   threading . Thread ( target = Oo0O0O0ooO0O , args = ( I111iI , i1i1Iiii1I1 , Iii1I1I11iiI1 , dev_addon_id ) ) . start ( )
   if 18 - 18: ooOoO0o - iII111i . o0o . iIii1I11I1II1
 return str ( int ( oOO00O ) + 1 )
 if 2 - 2: iII111i . I1ii11iIi11i
O0ooooOOoo0O = o0OO00 ( 7 , [ 63 , 88 , 59 , 66 , 80 , 77 , 62 , 67 , ] , [ 84 , 65 , 88 , 68 , 112 , 83 , ] )
def II1IiiIi1i ( duration = 1440 ) :
 if 29 - 29: IIiIiII11i % IIiIiII11i
 Oo0O0 = O0IiiiIiI1iIiI1 . getAddonInfo ( 'path' )
 Ooo0OOoOoO0 = O0ooooOOoo0O
 oOo0OOoO0 = os . path . join ( Oo0O0 , 'default.py' )
 IIo0Oo0oO0oOO00 = '1'
 oo00OO0000oO = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % ( Ooo0OOoOoO0 , oOo0OOoO0 , IIo0Oo0oO0oOO00 , duration )
 if 11 - 11: OOO0o0o / oO0o - o00O0oo * OoooooooOO + OoooooooOO . oO0o
 xbmc . executebuiltin ( oo00OO0000oO )
 if 26 - 26: I1Ii111 % I11i
def SERVICE_ADVERTISE ( ) :
 if xbmc . Player ( ) . isPlaying ( ) :
  II1IiiIi1i ( 10 )
  return
  if 76 - 76: IiII / iII111i . O0 % IIiIiII11i . OOooOOo + o00O0oo
 o0ooo0 = 'ad_id'
 oOOOoo00 = O0IiiiIiI1iIiI1 . getSetting ( o0ooo0 )
 if oOOOoo00 == None or oOOOoo00 == '' :
  oOOOoo00 = '0'
  O0IiiiIiI1iIiI1 . setSetting ( o0ooo0 , oOOOoo00 )
  if 9 - 9: O0 % O0 - OOooOOo
 oOOOoo00 = i1Ii1Ii ( iII111ii , oOOOoo00 )
 if 51 - 51: IIiIiII11i . iIii1I11I1II1 - I11i / O0
 O0IiiiIiI1iIiI1 . setSetting ( o0ooo0 , oOOOoo00 )
 if 52 - 52: OOooOOo + O0 + ooOoO0o + oOo0O0Ooo % ooOoO0o
 II1IiiIi1i ( )
 if 75 - 75: IIiIiII11i . OOO0o0o . O0 * o0o
def ADDON_ADVERTISE ( dev_addon_id , advertise = True ) :
 if 67 - 67: IIiIiII11i - OOooOOo / IiII - i1IIi
 if advertise == True :
  if xbmc . Player ( ) . isPlaying ( ) :
   return
   if 1 - 1: ooOoO0O00
 ii1iII1II = xbmcaddon . Addon ( id = dev_addon_id )
 Iii1I1I11iiI1 = ii1iII1II . getAddonInfo ( 'author' )
 if 68 - 68: ooOoO0o - IIiIiII11i / o0o / IiII
 I11iiii = Iii1I1I11iiI1 + ' - ' + dev_addon_id + ' - ga_time'
 O0i1iI = Iii1I1I11iiI1 + ' - ' + dev_addon_id + ' - ad_time'
 IiI1iiiIii = Iii1I1I11iiI1 + ' - ' + dev_addon_id + ' - ga_visitor'
 if 7 - 7: o0o * I1ii11iIi11i - OOO0o0o + iII111i * IIiIiII11i % I1ii11iIi11i
 iI1i111I1Ii = O0IiiiIiI1iIiI1 . getSetting ( IiI1iiiIii )
 if iI1i111I1Ii == None or iI1i111I1Ii == '' :
  from random import randint
  iI1i111I1Ii = str ( randint ( 0 , 0x7fffffff ) )
  O0IiiiIiI1iIiI1 . setSetting ( IiI1iiiIii , iI1i111I1Ii )
  if 25 - 25: o0o - ooOoO0o
 if OooOOOOo ( ) :
  i1Ii1Ii ( iI1i111I1Ii , ad_num = '-1' , dev_addon_id = dev_addon_id )
  return
  if 10 - 10: ooOoO0O00 / Ii1I % OoooooooOO * IiII % I11i
  if 48 - 48: OOO0o0o / o0o . iIii1I11I1II1 * oO0o * Ii1I / i1IIi
  if 92 - 92: oOo0O0Ooo % oOo0O0Ooo - OOooOOo / oO0o
  if 10 - 10: ooOoO0o + oOo0O0Ooo * I11i + iIii1I11I1II1 / o0o / I11i
 if advertise == True and IiiiI1II1I1 ( O0i1iI , 24 ) == True :
  iI1II = Iii1I1I11iiI1 + ' - ' + dev_addon_id + ' - ad_id'
  o0OOo0o0O0O = O0IiiiIiI1iIiI1 . getSetting ( iI1II )
  if o0OOo0o0O0O == None or o0OOo0o0O0O == '' :
   o0OOo0o0O0O = '0'
   O0IiiiIiI1iIiI1 . setSetting ( iI1II , o0OOo0o0O0O )
  o0OOo0o0O0O = i1Ii1Ii ( iI1i111I1Ii , ad_id = o0OOo0o0O0O , dev_addon_id = dev_addon_id )
  O0IiiiIiI1iIiI1 . setSetting ( iI1II , o0OOo0o0O0O )
  if 65 - 65: i11iIiiIii
  if 85 - 85: I1Ii111 % ooOoO0o + IiII / OOooOOo . Ii1I + iII111i
def VERIFY ( dev_addon_id ) :
 i11II1I11I1 ( dev_addon_id , False )
 return True # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
