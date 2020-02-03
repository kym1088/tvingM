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
  OoOooOOOO . notification ( __name__ , sting )
 except :
  None
  if 45 - 45: I1Ii111 + Ii1I
  if 17 - 17: o0oOOo0O0Ooo
  if 64 - 64: Ii1I % i1IIi % OoooooooOO
def i1iIIi1 ( string , isDebug = False ) :
 try :
  ii11iIi1I = string . encode ( 'utf-8' , 'ignore' )
 except :
  ii11iIi1I = 'addonException: addon_log'
 if isDebug : iI111I11I1I1 = xbmc . LOGDEBUG
 else : iI111I11I1I1 = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , ii11iIi1I ) , level = iI111I11I1I1 )
 if 55 - 55: OoOoOO00 % i1IIi / Ii1I - oO0o - O0 / II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
 if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
 if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
def oOoO ( title ) :
 oOo = None
 oOoOoO = xbmc . Keyboard ( )
 oOoOoO . setHeading ( title )
 xbmc . sleep ( 1000 )
 oOoOoO . doModal ( )
 if ( oOoOoO . isConfirmed ( ) ) :
  oOo = oOoOoO . getText ( )
 return oOo
 if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 if 84 - 84: i11iIiiIii . o0oOOo0O0Ooo
 if 100 - 100: Ii1I - Ii1I - I1Ii111
 if 20 - 20: OoooooooOO
def Ii11iI1i ( ) :
 Ooo = __addon__ . getSetting ( 'id' )
 O0o0Oo = __addon__ . getSetting ( 'pw' )
 Oo00OOOOO = __addon__ . getSetting ( 'login_type' )
 return ( Ooo , O0o0Oo , Oo00OOOOO )
 if 85 - 85: ooOoO0o . iII111i - OoO0O00 % ooOoO0o % II111iiii
 if 81 - 81: OoO0O00 + II111iiii % iII111i * O0
 if 89 - 89: oO0o + Oo0Ooo
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
def III1ii1iII ( ) :
 oo0oooooO0 = __addon__ . getSetting ( 'premium_movieyn' )
 if oo0oooooO0 == 'false' :
  return False
 else :
  return True
  if 19 - 19: I11i + ooOoO0o
  if 53 - 53: OoooooooOO . i1IIi
  if 18 - 18: o0oOOo0O0Ooo
  if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
def oOoOooOo0o0 ( credential ) :
 OOOO = xbmcgui . Window ( 10000 )
 OOOO . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
 OOOO . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
 OOOO . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
 if 87 - 87: oO0o / I11i - i1IIi * OOooOOo / OoooooooOO . O0
 OOOO . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
 if 1 - 1: II111iiii - I11i / I11i
 if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
def oo0 ( ) :
 OOOO = xbmcgui . Window ( 10000 )
 o00 = {
 'tving_token' : OOOO . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : OOOO . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : OOOO . getProperty ( 'TVING_M_UUID' )
 }
 return o00
 if 95 - 95: O0 + OoO0O00 . II111iiii / O0
def O000oo0O ( orderby ) :
 OOOO = xbmcgui . Window ( 10000 )
 OOOO . setProperty ( 'TVING_M_ORDERBY' , orderby )
 if 66 - 66: I1ii11iIi11i / OoOoOO00 - I1IiiI . OOooOOo / I1IiiI * OOooOOo
def IIIii1II1II ( ) :
 OOOO = xbmcgui . Window ( 10000 )
 return OOOO . getProperty ( 'TVING_M_ORDERBY' )
 if 42 - 42: Ii1I + oO0o
 if 76 - 76: I1Ii111 - OoO0O00
 if 70 - 70: ooOoO0o
def oOO ( ) :
 IIi1I1Ii11iI = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for I11i1I1I in IIi1I1Ii11iI . keys ( ) :
  IIi1I1Ii11iI [ I11i1I1I ] = IIi1I1Ii11iI [ I11i1I1I ] [ 0 ]
 return IIi1I1Ii11iI
 if 83 - 83: I1ii11iIi11i / ooOoO0o
 if 49 - 49: o0oOOo0O0Ooo
 if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
def o00OO00OoO ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 OOOO0OOoO0O0 = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 65 - 65: IiII * I1IiiI + Ii1I % i11iIiiIii * oO0o . I1Ii111
 if sublabel : OoO0O00IIiII = '%s < %s >' % ( label , sublabel )
 else : OoO0O00IIiII = label
 if not img : img = 'DefaultFolder.png'
 if 80 - 80: IiII . oO0o
 IIi = xbmcgui . ListItem ( OoO0O00IIiII , thumbnailImage = img )
 if infoLabels : IIi . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : IIi . setProperty ( 'IsPlayable' , 'true' )
 if 26 - 26: iII111i
 xbmcplugin . addDirectoryItem ( OOO , OOOO0OOoO0O0 , IIi , isFolder )
 if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 if 75 - 75: oO0o
