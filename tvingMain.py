# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon
import sys
import urlparse
import inputstreamhelper
import datetime
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
__cwd__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'path' ) )
__lib__ = os . path . join ( __cwd__ , 'resources' , 'lib' )
__data__ = os . path . join ( __cwd__ , 'resources' , 'data' )
sys . path . append ( __lib__ )
sys . path . append ( __data__ )
if 94 - 94: i1IIi % Oo0Ooo
o0oO0 = [
 { 'title' : 'LIVE 채널' , 'mode' : 'LIVE_GROUP' , 'stype' : 'live' , 'orderby' : '-' }
 , { 'title' : 'VOD 방송 (인기순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'viewDay' }
 , { 'title' : 'VOD 방송 (최신순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'new' }
 , { 'title' : '월정액 영화관 (인기)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'viewWeek' }
 , { 'title' : '월정액 영화관 (최신)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'new' }
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'orderby' : '-' }
 , { 'title' : '검색 (VOD,영화)' , 'mode' : 'SEARCH_GROUP' , 'stype' : '-' , 'orderby' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : '-' , 'orderby' : '-' }
 ]
if 100 - 100: i1IIi
xI1Ii11I1Ii1i = [
 { 'title' : '실시간 TV' , 'mode' : 'CHANNEL' , 'stype' : 'onair' }
 , { 'title' : 'TVING TV' , 'mode' : 'CHANNEL' , 'stype' : 'tvingtv' }
 ]
if 67 - 67: iIii1I11I1II1 . I1ii11iIi11i . oO0o / i1IIi % II111iiii - OoOoOO00
OOo = [
 { 'title' : 'VOD 시청내역' , 'mode' : 'WATCH' , 'stype' : 'vod' }
 , { 'title' : '영화 시청내역' , 'mode' : 'WATCH' , 'stype' : 'movie' }
 ]
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
Oooo0000 = [
 { 'title' : 'VOD 검색' , 'mode' : 'SEARCH' , 'stype' : 'vod' }
 , { 'title' : '영화 검색' , 'mode' : 'SEARCH' , 'stype' : 'movie' }
 ]
if 22 - 22: Ii1I . IiII
I11 = [
 { 'title' : '전체' , 'mode' : 'PROGRAM' , 'stype' : 'all' }
 , { 'title' : '드라마' , 'mode' : 'PROGRAM' , 'stype' : 'PCA' }
 , { 'title' : '예능' , 'mode' : 'PROGRAM' , 'stype' : 'PCD' }
 , { 'title' : '해외시리즈' , 'mode' : 'PROGRAM' , 'stype' : 'PCPOS' }
 , { 'title' : '디지털오리지널' , 'mode' : 'PROGRAM' , 'stype' : 'PCWD' }
 , { 'title' : '교양' , 'mode' : 'PROGRAM' , 'stype' : 'PCK' }
 , { 'title' : '키즈/애니' , 'mode' : 'PROGRAM' , 'stype' : 'PCC,PCAN' }
 , { 'title' : '스포츠/취미' , 'mode' : 'PROGRAM' , 'stype' : 'PCF' }
 , { 'title' : '뮤직' , 'mode' : 'PROGRAM' , 'stype' : 'PCG' }
 , { 'title' : 'e 스포츠' , 'mode' : 'PROGRAM' , 'stype' : 'PCE' }
 ]
if 98 - 98: i11iIiiIii * I1IiiI % iII111i * iII111i * II111iiii
o0o0Oo0oooo0 = { 'C00551' : 'tvN'
 , 'C00544' : '중화TV'
 , 'C00575' : 'Olive'
 , 'C00579' : 'Mnet'
 , 'C00590' : 'OGN'
 , 'C01141' : 'XtvN'
 , 'C01142' : 'ONSTYLE'
 , 'C01143' : 'OtvN'
 , 'C04601' : 'CGV'
 , 'C06941' : 'tooniverse'
 , 'C07381' : 'OCN'
 , 'C07382' : 'SUPER ACTION'
 , 'C15251' : 'OGN x LOL'
 , 'C15252' : 'OGN x 오버워치'
 , 'C15042' : '티빙라이브'
, 'C01581' : 'TV CHOSUN'
 , 'C01583' : '채널A'
 , 'C00708' : 'MBN'
 , 'C00593' : 'YTN'
 , 'C01101' : 'YTN Life'
 , 'C15347' : 'YTN science'
 , 'C01723' : '연합뉴스TV'
 , 'C15152' : 'DIA TV'
 , 'C01582' : 'JTBC'
 , 'C00588' : 'JTBC Golf'
 , 'C15741' : 'JTBC2'
 , 'C00805' : 'JTBC3 FOX Sports'
 , 'C05661' : '디즈니채널'
 , 'C18641' : 'IHQ'
 , 'C22041' : 'JTBC4'
 , 'C23343' : 't.cast'
 , 'C23441' : 'E channel'
 , 'C17341' : '히스토리'
 , 'C00585' : 'TV CHOSUN2'
 , 'C17141' : '채널A 플러스'
 , 'C00611' : 'LIFETIME'
 , 'C08041' : 'tvN go'
 , 'C05901' : '채널W'
 , 'C23442' : "D'LIVE"
 , 'C27441' : 'KBS N'
 }
if 97 - 97: Oo0Ooo - ooOoO0o
O0o = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
if 97 - 97: OoO0O00 . I11i
from tvingCore import *
if 32 - 32: Oo0Ooo - II111iiii - i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
def iIiiI1 ( sting ) :
 try :
  OoOooOOOO = xbmcgui . Dialog ( )
  if 45 - 45: I1Ii111 + Ii1I
  OoOooOOOO . notification ( __addonname__ , sting )
 except :
  None
  if 17 - 17: o0oOOo0O0Ooo
  if 64 - 64: Ii1I % i1IIi % OoooooooOO
  if 3 - 3: iII111i + O0
def I1Ii ( string , isDebug = False ) :
 try :
  o0oOo0Ooo0O = string . encode ( 'utf-8' , 'ignore' )
 except :
  o0oOo0Ooo0O = 'addonException: addon_log'
 if isDebug : OO00O0O0O00Oo = xbmc . LOGDEBUG
 else : OO00O0O0O00Oo = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , o0oOo0Ooo0O ) , level = OO00O0O0O00Oo )
 if 25 - 25: o0oOOo0O0Ooo % II111iiii - II111iiii . II111iiii
 if 32 - 32: i1IIi . I11i % OoO0O00 . o0oOOo0O0Ooo
 if 42 - 42: I1Ii111 + I1ii11iIi11i
 if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
def iiI1IiI ( title ) :
 II = None
 ooOoOoo0O = xbmc . Keyboard ( )
 ooOoOoo0O . setHeading ( title )
 xbmc . sleep ( 1000 )
 ooOoOoo0O . doModal ( )
 if ( ooOoOoo0O . isConfirmed ( ) ) :
  II = ooOoOoo0O . getText ( )
 return II
 if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
 if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
 if 75 - 75: iII111i
 if 97 - 97: i11iIiiIii
def II1i1Ii11Ii11 ( ) :
 iII11i = __addon__ . getSetting ( 'id' )
 O0O00o0OOO0 = __addon__ . getSetting ( 'pw' )
 Ii1iIIIi1ii = __addon__ . getSetting ( 'login_type' )
 return ( iII11i , O0O00o0OOO0 , Ii1iIIIi1ii )
 if 80 - 80: I11i * i11iIiiIii / I1Ii111
 if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
 if 26 - 26: OoooooooOO
def IiiI11Iiiii ( ) :
 ii1I1i1I = __addon__ . getSetting ( 'premium_movieyn' )
 if ii1I1i1I == 'false' :
  return False
 else :
  return True
  if 88 - 88: OoO0O00 + O0 / OoOoOO00 * iII111i
  if 41 - 41: oO0o
  if 6 - 6: I1ii11iIi11i
  if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * I1IiiI
def O0ooOooooO ( credential ) :
 o00O = xbmcgui . Window ( 10000 )
 o00O . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
 o00O . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
 o00O . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 o00O . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 if 4 - 4: II111iiii / ooOoO0o . iII111i
def O0oo0OO0oOOOo ( ) :
 o00O = xbmcgui . Window ( 10000 )
 i1i1i11IIi = {
 'tving_token' : o00O . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : o00O . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : o00O . getProperty ( 'TVING_M_UUID' )
 }
 return i1i1i11IIi
 if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
def II1i1IiiIIi11 ( orderby ) :
 o00O = xbmcgui . Window ( 10000 )
 o00O . setProperty ( 'TVING_M_ORDERBY' , orderby )
 if 47 - 47: iII111i
def Ii11iII1 ( ) :
 o00O = xbmcgui . Window ( 10000 )
 return o00O . getProperty ( 'TVING_M_ORDERBY' )
 if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / ooOoO0o
 if 49 - 49: o0oOOo0O0Ooo
 if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
def o00OO00OoO ( ) :
 OOOO0OOoO0O0 = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for O0Oo000ooO00 in OOOO0OOoO0O0 . keys ( ) :
  OOOO0OOoO0O0 [ O0Oo000ooO00 ] = OOOO0OOoO0O0 [ O0Oo000ooO00 ] [ 0 ]
 return OOOO0OOoO0O0
 if 75 - 75: oO0o . OoO0O00 * OOooOOo
 if 91 - 91: Ii1I
 if 30 - 30: o0oOOo0O0Ooo . Ii1I - OoooooooOO
def Ii1iIiii1 ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 OOO = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 if sublabel : Oo0OoO00oOO0o = '%s < %s >' % ( label , sublabel )
 else : Oo0OoO00oOO0o = label
 if not img : img = 'DefaultFolder.png'
 if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 OoOO0oo0o = xbmcgui . ListItem ( Oo0OoO00oOO0o , thumbnailImage = img )
 if infoLabels : OoOO0oo0o . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : OoOO0oo0o . setProperty ( 'IsPlayable' , 'true' )
 if 14 - 14: o0oOOo0O0Ooo * iII111i * iII111i / OoOoOO00
 xbmcplugin . addDirectoryItem ( Oo0o00 , OOO , OoOO0oo0o , isFolder )
 if 73 - 73: iII111i * Ii1I + o0oOOo0O0Ooo . OOooOOo + I1ii11iIi11i % iII111i
 if 95 - 95: i1IIi
 if 3 - 3: I1Ii111 - O0 / I1Ii111 % OoO0O00 / I1Ii111 . I1IiiI
def iiI111I1iIiI ( etype ) :
 try :
  if etype == 'movie' :
   IIIi1I1IIii1II = 'movie_quality'
  else :
   IIIi1I1IIii1II = 'selected_quality'
   if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  iii1i1iiiiIi = [ 1080 , 720 , 480 , 360 ]
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  o0o00OO0 = int ( __addon__ . getSetting ( IIIi1I1IIii1II ) )
  return iii1i1iiiiIi [ o0o00OO0 ]
 except :
  None
  if 7 - 7: OOooOOo + I1Ii111 + O0
 return 720
 if 9 - 9: II111iiii . o0oOOo0O0Ooo - ooOoO0o / o0oOOo0O0Ooo
 if 46 - 46: I11i . OOooOOo * I11i % i1IIi
 if 46 - 46: OoOoOO00 + OoO0O00
def iIi1i1ii1 ( ) :
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 for OOOOoOoo0O0O0 in o0oO0 :
  Oo0OoO00oOO0o = OOOOoOoo0O0O0 . get ( 'title' )
  if 85 - 85: oO0o % i11iIiiIii - iII111i * OoooooooOO / I1IiiI % I1IiiI
  IIiIi1iI = { 'mode' : OOOOoOoo0O0O0 . get ( 'mode' )
 , 'stype' : OOOOoOoo0O0O0 . get ( 'stype' )
 , 'orderby' : OOOOoOoo0O0O0 . get ( 'orderby' )
 , 'page' : '1'
 }
  if 35 - 35: Ii1I % O0 - O0
  if OOOOoOoo0O0O0 . get ( 'mode' ) == 'XXX' :
   IIiIi1iI [ 'mode' ] = 'XXX'
   IiIIIi1iIi = False
  else :
   IiIIIi1iIi = True
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = IiIIIi1iIi , params = IIiIi1iI )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 31 - 31: II111iiii . I1IiiI
 if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
 if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
 if 92 - 92: iII111i
