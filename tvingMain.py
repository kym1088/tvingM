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
 OOOO . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d %H:%M:%S' ) )
 if 87 - 87: oO0o / I11i - i1IIi * OOooOOo / OoooooooOO . O0
 if 1 - 1: II111iiii - I11i / I11i
def I1II1III11iii ( ) :
 OOOO = xbmcgui . Window ( 10000 )
 Oo000 = {
 'tving_token' : OOOO . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : OOOO . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : OOOO . getProperty ( 'TVING_M_UUID' )
 }
 return Oo000
 if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
def II111ii1II1i ( orderby ) :
 OOOO = xbmcgui . Window ( 10000 )
 OOOO . setProperty ( 'TVING_M_ORDERBY' , orderby )
 if 59 - 59: O0 + I1IiiI + IiII % I1IiiI
def o0OOoo0OO0OOO ( ) :
 OOOO = xbmcgui . Window ( 10000 )
 return OOOO . getProperty ( 'TVING_M_ORDERBY' )
 if 19 - 19: oO0o % i1IIi % o0oOOo0O0Ooo
 if 93 - 93: iIii1I11I1II1 % oO0o * i1IIi
 if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
def Ii11iII1 ( ) :
 Oo0O0O0ooO0O = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for IIIIii in Oo0O0O0ooO0O . keys ( ) :
  Oo0O0O0ooO0O [ IIIIii ] = Oo0O0O0ooO0O [ IIIIii ] [ 0 ]
 return Oo0O0O0ooO0O
 if 70 - 70: Ii1I / I11i . iII111i % Oo0Ooo
 if 67 - 67: OoOoOO00 * o0oOOo0O0Ooo . IiII - OoO0O00 * o0oOOo0O0Ooo
 if 46 - 46: OOooOOo + OoOoOO00 . I1IiiI * oO0o % IiII
def Oo000o ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 I11IiI1I11i1i = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 38 - 38: o0oOOo0O0Ooo
 if sublabel : Oo0O = '%s < %s >' % ( label , sublabel )
 else : Oo0O = label
 if not img : img = 'DefaultFolder.png'
 if 25 - 25: OoOoOO00 . II111iiii / iII111i . OOooOOo * OoO0O00 . I1IiiI
 Oo0oOOo = xbmcgui . ListItem ( Oo0O , thumbnailImage = img )
 if infoLabels : Oo0oOOo . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : Oo0oOOo . setProperty ( 'IsPlayable' , 'true' )
 if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 xbmcplugin . addDirectoryItem ( oO0o0OOOO , I11IiI1I11i1i , Oo0oOOo , isFolder )
 if 68 - 68: iII111i - I1Ii111 - I1IiiI - I1ii11iIi11i + I11i
 if 10 - 10: OoooooooOO % iIii1I11I1II1
 if 54 - 54: I1Ii111 - II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + ooOoO0o
def I1111I1iII11 ( etype ) :
 try :
  if etype == 'movie' :
   Oooo0O0oo00oO = 'movie_quality'
  else :
   Oooo0O0oo00oO = 'selected_quality'
   if 14 - 14: OoOoOO00 / IiII . OoOoOO00 . I11i % OoO0O00 * I11i
  iII = [ 1080 , 720 , 480 , 360 ]
  if 96 - 96: Oo0Ooo
  Ii1I1IIii1II = int ( __addon__ . getSetting ( Oooo0O0oo00oO ) )
  return iII [ Ii1I1IIii1II ]
 except :
  None
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
 return 720
 if 21 - 21: I1IiiI * iIii1I11I1II1
 if 91 - 91: IiII
 if 15 - 15: II111iiii