def I1III ( etype ) :
 try :
  if etype == 'movie' :
   OO0O0OoOO0 = 'movie_quality'
  else :
   OO0O0OoOO0 = 'selected_quality'
   if 10 - 10: OoooooooOO % iIii1I11I1II1
  O00o0O00 = [ 1080 , 720 , 480 , 360 ]
  if 34 - 34: ooOoO0o
  I1111I1iII11 = int ( __addon__ . getSetting ( OO0O0OoOO0 ) )
  return O00o0O00 [ I1111I1iII11 ]
 except :
  None
  if 59 - 59: iIii1I11I1II1 * i11iIiiIii / I1ii11iIi11i * i1IIi * O0
 return 720
 if 83 - 83: OoO0O00 / I1Ii111 . OoOoOO00 / IiII . OoOoOO00 . OOooOOo
 if 75 - 75: I11i + OoO0O00 . OoOoOO00 . ooOoO0o + Oo0Ooo . OoO0O00
 if 96 - 96: OOooOOo . ooOoO0o - Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * OOooOOo
def O0ii1ii1ii ( ) :
 if 91 - 91: IiII
 for iiIii in o0oO0 :
  OoO0O00IIiII = iiIii . get ( 'title' )
  if 79 - 79: OoooooooOO / O0
  OO0OoO0o00 = { 'mode' : iiIii . get ( 'mode' )
 , 'stype' : iiIii . get ( 'stype' )
 , 'orderby' : iiIii . get ( 'orderby' )
 , 'page' : '1'
 }
  if 53 - 53: O0 * OoO0O00 + OOooOOo
  if iiIii . get ( 'mode' ) == 'XXX' :
   OO0OoO0o00 [ 'mode' ] = 'XXX'
   Ii = False
  else :
   Ii = True
   if 61 - 61: II111iiii
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = Ii , params = OO0OoO0o00 )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( OOO )
 if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 if 42 - 42: OoO0O00
 if 67 - 67: I1Ii111 . iII111i . O0
def IIIIiiII111 ( ) :
 ( OOoOoo , oO0000OOo00 , iiIi1IIiIi ) = Ii11iI1i ( )
 if 75 - 75: I1IiiI + Oo0Ooo
 if 73 - 73: O0 - OoooooooOO . OOooOOo - OOooOOo / OoOoOO00
 if not ( OOoOoo and oO0000OOo00 ) :
  OoOooOOOO = xbmcgui . Dialog ( )
  iiIi1I1iIIi = OoOooOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if iiIi1I1iIIi == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 31 - 31: II111iiii . I1IiiI
 II1I = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
 if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
 if II1I != '' :
  if 42 - 42: i11iIiiIii
  if II1I == datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) :
   if 33 - 33: iII111i - O0 * i1IIi * o0oOOo0O0Ooo - Oo0Ooo
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
   if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
   if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
   if 51 - 51: O0 + iII111i
   if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
   if 48 - 48: O0
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   if 41 - 41: Ii1I - O0 - O0
   if 68 - 68: OOooOOo % I1Ii111
   return
   if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
   if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
 if not i1 . GetCredential ( OOoOoo , oO0000OOo00 , iiIi1IIiIi ) :
  iIiiI1 ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
  if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
 oOoOooOo0o0 ( i1 . LoadCredential ( ) )
 O000oo0O ( 'desc' )
 if 54 - 54: OoOoOO00 % iII111i
 if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
 if 88 - 88: iII111i . II111iiii * II111iiii % I1Ii111
 if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