def IIiIiiIi ( ) :
 ( O000oo , IIi1I11I1II , OooOoooOo ) = II1i1Ii11Ii11 ( )
 if 46 - 46: iII111i
 if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
 if not ( O000oo and IIi1I11I1II ) :
  OoOooOOOO = xbmcgui . Dialog ( )
  ii = OoOooOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if ii == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 90 - 90: o0oOOo0O0Ooo % i1IIi / OoO0O00
   if 44 - 44: Oo0Ooo . OoO0O00 / I1ii11iIi11i + Ii1I
 if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
  o0o = 0
  while True :
   o0o += 1
   xbmc . sleep ( 250 )
   if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'FALSE' or o0o > 500 :
    break
    if 73 - 73: IiII * I1ii11iIi11i + I1IiiI . ooOoO0o
 o0oO00000 = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
 if 69 - 69: OoO0O00 - Oo0Ooo + i1IIi / I1Ii111
 if o0oO00000 != '' :
  if 49 - 49: O0 . iII111i
  if o0oO00000 == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
   if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
   if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   if 54 - 54: OoOoOO00 % iII111i
   if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
   if 88 - 88: iII111i . II111iiii * II111iiii % I1Ii111
   if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
   if 80 - 80: II111iiii
   if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
   if 53 - 53: II111iiii
   if 31 - 31: OoO0O00
   return
   if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if not oO0OOOO0 . GetCredential ( O000oo , IIi1I11I1II , OooOoooOo ) :
  iIiiI1 ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  sys . exit ( )
  if 26 - 26: Ii1I
  if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
 O0ooOooooO ( oO0OOOO0 . LoadCredential ( ) )
 II1i1IiiIIi11 ( 'desc' )
 xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
 if 47 - 47: iII111i - Ii1I . II111iiii + OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 if 87 - 87: Oo0Ooo . IiII
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
def oO ( args ) :
 I1Ii1I1 = args . get ( 'stype' )
 if I1Ii1I1 == 'live' :
  IiII111iI1ii1 = xI1Ii11I1Ii1i
 else :
  IiII111iI1ii1 = I11
  if 37 - 37: oO0o - I1Ii111 % Oo0Ooo
 for OOOoo0OO in IiII111iI1ii1 :
  Oo0OoO00oOO0o = OOOoo0OO . get ( 'title' )
  if 57 - 57: OoO0O00 / ooOoO0o
  IIiIi1iI = { 'mode' : OOOoo0OO . get ( 'mode' )
 , 'stype' : OOOoo0OO . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
 if len ( IiII111iI1ii1 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
 if 13 - 13: Ii1I . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
def Oo0O0oooo ( args ) :
 if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 I1Ii1I1 = args . get ( 'stype' )
 Oo = int ( args . get ( 'page' ) )
 O0OOOOo0O , OooOO = oO0OOOO0 . GetLiveChannelList ( I1Ii1I1 , Oo )
 if 21 - 21: I11i / IiII % iIii1I11I1II1 * Oo0Ooo
 for oooooOO in O0OOOOo0O :
  Oo0OoO00oOO0o = oooooOO . get ( 'title' )
  IiI = oooooOO . get ( 'channel' )
  IIIii1I = oooooOO . get ( 'thumbnail' )
  ooO0OO = oooooOO . get ( 'synopsis' )
  O000OOO = oooooOO . get ( 'channelepg' )
  if 20 - 20: o0oOOo0O0Ooo . II111iiii % OOooOOo * iIii1I11I1II1
  oO00oOOoooO = { }
  oO00oOOoooO [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( IiI , Oo0OoO00oOO0o , O000OOO , ooO0OO )
  if 46 - 46: I1IiiI - OoooooooOO - I11i * II111iiii
  IIiIi1iI = { 'mode' : 'LIVE'
 , 'mediacode' : oooooOO . get ( 'mediacode' )
 , 'stype' : I1Ii1I1
  }
  if 34 - 34: I11i - iII111i / OOooOOo + I1ii11iIi11i * Ii1I
  Ii1iIiii1 ( IiI , sublabel = Oo0OoO00oOO0o , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = False , params = IIiIi1iI )
  if 73 - 73: OoOoOO00 . Ii1I * I1ii11iIi11i % I1ii11iIi11i % OoooooooOO
 if OooOO :
  if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
  IIiIi1iI [ 'mode' ] = 'CHANNEL'
  IIiIi1iI [ 'stype' ] = I1Ii1I1
  IIiIi1iI [ 'page' ] = str ( Oo + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  iI1111iiii = str ( Oo + 1 )
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = iI1111iiii , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
 if len ( O0OOOOo0O ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
 if 71 - 71: I1Ii111 + Ii1I
 if 28 - 28: OOooOOo
 if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
def OoOOo0OOoO ( args ) :
 if 72 - 72: Ii1I
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
 I1Ii1I1 = args . get ( 'stype' )
 IiII111i1i11 = args . get ( 'orderby' )
 Oo = int ( args . get ( 'page' ) )
 if 40 - 40: ooOoO0o * IiII * i11iIiiIii
 oo0OO00OoooOo , OooOO = oO0OOOO0 . GetProgramList ( I1Ii1I1 , IiII111i1i11 , Oo )
 if 19 - 19: I1ii11iIi11i % OoooooooOO % IiII * o0oOOo0O0Ooo % O0
 for ooo in oo0OO00OoooOo :
  Oo0OoO00oOO0o = ooo . get ( 'title' )
  IIIii1I = ooo . get ( 'thumbnail' )
  ooO0OO = ooo . get ( 'synopsis' )
  i1i1iI1iiiI = o0o0Oo0oooo0 . get ( ooo . get ( 'channel' ) )
  if 51 - 51: I1IiiI % I1Ii111 . oO0o / iIii1I11I1II1 / I11i . oO0o
  oO00oOOoooO = { }
  oO00oOOoooO [ 'plot' ] = '%s <%s>\n\n%s' % ( Oo0OoO00oOO0o , i1i1iI1iiiI , ooO0OO )
  if 42 - 42: o0oOOo0O0Ooo + i1IIi - Ii1I / IiII
  IIiIi1iI = { 'mode' : 'EPISODE'
 , 'programcode' : ooo . get ( 'program' )
 , 'page' : '1'
 }
  if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = i1i1iI1iiiI , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = True , params = IIiIi1iI )
  if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
 if OooOO :
  if 52 - 52: o0oOOo0O0Ooo + O0 + iII111i + Oo0Ooo % iII111i
  IIiIi1iI [ 'mode' ] = 'PROGRAM'
  IIiIi1iI [ 'stype' ] = I1Ii1I1
  IIiIi1iI [ 'orderby' ] = IiII111i1i11
  IIiIi1iI [ 'page' ] = str ( Oo + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  iI1111iiii = str ( Oo + 1 )
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = iI1111iiii , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if 75 - 75: I1IiiI . ooOoO0o . O0 * I1Ii111
 if len ( oo0OO00OoooOo ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 4 - 4: Ii1I % oO0o * OoO0O00
 if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
 if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
 if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
def oo00o0 ( args ) :
 if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 41 - 41: IiII / O0
 o0oO0oooOoo = args . get ( 'programcode' )
 Oo = int ( args . get ( 'page' ) )
 if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
 iI1i111I1Ii , OooOO , i11i1ii1I = oO0OOOO0 . GetEpisodoList ( o0oO0oooOoo , Oo , orderby = Ii11iII1 ( ) )
 if 88 - 88: I11i % I1ii11iIi11i
 for I1i11 in iI1i111I1Ii :
  Oo0OoO00oOO0o = I1i11 . get ( 'title' )
  IIIii1I = I1i11 . get ( 'thumbnail' )
  ooO0OO = I1i11 . get ( 'synopsis' )
  if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
  oO00oOOoooO = { }
  oO00oOOoooO [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , ooO0OO )
  if 52 - 52: ooOoO0o . iII111i + I1Ii111
  IIiIi1iI = { 'mode' : 'VOD'
 , 'mediacode' : I1i11 . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : o0oO0oooOoo
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : IIIii1I
 }
  if 38 - 38: i1IIi - II111iiii . I1Ii111
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = False , params = IIiIi1iI )
  if 58 - 58: I1IiiI . iII111i + OoOoOO00
  if 66 - 66: iII111i / oO0o * OoooooooOO + OoooooooOO % I11i
  if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
  if 71 - 71: o0oOOo0O0Ooo
  if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  if 53 - 53: i11iIiiIii * iII111i
 if Oo == 1 :
  oO00oOOoooO = { 'plot' : '정렬순서를 변경합니다.' }
  IIiIi1iI = { }
  IIiIi1iI [ 'mode' ] = 'ORDER_BY'
  if Ii11iII1 ( ) == 'desc' :
   Oo0OoO00oOO0o = '정렬순서변경 : 최신화부터 -> 1회부터'
   IIiIi1iI [ 'orderby' ] = 'asc'
  else :
   Oo0OoO00oOO0o = '정렬순서변경 : 1회부터 -> 최신화부터'
   IIiIi1iI [ 'orderby' ] = 'desc'
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = oO00oOOoooO , isFolder = False , params = IIiIi1iI )
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
  if 38 - 38: ooOoO0o - OOooOOo / iII111i
 if OooOO :
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
  IIiIi1iI [ 'mode' ] = 'EPISODE'
  IIiIi1iI [ 'programcode' ] = o0oO0oooOoo
  IIiIi1iI [ 'page' ] = str ( Oo + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  iI1111iiii = str ( Oo + 1 )
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = iI1111iiii , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if 86 - 86: o0oOOo0O0Ooo
 if len ( iI1i111I1Ii ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 5 - 5: IiII * OoOoOO00
 if 5 - 5: I1Ii111
 if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
 if 40 - 40: OoooooooOO
def I1i1i1 ( args ) :
 IiII111i1i11 = args . get ( 'orderby' )
 if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
 II1i1IiiIIi11 ( IiII111i1i11 )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
 if 9 - 9: I11i % OoooooooOO . oO0o % I11i
 if 32 - 32: i11iIiiIii
 if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
def iiIiIi ( args ) :
 if 39 - 39: I1Ii111
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
 IiII111i1i11 = args . get ( 'orderby' )
 Oo = int ( args . get ( 'page' ) )
 if 26 - 26: I1ii11iIi11i - OoooooooOO
 iiI1iI111ii1i , OooOO = oO0OOOO0 . GetMovieList ( IiII111i1i11 , Oo , premiumyn = IiiI11Iiiii ( ) )
 if 32 - 32: II111iiii * OoOoOO00 % i1IIi - iII111i + iIii1I11I1II1 + I1ii11iIi11i
 for OO0O0Oo000 in iiI1iI111ii1i :
  Oo0OoO00oOO0o = OO0O0Oo000 . get ( 'title' )
  IIIii1I = OO0O0Oo000 . get ( 'thumbnail' )
  ooO0OO = OO0O0Oo000 . get ( 'synopsis' )
  if 41 - 41: i1IIi - I11i - Ii1I
  oO00oOOoooO = { }
  oO00oOOoooO [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , ooO0OO )
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  IIiIi1iI = { 'mode' : 'MOVIE'
 , 'mediacode' : OO0O0Oo000 . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : IIIii1I
 }
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = False , params = IIiIi1iI )
  if 44 - 44: II111iiii
 if OooOO :
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  IIiIi1iI [ 'mode' ] = 'MOVIE_GROUP'
  IIiIi1iI [ 'orderby' ] = IiII111i1i11
  IIiIi1iI [ 'page' ] = str ( Oo + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  iI1111iiii = str ( Oo + 1 )
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = iI1111iiii , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if 35 - 35: iIii1I11I1II1
 if len ( iiI1iI111ii1i ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
 if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
 if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
 if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
 if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
def OOOO0O00o ( args ) :
 for OOOoo0OO in Oooo0000 :
  Oo0OoO00oOO0o = OOOoo0OO . get ( 'title' )
  if 62 - 62: iIii1I11I1II1
  IIiIi1iI = { 'mode' : OOOoo0OO . get ( 'mode' )
 , 'stype' : OOOoo0OO . get ( 'stype' )
 , 'page' : '1'
 }
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
 if len ( Oooo0000 ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 42 - 42: Oo0Ooo
 if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
 if 46 - 46: Oo0Ooo
 if 1 - 1: iII111i
def O0O0Ooo ( args ) :
 if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
 Oo00o0OO0O00o = __addon__ . getSetting ( 'id' )
 Oo = int ( args . get ( 'page' ) )
 I1Ii1I1 = args . get ( 'stype' )
 if 82 - 82: I11i + OoooooooOO - i1IIi . i1IIi
 if 'search_key' in args :
  iIi1i = args . get ( 'search_key' )
 else :
  iIi1i = iiI1IiI ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not iIi1i : return
  if 27 - 27: OOooOOo * ooOoO0o . I1Ii111 % IiII * IiII . i1IIi
 O0OOoOOO0oO , OooOO = oO0OOOO0 . GetSearchList ( iIi1i , Oo00o0OO0O00o , Oo , I1Ii1I1 , premiumyn = IiiI11Iiiii ( ) )
 if len ( O0OOoOOO0oO ) == 0 : return
 if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
 for ooo0OOO in O0OOoOOO0oO :
  Oo0OoO00oOO0o = ooo0OOO . get ( 'title' )
  IIIii1I = ooo0OOO . get ( 'thumbnail' )
  ooO0OO = ooo0OOO . get ( 'synopsis' )
  iii1Ii1Ii1 = ooo0OOO . get ( 'program' )
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  oO00oOOoooO = { }
  oO00oOOoooO [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , ooO0OO )
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if I1Ii1I1 == 'vod' :
   IIiIi1iI = { 'mode' : 'EPISODE'
 , 'programcode' : ooo0OOO . get ( 'program' )
 , 'page' : '1'
 }
   IiIIIi1iIi = True
  else :
   IIiIi1iI = { 'mode' : 'MOVIE'
 , 'mediacode' : ooo0OOO . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : IIIii1I
 }
   IiIIIi1iIi = False
   if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = IiIIIi1iIi , params = IIiIi1iI )
  if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
 if OooOO :
  if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
  IIiIi1iI [ 'mode' ] = 'SEARCH'
  IIiIi1iI [ 'search_key' ] = iIi1i
  IIiIi1iI [ 'page' ] = str ( Oo + 1 )
  Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
  iI1111iiii = str ( Oo + 1 )
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = iI1111iiii , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if 9 - 9: Ii1I
 if len ( O0OOoOOO0oO ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
 if 59 - 59: I1IiiI * II111iiii . O0
 if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
 if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
 if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
def i1 ( stype ) :
 try :
  OO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( OO0oOOoo , 'w' ) as oOOO00o000o :
   oOOO00o000o . write ( '' )
 except :
  None
  if 9 - 9: oO0o + I11i / I11i
  if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
  if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
  if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
def ooOOo00O00Oo ( args ) :
 I1Ii1I1 = args . get ( 'stype' )
 if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * ooOoO0o % ooOoO0o
 OoOooOOOO = xbmcgui . Dialog ( )
 ii = OoOooOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if ii == False : sys . exit ( )
 if 7 - 7: iII111i / I1ii11iIi11i / i11iIiiIii
 i1 ( I1Ii1I1 )
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 xbmc . executebuiltin ( "Container.Refresh" )
 if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
 if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 if 97 - 97: I1IiiI / iII111i
def Oooo0 ( stype ) :
 try :
  OO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( OO0oOOoo , 'r' ) as oOOO00o000o :
   oOO = oOOO00o000o . readlines ( )
 except :
  oOO = [ ]
  if 54 - 54: I1IiiI / iIii1I11I1II1 / OOooOOo . OOooOOo % iII111i . I1IiiI
 return oOO
 if 10 - 10: o0oOOo0O0Ooo + OOooOOo
 if 27 - 27: OoO0O00 . I11i + OoOoOO00 / iIii1I11I1II1 % iII111i . ooOoO0o
 if 14 - 14: oO0o + I1ii11iIi11i - iII111i / O0 . I1Ii111
 if 45 - 45: I1Ii111
def oOIIi1iiii1iI ( stype , in_params ) :
 try :
  OO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  iIiiii = Oooo0 ( stype )
  if 89 - 89: iII111i - ooOoO0o % Oo0Ooo % o0oOOo0O0Ooo
  with open ( OO0oOOoo , 'w' ) as oOOO00o000o :
   IIiii11i = urllib . urlencode ( in_params )
   IIiii11i = IIiii11i . encode ( 'utf-8' ) + '\n'
   oOOO00o000o . write ( IIiii11i )
   if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
   oo00O00oO000o = 0
   for OOo00OoO in iIiiii :
    iIi1 = dict ( urlparse . parse_qsl ( OOo00OoO ) )
    if in_params . get ( 'code' ) != iIi1 . get ( 'code' ) :
     oOOO00o000o . write ( OOo00OoO )
     oo00O00oO000o += 1
     if oo00O00oO000o >= 50 : break
 except :
  None
  if 21 - 21: I11i
  if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
  if 11 - 11: OoooooooOO . I1Ii111
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
def I1I11iI11iI1i ( args ) :
 I1Ii1I1 = args . get ( 'stype' )
 if 75 - 75: OoooooooOO * IiII
 if I1Ii1I1 == '-' :
  for OOOoo0OO in OOo :
   Oo0OoO00oOO0o = OOOoo0OO . get ( 'title' )
   if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   IIiIi1iI = { 'mode' : OOOoo0OO . get ( 'mode' )
 , 'stype' : OOOoo0OO . get ( 'stype' )
 }
   if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
   Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IIiIi1iI )
  if len ( OOo ) > 0 : xbmcplugin . endOfDirectory ( Oo0o00 )
  if 69 - 69: O0
 else :
  o0ooO = Oooo0 ( I1Ii1I1 )
  if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
  for Iii in o0ooO :
   I1iiiiI1iI = dict ( urlparse . parse_qsl ( Iii ) )
   if 43 - 43: oO0o - OoooooooOO
   Oo0OoO00oOO0o = I1iiiiI1iI . get ( 'title' )
   IIIii1I = I1iiiiI1iI . get ( 'img' )
   if 3 - 3: O0 / iII111i
   oO00oOOoooO = { }
   oO00oOOoooO [ 'plot' ] = Oo0OoO00oOO0o
   if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
   if I1Ii1I1 == 'vod' :
    IIiIi1iI = { 'mode' : 'EPISODE'
 , 'programcode' : I1iiiiI1iI . get ( 'code' )
 , 'page' : '1'
 }
    IiIIIi1iIi = True
   else :
    IIiIi1iI = { 'mode' : 'MOVIE'
 , 'mediacode' : I1iiiiI1iI . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : IIIii1I
 }
    IiIIIi1iIi = False
    if 89 - 89: II111iiii + i1IIi + II111iiii
   Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = IIIii1I , infoLabels = oO00oOOoooO , isFolder = IiIIIi1iIi , params = IIiIi1iI )
   if 7 - 7: O0 % o0oOOo0O0Ooo + I1ii11iIi11i * iII111i - iII111i
  oO00oOOoooO = { 'plot' : '시청목록을 삭제합니다.' }
  Oo0OoO00oOO0o = '*** 시청목록 삭제 ***'
  IIiIi1iI = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : I1Ii1I1
 }
  if 42 - 42: OoOoOO00 * OoOoOO00 * I1Ii111 . I11i
  Ii1iIiii1 ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = oO00oOOoooO , isFolder = False , params = IIiIi1iI )
  if 51 - 51: OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o * iIii1I11I1II1 % OoO0O00
  xbmcplugin . endOfDirectory ( Oo0o00 , cacheToDisc = False )
  if 99 - 99: oO0o * II111iiii * I1Ii111
  if 92 - 92: Oo0Ooo
  if 40 - 40: OoOoOO00 / IiII
  if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
  if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
def ooO0o ( args ) :
 if 89 - 89: I11i / I1Ii111
 oO0OOOO0 . SaveCredential ( O0oo0OO0oOOOo ( ) )
 if 90 - 90: iII111i
 i1i1i1I = args . get ( 'mediacode' )
 I1Ii1I1 = args . get ( 'stype' )
 oOoo000 = iiI111I1iIiI ( I1Ii1I1 )
 if 87 - 87: OoooooooOO - o0oOOo0O0Ooo / IiII . i11iIiiIii * OoooooooOO
 OO00 , IIiiIIi1 = oO0OOOO0 . GetBroadURL ( i1i1i1I , oOoo000 , I1Ii1I1 )
 if 59 - 59: IiII . OOooOOo % II111iiii
 I1Ii ( 'qt, stype, url : %s - %s - %s' % ( str ( oOoo000 ) , I1Ii1I1 , OO00 ) )
 if 39 - 39: I1ii11iIi11i
 if OO00 == '' :
  iIiiI1 ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 97 - 97: OOooOOo - OoO0O00 / Ii1I . i11iIiiIii % oO0o * oO0o
  if 1 - 1: I1IiiI % ooOoO0o
  if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
 oOOoOooo0O0o = OO00 . find ( 'Policy=' )
 if oOOoOooo0O0o != - 1 :
  Oo000 = OO00 . split ( '?' ) [ 0 ]
  if 81 - 81: OOooOOo - OOooOOo % II111iiii * OoO0O00
  iIi1iI111I = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OO00 ) . query ) )
  iIi1iI111I = urllib . urlencode ( iIi1iI111I )
  iIi1iI111I = iIi1iI111I . replace ( '&' , ';' )
  iIi1iI111I = iIi1iI111I . replace ( 'Policy' , 'CloudFront-Policy' )
  iIi1iI111I = iIi1iI111I . replace ( 'Signature' , 'CloudFront-Signature' )
  iIi1iI111I = iIi1iI111I . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
  I1iii = '%s|Cookie=%s' % ( Oo000 , iIi1iI111I )
 else :
  I1iii = OO00
  if 86 - 86: I1ii11iIi11i * O0 * IiII
  if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
 I1Ii ( I1iii , False )
 if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
 if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % OOooOOo
 if 63 - 63: I1IiiI % iIii1I11I1II1
 I1ii = xbmcgui . ListItem ( path = I1iii )
 if 73 - 73: IiII + I1IiiI * Oo0Ooo * OoooooooOO
 if 95 - 95: i1IIi + iIii1I11I1II1 % I1ii11iIi11i % Oo0Ooo / i11iIiiIii - IiII
 if IIiiIIi1 != '' :
  I1 = IIiiIIi1
  O0iIi1IiII = 'https://cj.drmkeyserver.com/widevine_license'
  if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
  iIi1ii1ii = 'mpd'
  O0ooO0ooo0oO = 'com.widevine.alpha'
  if 10 - 10: II111iiii . iII111i
  I1i = inputstreamhelper . Helper ( iIi1ii1ii , drm = O0ooO0ooo0oO )
  if 86 - 86: Oo0Ooo / oO0o + O0 * iII111i
  if I1i . check_inputstream ( ) :
   if 19 - 19: II111iiii * IiII + Ii1I
   O0ooO00oO = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % i1i1i1I
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
   , 'user-agent' : O0o
 , 'AcquireLicenseAssertion' : I1
 , 'Host' : 'cj.drmkeyserver.com'
 }
   i11i1iIiii = O0iIi1IiII + '|' + urllib . urlencode ( O0ooO00oO ) + '|R{SSM}|'
   if 71 - 71: I1ii11iIi11i % ooOoO0o - I1IiiI % I11i - O0
   I1ii . setProperty ( 'inputstreamaddon' , I1i . inputstream_addon )
   if 67 - 67: OOooOOo + Oo0Ooo
   I1ii . setProperty ( 'inputstream.adaptive.manifest_type' , iIi1ii1ii )
   I1ii . setProperty ( 'inputstream.adaptive.license_type' , O0ooO0ooo0oO )
   if 84 - 84: O0 * OoooooooOO - IiII * IiII
   I1ii . setProperty ( 'inputstream.adaptive.license_key' , i11i1iIiii )
   if 8 - 8: ooOoO0o / i1IIi . oO0o
   if 41 - 41: iII111i + OoO0O00
   if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
   if 56 - 56: O0
   if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
 xbmcplugin . setResolvedUrl ( Oo0o00 , True , I1ii )
 if 23 - 23: oO0o - OOooOOo + I11i
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
  IIiIi1iI = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
  oOIIi1iiii1iI ( args . get ( 'stype' ) , IIiIi1iI )
  if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
  if 11 - 11: iII111i * Ii1I - OoOoOO00
  if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
  if 74 - 74: Oo0Ooo
  if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