def Ii ( ) :
 if 79 - 79: OoooooooOO / O0
 for OO0OoO0o00 in o0oO0 :
  Oo0O = OO0OoO0o00 . get ( 'title' )
  if 53 - 53: O0 * OoO0O00 + OOooOOo
  IioOOo0 = { 'mode' : OO0OoO0o00 . get ( 'mode' )
 , 'stype' : OO0OoO0o00 . get ( 'stype' )
 , 'orderby' : OO0OoO0o00 . get ( 'orderby' )
 , 'page' : '1'
 }
  if 54 - 54: O0 - IiII % OOooOOo
  if OO0OoO0o00 . get ( 'mode' ) == 'XXX' :
   IioOOo0 [ 'mode' ] = 'XXX'
   OOoO = False
  else :
   OOoO = True
   if 46 - 46: OoO0O00 . Oo0Ooo - OoooooooOO
  Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = None , isFolder = OOoO , params = IioOOo0 )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO )
 if 93 - 93: iII111i
 if 10 - 10: I11i
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
def I1111IIi ( ) :
 ( Oo0oO , IIiIi1iI , i1IiiiI1iI ) = Ii11iI1i ( )
 if 49 - 49: Ii1I / OoO0O00 . II111iiii
 if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
 if not ( Oo0oO and IIiIi1iI ) :
  OoOooOOOO = xbmcgui . Dialog ( )
  iii = OoOooOOOO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if iii == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
 III1Iiii1I11 = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
 if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 if III1Iiii1I11 != '' :
  if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
  try :
   IIi1I11I1II = datetime . datetime . strptime ( III1Iiii1I11 , '%Y-%m-%d %H:%M:%S' )
  except TypeError :
   import time
   IIi1I11I1II = datetime . datetime . fromtimestamp ( time . mktime ( time . strptime ( III1Iiii1I11 , '%Y-%m-%d %H:%M:%S' ) ) )
   i1iIIi1 ( 'loginTime_str2 : ' + III1Iiii1I11 )
   if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
  if datetime . datetime . now ( ) < IIi1I11I1II + datetime . timedelta ( days = 1 ) :
   return
   if 84 - 84: IiII
   if 86 - 86: OoOoOO00 - Ii1I - OoO0O00 * iII111i
 if not oooo0O0 . GetCredential ( Oo0oO , IIiIi1iI , i1IiiiI1iI ) :
  iIiiI1 ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 51 - 51: OoO0O00 / OoO0O00
  if 53 - 53: Oo0Ooo
 oOoOooOo0o0 ( oooo0O0 . LoadCredential ( ) )
 II111ii1II1i ( 'desc' )
 if 29 - 29: I1ii11iIi11i + oO0o % O0
 if 10 - 10: I11i / I1Ii111 - I1IiiI * iIii1I11I1II1 - I1IiiI
 if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % iII111i
 if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