def I1Ii ( args ) :
 O0oo00o0O = args . get ( 'stype' )
 if O0oo00o0O == 'live' :
  i1I1I = xI1Ii11I1Ii1i
 else :
  i1I1I = I11
  if 12 - 12: i11iIiiIii / OoO0O00
 for o0O in i1I1I :
  OoO0O00IIiII = o0O . get ( 'title' )
  if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
  OO0OoO0o00 = { 'mode' : o0O . get ( 'mode' )
 , 'stype' : o0O . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
  if 9 - 9: o0oOOo0O0Ooo . ooOoO0o - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
 if len ( i1I1I ) > 0 : xbmcplugin . endOfDirectory ( OOO )
 if 79 - 79: oO0o % I11i % I1IiiI
 if 5 - 5: OoooooooOO % OoOoOO00 % oO0o % iII111i
 if 7 - 7: II111iiii + OoooooooOO . I1Ii111 . ooOoO0o - o0oOOo0O0Ooo
 if 26 - 26: Oo0Ooo / IiII % iIii1I11I1II1 / IiII + I11i
def oOO0O00oO0Ooo ( args ) :
 if 67 - 67: OoO0O00 - OOooOOo
 i1 . SaveCredential ( oo0 ( ) )
 if 36 - 36: IiII
 O0oo00o0O = args . get ( 'stype' )
 I11iI = int ( args . get ( 'page' ) )
 I1iI1ii1II , O0O0OOOOoo = i1 . GetLiveChannelList ( O0oo00o0O , I11iI )
 if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
 for oOo0O0Oo00oO in I1iI1ii1II :
  OoO0O00IIiII = oOo0O0Oo00oO . get ( 'title' )
  I111I1Iiii1i = oOo0O0Oo00oO . get ( 'channel' )
  oOOoo00O00o = oOo0O0Oo00oO . get ( 'thumbnail' )
  O0O00Oo = oOo0O0Oo00oO . get ( 'synopsis' )
  oooooo0O000o = oOo0O0Oo00oO . get ( 'channelepg' )
  if 64 - 64: I1IiiI . o0oOOo0O0Ooo - I1Ii111 / OoooooooOO
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( I111I1Iiii1i , OoO0O00IIiII , oooooo0O000o , O0O00Oo )
  if 77 - 77: OoOoOO00 - II111iiii - ooOoO0o
  OO0OoO0o00 = { 'mode' : 'LIVE'
 , 'mediacode' : oOo0O0Oo00oO . get ( 'mediacode' )
 , 'stype' : O0oo00o0O
  }
  if 49 - 49: II111iiii % O0 . OoOoOO00 + oO0o / I1IiiI
  o00OO00OoO ( I111I1Iiii1i , sublabel = OoO0O00IIiII , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = False , params = OO0OoO0o00 )
  if 72 - 72: ooOoO0o * Oo0Ooo . I1IiiI - II111iiii + i1IIi
 if O0O0OOOOoo :
  if 10 - 10: oO0o + i1IIi
  OO0OoO0o00 [ 'mode' ] = 'CHANNEL'
  OO0OoO0o00 [ 'stype' ] = O0oo00o0O
  OO0OoO0o00 [ 'page' ] = str ( I11iI + 1 )
  OoO0O00IIiII = '[B]%s >>[/B]' % '다음 페이지'
  oOo0O = str ( I11iI + 1 )
  o00OO00OoO ( OoO0O00IIiII , sublabel = oOo0O , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if 52 - 52: i11iIiiIii / o0oOOo0O0Ooo * ooOoO0o
 if len ( I1iI1ii1II ) > 0 : xbmcplugin . endOfDirectory ( OOO , cacheToDisc = False )
 if 22 - 22: OoOoOO00 . OOooOOo * OoOoOO00
 if 54 - 54: IiII + Ii1I % OoO0O00 + OoooooooOO - O0 - o0oOOo0O0Ooo
 if 77 - 77: OOooOOo * iIii1I11I1II1
 if 98 - 98: I1IiiI % Ii1I * OoooooooOO
def Oo ( args ) :
 if 34 - 34: oO0o + I1IiiI - oO0o
 i1 . SaveCredential ( oo0 ( ) )
 if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
 O0oo00o0O = args . get ( 'stype' )
 O0oO000O0O = args . get ( 'orderby' )
 I11iI = int ( args . get ( 'page' ) )
 if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
 i1I , O0O0OOOOoo = i1 . GetProgramList ( O0oo00o0O , O0oO000O0O , I11iI )
 if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
 for i1I1IiiIi1i in i1I :
  OoO0O00IIiII = i1I1IiiIi1i . get ( 'title' )
  oOOoo00O00o = i1I1IiiIi1i . get ( 'thumbnail' )
  O0O00Oo = i1I1IiiIi1i . get ( 'synopsis' )
  iiI11ii1I1 = o0o0Oo0oooo0 . get ( i1I1IiiIi1i . get ( 'channel' ) )
  if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = '%s <%s>\n\n%s' % ( OoO0O00IIiII , iiI11ii1I1 , O0O00Oo )
  if 70 - 70: oO0o
  OO0OoO0o00 = { 'mode' : 'EPISODE'
 , 'programcode' : i1I1IiiIi1i . get ( 'program' )
 , 'page' : '1'
 }
  if 59 - 59: o0oOOo0O0Ooo % oO0o
  o00OO00OoO ( OoO0O00IIiII , sublabel = iiI11ii1I1 , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = True , params = OO0OoO0o00 )
  if 6 - 6: iIii1I11I1II1 % i11iIiiIii % I1ii11iIi11i
 if O0O0OOOOoo :
  if 93 - 93: IiII * OoooooooOO + ooOoO0o
  OO0OoO0o00 [ 'mode' ] = 'PROGRAM'
  OO0OoO0o00 [ 'stype' ] = O0oo00o0O
  OO0OoO0o00 [ 'orderby' ] = O0oO000O0O
  OO0OoO0o00 [ 'page' ] = str ( I11iI + 1 )
  OoO0O00IIiII = '[B]%s >>[/B]' % '다음 페이지'
  oOo0O = str ( I11iI + 1 )
  o00OO00OoO ( OoO0O00IIiII , sublabel = oOo0O , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
 if len ( i1I ) > 0 : xbmcplugin . endOfDirectory ( OOO , cacheToDisc = False )
 if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
 if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
 if 26 - 26: Ii1I % I1ii11iIi11i
 if 76 - 76: IiII * iII111i
def ooooooo00o ( args ) :
 if 73 - 73: OOooOOo
 i1 . SaveCredential ( oo0 ( ) )
 if 70 - 70: iIii1I11I1II1
 i11ii1iI = args . get ( 'programcode' )
 I11iI = int ( args . get ( 'page' ) )
 if 22 - 22: OoooooooOO
 OOOOOo , O0O0OOOOoo , IiI1iIiIIIii = i1 . GetEpisodoList ( i11ii1iI , I11iI , orderby = IIIii1II1II ( ) )
 if 53 - 53: i1IIi
 for o0OOOoO0 in OOOOOo :
  OoO0O00IIiII = o0OOOoO0 . get ( 'title' )
  oOOoo00O00o = o0OOOoO0 . get ( 'thumbnail' )
  O0O00Oo = o0OOOoO0 . get ( 'synopsis' )
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = '%s\n\n%s' % ( OoO0O00IIiII , O0O00Oo )
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  OO0OoO0o00 = { 'mode' : 'VOD'
 , 'mediacode' : o0OOOoO0 . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : i11ii1iI
 , 'title' : OoO0O00IIiII
 , 'thumbnail' : oOOoo00O00o
 }
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = False , params = OO0OoO0o00 )
  if 23 - 23: i11iIiiIii
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
  if 31 - 31: OOooOOo
 if I11iI == 1 :
  O0O0ooOOO = { 'plot' : '정렬순서를 변경합니다.' }
  OO0OoO0o00 = { }
  OO0OoO0o00 [ 'mode' ] = 'ORDER_BY'
  if IIIii1II1II ( ) == 'desc' :
   OoO0O00IIiII = '정렬순서변경 : 최신화부터 -> 1회부터'
   OO0OoO0o00 [ 'orderby' ] = 'asc'
  else :
   OoO0O00IIiII = '정렬순서변경 : 1회부터 -> 최신화부터'
   OO0OoO0o00 [ 'orderby' ] = 'desc'
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = O0O0ooOOO , isFolder = False , params = OO0OoO0o00 )
  if 23 - 23: I1Ii111 . IiII
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
 if O0O0OOOOoo :
  if 42 - 42: Oo0Ooo
  OO0OoO0o00 [ 'mode' ] = 'EPISODE'
  OO0OoO0o00 [ 'programcode' ] = i11ii1iI
  OO0OoO0o00 [ 'page' ] = str ( I11iI + 1 )
  OoO0O00IIiII = '[B]%s >>[/B]' % '다음 페이지'
  oOo0O = str ( I11iI + 1 )
  o00OO00OoO ( OoO0O00IIiII , sublabel = oOo0O , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if 76 - 76: I1IiiI * iII111i % I1Ii111
 if len ( OOOOOo ) > 0 : xbmcplugin . endOfDirectory ( OOO , cacheToDisc = False )
 if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
 if 68 - 68: OoooooooOO * I11i % OoOoOO00 - IiII
 if 34 - 34: I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / I1Ii111 / I1ii11iIi11i
 if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
def I11IIIi ( args ) :
 O0oO000O0O = args . get ( 'orderby' )
 if 15 - 15: I1ii11iIi11i * OoO0O00
 O000oo0O ( O0oO000O0O )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 16 - 16: iII111i + OoOoOO00
 if 66 - 66: iII111i / oO0o * OoooooooOO + OoooooooOO % I11i
 if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
 if 71 - 71: o0oOOo0O0Ooo
def IIIIiIiIi1 ( args ) :
 if 2 - 2: iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
 i1 . SaveCredential ( oo0 ( ) )
 if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
 O0oO000O0O = args . get ( 'orderby' )
 I11iI = int ( args . get ( 'page' ) )
 if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
 OoOoo00Ooo00 , O0O0OOOOoo = i1 . GetMovieList ( O0oO000O0O , I11iI , premiumyn = III1ii1iII ( ) )
 if 57 - 57: I1Ii111
 for I11Iiii1I in OoOoo00Ooo00 :
  OoO0O00IIiII = I11Iiii1I . get ( 'title' )
  oOOoo00O00o = I11Iiii1I . get ( 'thumbnail' )
  O0O00Oo = I11Iiii1I . get ( 'synopsis' )
  if 90 - 90: iIii1I11I1II1 % ooOoO0o
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = '%s\n\n%s' % ( OoO0O00IIiII , O0O00Oo )
  if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
  OO0OoO0o00 = { 'mode' : 'MOVIE'
 , 'mediacode' : I11Iiii1I . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : OoO0O00IIiII
 , 'thumbnail' : oOOoo00O00o
 }
  if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = False , params = OO0OoO0o00 )
  if 9 - 9: I11i % OoooooooOO . oO0o % I11i
 if O0O0OOOOoo :
  if 32 - 32: i11iIiiIii
  OO0OoO0o00 [ 'mode' ] = 'MOVIE_GROUP'
  OO0OoO0o00 [ 'orderby' ] = O0oO000O0O
  OO0OoO0o00 [ 'page' ] = str ( I11iI + 1 )
  OoO0O00IIiII = '[B]%s >>[/B]' % '다음 페이지'
  oOo0O = str ( I11iI + 1 )
  o00OO00OoO ( OoO0O00IIiII , sublabel = oOo0O , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
 if len ( OoOoo00Ooo00 ) > 0 : xbmcplugin . endOfDirectory ( OOO , cacheToDisc = False )
 if 41 - 41: Oo0Ooo
 if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
 if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
 if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
def i1iI1 ( args ) :
 for o0O in Oooo0000 :
  OoO0O00IIiII = o0O . get ( 'title' )
  if 33 - 33: IiII % iIii1I11I1II1 * I1IiiI
  OO0OoO0o00 = { 'mode' : o0O . get ( 'mode' )
 , 'stype' : o0O . get ( 'stype' )
 , 'page' : '1'
 }
  if 95 - 95: ooOoO0o / ooOoO0o
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
 if len ( Oooo0000 ) > 0 : xbmcplugin . endOfDirectory ( OOO )
 if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
 if 41 - 41: i1IIi - I11i - Ii1I
 if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
def IIIi11I11 ( args ) :
 if 44 - 44: II111iiii
 i1 . SaveCredential ( oo0 ( ) )
 if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
 iI1 = __addon__ . getSetting ( 'id' )
 I11iI = int ( args . get ( 'page' ) )
 O0oo00o0O = args . get ( 'stype' )
 if 12 - 12: I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI / iII111i
 if 'search_key' in args :
  I1i1iiiI1 = args . get ( 'search_key' )
 else :
  I1i1iiiI1 = oOoO ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not I1i1iiiI1 : return
  if 24 - 24: oO0o / i11iIiiIii + oO0o
 I1i11i , O0O0OOOOoo = i1 . GetSearchList ( I1i1iiiI1 , iI1 , I11iI , O0oo00o0O , premiumyn = III1ii1iII ( ) )
 if len ( I1i11i ) == 0 : return
 if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
 for O0oOooooo0O in I1i11i :
  OoO0O00IIiII = O0oOooooo0O . get ( 'title' )
  oOOoo00O00o = O0oOooooo0O . get ( 'thumbnail' )
  O0O00Oo = O0oOooooo0O . get ( 'synopsis' )
  iiI1I1 = O0oOooooo0O . get ( 'program' )
  if 56 - 56: I1IiiI . O0 + Oo0Ooo
  O0O0ooOOO = { }
  O0O0ooOOO [ 'plot' ] = '%s\n\n%s' % ( OoO0O00IIiII , O0O00Oo )
  if 1 - 1: iII111i
  if O0oo00o0O == 'vod' :
   OO0OoO0o00 = { 'mode' : 'EPISODE'
 , 'programcode' : O0oOooooo0O . get ( 'program' )
 , 'page' : '1'
 }
   Ii = True
  else :
   OO0OoO0o00 = { 'mode' : 'MOVIE'
 , 'mediacode' : O0oOooooo0O . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : OoO0O00IIiII
 , 'thumbnail' : oOOoo00O00o
 }
   Ii = False
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = Ii , params = OO0OoO0o00 )
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 if O0O0OOOOoo :
  if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
  OO0OoO0o00 [ 'mode' ] = 'SEARCH'
  OO0OoO0o00 [ 'search_key' ] = I1i1iiiI1
  OO0OoO0o00 [ 'page' ] = str ( I11iI + 1 )
  OoO0O00IIiII = '[B]%s >>[/B]' % '다음 페이지'
  oOo0O = str ( I11iI + 1 )
  o00OO00OoO ( OoO0O00IIiII , sublabel = oOo0O , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
 if len ( I1i11i ) > 0 : xbmcplugin . endOfDirectory ( OOO )
 if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
 if 17 - 17: i1IIi
 if 21 - 21: Oo0Ooo
 if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
def I111i1i1111 ( stype ) :
 try :
  IIII1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( IIII1 , 'w' ) as I1I1i :
   I1I1i . write ( '' )
 except :
  None
  if 1 - 1: I11i % OOooOOo + O0 + i1IIi - OoO0O00
  if 22 - 22: I1IiiI % I1ii11iIi11i
  if 57 - 57: OOooOOo + O0 . Ii1I
  if 46 - 46: IiII
def ii1iIi1iIiI1i ( args ) :
 O0oo00o0O = args . get ( 'stype' )
 if 40 - 40: i1IIi % OOooOOo
 OoOooOOOO = xbmcgui . Dialog ( )
 iiIi1I1iIIi = OoOooOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if iiIi1I1iIIi == False : sys . exit ( )
 if 71 - 71: OoOoOO00
 I111i1i1111 ( O0oo00o0O )
 if 14 - 14: i11iIiiIii % OOooOOo
 xbmc . executebuiltin ( "Container.Refresh" )
 if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
 if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
 if 9 - 9: Ii1I
 if 59 - 59: I1IiiI * II111iiii . O0
def O000OoOO0 ( stype ) :
 try :
  IIII1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( IIII1 , 'r' ) as I1I1i :
   i1IiIII111i1 = I1I1i . readlines ( )
 except :
  i1IiIII111i1 = [ ]
  if 57 - 57: Ii1I % Ii1I * i11iIiiIii
 return i1IiIII111i1
 if 7 - 7: O0 . Ii1I
 if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
 if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
 if 7 - 7: iII111i % O0 . OoOoOO00 + I1IiiI - I11i
def o0o0O00oo0 ( stype , in_params ) :
 try :
  IIII1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  Ii1ii1IiIII = O000OoOO0 ( stype )
  if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
  with open ( IIII1 , 'w' ) as I1I1i :
   ooOOo00O00Oo = urllib . urlencode ( in_params )
   ooOOo00O00Oo = ooOOo00O00Oo . encode ( 'utf-8' ) + '\n'
   I1I1i . write ( ooOOo00O00Oo )
   if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * ooOoO0o % ooOoO0o
   i1iIi = 0
   for IIIII in Ii1ii1IiIII :
    o0ooOoO000oO = dict ( urlparse . parse_qsl ( IIIII ) )
    if in_params . get ( 'code' ) != o0ooOoO000oO . get ( 'code' ) :
     I1I1i . write ( IIIII )
     i1iIi += 1
     if i1iIi >= 50 : break
 except :
  None
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  if 74 - 74: O0 / i1IIi
def OoO ( args ) :
 O0oo00o0O = args . get ( 'stype' )
 if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
 if O0oo00o0O == '-' :
  for o0O in OOo :
   OoO0O00IIiII = o0O . get ( 'title' )
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
   OO0OoO0o00 = { 'mode' : o0O . get ( 'mode' )
 , 'stype' : o0O . get ( 'stype' )
 }
   if 100 - 100: OoO0O00
   o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = OO0OoO0o00 )
  if len ( OOo ) > 0 : xbmcplugin . endOfDirectory ( OOO )
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
 else :
  IIi1ii1Ii = O000OoOO0 ( O0oo00o0O )
  if 91 - 91: i11iIiiIii / OoooooooOO + iII111i - i11iIiiIii + OOooOOo
  for ii1i in IIi1ii1Ii :
   oOOoo = dict ( urlparse . parse_qsl ( ii1i ) )
   if 14 - 14: o0oOOo0O0Ooo * oO0o
   OoO0O00IIiII = oOOoo . get ( 'title' )
   oOOoo00O00o = oOOoo . get ( 'img' )
   if 81 - 81: Ii1I * o0oOOo0O0Ooo + I1Ii111 + Oo0Ooo - OoooooooOO
   O0O0ooOOO = { }
   O0O0ooOOO [ 'plot' ] = OoO0O00IIiII
   if 32 - 32: Ii1I * O0
   if O0oo00o0O == 'vod' :
    OO0OoO0o00 = { 'mode' : 'EPISODE'
 , 'programcode' : oOOoo . get ( 'code' )
 , 'page' : '1'
 }
    Ii = True
   else :
    OO0OoO0o00 = { 'mode' : 'MOVIE'
 , 'mediacode' : oOOoo . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : OoO0O00IIiII
 , 'thumbnail' : oOOoo00O00o
 }
    Ii = False
    if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
   o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = oOOoo00O00o , infoLabels = O0O0ooOOO , isFolder = Ii , params = OO0OoO0o00 )
   if 92 - 92: ooOoO0o
  O0O0ooOOO = { 'plot' : '시청목록을 삭제합니다.' }
  OoO0O00IIiII = '*** 시청목록 삭제 ***'
  OO0OoO0o00 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : O0oo00o0O
 }
  if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  o00OO00OoO ( OoO0O00IIiII , sublabel = '' , img = '' , infoLabels = O0O0ooOOO , isFolder = False , params = OO0OoO0o00 )
  if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
  xbmcplugin . endOfDirectory ( OOO , cacheToDisc = False )
  if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  if 92 - 92: I11i . I1Ii111
  if 85 - 85: I1ii11iIi11i . I1Ii111
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
  if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
