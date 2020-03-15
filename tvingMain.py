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
 { 'title' : 'LIVE 채널' , 'mode' : 'LIVE_GROUP' , 'stype' : 'live' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : 'VOD 방송 (인기순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'viewDay' , 'ordernm' : '인기' }
 , { 'title' : 'VOD 방송 (최신순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'new' , 'ordernm' : '최신' }
 , { 'title' : '월정액 영화관 (인기)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'viewWeek' , 'ordernm' : '-' }
 , { 'title' : '월정액 영화관 (최신)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'new' , 'ordernm' : '-' }
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : '검색 (VOD,영화)' , 'mode' : 'SEARCH_GROUP' , 'stype' : '-' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : '-' , 'orderby' : '-' , 'ordernm' : '-' }
 ]
if 100 - 100: i1IIi
I1Ii11I1Ii1ix = [
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
def O0ooOooooO ( ) :
 o00O = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
 if o00O == 0 :
  return True
 else :
  return False
  if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
  if 4 - 4: II111iiii / ooOoO0o . iII111i
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
def ii11i1 ( credential ) :
 IIIii1II1II = xbmcgui . Window ( 10000 )
 IIIii1II1II . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
 IIIii1II1II . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
 IIIii1II1II . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
 if 42 - 42: Ii1I + oO0o
 IIIii1II1II . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 76 - 76: I1Ii111 - OoO0O00
 if 70 - 70: ooOoO0o
def oOO ( ) :
 IIIii1II1II = xbmcgui . Window ( 10000 )
 IIi1I1Ii11iI = {
 'tving_token' : IIIii1II1II . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : IIIii1II1II . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : IIIii1II1II . getProperty ( 'TVING_M_UUID' )
 }
 return IIi1I1Ii11iI
 if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
def OoOOOOO ( orderby ) :
 IIIii1II1II = xbmcgui . Window ( 10000 )
 IIIii1II1II . setProperty ( 'TVING_M_ORDERBY' , orderby )
 if 33 - 33: I1ii11iIi11i % i1IIi
def o00OO00OoO ( ) :
 IIIii1II1II = xbmcgui . Window ( 10000 )
 return IIIii1II1II . getProperty ( 'TVING_M_ORDERBY' )
 if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
 if 70 - 70: IiII * Oo0Ooo * I11i / Ii1I
 if 88 - 88: O0
def O0OoO0O00o0oO ( ) :
 I1ii1Ii1 = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for iii11 in I1ii1Ii1 . keys ( ) :
  I1ii1Ii1 [ iii11 ] = I1ii1Ii1 [ iii11 ] [ 0 ]
 return I1ii1Ii1
 if 68 - 68: OoO0O00
 if 35 - 35: OoO0O00 - iII111i / Oo0Ooo / OoOoOO00
 if 24 - 24: ooOoO0o - ooOoO0o / II111iiii - I1ii11iIi11i
def OO ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 I1III = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 63 - 63: OOooOOo % oO0o * oO0o * OoO0O00 / I1ii11iIi11i
 if sublabel : o0ooO = '%s < %s >' % ( label , sublabel )
 else : o0ooO = label
 if not img : img = 'DefaultFolder.png'
 if 98 - 98: iII111i * iII111i / iII111i + I11i
 ii111111I1iII = xbmcgui . ListItem ( o0ooO , thumbnailImage = img )
 if infoLabels : ii111111I1iII . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : ii111111I1iII . setProperty ( 'IsPlayable' , 'true' )
 if 68 - 68: iII111i - iIii1I11I1II1 * i11iIiiIii / I1ii11iIi11i * I1Ii111
 xbmcplugin . addDirectoryItem ( i1iIi1iIi1i , I1III , ii111111I1iII , isFolder )
 if 46 - 46: I1Ii111 % I11i + OoO0O00 . OoOoOO00 . OoO0O00
 if 96 - 96: Oo0Ooo
 if 45 - 45: O0 * o0oOOo0O0Ooo % Oo0Ooo * OoooooooOO + iII111i . OoOoOO00
def Oo0ooOo0o ( etype ) :
 try :
  if etype == 'movie' :
   Ii1i1 = 'movie_quality'
  else :
   Ii1i1 = 'selected_quality'
   if 15 - 15: II111iiii
  Ii = [ 1080 , 720 , 480 , 360 ]
  if 79 - 79: OoooooooOO / O0
  OO0OoO0o00 = int ( __addon__ . getSetting ( Ii1i1 ) )
  return Ii [ OO0OoO0o00 ]
 except :
  None
  if 53 - 53: O0 * OoO0O00 + OOooOOo
 return 720
 if 50 - 50: O0 . O0 - oO0o / I1IiiI - o0oOOo0O0Ooo * OoOoOO00
 if 61 - 61: I11i
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
def iIIi1i1 ( ) :
 if 10 - 10: I11i
 for OOooOO000 in o0oO0 :
  o0ooO = OOooOO000 . get ( 'title' )
  if 97 - 97: I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
  I1111IIi = { 'mode' : OOooOO000 . get ( 'mode' )
 , 'stype' : OOooOO000 . get ( 'stype' )
 , 'orderby' : OOooOO000 . get ( 'orderby' )
 , 'ordernm' : OOooOO000 . get ( 'ordernm' )
 , 'page' : '1'
 }
  if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
  if OOooOO000 . get ( 'mode' ) == 'XXX' :
   I1111IIi [ 'mode' ] = 'XXX'
   I1 = False
  else :
   I1 = True
   if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
  OO ( o0ooO , sublabel = '' , img = '' , infoLabels = None , isFolder = I1 , params = I1111IIi )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i )
 if 9 - 9: OoooooooOO
 if 62 - 62: OOooOOo / OoO0O00 + Ii1I / OoO0O00 . II111iiii
 if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
 if 31 - 31: II111iiii . I1IiiI
def II1I ( ) :
 ( O0i1II1Iiii1I11 , IIII , iiIiI ) = II1i1Ii11Ii11 ( )
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if not ( O0i1II1Iiii1I11 and IIII ) :
  OoOooOOOO = xbmcgui . Dialog ( )
  III1IiiI = OoOooOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if III1IiiI == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 31 - 31: o0oOOo0O0Ooo . I1IiiI
   if 46 - 46: iII111i
 if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
  IIIII11I1IiI = 0
  while True :
   IIIII11I1IiI += 1
   xbmc . sleep ( 250 )
   if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'FALSE' or IIIII11I1IiI > 500 :
    break
    if 16 - 16: iIii1I11I1II1
 oOooOOOoOo = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
 if 41 - 41: Ii1I - O0 - O0
 if oOooOOOoOo != '' :
  if 68 - 68: OOooOOo % I1Ii111
  if oOooOOOoOo == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
   if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
   if 23 - 23: O0
   if 85 - 85: Ii1I
   if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
   if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
   if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
   if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
   if 77 - 77: iIii1I11I1II1 * OoO0O00
   if 95 - 95: I1IiiI + i11iIiiIii
   return
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if not oooO0 . GetCredential ( O0i1II1Iiii1I11 , IIII , iiIiI ) :
  iIiiI1 ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  sys . exit ( )
  if 46 - 46: I1Ii111
  if 60 - 60: o0oOOo0O0Ooo
 ii11i1 ( oooO0 . LoadCredential ( ) )
 OoOOOOO ( 'desc' )
 xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
 if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
def OoO0o ( args ) :
 oO0o0Ooooo = args . get ( 'stype' )
 if oO0o0Ooooo == 'live' :
  OOo0oO00ooO00 = I1Ii11I1Ii1ix
 else :
  OOo0oO00ooO00 = I11
  if 90 - 90: OoOoOO00 * I1Ii111 + o0oOOo0O0Ooo
 for OOOoOoO in OOo0oO00ooO00 :
  o0ooO = OOOoOoO . get ( 'title' )
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  if args . get ( 'ordernm' ) != '-' :
   o0ooO += '  (' + args . get ( 'ordernm' ) + ')'
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  I1111IIi = { 'mode' : OOOoOoO . get ( 'mode' )
 , 'stype' : OOOoOoO . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
  if 79 - 79: O0
  OO ( o0ooO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
 if len ( OOo0oO00ooO00 ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i )
 if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
 if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 if 57 - 57: OoO0O00 / ooOoO0o
 if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
def I111I1Iiii1i ( args ) :
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 oooO0 . SaveCredential ( oOO ( ) )
 if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
 oO0o0Ooooo = args . get ( 'stype' )
 Oo0O0oooo = int ( args . get ( 'page' ) )
 I111iI , oOOo0 = oooO0 . GetLiveChannelList ( oO0o0Ooooo , Oo0O0oooo )
 if 16 - 16: oO0o % I1ii11iIi11i * i11iIiiIii % i11iIiiIii
 for O0OOOOo0O in I111iI :
  o0ooO = O0OOOOo0O . get ( 'title' )
  OooOO = O0OOOOo0O . get ( 'channel' )
  I1111 = O0OOOOo0O . get ( 'thumbnail' )
  iiIiiiiI = O0OOOOo0O . get ( 'synopsis' )
  oooOo0OOOoo0 = O0OOOOo0O . get ( 'channelepg' )
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  OOOoOo = { }
  OOOoOo [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( OooOO , o0ooO , oooOo0OOOoo0 , iiIiiiiI )
  if 51 - 51: ooOoO0o / iIii1I11I1II1 % Oo0Ooo * I1IiiI % I1Ii111
  I1111IIi = { 'mode' : 'LIVE'
 , 'mediacode' : O0OOOOo0O . get ( 'mediacode' )
 , 'stype' : oO0o0Ooooo
  }
  if 76 - 76: o0oOOo0O0Ooo - i11iIiiIii
  OO ( OooOO , sublabel = o0ooO , img = I1111 , infoLabels = OOOoOo , isFolder = False , params = I1111IIi )
  if 14 - 14: OoOoOO00 + oO0o
 if oOOo0 :
  if 52 - 52: OoooooooOO - ooOoO0o
  I1111IIi [ 'mode' ] = 'CHANNEL'
  I1111IIi [ 'stype' ] = oO0o0Ooooo
  I1111IIi [ 'page' ] = str ( Oo0O0oooo + 1 )
  o0ooO = '[B]%s >>[/B]' % '다음 페이지'
  o0O0o0 = str ( Oo0O0oooo + 1 )
  OO ( o0ooO , sublabel = o0O0o0 , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if 37 - 37: I1ii11iIi11i * I11i % i11iIiiIii % ooOoO0o + Ii1I
 if len ( I111iI ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i , cacheToDisc = False )
 if 78 - 78: I1ii11iIi11i % oO0o / iII111i - iIii1I11I1II1
 if 69 - 69: I1Ii111
 if 11 - 11: I1IiiI
 if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
def Oo0OO ( args ) :
 if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
 oooO0 . SaveCredential ( oOO ( ) )
 if 29 - 29: I1IiiI % I1IiiI
 oO0o0Ooooo = args . get ( 'stype' )
 Oo0O0 = args . get ( 'orderby' )
 Oo0O0oooo = int ( args . get ( 'page' ) )
 if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
 oOo0OOoO0 , oOOo0 = oooO0 . GetProgramList ( oO0o0Ooooo , Oo0O0 , Oo0O0oooo , landyn = O0ooOooooO ( ) )
 if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
 for IiII111i1i11 in oOo0OOoO0 :
  o0ooO = IiII111i1i11 . get ( 'title' )
  I1111 = IiII111i1i11 . get ( 'thumbnail' )
  iiIiiiiI = IiII111i1i11 . get ( 'synopsis' )
  i111iIi1i1II1 = o0o0Oo0oooo0 . get ( IiII111i1i11 . get ( 'channel' ) )
  if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
  OOOoOo = { }
  OOOoOo [ 'plot' ] = '%s <%s>\n\n%s' % ( o0ooO , i111iIi1i1II1 , iiIiiiiI )
  if 19 - 19: I1ii11iIi11i % OoooooooOO % IiII * o0oOOo0O0Ooo % O0
  I1111IIi = { 'mode' : 'EPISODE'
 , 'programcode' : IiII111i1i11 . get ( 'program' )
 , 'page' : '1'
 }
  if 67 - 67: I1IiiI . i1IIi
  OO ( o0ooO , sublabel = i111iIi1i1II1 , img = I1111 , infoLabels = OOOoOo , isFolder = True , params = I1111IIi )
  if 27 - 27: ooOoO0o % I1IiiI
 if oOOo0 :
  if 73 - 73: OOooOOo
  I1111IIi [ 'mode' ] = 'PROGRAM'
  I1111IIi [ 'stype' ] = oO0o0Ooooo
  I1111IIi [ 'orderby' ] = Oo0O0
  I1111IIi [ 'page' ] = str ( Oo0O0oooo + 1 )
  o0ooO = '[B]%s >>[/B]' % '다음 페이지'
  o0O0o0 = str ( Oo0O0oooo + 1 )
  OO ( o0ooO , sublabel = o0O0o0 , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if 70 - 70: iIii1I11I1II1
 if len ( oOo0OOoO0 ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i , cacheToDisc = False )
 if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
 if 92 - 92: i1IIi - iIii1I11I1II1
 if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
 if 88 - 88: OoO0O00
def ooOOOooO ( args ) :
 if 12 - 12: O0 - o0oOOo0O0Ooo
 oooO0 . SaveCredential ( oOO ( ) )
 if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
 o0OoOo00o0o = args . get ( 'programcode' )
 Oo0O0oooo = int ( args . get ( 'page' ) )
 if 41 - 41: ooOoO0o % OoO0O00 - Oo0Ooo * I1Ii111 * Oo0Ooo
 OOOoOO0o , oOOo0 , i1II1 = oooO0 . GetEpisodoList ( o0OoOo00o0o , Oo0O0oooo , orderby = o00OO00OoO ( ) )
 if 25 - 25: I1Ii111 / iIii1I11I1II1 % iII111i
 for IiiiiI1i1Iii in OOOoOO0o :
  o0ooO = IiiiiI1i1Iii . get ( 'title' )
  I1111 = IiiiiI1i1Iii . get ( 'thumbnail' )
  iiIiiiiI = IiiiiI1i1Iii . get ( 'synopsis' )
  if 87 - 87: o0oOOo0O0Ooo
  OOOoOo = { }
  OOOoOo [ 'plot' ] = '%s\n\n%s' % ( o0ooO , iiIiiiiI )
  if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
  I1111IIi = { 'mode' : 'VOD'
 , 'mediacode' : IiiiiI1i1Iii . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : o0OoOo00o0o
 , 'title' : o0ooO
 , 'thumbnail' : I1111
 }
  if 31 - 31: I1Ii111
  OO ( o0ooO , sublabel = '' , img = I1111 , infoLabels = OOOoOo , isFolder = False , params = I1111IIi )
  if 88 - 88: OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % iIii1I11I1II1 + Oo0Ooo
  if 76 - 76: I1IiiI * iII111i % I1Ii111
  if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
  if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
  if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
  if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
 if Oo0O0oooo == 1 :
  OOOoOo = { 'plot' : '정렬순서를 변경합니다.' }
  I1111IIi = { }
  I1111IIi [ 'mode' ] = 'ORDER_BY'
  if o00OO00OoO ( ) == 'desc' :
   o0ooO = '정렬순서변경 : 최신화부터 -> 1회부터'
   I1111IIi [ 'orderby' ] = 'asc'
  else :
   o0ooO = '정렬순서변경 : 1회부터 -> 최신화부터'
   I1111IIi [ 'orderby' ] = 'desc'
  OO ( o0ooO , sublabel = '' , img = '' , infoLabels = OOOoOo , isFolder = False , params = I1111IIi )
  if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  if 42 - 42: I1IiiI
 if oOOo0 :
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  I1111IIi [ 'mode' ] = 'EPISODE'
  I1111IIi [ 'programcode' ] = o0OoOo00o0o
  I1111IIi [ 'page' ] = str ( Oo0O0oooo + 1 )
  o0ooO = '[B]%s >>[/B]' % '다음 페이지'
  o0O0o0 = str ( Oo0O0oooo + 1 )
  OO ( o0ooO , sublabel = o0O0o0 , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
 if len ( OOOoOO0o ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i , cacheToDisc = False )
 if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
 if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
 if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
def O00oOOooo ( args ) :
 Oo0O0 = args . get ( 'orderby' )
 if 50 - 50: I1ii11iIi11i % O0 * o0oOOo0O0Ooo
 OoOOOOO ( Oo0O0 )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 5 - 5: IiII * OoOoOO00
 if 5 - 5: I1Ii111
 if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
 if 40 - 40: OoooooooOO
def I1i1i1 ( args ) :
 if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
 oooO0 . SaveCredential ( oOO ( ) )
 if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
 Oo0O0 = args . get ( 'orderby' )
 Oo0O0oooo = int ( args . get ( 'page' ) )
 if 9 - 9: I11i % OoooooooOO . oO0o % I11i
 ii , oOOo0 = oooO0 . GetMovieList ( Oo0O0 , Oo0O0oooo , premiumyn = IiiI11Iiiii ( ) , landyn = O0ooOooooO ( ) )
 if 36 - 36: OoooooooOO . OoO0O00
 for oO in ii :
  o0ooO = oO . get ( 'title' )
  I1111 = oO . get ( 'thumbnail' )
  iiIiiiiI = oO . get ( 'synopsis' )
  if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
  OOOoOo = { }
  OOOoOo [ 'plot' ] = '%s\n\n%s' % ( o0ooO , iiIiiiiI )
  if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
  I1111IIi = { 'mode' : 'MOVIE'
 , 'mediacode' : oO . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : o0ooO
 , 'thumbnail' : I1111
 }
  if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
  OO ( o0ooO , sublabel = '' , img = I1111 , infoLabels = OOOoOo , isFolder = False , params = I1111IIi )
  if 20 - 20: I1IiiI
 if oOOo0 :
  if 95 - 95: iII111i - I1IiiI
  I1111IIi [ 'mode' ] = 'MOVIE_GROUP'
  I1111IIi [ 'orderby' ] = Oo0O0
  I1111IIi [ 'page' ] = str ( Oo0O0oooo + 1 )
  o0ooO = '[B]%s >>[/B]' % '다음 페이지'
  o0O0o0 = str ( Oo0O0oooo + 1 )
  OO ( o0ooO , sublabel = o0O0o0 , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
 if len ( ii ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i , cacheToDisc = False )
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
 if 41 - 41: i1IIi - I11i - Ii1I
 if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
def IIIi11I11 ( args ) :
 for OOOoOoO in Oooo0000 :
  o0ooO = OOOoOoO . get ( 'title' )
  if 44 - 44: II111iiii
  I1111IIi = { 'mode' : OOOoOoO . get ( 'mode' )
 , 'stype' : OOOoOoO . get ( 'stype' )
 , 'page' : '1'
 }
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  OO ( o0ooO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
 if len ( Oooo0000 ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i )
 if 35 - 35: iIii1I11I1II1
 if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
 if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
 if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
def Iii1iiIi1II ( args ) :
 if 60 - 60: I1IiiI - oO0o * I11i % II111iiii
 oooO0 . SaveCredential ( oOO ( ) )
 if 62 - 62: iIii1I11I1II1
 i1II = __addon__ . getSetting ( 'id' )
 Oo0O0oooo = int ( args . get ( 'page' ) )
 oO0o0Ooooo = args . get ( 'stype' )
 if 14 - 14: oO0o / oO0o % ooOoO0o
 if 'search_key' in args :
  ooO = args . get ( 'search_key' )
 else :
  ooO = iiI1IiI ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not ooO : return
  if 6 - 6: iIii1I11I1II1 . ooOoO0o % o0oOOo0O0Ooo
 I1Iii1 , oOOo0 = oooO0 . GetSearchList ( ooO , i1II , Oo0O0oooo , oO0o0Ooooo , premiumyn = IiiI11Iiiii ( ) , landyn = O0ooOooooO ( ) )
 if len ( I1Iii1 ) == 0 : return
 if 30 - 30: OoooooooOO - OoOoOO00
 for Ooo00O0o in I1Iii1 :
  o0ooO = Ooo00O0o . get ( 'title' )
  I1111 = Ooo00O0o . get ( 'thumbnail' )
  iiIiiiiI = Ooo00O0o . get ( 'synopsis' )
  Oo00o0OO0O00o = Ooo00O0o . get ( 'program' )
  if 82 - 82: I11i + OoooooooOO - i1IIi . i1IIi
  OOOoOo = { }
  OOOoOo [ 'plot' ] = '%s\n\n%s' % ( o0ooO , iiIiiiiI )
  if 6 - 6: o0oOOo0O0Ooo / I11i / II111iiii
  if oO0o0Ooooo == 'vod' :
   I1111IIi = { 'mode' : 'EPISODE'
 , 'programcode' : Ooo00O0o . get ( 'program' )
 , 'page' : '1'
 }
   I1 = True
  else :
   I1111IIi = { 'mode' : 'MOVIE'
 , 'mediacode' : Ooo00O0o . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : o0ooO
 , 'thumbnail' : I1111
 }
   I1 = False
   if 27 - 27: OOooOOo * ooOoO0o . I1Ii111 % IiII * IiII . i1IIi
  OO ( o0ooO , sublabel = '' , img = I1111 , infoLabels = OOOoOo , isFolder = I1 , params = I1111IIi )
  if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + IiII
 if oOOo0 :
  if 10 - 10: I1Ii111 / ooOoO0o + i11iIiiIii / Ii1I
  I1111IIi [ 'mode' ] = 'SEARCH'
  I1111IIi [ 'search_key' ] = ooO
  I1111IIi [ 'page' ] = str ( Oo0O0oooo + 1 )
  o0ooO = '[B]%s >>[/B]' % '다음 페이지'
  o0O0o0 = str ( Oo0O0oooo + 1 )
  OO ( o0ooO , sublabel = o0O0o0 , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
 if len ( I1Iii1 ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i )
 if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
 if 5 - 5: Ii1I
 if 46 - 46: IiII
 if 45 - 45: ooOoO0o
def IIi ( stype ) :
 try :
  ooO0oOo0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( ooO0oOo0o , 'w' ) as OOii111IiiI1 :
   OOii111IiiI1 . write ( '' )
 except :
  None
  if 11 - 11: iIii1I11I1II1 * Ii1I
  if 76 - 76: ooOoO0o
  if 15 - 15: OOooOOo . I11i + OoooooooOO - OoO0O00
  if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
def O00OoOO0oo0 ( args ) :
 oO0o0Ooooo = args . get ( 'stype' )
 if 96 - 96: OoOoOO00 . o0oOOo0O0Ooo - ooOoO0o
 OoOooOOOO = xbmcgui . Dialog ( )
 III1IiiI = OoOooOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if III1IiiI == False : sys . exit ( )
 if 99 - 99: IiII . Oo0Ooo - Ii1I % Ii1I * O0 . II111iiii
 IIi ( oO0o0Ooooo )
 if 4 - 4: Ii1I
 xbmc . executebuiltin ( "Container.Refresh" )
 if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
 if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
 if 7 - 7: iII111i % O0 . OoOoOO00 + I1IiiI - I11i
 if 75 - 75: I11i
def oO00oo0o00o0o ( stype ) :
 try :
  ooO0oOo0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( ooO0oOo0o , 'r' ) as OOii111IiiI1 :
   IiIIIIIi = OOii111IiiI1 . readlines ( )
 except :
  IiIIIIIi = [ ]
  if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
 return IiIIIIIi
 if 39 - 39: I1Ii111
 if 86 - 86: I11i * I1IiiI + I11i + II111iiii
 if 8 - 8: I1Ii111 - iII111i / ooOoO0o
 if 96 - 96: OoOoOO00
def IIiiI ( stype , in_params ) :
 try :
  ooO0oOo0o = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  III1i11 = oO00oo0o00o0o ( stype )
  if 25 - 25: OoO0O00
  with open ( ooO0oOo0o , 'w' ) as OOii111IiiI1 :
   i11iI11iIiIi = urllib . urlencode ( in_params )
   i11iI11iIiIi = i11iI11iIiIi . encode ( 'utf-8' ) + '\n'
   OOii111IiiI1 . write ( i11iI11iIiIi )
   if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
   IIIii1 = 0
   for Oooo0 in III1i11 :
    oOOOooo = dict ( urlparse . parse_qsl ( Oooo0 ) )
    if in_params . get ( 'code' ) != oOOOooo . get ( 'code' ) :
     OOii111IiiI1 . write ( Oooo0 )
     IIIii1 += 1
     if IIIii1 >= 50 : break
 except :
  None
  if 16 - 16: OOooOOo % iII111i . O0 / Oo0Ooo / o0oOOo0O0Ooo
  if 68 - 68: i11iIiiIii * OoO0O00
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
def i1iiIiI1Ii1i ( args ) :
 oO0o0Ooooo = args . get ( 'stype' )
 if 22 - 22: IiII / i11iIiiIii
 if oO0o0Ooooo == '-' :
  for OOOoOoO in OOo :
   o0ooO = OOOoOoO . get ( 'title' )
   if 62 - 62: OoO0O00 / I1ii11iIi11i
   I1111IIi = { 'mode' : OOOoOoO . get ( 'mode' )
 , 'stype' : OOOoOoO . get ( 'stype' )
 }
   if 7 - 7: OoooooooOO . IiII
   OO ( o0ooO , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1111IIi )
  if len ( OOo ) > 0 : xbmcplugin . endOfDirectory ( i1iIi1iIi1i )
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
 else :
  Oooo00 = oO00oo0o00o0o ( oO0o0Ooooo )
  if 6 - 6: Ii1I - ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
  for II11iI111i1 in Oooo00 :
   Oo00OoOo = dict ( urlparse . parse_qsl ( II11iI111i1 ) )
   if 24 - 24: i11iIiiIii - I1Ii111
   o0ooO = Oo00OoOo . get ( 'title' )
   I1111 = Oo00OoOo . get ( 'img' )
   if 21 - 21: I11i
   OOOoOo = { }
   OOOoOo [ 'plot' ] = o0ooO
   if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
   if oO0o0Ooooo == 'vod' :
    I1111IIi = { 'mode' : 'EPISODE'
 , 'programcode' : Oo00OoOo . get ( 'code' )
 , 'page' : '1'
 }
    I1 = True
   else :
    I1111IIi = { 'mode' : 'MOVIE'
 , 'mediacode' : Oo00OoOo . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : o0ooO
 , 'thumbnail' : I1111
 }
    I1 = False
    if 11 - 11: OoooooooOO . I1Ii111
   OO ( o0ooO , sublabel = '' , img = I1111 , infoLabels = OOOoOo , isFolder = I1 , params = I1111IIi )
   if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  OOOoOo = { 'plot' : '시청목록을 삭제합니다.' }
  o0ooO = '*** 시청목록 삭제 ***'
  I1111IIi = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : oO0o0Ooooo
 }
  if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
  OO ( o0ooO , sublabel = '' , img = '' , infoLabels = OOOoOo , isFolder = False , params = I1111IIi )
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * IiII
  xbmcplugin . endOfDirectory ( i1iIi1iIi1i , cacheToDisc = False )
  if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
  if 69 - 69: O0
  if 85 - 85: ooOoO0o / O0
  if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
def o0 ( args ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
 oooO0 . SaveCredential ( oOO ( ) )
 if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
 oOOoOo = args . get ( 'mediacode' )
 oO0o0Ooooo = args . get ( 'stype' )
 ooOooo0 = Oo0ooOo0o ( oO0o0Ooooo )
 if 67 - 67: I1IiiI
 OO00OO0O0 , i1I111Ii1i11 = oooO0 . GetBroadURL ( oOOoOo , ooOooo0 , oO0o0Ooooo )
 if 81 - 81: OoO0O00
 I1Ii ( 'qt, stype, url : %s - %s - %s' % ( str ( ooOooo0 ) , oO0o0Ooooo , OO00OO0O0 ) )
 if 99 - 99: oO0o * II111iiii * I1Ii111
 if OO00OO0O0 == '' :
  iIiiI1 ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 92 - 92: Oo0Ooo
  if 40 - 40: OoOoOO00 / IiII
  if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
 OoO = OO00OO0O0 . find ( 'Policy=' )
 if OoO != - 1 :
  iIIiii = OO00OO0O0 . split ( '?' ) [ 0 ]
  if 61 - 61: IiII . i1IIi / I1Ii111 % i11iIiiIii * iII111i
  i1i1i1I = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( OO00OO0O0 ) . query ) )
  i1i1i1I = urllib . urlencode ( i1i1i1I )
  i1i1i1I = i1i1i1I . replace ( '&' , ';' )
  i1i1i1I = i1i1i1I . replace ( 'Policy' , 'CloudFront-Policy' )
  i1i1i1I = i1i1i1I . replace ( 'Signature' , 'CloudFront-Signature' )
  i1i1i1I = i1i1i1I . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
  if 83 - 83: oO0o + OoooooooOO
  I111IiiIi1 = '%s|Cookie=%s' % ( iIIiii , i1i1i1I )
 else :
  I111IiiIi1 = OO00OO0O0
  if 88 - 88: OoooooooOO
  if 84 - 84: OoOoOO00 / I11i * iII111i / oO0o - i11iIiiIii . Oo0Ooo
 I1Ii ( I111IiiIi1 , False )
 if 60 - 60: I1ii11iIi11i * I1IiiI
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
 if 77 - 77: I1Ii111
 Oo = xbmcgui . ListItem ( path = I111IiiIi1 )
 if 81 - 81: oO0o * OoO0O00
 if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
 if i1I111Ii1i11 != '' :
  I1IIIiii1 = i1I111Ii1i11
  O00oo = 'https://cj.drmkeyserver.com/widevine_license'
  if 77 - 77: iII111i % OOooOOo - I11i % ooOoO0o - OoO0O00 / Oo0Ooo
  Ii1iI111 = 'mpd'
  O0oooo00o0Oo = 'com.widevine.alpha'
  if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
  oO0Ooo0ooOO0 = inputstreamhelper . Helper ( Ii1iI111 , drm = O0oooo00o0Oo )
  if 46 - 46: Ii1I % OoOoOO00
  if oO0Ooo0ooOO0 . check_inputstream ( ) :
   if 64 - 64: i11iIiiIii - II111iiii
   oO0oOOO0Ooo = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % oOOoOo
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
   , 'user-agent' : O0o
 , 'AcquireLicenseAssertion' : I1IIIiii1
 , 'Host' : 'cj.drmkeyserver.com'
 }
   i1i1I = O00oo + '|' + urllib . urlencode ( oO0oOOO0Ooo ) + '|R{SSM}|'
   if 25 - 25: iIii1I11I1II1 + I1ii11iIi11i + iII111i / II111iiii / I11i
   Oo . setProperty ( 'inputstreamaddon' , oO0Ooo0ooOO0 . inputstream_addon )
   if 60 - 60: ooOoO0o * I1Ii111 + Oo0Ooo
   Oo . setProperty ( 'inputstream.adaptive.manifest_type' , Ii1iI111 )
   Oo . setProperty ( 'inputstream.adaptive.license_type' , O0oooo00o0Oo )
   if 19 - 19: OoO0O00 * I11i / I11i . OoooooooOO - OOooOOo + i11iIiiIii
   Oo . setProperty ( 'inputstream.adaptive.license_key' , i1i1I )
   if 88 - 88: i11iIiiIii - ooOoO0o
   if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
   if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
   if 30 - 30: OoOoOO00
 xbmcplugin . setResolvedUrl ( i1iIi1iIi1i , True , Oo )
 if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
  I1111IIi = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
  IIiiI ( args . get ( 'stype' ) , I1111IIi )
  if 26 - 26: II111iiii * OoOoOO00
  if 10 - 10: II111iiii . iII111i
  if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
  if 88 - 88: iII111i
  if 19 - 19: II111iiii * IiII + Ii1I
  if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
oooO0 = oo0Ooo0 ( )
i1iIi1iIi1i = int ( sys . argv [ 1 ] )
if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
I1111IIi = O0OoO0O00o0oO ( )
IIii11II11II1 = I1111IIi . get ( 'mode' , None )
if 10 - 10: I1IiiI / Oo0Ooo % I1ii11iIi11i * ooOoO0o
II1I ( )
if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
if IIii11II11II1 is None :
 if 98 - 98: i1IIi
 iIIi1i1 ( )
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
elif IIii11II11II1 in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
 OoO0o ( I1111IIi )
 if 66 - 66: OoO0O00
elif IIii11II11II1 == 'CHANNEL' :
 I111I1Iiii1i ( I1111IIi )
 if 56 - 56: O0
elif IIii11II11II1 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 o0 ( I1111IIi )
 xbmc . sleep ( 200 )
 if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
elif IIii11II11II1 == 'PROGRAM' :
 Oo0OO ( I1111IIi )
 if 23 - 23: oO0o - OOooOOo + I11i
elif IIii11II11II1 == 'EPISODE' :
 ooOOOooO ( I1111IIi )
 if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
elif IIii11II11II1 == 'MOVIE_GROUP' :
 I1i1i1 ( I1111IIi )
 if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
elif IIii11II11II1 == 'SEARCH_GROUP' :
 IIIi11I11 ( I1111IIi )
 if 11 - 11: iII111i * Ii1I - OoOoOO00
elif IIii11II11II1 == 'SEARCH' :
 Iii1iiIi1II ( I1111IIi )
 if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
elif IIii11II11II1 == 'WATCH' :
 i1iiIiI1Ii1i ( I1111IIi )
 if 74 - 74: Oo0Ooo
elif IIii11II11II1 == 'MYVIEW_REMOVE' :
 O00OoOO0oo0 ( I1111IIi )
 if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
elif IIii11II11II1 == 'ORDER_BY' :
 O00oOOooo ( I1111IIi )
 if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
else :
 None
 if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
 if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
 if 68 - 68: OoooooooOO % II111iiii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