def i1 ( args ) :
 I1iI1iIi111i = args . get ( 'stype' )
 if I1iI1iIi111i == 'live' :
  iiIi1IIi1I = xI1Ii11I1Ii1i
 else :
  iiIi1IIi1I = I11
  if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
 for O0ooO0Oo00o in iiIi1IIi1I :
  Oo0O = O0ooO0Oo00o . get ( 'title' )
  if 77 - 77: iIii1I11I1II1 * OoO0O00
  IioOOo0 = { 'mode' : O0ooO0Oo00o . get ( 'mode' )
 , 'stype' : O0ooO0Oo00o . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
  if 95 - 95: I1IiiI + i11iIiiIii
  Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
 if len ( iiIi1IIi1I ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO )
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if 53 - 53: II111iiii
def i1Ii1Ii ( args ) :
 if 52 - 52: OoO0O00 . oO0o
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 25 - 25: O0 - O0 * o0oOOo0O0Ooo
 I1iI1iIi111i = args . get ( 'stype' )
 OOOO0oo0 = int ( args . get ( 'page' ) )
 I11iiI1i1 , I1i1Iiiii = oooo0O0 . GetLiveChannelList ( I1iI1iIi111i , OOOO0oo0 )
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 for oO0 in I11iiI1i1 :
  Oo0O = oO0 . get ( 'title' )
  O0OO0O = oO0 . get ( 'channel' )
  OO = oO0 . get ( 'thumbnail' )
  OoOoO = oO0 . get ( 'synopsis' )
  Ii1I1i = oO0 . get ( 'channelepg' )
  if 99 - 99: oO0o . iII111i + ooOoO0o % oO0o . i11iIiiIii % O0
  oOO00O = { }
  oOO00O [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( O0OO0O , Oo0O , Ii1I1i , OoOoO )
  if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
  IioOOo0 = { 'mode' : 'LIVE'
 , 'mediacode' : oO0 . get ( 'mediacode' )
 , 'stype' : I1iI1iIi111i
  }
  if 39 - 39: II111iiii / ooOoO0o + I1Ii111 / OoOoOO00
  Oo000o ( O0OO0O , sublabel = Oo0O , img = OO , infoLabels = oOO00O , isFolder = False , params = IioOOo0 )
  if 13 - 13: IiII + O0 + iII111i % I1IiiI / o0oOOo0O0Ooo . IiII
 if I1i1Iiiii :
  if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
  IioOOo0 [ 'mode' ] = 'CHANNEL'
  IioOOo0 [ 'stype' ] = I1iI1iIi111i
  IioOOo0 [ 'page' ] = str ( OOOO0oo0 + 1 )
  Oo0O = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( OOOO0oo0 + 1 )
  Oo000o ( Oo0O , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if 98 - 98: OOooOOo + IiII + oO0o % OoooooooOO
 if len ( I11iiI1i1 ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO , cacheToDisc = False )
 if 97 - 97: O0 * OoooooooOO . OoooooooOO
 if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
 if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
def oO00oooOOoOo0 ( args ) :
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 62 - 62: OoooooooOO * I1IiiI
 I1iI1iIi111i = args . get ( 'stype' )
 oOOOoo0O0oO = args . get ( 'orderby' )
 OOOO0oo0 = int ( args . get ( 'page' ) )
 if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
 I1IIIiIiI1 , I1i1Iiiii = oooo0O0 . GetProgramList ( I1iI1iIi111i , oOOOoo0O0oO , OOOO0oo0 )
 if 28 - 28: iIii1I11I1II1 % Oo0Ooo * I1IiiI % Ii1I * o0oOOo0O0Ooo / o0oOOo0O0Ooo
 for iIIII in I1IIIiIiI1 :
  Oo0O = iIIII . get ( 'title' )
  OO = iIIII . get ( 'thumbnail' )
  OoOoO = iIIII . get ( 'synopsis' )
  I11iI1i1I11I11 = o0o0Oo0oooo0 . get ( iIIII . get ( 'channel' ) )
  if 69 - 69: OoOoOO00
  oOO00O = { }
  oOO00O [ 'plot' ] = '%s <%s>\n\n%s' % ( Oo0O , I11iI1i1I11I11 , OoOoO )
  if 97 - 97: I1ii11iIi11i % I1ii11iIi11i % oO0o / iII111i - iIii1I11I1II1
  IioOOo0 = { 'mode' : 'EPISODE'
 , 'programcode' : iIIII . get ( 'program' )
 , 'page' : '1'
 }
  if 69 - 69: I1Ii111
  Oo000o ( Oo0O , sublabel = I11iI1i1I11I11 , img = OO , infoLabels = oOO00O , isFolder = True , params = IioOOo0 )
  if 11 - 11: I1IiiI
 if I1i1Iiiii :
  if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
  IioOOo0 [ 'mode' ] = 'PROGRAM'
  IioOOo0 [ 'stype' ] = I1iI1iIi111i
  IioOOo0 [ 'orderby' ] = oOOOoo0O0oO
  IioOOo0 [ 'page' ] = str ( OOOO0oo0 + 1 )
  Oo0O = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( OOOO0oo0 + 1 )
  Oo000o ( Oo0O , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
 if len ( I1IIIiIiI1 ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO , cacheToDisc = False )
 if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
 if 71 - 71: I1Ii111 + Ii1I
 if 28 - 28: OOooOOo
 if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
def OoOOo0OOoO ( args ) :
 if 72 - 72: Ii1I
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
 IiII111i1i11 = args . get ( 'programcode' )
 OOOO0oo0 = int ( args . get ( 'page' ) )
 if 40 - 40: ooOoO0o * IiII * i11iIiiIii
 oo0OO00OoooOo , I1i1Iiiii , II1i111Ii1i = oooo0O0 . GetEpisodoList ( IiII111i1i11 , OOOO0oo0 , orderby = o0OOoo0OO0OOO ( ) )
 if 15 - 15: II111iiii / i1IIi
 for O0oO0 in oo0OO00OoooOo :
  Oo0O = O0oO0 . get ( 'title' )
  OO = O0oO0 . get ( 'thumbnail' )
  OoOoO = O0oO0 . get ( 'synopsis' )
  if 7 - 7: I1IiiI
  oOO00O = { }
  oOO00O [ 'plot' ] = '%s\n\n%s' % ( Oo0O , OoOoO )
  if 41 - 41: I11i * iIii1I11I1II1 / II111iiii * oO0o
  IioOOo0 = { 'mode' : 'VOD'
 , 'mediacode' : O0oO0 . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : IiII111i1i11
 , 'title' : Oo0O
 , 'thumbnail' : OO
 }
  if 22 - 22: OoooooooOO
  Oo000o ( Oo0O , sublabel = '' , img = OO , infoLabels = oOO00O , isFolder = False , params = IioOOo0 )
  if 75 - 75: o0oOOo0O0Ooo + o0oOOo0O0Ooo + i1IIi - i1IIi
  if 76 - 76: OoO0O00 . O0 % O0 - o0oOOo0O0Ooo - iIii1I11I1II1 - I1IiiI
  if 53 - 53: i1IIi
  if 59 - 59: o0oOOo0O0Ooo
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
 if OOOO0oo0 == 1 :
  oOO00O = { 'plot' : '정렬순서를 변경합니다.' }
  IioOOo0 = { }
  IioOOo0 [ 'mode' ] = 'ORDER_BY'
  if o0OOoo0OO0OOO ( ) == 'desc' :
   Oo0O = '정렬순서변경 : 최신화부터 -> 1회부터'
   IioOOo0 [ 'orderby' ] = 'asc'
  else :
   Oo0O = '정렬순서변경 : 1회부터 -> 최신화부터'
   IioOOo0 [ 'orderby' ] = 'desc'
  Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = oOO00O , isFolder = False , params = IioOOo0 )
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 if I1i1Iiiii :
  if 23 - 23: i11iIiiIii
  IioOOo0 [ 'mode' ] = 'EPISODE'
  IioOOo0 [ 'programcode' ] = IiII111i1i11
  IioOOo0 [ 'page' ] = str ( OOOO0oo0 + 1 )
  Oo0O = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( OOOO0oo0 + 1 )
  Oo000o ( Oo0O , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
 if len ( oo0OO00OoooOo ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO , cacheToDisc = False )
 if 81 - 81: IiII % i1IIi . iIii1I11I1II1
 if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
 if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
 if 31 - 31: OOooOOo
def i1OOO0000oO ( args ) :
 oOOOoo0O0oO = args . get ( 'orderby' )
 if 15 - 15: OoOoOO00 % I1IiiI * I11i
 II111ii1II1i ( oOOOoo0O0oO )
 xbmc . executebuiltin ( "Container.Refresh" )
 if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
 if 20 - 20: oO0o % IiII
 if 19 - 19: I1ii11iIi11i % IiII + ooOoO0o / I1Ii111 . ooOoO0o
 if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
def o0O ( args ) :
 if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
 oOOOoo0O0oO = args . get ( 'orderby' )
 OOOO0oo0 = int ( args . get ( 'page' ) )
 if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
 O0O0o0oOOO , I1i1Iiiii = oooo0O0 . GetMovieList ( oOOOoo0O0oO , OOOO0oo0 , premiumyn = III1ii1iII ( ) )
 if 67 - 67: OoOoOO00 + I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
 for o000ooooO0o in O0O0o0oOOO :
  Oo0O = o000ooooO0o . get ( 'title' )
  OO = o000ooooO0o . get ( 'thumbnail' )
  OoOoO = o000ooooO0o . get ( 'synopsis' )
  if 40 - 40: I1ii11iIi11i + i1IIi * OOooOOo
  oOO00O = { }
  oOO00O [ 'plot' ] = '%s\n\n%s' % ( Oo0O , OoOoO )
  if 85 - 85: Ii1I * Oo0Ooo . O0 - i11iIiiIii
  IioOOo0 = { 'mode' : 'MOVIE'
 , 'mediacode' : o000ooooO0o . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : Oo0O
 , 'thumbnail' : OO
 }
  if 18 - 18: Ii1I + IiII - O0
  Oo000o ( Oo0O , sublabel = '' , img = OO , infoLabels = oOO00O , isFolder = False , params = IioOOo0 )
  if 53 - 53: i1IIi
 if I1i1Iiiii :
  if 87 - 87: i11iIiiIii + I1Ii111 . I1ii11iIi11i * I1Ii111 . ooOoO0o / I1ii11iIi11i
  IioOOo0 [ 'mode' ] = 'MOVIE_GROUP'
  IioOOo0 [ 'orderby' ] = oOOOoo0O0oO
  IioOOo0 [ 'page' ] = str ( OOOO0oo0 + 1 )
  Oo0O = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( OOOO0oo0 + 1 )
  Oo000o ( Oo0O , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if 76 - 76: O0 + i1IIi . Oo0Ooo * I1IiiI * Ii1I
 if len ( O0O0o0oOOO ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO , cacheToDisc = False )
 if 14 - 14: o0oOOo0O0Ooo % O0 * iII111i + Ii1I + Oo0Ooo * Ii1I
 if 3 - 3: OoOoOO00 * Oo0Ooo
 if 95 - 95: OOooOOo % oO0o . Ii1I
 if 72 - 72: OoooooooOO
def OooooOoooO ( args ) :
 for O0ooO0Oo00o in Oooo0000 :
  Oo0O = O0ooO0Oo00o . get ( 'title' )
  if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
  IioOOo0 = { 'mode' : O0ooO0Oo00o . get ( 'mode' )
 , 'stype' : O0ooO0Oo00o . get ( 'stype' )
 , 'page' : '1'
 }
  if 39 - 39: O0 + I1Ii111
  Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
 if len ( Oooo0000 ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO )
 if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
 if 26 - 26: I1ii11iIi11i - OoooooooOO
 if 11 - 11: I1IiiI * oO0o
 if 81 - 81: iII111i + IiII
def o0oo0 ( args ) :
 if 97 - 97: OoOoOO00 % I1ii11iIi11i
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 = __addon__ . getSetting ( 'id' )
 OOOO0oo0 = int ( args . get ( 'page' ) )
 I1iI1iIi111i = args . get ( 'stype' )
 if 80 - 80: oO0o + OOooOOo / I11i
 if 'search_key' in args :
  oOOO00O0O0OOo = args . get ( 'search_key' )
 else :
  oOOO00O0O0OOo = oOoO ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not oOOO00O0O0OOo : return
  if 77 - 77: oO0o + ooOoO0o . Oo0Ooo % Ii1I
 oo , I1i1Iiiii = oooo0O0 . GetSearchList ( oOOO00O0O0OOo , O0O0Oo00 , OOOO0oo0 , I1iI1iIi111i , premiumyn = III1ii1iII ( ) )
 if len ( oo ) == 0 : return
 if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
 for iI1 in oo :
  Oo0O = iI1 . get ( 'title' )
  OO = iI1 . get ( 'thumbnail' )
  OoOoO = iI1 . get ( 'synopsis' )
  IiI = iI1 . get ( 'program' )
  if 21 - 21: OoO0O00 + I1IiiI % I1IiiI
  oOO00O = { }
  oOO00O [ 'plot' ] = '%s\n\n%s' % ( Oo0O , OoOoO )
  if 82 - 82: iII111i
  if I1iI1iIi111i == 'vod' :
   IioOOo0 = { 'mode' : 'EPISODE'
 , 'programcode' : iI1 . get ( 'program' )
 , 'page' : '1'
 }
   OOoO = True
  else :
   IioOOo0 = { 'mode' : 'MOVIE'
 , 'mediacode' : iI1 . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : Oo0O
 , 'thumbnail' : OO
 }
   OOoO = False
   if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
  Oo000o ( Oo0O , sublabel = '' , img = OO , infoLabels = oOO00O , isFolder = OOoO , params = IioOOo0 )
  if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
 if I1i1Iiiii :
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  IioOOo0 [ 'mode' ] = 'SEARCH'
  IioOOo0 [ 'search_key' ] = oOOO00O0O0OOo
  IioOOo0 [ 'page' ] = str ( OOOO0oo0 + 1 )
  Oo0O = '[B]%s >>[/B]' % '다음 페이지'
  oOOoo00O00o = str ( OOOO0oo0 + 1 )
  Oo000o ( Oo0O , sublabel = oOOoo00O00o , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
 if len ( oo ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO )
 if 71 - 71: O0 - iIii1I11I1II1
 if 12 - 12: OOooOOo / o0oOOo0O0Ooo
 if 42 - 42: Oo0Ooo
 if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
def iii11I ( stype ) :
 try :
  I1Iii1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( I1Iii1 , 'w' ) as iiI11Iii :
   iiI11Iii . write ( '' )
 except :
  None
  if 78 - 78: iII111i + I11i . ooOoO0o - iII111i . Ii1I
  if 30 - 30: I1IiiI + OoO0O00 % Ii1I * iII111i / Oo0Ooo - I11i
  if 64 - 64: iIii1I11I1II1
  if 21 - 21: Oo0Ooo . II111iiii
def ooo000o000 ( args ) :
 I1iI1iIi111i = args . get ( 'stype' )
 if 100 - 100: IiII . I11i / Ii1I % OoOoOO00 % II111iiii - OoO0O00
 OoOooOOOO = xbmcgui . Dialog ( )
 iii = OoOooOOOO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if iii == False : sys . exit ( )
 if 46 - 46: O0 * II111iiii - Oo0Ooo * ooOoO0o
 iii11I ( I1iI1iIi111i )
 if 33 - 33: Ii1I
 xbmc . executebuiltin ( "Container.Refresh" )
 if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
 if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
 if 5 - 5: Ii1I
 if 46 - 46: IiII
def ii1iIi1iIiI1i ( stype ) :
 try :
  I1Iii1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( I1Iii1 , 'r' ) as iiI11Iii :
   iiI1iIii1i = iiI11Iii . readlines ( )
 except :
  iiI1iIii1i = [ ]
  if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . IiII
 return iiI1iIii1i
 if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
 if 63 - 63: OoO0O00
 if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
 if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
def o0 ( stype , in_params ) :
 try :
  I1Iii1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  oOO = ii1iIi1iIiI1i ( stype )
  if 53 - 53: I1Ii111 * IiII . Oo0Ooo - Ii1I % Ii1I * i11iIiiIii
  with open ( I1Iii1 , 'w' ) as iiI11Iii :
   ii = urllib . urlencode ( in_params )
   ii = ii . encode ( 'utf-8' ) + '\n'
   iiI11Iii . write ( ii )
   if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
   ii1III11 = 0
   for I1iiIIIi11 in oOO :
    Ii1I11ii1i = dict ( urlparse . parse_qsl ( I1iiIIIi11 ) )
    if in_params . get ( 'code' ) != Ii1I11ii1i . get ( 'code' ) :
     iiI11Iii . write ( I1iiIIIi11 )
     ii1III11 += 1
     if ii1III11 >= 50 : break
 except :
  None
  if 89 - 89: iII111i . O0 / I1ii11iIi11i % OoOoOO00 . Oo0Ooo
  if 50 - 50: II111iiii + I1ii11iIi11i . i1IIi % o0oOOo0O0Ooo
  if 5 - 5: OoOoOO00 / OoooooooOO + IiII * I1Ii111 - OoO0O00 % I1IiiI
  if 42 - 42: O0 / o0oOOo0O0Ooo + OoooooooOO * ooOoO0o % ooOoO0o
def i1iIi ( args ) :
 I1iI1iIi111i = args . get ( 'stype' )
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 if I1iI1iIi111i == '-' :
  for O0ooO0Oo00o in OOo :
   Oo0O = O0ooO0Oo00o . get ( 'title' )
   if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
   IioOOo0 = { 'mode' : O0ooO0Oo00o . get ( 'mode' )
 , 'stype' : O0ooO0Oo00o . get ( 'stype' )
 }
   if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
   Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = IioOOo0 )
  if len ( OOo ) > 0 : xbmcplugin . endOfDirectory ( oO0o0OOOO )
  if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 else :
  oo000 = ii1iIi1iIiI1i ( I1iI1iIi111i )
  if 32 - 32: i1IIi . Ii1I
  for oOOOooo in oo000 :
   I1i1iiiII1i = dict ( urlparse . parse_qsl ( oOOOooo ) )
   if 100 - 100: OoO0O00
   Oo0O = I1i1iiiII1i . get ( 'title' )
   OO = I1i1iiiII1i . get ( 'img' )
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   oOO00O = { }
   oOO00O [ 'plot' ] = Oo0O
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   if I1iI1iIi111i == 'vod' :
    IioOOo0 = { 'mode' : 'EPISODE'
 , 'programcode' : I1i1iiiII1i . get ( 'code' )
 , 'page' : '1'
 }
    OOoO = True
   else :
    IioOOo0 = { 'mode' : 'MOVIE'
 , 'mediacode' : I1i1iiiII1i . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : Oo0O
 , 'thumbnail' : OO
 }
    OOoO = False
    if 45 - 45: I1Ii111
   Oo000o ( Oo0O , sublabel = '' , img = OO , infoLabels = oOO00O , isFolder = OOoO , params = IioOOo0 )
   if 83 - 83: OoOoOO00 . OoooooooOO
  oOO00O = { 'plot' : '시청목록을 삭제합니다.' }
  Oo0O = '*** 시청목록 삭제 ***'
  IioOOo0 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : I1iI1iIi111i
 }
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  Oo000o ( Oo0O , sublabel = '' , img = '' , infoLabels = oOO00O , isFolder = False , params = IioOOo0 )
  if 62 - 62: OoO0O00 / I1ii11iIi11i
  xbmcplugin . endOfDirectory ( oO0o0OOOO , cacheToDisc = False )
  if 7 - 7: OoooooooOO . IiII
  if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  if 92 - 92: ooOoO0o
def II11iI111i1 ( args ) :
 if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
 oooo0O0 . SaveCredential ( I1II1III11iii ( ) )
 if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
 o00 = args . get ( 'mediacode' )
 I1iI1iIi111i = args . get ( 'stype' )
 oO = I1111I1iII11 ( I1iI1iIi111i )
 if 92 - 92: IiII * Oo0Ooo * Oo0Ooo * I1IiiI . iIii1I11I1II1
 I1Ii1111iIi , I11o0oO00oO0o0o0 = oooo0O0 . GetBroadURL ( o00 , oO , I1iI1iIi111i )
 if 17 - 17: I11i . IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 i1iIIi1 ( 'qt, stype, url : %s - %s - %s' % ( str ( oO ) , I1iI1iIi111i , I1Ii1111iIi ) )
 if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
 if I1Ii1111iIi == '' :
  iIiiI1 ( __language__ ( 30303 ) . encode ( 'utf8' ) )
  return
  if 69 - 69: O0
  if 85 - 85: ooOoO0o / O0
  if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 o0Iii = I1Ii1111iIi . find ( 'Policy=' )
 if o0Iii != - 1 :
  I1iiiiI1iI = I1Ii1111iIi . split ( '?' ) [ 0 ]
  if 43 - 43: oO0o - OoooooooOO
  ii1iI = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( I1Ii1111iIi ) . query ) )
  ii1iI = urllib . urlencode ( ii1iI )
  ii1iI = ii1iI . replace ( '&' , ';' )
  ii1iI = ii1iI . replace ( 'Policy' , 'CloudFront-Policy' )
  ii1iI = ii1iI . replace ( 'Signature' , 'CloudFront-Signature' )
  ii1iI = ii1iI . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
  if 49 - 49: o0oOOo0O0Ooo . IiII / OoO0O00 + II111iiii
  ii11i = '%s|Cookie=%s' % ( I1iiiiI1iI , ii1iI )
 else :
  ii11i = I1Ii1111iIi
  if 35 - 35: I1ii11iIi11i * iII111i - OoO0O00 % o0oOOo0O0Ooo
  if 87 - 87: OoOoOO00 * I1Ii111 . I11i
 i1iIIi1 ( ii11i , False )
 if 51 - 51: OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o * iIii1I11I1II1 % OoO0O00
 if 99 - 99: oO0o * II111iiii * I1Ii111
 if 92 - 92: Oo0Ooo
 if 40 - 40: OoOoOO00 / IiII
 OOOoO000 = xbmcgui . ListItem ( path = ii11i )
 if 57 - 57: II111iiii
 if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
 if I11o0oO00oO0o0o0 != '' :
  i1i1ii111 = I11o0oO00oO0o0o0
  IiI1i = 'https://cj.drmkeyserver.com/widevine_license'
  if 87 - 87: ooOoO0o
  IIIii = 'mpd'
  O00OooOo00o = 'com.widevine.alpha'
  if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
  iIi1II = inputstreamhelper . Helper ( IIIii , drm = O00OooOo00o )
  if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
  if iIi1II . check_inputstream ( ) :
   if 41 - 41: Ii1I
   oOOoo0o0OOOO = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % o00
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
   , 'user-agent' : O0o
 , 'AcquireLicenseAssertion' : i1i1ii111
 , 'Host' : 'cj.drmkeyserver.com'
 }
   i1IiII1III = IiI1i + '|' + urllib . urlencode ( oOOoo0o0OOOO ) + '|R{SSM}|'
   if 30 - 30: O0
   OOOoO000 . setProperty ( 'inputstreamaddon' , iIi1II . inputstream_addon )
   if 99 - 99: II111iiii * IiII % iIii1I11I1II1 / Ii1I
   OOOoO000 . setProperty ( 'inputstream.adaptive.manifest_type' , IIIii )
   OOOoO000 . setProperty ( 'inputstream.adaptive.license_type' , O00OooOo00o )
   if 90 - 90: oO0o % OOooOOo - OOooOOo % II111iiii * OoO0O00
   OOOoO000 . setProperty ( 'inputstream.adaptive.license_key' , i1IiII1III )
   if 39 - 39: I11i
   if 58 - 58: i1IIi % o0oOOo0O0Ooo
   if 79 - 79: o0oOOo0O0Ooo % iII111i * OoooooooOO * iIii1I11I1II1 . iII111i / Ii1I
   if 19 - 19: O0 + I11i + Ii1I / II111iiii / II111iiii
   if 86 - 86: I1ii11iIi11i * O0 * IiII
 xbmcplugin . setResolvedUrl ( oO0o0OOOO , True , OOOoO000 )
 if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
 if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
  IioOOo0 = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
  o0 ( args . get ( 'stype' ) , IioOOo0 )
  if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
  if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  if 2 - 2: OoooooooOO % OOooOOo
  if 63 - 63: I1IiiI % iIii1I11I1II1
  if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
  if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
oooo0O0 = oo0Ooo0 ( )
oO0o0OOOO = int ( sys . argv [ 1 ] )
if 59 - 59: OOooOOo + i11iIiiIii
IioOOo0 = Ii11iII1 ( )
oo0OOo0O = IioOOo0 . get ( 'mode' , None )
if 39 - 39: OoooooooOO + oO0o % OOooOOo / OOooOOo
I1111IIi ( )
if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
if oo0OOo0O is None :
 if 20 - 20: o0oOOo0O0Ooo / i1IIi
 Ii ( )
 if 71 - 71: OoOoOO00 . i1IIi
 if 94 - 94: OOooOOo . I1Ii111
elif oo0OOo0O in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
 i1 ( IioOOo0 )
 if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
elif oo0OOo0O == 'CHANNEL' :
 i1Ii1Ii ( IioOOo0 )
 if 47 - 47: OoooooooOO
elif oo0OOo0O in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
 II11iI111i1 ( IioOOo0 )
 xbmc . sleep ( 200 )
 if 4 - 4: I1IiiI % I11i
elif oo0OOo0O == 'PROGRAM' :
 oO00oooOOoOo0 ( IioOOo0 )
 if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
elif oo0OOo0O == 'EPISODE' :
 OoOOo0OOoO ( IioOOo0 )
 if 82 - 82: ooOoO0o + II111iiii
elif oo0OOo0O == 'MOVIE_GROUP' :
 o0O ( IioOOo0 )
 if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
elif oo0OOo0O == 'SEARCH_GROUP' :
 OooooOoooO ( IioOOo0 )
 if 68 - 68: Oo0Ooo + i11iIiiIii
elif oo0OOo0O == 'SEARCH' :
 o0oo0 ( IioOOo0 )
 if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
elif oo0OOo0O == 'WATCH' :
 i1iIi ( IioOOo0 )
 if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
elif oo0OOo0O == 'MYVIEW_REMOVE' :
 ooo000o000 ( IioOOo0 )
 if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
elif oo0OOo0O == 'ORDER_BY' :
 i1OOO0000oO ( IioOOo0 )
 if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
else :
 None
 if 98 - 98: i1IIi
 if 65 - 65: OoOoOO00 / OoO0O00 % IiII
 if 45 - 45: OoOoOO00
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