oO0OOOO0 = oo0Ooo0 ( )
Oo0o00 = int ( sys . argv [ 1 ] )
if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
IIiIi1iI = o00OO00OoO ( )
II1I1iiIII1I1 = IIiIi1iI . get ( 'mode' , None )
if 85 - 85: iII111i * o0oOOo0O0Ooo
IIiIiiIi ( )
if 3 - 3: OOooOOo
if II1I1iiIII1I1 is None :
 if 20 - 20: II111iiii . iII111i / II111iiii % i11iIiiIii % iII111i
 iIi1i1ii1 ( )
 if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
 if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
elif II1I1iiIII1I1 in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
 oO ( IIiIi1iI )
 if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
elif II1I1iiIII1I1 == 'CHANNEL' :
 Oo0O0oooo ( IIiIi1iI )
 if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
elif II1I1iiIII1I1 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 ooO0o ( IIiIi1iI )
 xbmc . sleep ( 200 )
 if 71 - 71: OoooooooOO
elif II1I1iiIII1I1 == 'PROGRAM' :
 OoOOo0OOoO ( IIiIi1iI )
 if 33 - 33: I1Ii111
elif II1I1iiIII1I1 == 'EPISODE' :
 oo00o0 ( IIiIi1iI )
 if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
elif II1I1iiIII1I1 == 'MOVIE_GROUP' :
 iiIiIi ( IIiIi1iI )
 if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
elif II1I1iiIII1I1 == 'SEARCH_GROUP' :
 OOOO0O00o ( IIiIi1iI )
 if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
elif II1I1iiIII1I1 == 'SEARCH' :
 O0O0Ooo ( IIiIi1iI )
 if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
elif II1I1iiIII1I1 == 'WATCH' :
 I1I11iI11iI1i ( IIiIi1iI )
 if 45 - 45: IiII
elif II1I1iiIII1I1 == 'MYVIEW_REMOVE' :
 ooOOo00O00Oo ( IIiIi1iI )
 if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
elif II1I1iiIII1I1 == 'ORDER_BY' :
 I1i1i1 ( IIiIi1iI )
 if 78 - 78: iIii1I11I1II1 + I11i - Ii1I * I1Ii111 - OoooooooOO % OoOoOO00
else :
 None
 if 34 - 34: O0
 if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
 if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
