# -*- coding: utf-8 -*-
__author__ = "NightRain"
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
import os
import xbmcplugin , xbmcgui , xbmcaddon , xbmc
import sys
import urlparse
import inputstreamhelper
import datetime
import time
import base64
if 46 - 46: ooOoO0o * I11i - OoooooooOO
if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo
if 94 - 94: i1IIi % Oo0Ooo
__addon__ = xbmcaddon . Addon ( )
__language__ = __addon__ . getLocalizedString
__profile__ = xbmc . translatePath ( __addon__ . getAddonInfo ( 'profile' ) )
__version__ = __addon__ . getAddonInfo ( 'version' )
__addonid__ = __addon__ . getAddonInfo ( 'id' )
__addonname__ = __addon__ . getAddonInfo ( 'name' )
if 68 - 68: Ii1I / O0
if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i
Oo0oO0ooo = [
 { 'title' : 'LIVE 채널' , 'mode' : 'LIVE_GROUP' , 'stype' : 'live' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : 'VOD 방송 (인기순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'viewDay' , 'ordernm' : '인기' }
 , { 'title' : 'VOD 방송 (최신순)' , 'mode' : 'VOD_GROUP' , 'stype' : 'vod' , 'orderby' : 'new' , 'ordernm' : '최신' }
 , { 'title' : '월정액 영화관 (인기)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'viewWeek' , 'ordernm' : '-' }
 , { 'title' : '월정액 영화관 (최신)' , 'mode' : 'MOVIE_GROUP' , 'stype' : 'movie' , 'orderby' : 'new' , 'ordernm' : '-' }
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : '검색 (search)' , 'mode' : 'SEARCH_GROUP' , 'stype' : '-' , 'orderby' : '-' , 'ordernm' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : '-' , 'orderby' : '-' , 'ordernm' : '-' }
 ]
if 56 - 56: I11i - i1IIi
o00oOoo = [
 { 'title' : '실시간 TV' , 'mode' : 'CHANNEL' , 'stype' : 'onair' }
 , { 'title' : 'TVING TV' , 'mode' : 'CHANNEL' , 'stype' : 'tvingtv' }
 ]
if 78 - 78: I11i / OoO0O00 - O0 . IiII
OOooo0000ooo = [
 { 'title' : 'VOD 시청내역' , 'mode' : 'WATCH' , 'stype' : 'vod' }
 , { 'title' : '영화 시청내역' , 'mode' : 'WATCH' , 'stype' : 'movie' }
 ]
if 79 - 79: oO0o + I1Ii111 . ooOoO0o * IiII % I11i . I1IiiI
O0o0o00o0Oo0 = [
 { 'title' : 'VOD 검색' , 'mode' : 'SEARCH' , 'stype' : 'vod' }
 , { 'title' : '영화 검색' , 'mode' : 'SEARCH' , 'stype' : 'movie' }
 ]
if 23 - 23: OoooooooOO
IiII1I1i1i1ii = [
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
if 44 - 44: oO0o / Oo0Ooo - II111iiii - i11iIiiIii % I1Ii111
O0OoOoo00o = { 'C00551' : 'tvN'
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
if 31 - 31: II111iiii + OoO0O00 . I1Ii111
OoOooOOOO = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
i11iiII = xbmc . translatePath ( os . path . join ( __profile__ , 'tving_cookies.json' ) )
if 34 - 34: OOooOOo % OoooooooOO / i1IIi . iII111i + O0
if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
from tvingCore import *
if 78 - 78: OoO0O00
if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
class O0O00Ooo ( object ) :
 def __init__ ( self , in_addonurl , in_handle , in_params ) :
  if 64 - 64: oO0o - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
  if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + I1Ii111 + I1ii11iIi11i
  if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
  if 23 - 23: i11iIiiIii + I1IiiI
  self . _addon_url = in_addonurl
  self . _addon_handle = in_handle
  self . main_params = in_params
  self . TvingObj = oOOo0oo ( )
  if 68 - 68: OoOoOO00 . oO0o . i11iIiiIii
  if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
  if 33 - 33: Ii1I + II111iiii % i11iIiiIii . ooOoO0o - I1IiiI
 def addon_noti ( self , sting ) :
  try :
   O00oooo0O = xbmcgui . Dialog ( )
   if 22 - 22: OoooooooOO % I11i - iII111i . iIii1I11I1II1 * i11iIiiIii
   O00oooo0O . notification ( __addonname__ , sting )
  except :
   None
   if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . IiII
   if 61 - 61: ooOoO0o
   if 79 - 79: Oo0Ooo + I1IiiI - iII111i
 def addon_log ( self , string , isDebug = False ) :
  try :
   oO00O00o0OOO0 = string . encode ( 'utf-8' , 'ignore' )
  except :
   oO00O00o0OOO0 = 'addonException: addon_log'
  if isDebug : Ii1iIIIi1ii = xbmc . LOGDEBUG
  else : Ii1iIIIi1ii = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , oO00O00o0OOO0 ) , level = Ii1iIIIi1ii )
  if 80 - 80: I11i * i11iIiiIii / I1Ii111
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
  if 31 - 31: o0oOOo0O0Ooo + I11i + I11i / II111iiii
  if 26 - 26: OoooooooOO
 def get_keyboard_input ( self , title ) :
  IiiI11Iiiii = None
  ii1I1i1I = xbmc . Keyboard ( )
  ii1I1i1I . setHeading ( title )
  xbmc . sleep ( 1000 )
  ii1I1i1I . doModal ( )
  if ( ii1I1i1I . isConfirmed ( ) ) :
   IiiI11Iiiii = ii1I1i1I . getText ( )
  return IiiI11Iiiii
  if 88 - 88: OoO0O00 + O0 / OoOoOO00 * iII111i
  if 41 - 41: oO0o
  if 6 - 6: I1ii11iIi11i
  if 31 - 31: Ii1I . Ii1I - o0oOOo0O0Ooo / OoO0O00 + ooOoO0o * I1IiiI
 def get_settings_login_info ( self ) :
  O0ooOooooO = __addon__ . getSetting ( 'id' )
  o00O = __addon__ . getSetting ( 'pw' )
  OOO0OOO00oo = __addon__ . getSetting ( 'login_type' )
  return ( O0ooOooooO , o00O , OOO0OOO00oo )
  if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
  if 4 - 4: II111iiii / ooOoO0o . iII111i
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  if 50 - 50: I1IiiI
 def get_settings_premiumyn ( self ) :
  Ii1i11IIii1I = __addon__ . getSetting ( 'premium_movieyn' )
  if Ii1i11IIii1I == 'false' :
   return False
  else :
   return True
   if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + Ii1I + Ii1I - o0oOOo0O0Ooo / I1Ii111
   if 44 - 44: ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
   if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def get_settings_direct_replay ( self ) :
  IiII1I11i1I1I = int ( __addon__ . getSetting ( 'direct_replay' ) )
  if IiII1I11i1I1I == 0 :
   return False
  else :
   return True
   if 83 - 83: I1ii11iIi11i / ooOoO0o
   if 49 - 49: o0oOOo0O0Ooo
   if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
 def get_settings_thumbnail_landyn ( self ) :
  o00OO00OoO = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if o00OO00OoO == 0 :
   return True
  else :
   return False
   if 60 - 60: OoO0O00 * OoOoOO00 - OoO0O00 % OoooooooOO - ooOoO0o + I1IiiI
   if 70 - 70: IiII * Oo0Ooo * I11i / Ii1I
   if 88 - 88: O0
   if 64 - 64: I11i * O0 + IiII - OOooOOo + i11iIiiIii * Ii1I
 def set_winCredential ( self , credential ) :
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
  iII . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
  iII . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
  if 80 - 80: IiII . oO0o
  iII . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 25 - 25: OoOoOO00 . II111iiii / iII111i . OOooOOo * OoO0O00 . I1IiiI
  if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
 def get_winCredential ( self ) :
  iII = xbmcgui . Window ( 10000 )
  Oo0OoO00oOO0o = {
 'tving_token' : iII . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : iII . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : iII . getProperty ( 'TVING_M_UUID' )
 }
  return Oo0OoO00oOO0o
  if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
 def set_winEpisodeOrderby ( self , orderby ) :
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_ORDERBY' , orderby )
  if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
 def get_winEpisodeOrderby ( self ) :
  iII = xbmcgui . Window ( 10000 )
  return iII . getProperty ( 'TVING_M_ORDERBY' )
  if 98 - 98: iII111i * iII111i / iII111i + I11i
  if 34 - 34: ooOoO0o
  if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  o0 = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 91 - 91: iIii1I11I1II1 + I1Ii111
  if sublabel : i1i = '%s < %s >' % ( label , sublabel )
  else : i1i = label
  if not img : img = 'DefaultFolder.png'
  if 46 - 46: I1Ii111 % I11i + OoO0O00 . OoOoOO00 . OoO0O00
  if 96 - 96: Oo0Ooo
  Ii1I1IIii1II = xbmcgui . ListItem ( i1i )
  Ii1I1IIii1II . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 65 - 65: Ii1I . iIii1I11I1II1 / O0 - Ii1I
  if infoLabels : Ii1I1IIii1II . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : Ii1I1IIii1II . setProperty ( 'IsPlayable' , 'true' )
  if 21 - 21: I1IiiI * iIii1I11I1II1
  xbmcplugin . addDirectoryItem ( self . _addon_handle , o0 , Ii1I1IIii1II , isFolder )
  if 91 - 91: IiII
  if 15 - 15: II111iiii
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 def get_selQuality ( self , etype ) :
  try :
   OO0OoO0o00 = 'selected_quality'
   if 53 - 53: O0 * OoO0O00 + OOooOOo
   if 50 - 50: O0 . O0 - oO0o / I1IiiI - o0oOOo0O0Ooo * OoOoOO00
   if 61 - 61: I11i
   if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
   if 42 - 42: OoO0O00
   if 67 - 67: I1Ii111 . iII111i . O0
   if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
   OOOOoOoo0O0O0 = [ 1080 , 720 , 480 , 360 ]
   if 85 - 85: oO0o % i11iIiiIii - iII111i * OoooooooOO / I1IiiI % I1IiiI
   IIiIi1iI = int ( __addon__ . getSetting ( OO0OoO0o00 ) )
   return OOOOoOoo0O0O0 [ IIiIi1iI ]
  except :
   None
   if 35 - 35: Ii1I % O0 - O0
  return 720
  if 16 - 16: II111iiii % OoOoOO00 - II111iiii + Ii1I
  if 12 - 12: OOooOOo / OOooOOo + i11iIiiIii
  if 40 - 40: I1IiiI . iIii1I11I1II1 / I1IiiI / i11iIiiIii
 def dp_Main_List ( self ) :
  if 75 - 75: I11i + o0oOOo0O0Ooo
  for O0i1II1Iiii1I11 in Oo0oO0ooo :
   i1i = O0i1II1Iiii1I11 . get ( 'title' )
   if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   o00oooO0Oo = { 'mode' : O0i1II1Iiii1I11 . get ( 'mode' )
 , 'stype' : O0i1II1Iiii1I11 . get ( 'stype' )
 , 'orderby' : O0i1II1Iiii1I11 . get ( 'orderby' )
 , 'ordernm' : O0i1II1Iiii1I11 . get ( 'ordernm' )
 , 'page' : '1'
 }
   if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
   if O0i1II1Iiii1I11 . get ( 'mode' ) == 'XXX' :
    o00oooO0Oo [ 'mode' ] = 'XXX'
    OOooOoooOoOo = False
   else :
    OOooOoooOoOo = True
    if 84 - 84: IiII
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = OOooOoooOoOo , params = o00oooO0Oo )
  if len ( Oo0oO0ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 86 - 86: OoOoOO00 - Ii1I - OoO0O00 * iII111i
  if 66 - 66: OoooooooOO + O0
  if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
  if 41 - 41: Ii1I - O0 - O0
  if 68 - 68: OOooOOo % I1Ii111
 def login_main ( self ) :
  ( ooO00OO0 , i11111IIIII , iIiii1i111iI1 ) = self . get_settings_login_info ( )
  if 14 - 14: iII111i . iII111i % OoooooooOO
  if 44 - 44: i1IIi % II111iiii + I11i
  if not ( ooO00OO0 and i11111IIIII ) :
   O00oooo0O = xbmcgui . Dialog ( )
   I1I1I = O00oooo0O . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if I1I1I == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 95 - 95: II111iiii + o0oOOo0O0Ooo + iII111i * iIii1I11I1II1 % oO0o / IiII
    if 56 - 56: iII111i
    if 86 - 86: II111iiii % I1Ii111
  if self . get_winEpisodeOrderby ( ) == '' :
   self . set_winEpisodeOrderby ( 'desc' )
   if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
   if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
  if self . cookiefile_check ( ) : return
  if 80 - 80: II111iiii
  if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
  if 53 - 53: II111iiii
  i1Ii1Ii = datetime . datetime . now ( ) . date ( )
  oOO = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
  if oOO == None or oOO == '' : oOO = '1900-01-01'
  try :
   oOO = datetime . datetime . strptime ( oOO , '%Y-%m-%d' ) . date ( )
  except TypeError :
   oOO = datetime . datetime ( * ( time . strptime ( oOO , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 25 - 25: O0 - O0 * o0oOOo0O0Ooo
   if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
   if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
   oOoooo0O0Oo = 0
   while True :
    oOoooo0O0Oo += 1
    if 76 - 76: Ii1I + IiII
    time . sleep ( 0.05 )
    if 34 - 34: Oo0Ooo
    if 89 - 89: Oo0Ooo * OoOoOO00 * I1Ii111 + iII111i - I11i
    if oOO >= i1Ii1Ii : return
    if oOoooo0O0Oo > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
   if 8 - 8: o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
   if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  if oOO >= i1Ii1Ii :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   return
   if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
   if 79 - 79: O0
  if not self . TvingObj . GetCredential ( ooO00OO0 , i11111IIIII , iIiii1i111iI1 ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
   if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  self . set_winCredential ( self . TvingObj . LoadCredential ( ) )
  if 57 - 57: OoO0O00 / ooOoO0o
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
  if 13 - 13: Ii1I . i11iIiiIii
  if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 def dp_Title_Group ( self , args ) :
  I111iI = args . get ( 'stype' )
  if I111iI == 'live' :
   oOOo0 = o00oOoo
  else :
   oOOo0 = IiII1I1i1i1ii
   if 16 - 16: oO0o % I1ii11iIi11i * i11iIiiIii % i11iIiiIii
  for O0OOOOo0O in oOOo0 :
   i1i = O0OOOOo0O . get ( 'title' )
   if 81 - 81: O0 / OoO0O00 . i1IIi + I1IiiI - I11i
   if args . get ( 'ordernm' ) != '-' :
    i1i += '  (' + args . get ( 'ordernm' ) + ')'
    if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
   o00oooO0Oo = { 'mode' : O0OOOOo0O . get ( 'mode' )
 , 'stype' : O0OOOOo0O . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
   if 62 - 62: OoooooooOO * I1IiiI
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
  if len ( oOOo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
  if 97 - 97: O0 + OoOoOO00
  if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
 def dp_LiveChannel_List ( self , args ) :
  if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 77 - 77: OOooOOo * iIii1I11I1II1
  I111iI = args . get ( 'stype' )
  oO00oOOoooO = int ( args . get ( 'page' ) )
  IiIi11iI , Oo0O00O000 = self . TvingObj . GetLiveChannelList ( I111iI , oO00oOOoooO )
  if 3 - 3: Ii1I * I1ii11iIi11i % I11i
  for oO0o0o0oo in IiIi11iI :
   i1i = oO0o0o0oo . get ( 'title' )
   iI1111iiii = oO0o0o0oo . get ( 'channel' )
   Oo0OO = oO0o0o0oo . get ( 'thumbnail' )
   O0OooOo0o = oO0o0o0oo . get ( 'synopsis' )
   iiI11ii1I1 = oO0o0o0oo . get ( 'channelepg' )
   if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
   oOo0OOoO0 = oO0o0o0oo . get ( 'info' )
   oOo0OOoO0 [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( iI1111iiii , i1i , iiI11ii1I1 , O0OooOo0o )
   if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
   o00oooO0Oo = { 'mode' : 'LIVE'
 , 'mediacode' : oO0o0o0oo . get ( 'mediacode' )
 , 'stype' : I111iI
   }
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
   self . add_dir ( iI1111iiii , sublabel = i1i , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = False , params = o00oooO0Oo )
   if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  if Oo0O00O000 :
   if 11 - 11: ooOoO0o / OoOoOO00 - IiII * OoooooooOO + OoooooooOO . OoOoOO00
   o00oooO0Oo [ 'mode' ] = 'CHANNEL'
   o00oooO0Oo [ 'stype' ] = I111iI
   o00oooO0Oo [ 'page' ] = str ( oO00oOOoooO + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   i1I1i111Ii = str ( oO00oOOoooO + 1 )
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if 67 - 67: I1IiiI . i1IIi
  if len ( IiIi11iI ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 27 - 27: ooOoO0o % I1IiiI
  if 73 - 73: OOooOOo
  if 70 - 70: iIii1I11I1II1
  if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
 def dp_Program_List ( self , args ) :
  if 92 - 92: i1IIi - iIii1I11I1II1
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
  I111iI = args . get ( 'stype' )
  o0oOoOO = args . get ( 'orderby' )
  oO00oOOoooO = int ( args . get ( 'page' ) )
  if 58 - 58: I1IiiI
  oOoO , Oo0O00O000 = self . TvingObj . GetProgramList ( I111iI , o0oOoOO , oO00oOOoooO , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  for o0OoOo00o0o in oOoO :
   i1i = o0OoOo00o0o . get ( 'title' )
   Oo0OO = o0OoOo00o0o . get ( 'thumbnail' )
   O0OooOo0o = o0OoOo00o0o . get ( 'synopsis' )
   I1II1I11I1I = O0OoOoo00o . get ( o0OoOo00o0o . get ( 'channel' ) )
   if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
   oOo0OOoO0 = o0OoOo00o0o . get ( 'info' )
   oOo0OOoO0 [ 'studio' ] = I1II1I11I1I
   oOo0OOoO0 [ 'plot' ] = '%s <%s>\n\n%s' % ( i1i , I1II1I11I1I , O0OooOo0o )
   if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
   o00oooO0Oo = { 'mode' : 'EPISODE'
 , 'programcode' : o0OoOo00o0o . get ( 'program' )
 , 'page' : '1'
 }
   if 83 - 83: II111iiii + I1Ii111
   self . add_dir ( i1i , sublabel = I1II1I11I1I , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = True , params = o00oooO0Oo )
   if 73 - 73: iII111i
  if Oo0O00O000 :
   if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % I11i
   o00oooO0Oo [ 'mode' ] = 'PROGRAM'
   o00oooO0Oo [ 'stype' ] = I111iI
   o00oooO0Oo [ 'orderby' ] = o0oOoOO
   o00oooO0Oo [ 'page' ] = str ( oO00oOOoooO + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   i1I1i111Ii = str ( oO00oOOoooO + 1 )
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if 41 - 41: IiII / O0
  if len ( oOoO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 51 - 51: I11i % I1IiiI
  if 60 - 60: I1IiiI / OOooOOo . I1IiiI / I1Ii111 . IiII
  if 92 - 92: OoOoOO00 + I1Ii111 * Ii1I % I1IiiI
  if 42 - 42: Oo0Ooo
 def dp_Episode_List ( self , args ) :
  if 76 - 76: I1IiiI * iII111i % I1Ii111
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 57 - 57: iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * OoooooooOO % II111iiii
  Oo00OO0o0o00 = args . get ( 'programcode' )
  oO00oOOoooO = int ( args . get ( 'page' ) )
  if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
  o0O , Oo0O00O000 , OOOooo = self . TvingObj . GetEpisodoList ( Oo00OO0o0o00 , oO00oOOoooO , orderby = self . get_winEpisodeOrderby ( ) )
  if 94 - 94: OoooooooOO + Oo0Ooo / OoOoOO00 * OOooOOo
  for o0OOo0o0O0O in o0O :
   i1i = o0OOo0o0O0O . get ( 'title' )
   i1I1i111Ii = o0OOo0o0O0O . get ( 'subtitle' )
   Oo0OO = o0OOo0o0O0O . get ( 'thumbnail' )
   O0OooOo0o = o0OOo0o0O0O . get ( 'synopsis' )
   if 65 - 65: i11iIiiIii
   oOo0OOoO0 = o0OOo0o0O0O . get ( 'info' )
   oOo0OOoO0 [ 'plot' ] = '%s\n\n%s' % ( i1i , O0OooOo0o )
   if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
   o00oooO0Oo = { 'mode' : 'VOD'
 , 'mediacode' : o0OOo0o0O0O . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : Oo00OO0o0o00
 , 'title' : i1i
 , 'thumbnail' : Oo0OO
 }
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = False , params = o00oooO0Oo )
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
   if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
   if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
   if 79 - 79: O0 * i11iIiiIii - IiII / IiII
   if 48 - 48: O0
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  if oO00oOOoooO == 1 :
   oOo0OOoO0 = { 'plot' : '정렬순서를 변경합니다.' }
   o00oooO0Oo = { }
   o00oooO0Oo [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    i1i = '정렬순서변경 : 최신화부터 -> 1회부터'
    o00oooO0Oo [ 'orderby' ] = 'asc'
   else :
    i1i = '정렬순서변경 : 1회부터 -> 최신화부터'
    o00oooO0Oo [ 'orderby' ] = 'desc'
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = oOo0OOoO0 , isFolder = False , params = o00oooO0Oo )
   if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
   if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  if Oo0O00O000 :
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
   o00oooO0Oo [ 'mode' ] = 'EPISODE'
   o00oooO0Oo [ 'programcode' ] = Oo00OO0o0o00
   o00oooO0Oo [ 'page' ] = str ( oO00oOOoooO + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   i1I1i111Ii = str ( oO00oOOoooO + 1 )
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   if 19 - 19: OoO0O00 - Oo0Ooo . O0
  if len ( o0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 60 - 60: II111iiii + Oo0Ooo
  if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
  if 49 - 49: II111iiii
  if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
 def dp_setEpOrderby ( self , args ) :
  o0oOoOO = args . get ( 'orderby' )
  if 81 - 81: iII111i + IiII
  self . set_winEpisodeOrderby ( o0oOoOO )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 98 - 98: I1IiiI
  if 95 - 95: ooOoO0o / ooOoO0o
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
 def dp_Movie_List ( self , args ) :
  if 41 - 41: i1IIi - I11i - Ii1I
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  o0oOoOO = args . get ( 'orderby' )
  oO00oOOoooO = int ( args . get ( 'page' ) )
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  iIIII , Oo0O00O000 = self . TvingObj . GetMovieList ( o0oOoOO , oO00oOOoooO , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
  for ii1iiIiIII1ii in iIIII :
   i1i = ii1iiIiIII1ii . get ( 'title' )
   Oo0OO = ii1iiIiIII1ii . get ( 'thumbnail' )
   O0OooOo0o = ii1iiIiIII1ii . get ( 'synopsis' )
   if 82 - 82: iII111i
   oOo0OOoO0 = ii1iiIiIII1ii . get ( 'info' )
   oOo0OOoO0 [ 'plot' ] = '%s\n\n%s' % ( i1i , O0OooOo0o )
   if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
   o00oooO0Oo = { 'mode' : 'MOVIE'
 , 'mediacode' : ii1iiIiIII1ii . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : Oo0OO
 }
   if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
   self . add_dir ( i1i , sublabel = '' , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = False , params = o00oooO0Oo )
   if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  if Oo0O00O000 :
   if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
   o00oooO0Oo [ 'mode' ] = 'MOVIE_GROUP'
   o00oooO0Oo [ 'orderby' ] = o0oOoOO
   o00oooO0Oo [ 'page' ] = str ( oO00oOOoooO + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   i1I1i111Ii = str ( oO00oOOoooO + 1 )
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if 71 - 71: O0 - iIii1I11I1II1
  if len ( iIIII ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  if 42 - 42: Oo0Ooo
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  if 46 - 46: Oo0Ooo
 def dp_Search_Group ( self , args ) :
  for O0OOOOo0O in O0o0o00o0Oo0 :
   i1i = O0OOOOo0O . get ( 'title' )
   if 1 - 1: iII111i
   o00oooO0Oo = { 'mode' : O0OOOOo0O . get ( 'mode' )
 , 'stype' : O0OOOOo0O . get ( 'stype' )
 , 'page' : '1'
 }
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
  if len ( O0o0o00o0Oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
  if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
  if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
 def dp_Search_List ( self , args ) :
  if 17 - 17: i1IIi
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 21 - 21: Oo0Ooo
  I1ii1 = __addon__ . getSetting ( 'id' )
  oO00oOOoooO = int ( args . get ( 'page' ) )
  I111iI = args . get ( 'stype' )
  if 99 - 99: ooOoO0o . I1Ii111 % IiII * IiII . i1IIi
  if 'search_key' in args :
   O0OOoOOO0oO = args . get ( 'search_key' )
  else :
   O0OOoOOO0oO = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not O0OOoOOO0oO : return
   if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
  ooo0OOO , Oo0O00O000 = self . TvingObj . GetSearchList ( O0OOoOOO0oO , I1ii1 , oO00oOOoooO , I111iI , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if len ( ooo0OOO ) == 0 : return
  if 49 - 49: i11iIiiIii % Ii1I . OoOoOO00
  for Ii1i1iI in ooo0OOO :
   i1i = Ii1i1iI . get ( 'title' )
   Oo0OO = Ii1i1iI . get ( 'thumbnail' )
   O0OooOo0o = Ii1i1iI . get ( 'synopsis' )
   IIiI1 = Ii1i1iI . get ( 'program' )
   if 17 - 17: OOooOOo / OOooOOo / I11i
   oOo0OOoO0 = Ii1i1iI . get ( 'info' )
   oOo0OOoO0 [ 'plot' ] = '%s\n\n%s' % ( i1i , O0OooOo0o )
   if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
   if I111iI == 'vod' :
    o00oooO0Oo = { 'mode' : 'EPISODE'
 , 'programcode' : Ii1i1iI . get ( 'program' )
 , 'page' : '1'
 }
    OOooOoooOoOo = True
   else :
    o00oooO0Oo = { 'mode' : 'MOVIE'
 , 'mediacode' : Ii1i1iI . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : Oo0OO
 }
    OOooOoooOoOo = False
    if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
   self . add_dir ( i1i , sublabel = '' , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = OOooOoooOoOo , params = o00oooO0Oo )
   if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
  if Oo0O00O000 :
   if 9 - 9: Ii1I
   o00oooO0Oo [ 'mode' ] = 'SEARCH'
   o00oooO0Oo [ 'search_key' ] = O0OOoOOO0oO
   o00oooO0Oo [ 'page' ] = str ( oO00oOOoooO + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   i1I1i111Ii = str ( oO00oOOoooO + 1 )
   self . add_dir ( i1i , sublabel = i1I1i111Ii , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if 59 - 59: I1IiiI * II111iiii . O0
  if len ( ooo0OOO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
  if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
  if 27 - 27: O0
 def Delete_Watched_List ( self , stype ) :
  try :
   OOO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( OOO0oOOoo , 'w' ) as oOOO00o000o :
    oOOO00o000o . write ( '' )
  except :
   None
   if 9 - 9: oO0o + I11i / I11i
   if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
   if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
   if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
 def dp_WatchList_Delete ( self , args ) :
  I111iI = args . get ( 'stype' )
  if 51 - 51: IiII
  O00oooo0O = xbmcgui . Dialog ( )
  I1I1I = O00oooo0O . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I1I1I == False : sys . exit ( )
  if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
  self . Delete_Watched_List ( I111iI )
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
  xbmc . executebuiltin ( "Container.Refresh" )
  if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 def Load_Watched_List ( self , stype ) :
  try :
   OOO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( OOO0oOOoo , 'r' ) as oOOO00o000o :
    O0ooo0 = oOOO00o000o . readlines ( )
  except :
   O0ooo0 = [ ]
   if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  return O0ooo0
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  if 31 - 31: OoooooooOO . OOooOOo
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   OOO0oOOoo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   oO0oO0 = self . Load_Watched_List ( stype )
   if 14 - 14: iII111i
   with open ( OOO0oOOoo , 'w' ) as oOOO00o000o :
    oOOOOo0oo0O = urllib . urlencode ( in_params )
    oOOOOo0oo0O = oOOOOo0oo0O . encode ( 'utf-8' ) + '\n'
    oOOO00o000o . write ( oOOOOo0oo0O )
    if 13 - 13: I1IiiI % OoOoOO00 . I1ii11iIi11i / Oo0Ooo % OOooOOo . OoooooooOO
    i1iIi = 0
    for iiiii1II in oO0oO0 :
     O0OOO0OOooo00 = dict ( urlparse . parse_qsl ( iiiii1II ) )
     if 6 - 6: Ii1I - ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
     II11iI111i1 = in_params . get ( 'code' )
     Oo00OoOo = O0OOO0OOooo00 . get ( 'code' )
     if stype == 'vod' and self . get_settings_direct_replay ( ) == True :
      II11iI111i1 = in_params . get ( 'videoid' )
      Oo00OoOo = O0OOO0OOooo00 . get ( 'videoid' ) if Oo00OoOo != None else '-'
      if 24 - 24: i11iIiiIii - I1Ii111
      if 21 - 21: I11i
     if II11iI111i1 != Oo00OoOo :
      oOOO00o000o . write ( iiiii1II )
      i1iIi += 1
      if i1iIi >= 50 : break
  except :
   None
   if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
   if 11 - 11: OoooooooOO . I1Ii111
   if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
   if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
 def dp_Watch_List ( self , args ) :
  I111iI = args . get ( 'stype' )
  IiII1I11i1I1I = self . get_settings_direct_replay ( )
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * IiII
  if I111iI == '-' :
   for O0OOOOo0O in OOooo0000ooo :
    i1i = O0OOOOo0O . get ( 'title' )
    if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
    o00oooO0Oo = { 'mode' : O0OOOOo0O . get ( 'mode' )
 , 'stype' : O0OOOOo0O . get ( 'stype' )
 }
    if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
    self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = o00oooO0Oo )
   if len ( OOooo0000ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 69 - 69: O0
  else :
   o0ooO = self . Load_Watched_List ( I111iI )
   if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
   for Iii in o0ooO :
    I1iiiiI1iI = dict ( urlparse . parse_qsl ( Iii ) )
    if 43 - 43: oO0o - OoooooooOO
    i1i = I1iiiiI1iI . get ( 'title' )
    Oo0OO = I1iiiiI1iI . get ( 'img' )
    ii1iI = I1iiiiI1iI . get ( 'videoid' )
    if 49 - 49: o0oOOo0O0Ooo . IiII / OoO0O00 + II111iiii
    oOo0OOoO0 = { }
    oOo0OOoO0 [ 'plot' ] = i1i
    if 47 - 47: O0 / Ii1I
    if I111iI == 'vod' :
     if IiII1I11i1I1I == False or ii1iI == None :
      o00oooO0Oo = { 'mode' : 'EPISODE'
 , 'programcode' : I1iiiiI1iI . get ( 'code' )
 , 'page' : '1'
 }
      OOooOoooOoOo = True
     else :
      o00oooO0Oo = { 'mode' : 'VOD'
 , 'mediacode' : ii1iI
 , 'stype' : 'vod'
 , 'programcode' : I1iiiiI1iI . get ( 'code' )
 , 'title' : i1i
 , 'thumbnail' : Oo0OO
 }
      OOooOoooOoOo = False
    else :
     o00oooO0Oo = { 'mode' : 'MOVIE'
 , 'mediacode' : I1iiiiI1iI . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : Oo0OO
 }
     OOooOoooOoOo = False
     if 67 - 67: I1IiiI
    self . add_dir ( i1i , sublabel = '' , img = Oo0OO , infoLabels = oOo0OOoO0 , isFolder = OOooOoooOoOo , params = o00oooO0Oo )
    if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
   oOo0OOoO0 = { 'plot' : '시청목록을 삭제합니다.' }
   i1i = '*** 시청목록 삭제 ***'
   o00oooO0Oo = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : I111iI
 }
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = oOo0OOoO0 , isFolder = False , params = o00oooO0Oo )
   if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
   if 92 - 92: Oo0Ooo
   if 40 - 40: OoOoOO00 / IiII
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
   if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
 def play_VIDEO ( self , args ) :
  if 61 - 61: II111iiii
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
  oooO0o0o0O0 = args . get ( 'mediacode' )
  I111iI = args . get ( 'stype' )
  iii11111I = self . get_selQuality ( I111iI )
  if 16 - 16: iIii1I11I1II1 - IiII
  o00o , Ii1IIiiIIi = self . TvingObj . GetBroadURL ( oooO0o0o0O0 , iii11111I , I111iI )
  if 88 - 88: OoooooooOO + I11i * II111iiii % Oo0Ooo
  self . addon_log ( 'qt, stype, url : %s - %s - %s' % ( str ( iii11111I ) , I111iI , o00o ) )
  if 17 - 17: IiII * OOooOOo - OoO0O00 / i11iIiiIii
  if o00o == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 79 - 79: I1Ii111 . oO0o - II111iiii . I1IiiI % ooOoO0o
   if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
   if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
  Ooo0O = o00o . find ( 'Policy=' )
  if Ooo0O != - 1 :
   o0oo0000OO = o00o . split ( '?' ) [ 0 ]
   if 69 - 69: ooOoO0o - OoO0O00 / i11iIiiIii + I1ii11iIi11i % OoooooooOO
   o000O000 = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( o00o ) . query ) )
   o000O000 = urllib . urlencode ( o000O000 )
   o000O000 = o000O000 . replace ( '&' , ';' )
   o000O000 = o000O000 . replace ( 'Policy' , 'CloudFront-Policy' )
   o000O000 = o000O000 . replace ( 'Signature' , 'CloudFront-Signature' )
   o000O000 = o000O000 . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
   if 19 - 19: iIii1I11I1II1
   Ii1IiI1i1ii = '%s|Cookie=%s' % ( o0oo0000OO , o000O000 )
  else :
   Ii1IiI1i1ii = o00o
   if 30 - 30: IiII + I1Ii111 - IiII . IiII - II111iiii + O0
   if 86 - 86: i1IIi
  self . addon_log ( Ii1IiI1i1ii , False )
  if 41 - 41: OoOoOO00 * I11i / OoOoOO00 % oO0o
  if 18 - 18: II111iiii . OoooooooOO % OoOoOO00 % Ii1I
  if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  if 2 - 2: OoooooooOO % OOooOOo
  oOoOOo0oo0 = xbmcgui . ListItem ( path = Ii1IiI1i1ii )
  if 60 - 60: ooOoO0o * I1Ii111 + Oo0Ooo
  if 19 - 19: OoO0O00 * I11i / I11i . OoooooooOO - OOooOOo + i11iIiiIii
  if Ii1IIiiIIi != '' :
   oo0OOo0O = Ii1IIiiIIi
   Ii1IiII = 'https://cj.drmkeyserver.com/widevine_license'
   if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
   iIi1i = 'mpd'
   i1ii = 'com.widevine.alpha'
   if 68 - 68: OOooOOo * O0 . I11i - II111iiii . ooOoO0o / II111iiii
   iii1 = inputstreamhelper . Helper ( iIi1i , drm = i1ii )
   if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
   if iii1 . check_inputstream ( ) :
    if 88 - 88: iII111i
    iiI11I1i1i1iI = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % oooO0o0o0O0
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
    , 'user-agent' : OoOooOOOO
 , 'AcquireLicenseAssertion' : oo0OOo0O
 , 'Host' : 'cj.drmkeyserver.com'
 }
    OoOOo000o0 = Ii1IiII + '|' + urllib . urlencode ( iiI11I1i1i1iI ) + '|R{SSM}|'
    if 12 - 12: II111iiii . I11i / OOooOOo
    oOoOOo0oo0 . setProperty ( 'inputstreamaddon' , iii1 . inputstream_addon )
    if 77 - 77: ooOoO0o - I1IiiI % I11i - O0
    oOoOOo0oo0 . setProperty ( 'inputstream.adaptive.manifest_type' , iIi1i )
    oOoOOo0oo0 . setProperty ( 'inputstream.adaptive.license_type' , i1ii )
    if 67 - 67: OOooOOo + Oo0Ooo
    oOoOOo0oo0 . setProperty ( 'inputstream.adaptive.license_key' , OoOOo000o0 )
    if 84 - 84: O0 * OoooooooOO - IiII * IiII
    if 8 - 8: ooOoO0o / i1IIi . oO0o
    if 41 - 41: iII111i + OoO0O00
    if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
    if 56 - 56: O0
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , oOoOOo0oo0 )
  if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
    o00oooO0Oo = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'videoid' : args . get ( 'mediacode' )
    }
    self . Save_Watched_List ( args . get ( 'stype' ) , o00oooO0Oo )
  except :
   None
   if 23 - 23: oO0o - OOooOOo + I11i
   if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
   if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
   if 11 - 11: iII111i * Ii1I - OoOoOO00
   if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
 def logout ( self ) :
  O00oooo0O = xbmcgui . Dialog ( )
  I1I1I = O00oooo0O . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if I1I1I == False : sys . exit ( )
  if 74 - 74: Oo0Ooo
  self . wininfo_clear ( )
  if 61 - 61: Oo0Ooo - I1Ii111 * II111iiii % ooOoO0o * iIii1I11I1II1 + OoO0O00
  if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
  if os . path . isfile ( i11iiII ) : os . remove ( i11iiII )
  if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
  if 68 - 68: OoooooooOO % II111iiii
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
  if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
 def wininfo_clear ( self ) :
  if 2 - 2: Ii1I - IiII
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_TOKEN' , '' )
  iII . setProperty ( 'TVING_M_USERINFO' , '' )
  iII . setProperty ( 'TVING_M_UUID' , '' )
  iII . setProperty ( 'TVING_M_LOGINTIME' , '' )
  if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  if 71 - 71: OoooooooOO
  if 33 - 33: I1Ii111
 def cookiefile_save ( self ) :
  OOO0ooo = datetime . datetime . now ( )
  IIiiii = OOO0ooo + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 37 - 37: o0oOOo0O0Ooo % ooOoO0o
  iII = xbmcgui . Window ( 10000 )
  O0II11i11II = { 'tving_token' : iII . getProperty ( 'TVING_M_TOKEN' )
 , 'tving_userinfo' : iII . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : iII . getProperty ( 'TVING_M_UUID' )
 , 'tving_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'tving_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'tving_logintype' : __addon__ . getSetting ( 'login_type' )
 , 'tving_limitdate' : IIiiii . strftime ( '%Y-%m-%d' )
 }
  if 29 - 29: Oo0Ooo % OoO0O00 % IiII . o0oOOo0O0Ooo / OoooooooOO * ooOoO0o
  try :
   with open ( i11iiII , 'w' ) as oOOO00o000o :
    json . dump ( O0II11i11II , oOOO00o000o )
  except Exception as o0OoO000O :
   print ( o0OoO000O )
   if 94 - 94: OoOoOO00 . O0 / Ii1I . I1ii11iIi11i - i1IIi
   if 26 - 26: OoO0O00 - OOooOOo . o0oOOo0O0Ooo
   if 65 - 65: I1ii11iIi11i % O0 % iIii1I11I1II1 * Ii1I
   if 31 - 31: Ii1I
 def cookiefile_check ( self ) :
  if 44 - 44: OoOoOO00 - iIii1I11I1II1 - Oo0Ooo
  if 80 - 80: iIii1I11I1II1 * I1Ii111 % I11i % Oo0Ooo
  O0II11i11II = { }
  try :
   with open ( i11iiII , 'r' ) as oOOO00o000o :
    O0II11i11II = json . load ( oOOO00o000o )
  except Exception as o0OoO000O :
   self . wininfo_clear ( )
   return False
   if 95 - 95: iIii1I11I1II1 - I1ii11iIi11i . I1Ii111 - I1IiiI
   if 75 - 75: OoO0O00 + o0oOOo0O0Ooo - i1IIi . OoooooooOO * Ii1I / IiII
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  ooO00OO0 = __addon__ . getSetting ( 'id' )
  i11111IIIII = __addon__ . getSetting ( 'pw' )
  IiIIiIIIiIii = __addon__ . getSetting ( 'login_type' )
  O0II11i11II [ 'tving_id' ] = base64 . standard_b64decode ( O0II11i11II [ 'tving_id' ] ) . decode ( 'utf-8' )
  O0II11i11II [ 'tving_pw' ] = base64 . standard_b64decode ( O0II11i11II [ 'tving_pw' ] ) . decode ( 'utf-8' )
  if ooO00OO0 != O0II11i11II [ 'tving_id' ] or i11111IIIII != O0II11i11II [ 'tving_pw' ] or IiIIiIIIiIii != O0II11i11II [ 'tving_logintype' ] :
   self . wininfo_clear ( )
   return False
   if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
   if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
  i1Ii1Ii = datetime . datetime . now ( ) . date ( )
  iiIII1II = O0II11i11II [ 'tving_limitdate' ]
  try :
   oOO = datetime . datetime . strptime ( iiIII1II , '%Y-%m-%d' ) . date ( )
  except TypeError :
   oOO = datetime . datetime ( * ( time . strptime ( iiIII1II , '%Y-%m-%d' ) [ 0 : 6 ] ) ) . date ( )
   if 100 - 100: Oo0Ooo % Ii1I / I11i
  if oOO < i1Ii1Ii :
   self . wininfo_clear ( )
   return False
   if 30 - 30: Oo0Ooo - OOooOOo - iII111i
   if 81 - 81: o0oOOo0O0Ooo . OoooooooOO + OOooOOo * ooOoO0o
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_TOKEN' , O0II11i11II [ 'tving_token' ] )
  iII . setProperty ( 'TVING_M_USERINFO' , O0II11i11II [ 'tving_userinfo' ] )
  iII . setProperty ( 'TVING_M_UUID' , O0II11i11II [ 'tving_uuid' ] )
  iII . setProperty ( 'TVING_M_LOGINTIME' , iiIII1II )
  if 74 - 74: i1IIi + O0 + Oo0Ooo
  return True
  if 5 - 5: Oo0Ooo * OoOoOO00
  if 46 - 46: ooOoO0o
  if 33 - 33: iII111i - II111iiii * OoooooooOO - Oo0Ooo - OOooOOo
  if 84 - 84: I1Ii111 + Oo0Ooo - OoOoOO00 * OoOoOO00
 def tving_main ( self ) :
  Ooo = self . main_params . get ( 'mode' , None )
  if 65 - 65: Oo0Ooo / I11i
  self . login_main ( )
  if 12 - 12: I11i % OoOoOO00
  if Ooo is None :
   self . dp_Main_List ( )
   if 48 - 48: iII111i . i11iIiiIii
  elif Ooo in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
   self . dp_Title_Group ( self . main_params )
   if 5 - 5: oO0o . I1ii11iIi11i . II111iiii . OoooooooOO
  elif Ooo == 'CHANNEL' :
   self . dp_LiveChannel_List ( self . main_params )
   if 96 - 96: i11iIiiIii - OOooOOo % O0 / OoO0O00
  elif Ooo in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 100 - 100: iII111i / Ii1I - OoooooooOO % II111iiii - I1IiiI % OoOoOO00
   time . sleep ( 0.1 )
   if 60 - 60: iIii1I11I1II1 + i1IIi
  elif Ooo == 'PROGRAM' :
   self . dp_Program_List ( self . main_params )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
  elif Ooo == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 51 - 51: OoOoOO00
  elif Ooo == 'MOVIE_GROUP' :
   self . dp_Movie_List ( self . main_params )
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
  elif Ooo == 'SEARCH_GROUP' :
   self . dp_Search_Group ( self . main_params )
   if 53 - 53: Ii1I % Oo0Ooo
  elif Ooo == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
  elif Ooo == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 41 - 41: Ii1I % I1ii11iIi11i
  elif Ooo == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 12 - 12: OOooOOo
  elif Ooo == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 69 - 69: OoooooooOO + OOooOOo
  elif Ooo == 'LOGOUT' :
   self . logout ( )
   if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
   if 31 - 31: I11i % OOooOOo * I11i
   if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
   if 1 - 1: iIii1I11I1II1
   if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
   if 99 - 99: I11i - I1Ii111 - oO0o % OoO0O00
  else :
   None
   if 21 - 21: II111iiii % I1ii11iIi11i . i1IIi - OoooooooOO
   if 4 - 4: OoooooooOO . ooOoO0o
   if 78 - 78: I1ii11iIi11i + I11i - O0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