def ii111I11iI ( args ) :
 if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * I11i
 i1 . SaveCredential ( oo0 ( ) )
 if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . ooOoO0o % IiII
 iiI1I1ii = args . get ( 'mediacode' )
 O0oo00o0O = args . get ( 'stype' )
 o0ooO = I1III ( O0oo00o0O )
 if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
 Iii , I1iiiiI1iI = i1 . GetBroadURL ( iiI1I1ii , o0ooO , O0oo00o0O )
 if 43 - 43: oO0o - OoooooooOO
 i1iIIi1 ( 'qt, stype, url : %s - %s - %s' % ( str ( o0ooO ) , O0oo00o0O , Iii ) )
 if 3 - 3: O0 / iII111i
 if Iii == '' :
  iIiiI1 ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
  if 89 - 89: II111iiii + i1IIi + II111iiii
  if 7 - 7: O0 % o0oOOo0O0Ooo + I1ii11iIi11i * iII111i - iII111i
 II1Ii11I111I = Iii . find ( 'Policy=' )
 if II1Ii11I111I != - 1 :
  I111 = Iii . split ( '?' ) [ 0 ]
  if 13 - 13: OoO0O00 * oO0o * iII111i
  IiIIiiI11III = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( Iii ) . query ) )
  IiIIiiI11III = urllib . urlencode ( IiIIiiI11III )
  IiIIiiI11III = IiIIiiI11III . replace ( '&' , ';' )
  IiIIiiI11III = IiIIiiI11III . replace ( 'Policy' , 'CloudFront-Policy' )
  IiIIiiI11III = IiIIiiI11III . replace ( 'Signature' , 'CloudFront-Signature' )
  IiIIiiI11III = IiIIiiI11III . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
  if 42 - 42: I1ii11iIi11i
  OOooOOOOOOooo = '%s|Cookie=%s' % ( I111 , IiIIiiI11III )
 else :
  OOooOOOOOOooo = Iii
  if 61 - 61: IiII . i1IIi / I1Ii111 % i11iIiiIii * iII111i
  if 31 - 31: OOooOOo + O0
 i1iIIi1 ( OOooOOOOOOooo , False )
 if 87 - 87: ooOoO0o
 if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
 if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
 if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
 iIi1II = xbmcgui . ListItem ( path = OOooOOOOOOooo )
 if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
 if 41 - 41: Ii1I
 if I1iiiiI1iI != '' :
  oOOoo0o0OOOO = I1iiiiI1iI
  i1IiII1III = 'https://cj.drmkeyserver.com/widevine_license'
  if 30 - 30: O0
  Oo00oo0000OO = 'mpd'
  O0oOOo0Oo = 'com.widevine.alpha'
  if 73 - 73: Ii1I - I1Ii111
  O00oooo00o0O = inputstreamhelper . Helper ( Oo00oo0000OO , drm = O0oOOo0Oo )
  if 9 - 9: I1IiiI % I1IiiI % II111iiii
  if O00oooo00o0O . check_inputstream ( ) :
   if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
   oOO0 = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % iiI1I1ii
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
   , 'user-agent' : O0o
 , 'AcquireLicenseAssertion' : oOOoo0o0OOOO
 , 'Host' : 'cj.drmkeyserver.com'
 }
   i1IIiIii1i = i1IiII1III + '|' + urllib . urlencode ( oOO0 ) + '|R{SSM}|'
   if 77 - 77: O0 % oO0o - OoO0O00
   iIi1II . setProperty ( 'inputstreamaddon' , O00oooo00o0O . inputstream_addon )
   if 97 - 97: OoooooooOO . i11iIiiIii + I1IiiI
   iIi1II . setProperty ( 'inputstream.adaptive.manifest_type' , Oo00oo0000OO )
   iIi1II . setProperty ( 'inputstream.adaptive.license_type' , O0oOOo0Oo )
   if 84 - 84: oO0o % i1IIi
   iIi1II . setProperty ( 'inputstream.adaptive.license_key' , i1IIiIii1i )
   if 70 - 70: Oo0Ooo . OoooooooOO - iII111i
   if 30 - 30: I1ii11iIi11i % I1IiiI
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   if 59 - 59: OOooOOo + i11iIiiIii
   if 88 - 88: i11iIiiIii - ooOoO0o
 xbmcplugin . setResolvedUrl ( OOO , True , iIi1II )
 if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
  OO0OoO0o00 = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
  o0o0O00oo0 ( args . get ( 'stype' ) , OO0OoO0o00 )
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - I11i
  if 30 - 30: OoOoOO00
  if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
  if 26 - 26: II111iiii * OoOoOO00
  if 10 - 10: II111iiii . iII111i
i1 = oo0Ooo0 ( )
OOO = int ( sys . argv [ 1 ] )
if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
OO0OoO0o00 = oOO ( )
ooO0oO00O0o = OO0OoO0o00 . get ( 'mode' , None )
if 70 - 70: I1Ii111
IIIIiiII111 ( )
if 16 - 16: iII111i - OoooooooOO % Oo0Ooo
if ooO0oO00O0o is None :
 if 36 - 36: OOooOOo
 O0ii1ii1ii ( )
 if 84 - 84: I1Ii111 . OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i
 if 57 - 57: I1IiiI % I11i - OOooOOo . I1IiiI / Oo0Ooo % iII111i
elif ooO0oO00O0o in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
 I1Ii ( OO0OoO0o00 )
 if 56 - 56: oO0o . iII111i . IiII * OoOoOO00 . ooOoO0o / O0
elif ooO0oO00O0o == 'CHANNEL' :
 oOO0O00oO0Ooo ( OO0OoO0o00 )
 if 23 - 23: i1IIi + iII111i + IiII + OoO0O00
elif ooO0oO00O0o in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 ii111I11iI ( OO0OoO0o00 )
 xbmc . sleep ( 200 )
 if 12 - 12: iIii1I11I1II1 - I1ii11iIi11i + i11iIiiIii
elif ooO0oO00O0o == 'PROGRAM' :
 Oo ( OO0OoO0o00 )
 if 10 - 10: I1IiiI - i1IIi - ooOoO0o % Oo0Ooo
elif ooO0oO00O0o == 'EPISODE' :
 ooooooo00o ( OO0OoO0o00 )
 if 6 - 6: I1ii11iIi11i + oO0o
elif ooO0oO00O0o == 'MOVIE_GROUP' :
 IIIIiIiIi1 ( OO0OoO0o00 )
 if 48 - 48: iIii1I11I1II1 % i1IIi % iII111i + ooOoO0o
elif ooO0oO00O0o == 'SEARCH_GROUP' :
 i1iI1 ( OO0OoO0o00 )
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . I11i % iIii1I11I1II1
elif ooO0oO00O0o == 'SEARCH' :
 IIIi11I11 ( OO0OoO0o00 )
 if 62 - 62: Oo0Ooo * OoOoOO00
elif ooO0oO00O0o == 'WATCH' :
 OoO ( OO0OoO0o00 )
 if 79 - 79: OoO0O00 . iII111i * Ii1I - OOooOOo + ooOoO0o
elif ooO0oO00O0o == 'MYVIEW_REMOVE' :
 ii1iIi1iIiI1i ( OO0OoO0o00 )
 if 14 - 14: i11iIiiIii - iII111i * OoOoOO00
elif ooO0oO00O0o == 'ORDER_BY' :
 I11IIIi ( OO0OoO0o00 )
 if 51 - 51: I1ii11iIi11i / iIii1I11I1II1 % oO0o + o0oOOo0O0Ooo * ooOoO0o + I1Ii111
else :
 None
 if 77 - 77: ooOoO0o * OoOoOO00
 if 14 - 14: I11i % I11i / IiII
 if 72 - 72: i1IIi - II111iiii - OOooOOo + OOooOOo * o0oOOo0O0Ooo * OOooOOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
