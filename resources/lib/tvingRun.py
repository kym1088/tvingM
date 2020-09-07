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
   Ii = [ 1080 , 720 , 480 , 360 ]
   if 61 - 61: II111iiii
   O0OOO = int ( __addon__ . getSetting ( OO0OoO0o00 ) )
   return Ii [ O0OOO ]
  except :
   None
   if 10 - 10: OOooOOo * I11i % OoOoOO00 / I1IiiI / OoOoOO00
  return 720
  if 42 - 42: OoO0O00
  if 67 - 67: I1Ii111 . iII111i . O0
  if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 def dp_Main_List ( self ) :
  if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
  for I1111IIi in Oo0oO0ooo :
   i1i = I1111IIi . get ( 'title' )
   if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
   I1 = { 'mode' : I1111IIi . get ( 'mode' )
 , 'stype' : I1111IIi . get ( 'stype' )
 , 'orderby' : I1111IIi . get ( 'orderby' )
 , 'ordernm' : I1111IIi . get ( 'ordernm' )
 , 'page' : '1'
 }
   if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
   if I1111IIi . get ( 'mode' ) == 'XXX' :
    I1 [ 'mode' ] = 'XXX'
    iI1 = False
   else :
    iI1 = True
    if 28 - 28: OoO0O00 + Ii1I / OoO0O00 . II111iiii
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = iI1 , params = I1 )
  if len ( Oo0oO0ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  if 31 - 31: II111iiii . I1IiiI
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
  if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
  if 92 - 92: iII111i
 def login_main ( self ) :
  ( IIiIiiIi , O000oo , IIi1I11I1II ) = self . get_settings_login_info ( )
  if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
  if 84 - 84: IiII
  if not ( IIiIiiIi and O000oo ) :
   O00oooo0O = xbmcgui . Dialog ( )
   OOO00O0O = O00oooo0O . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if OOO00O0O == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 33 - 33: O0 . IiII . I1IiiI
    if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
    if 29 - 29: I1ii11iIi11i + oO0o % O0
  if self . get_winEpisodeOrderby ( ) == '' :
   self . set_winEpisodeOrderby ( 'desc' )
   if 10 - 10: I11i / I1Ii111 - I1IiiI * iIii1I11I1II1 - I1IiiI
   if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % iII111i
  if self . cookiefile_check ( ) : return
  if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
  if 23 - 23: O0
  if 85 - 85: Ii1I
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
  if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
  if 84 - 84: ooOoO0o * II111iiii + Oo0Ooo
  if 53 - 53: iII111i % II111iiii . IiII - iIii1I11I1II1 - IiII * II111iiii
  if 77 - 77: iIii1I11I1II1 * OoO0O00
  if 95 - 95: I1IiiI + i11iIiiIii
  if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
  if 80 - 80: II111iiii
  O0O = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  i1I1I = xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' )
  if i1I1I == None or i1I1I == '' : i1I1I = int ( '19000101' )
  if 12 - 12: i11iIiiIii / OoO0O00
  if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
  if 25 - 25: OoO0O00
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
   oOo0oO = 0
   while True :
    oOo0oO += 1
    if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
    time . sleep ( 0.05 )
    if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
    if i1I1I >= O0O : return
    if oOo0oO > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
   if 82 - 82: Ii1I
  if i1I1I >= O0O :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   return
   if 46 - 46: OoooooooOO . i11iIiiIii
   if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if not self . TvingObj . GetCredential ( IIiIiiIi , O000oo , IIi1I11I1II ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 87 - 87: Oo0Ooo . IiII
   if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
  self . set_winCredential ( self . TvingObj . LoadCredential ( ) )
  self . cookiefile_save ( )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  if 55 - 55: OOooOOo . I1IiiI
  if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
  if 100 - 100: I1Ii111 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
 def dp_Title_Group ( self , args ) :
  IIIIii1I = args . get ( 'stype' )
  if IIIIii1I == 'live' :
   IiI1i = o00oOoo
  else :
   IiI1i = IiII1I1i1i1ii
   if 92 - 92: IiII . IiII + OoO0O00
  for IiIiI1111I1I in IiI1i :
   i1i = IiIiI1111I1I . get ( 'title' )
   if 13 - 13: Ii1I . i11iIiiIii
   if args . get ( 'ordernm' ) != '-' :
    i1i += '  (' + args . get ( 'ordernm' ) + ')'
    if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   I1 = { 'mode' : IiIiI1111I1I . get ( 'mode' )
 , 'stype' : IiIiI1111I1I . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
  if len ( IiI1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 def dp_LiveChannel_List ( self , args ) :
  if 63 - 63: OoOoOO00 * iII111i
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 69 - 69: O0 . OoO0O00
  IIIIii1I = args . get ( 'stype' )
  ii1111iII = int ( args . get ( 'page' ) )
  iiiiI , oooOo0OOOoo0 = self . TvingObj . GetLiveChannelList ( IIIIii1I , ii1111iII )
  if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
  for OOOoOo in iiiiI :
   i1i = OOOoOo . get ( 'title' )
   O00o0 = OOOoOo . get ( 'channel' )
   I11iII = OOOoOo . get ( 'thumbnail' )
   iIIII = OOOoOo . get ( 'synopsis' )
   I11 = OOOoOo . get ( 'channelepg' )
   if 30 - 30: o0oOOo0O0Ooo % II111iiii % iII111i
   II111iI111I1I = OOOoOo . get ( 'info' )
   II111iI111I1I [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( O00o0 , i1i , I11 , iIIII )
   if 18 - 18: iII111i - OOooOOo . I1Ii111 . iIii1I11I1II1
   I1 = { 'mode' : 'LIVE'
 , 'mediacode' : OOOoOo . get ( 'mediacode' )
 , 'stype' : IIIIii1I
   }
   if 2 - 2: OOooOOo . OoO0O00
   self . add_dir ( O00o0 , sublabel = i1i , img = I11iII , infoLabels = II111iI111I1I , isFolder = False , params = I1 )
   if 78 - 78: I11i * iIii1I11I1II1 . I1IiiI / o0oOOo0O0Ooo - OoooooooOO / I1Ii111
  if oooOo0OOOoo0 :
   if 35 - 35: I11i % OOooOOo - oO0o
   I1 [ 'mode' ] = 'CHANNEL'
   I1 [ 'stype' ] = IIIIii1I
   I1 [ 'page' ] = str ( ii1111iII + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   ii1iii1i = str ( ii1111iII + 1 )
   self . add_dir ( i1i , sublabel = ii1iii1i , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  if len ( iiiiI ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
  if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
  if 72 - 72: Ii1I
  if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
 def dp_Program_List ( self , args ) :
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
  IIIIii1I = args . get ( 'stype' )
  I1II1 = args . get ( 'orderby' )
  ii1111iII = int ( args . get ( 'page' ) )
  if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
  II1i111Ii1i , oooOo0OOOoo0 = self . TvingObj . GetProgramList ( IIIIii1I , I1II1 , ii1111iII , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 15 - 15: II111iiii / i1IIi
  for O0oO0 in II1i111Ii1i :
   i1i = O0oO0 . get ( 'title' )
   I11iII = O0oO0 . get ( 'thumbnail' )
   iIIII = O0oO0 . get ( 'synopsis' )
   iII11 = O0OoOoo00o . get ( O0oO0 . get ( 'channel' ) )
   if 32 - 32: I1Ii111
   II111iI111I1I = O0oO0 . get ( 'info' )
   II111iI111I1I [ 'studio' ] = iII11
   II111iI111I1I [ 'plot' ] = '%s <%s>\n\n%s' % ( i1i , iII11 , iIIII )
   if 30 - 30: iIii1I11I1II1 / I11i . OoO0O00 - o0oOOo0O0Ooo
   I1 = { 'mode' : 'EPISODE'
 , 'programcode' : O0oO0 . get ( 'program' )
 , 'page' : '1'
 }
   if 48 - 48: i1IIi - Ii1I / O0 * OoO0O00
   self . add_dir ( i1i , sublabel = iII11 , img = I11iII , infoLabels = II111iI111I1I , isFolder = True , params = I1 )
   if 71 - 71: I1ii11iIi11i
  if oooOo0OOOoo0 :
   if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
   I1 [ 'mode' ] = 'PROGRAM'
   I1 [ 'stype' ] = IIIIii1I
   I1 [ 'orderby' ] = I1II1
   I1 [ 'page' ] = str ( ii1111iII + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   ii1iii1i = str ( ii1111iII + 1 )
   self . add_dir ( i1i , sublabel = ii1iii1i , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 59 - 59: o0oOOo0O0Ooo
  if len ( II1i111Ii1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 def dp_Episode_List ( self , args ) :
  if 23 - 23: i11iIiiIii
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  o0ooooO0o0O = args . get ( 'programcode' )
  ii1111iII = int ( args . get ( 'page' ) )
  if 24 - 24: O0 * o0oOOo0O0Ooo
  IiI1iiiIii , oooOo0OOOoo0 , I1III1111iIi = self . TvingObj . GetEpisodoList ( o0ooooO0o0O , ii1111iII , orderby = self . get_winEpisodeOrderby ( ) )
  if 38 - 38: iII111i + I11i / I1Ii111 % ooOoO0o - I1ii11iIi11i
  for iI11 in IiI1iiiIii :
   i1i = iI11 . get ( 'title' )
   ii1iii1i = iI11 . get ( 'subtitle' )
   I11iII = iI11 . get ( 'thumbnail' )
   iIIII = iI11 . get ( 'synopsis' )
   if 10 - 10: II111iiii / oO0o % OoooooooOO * I11i % I1ii11iIi11i
   II111iI111I1I = iI11 . get ( 'info' )
   II111iI111I1I [ 'plot' ] = '%s\n\n%s' % ( i1i , iIIII )
   if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
   I1 = { 'mode' : 'VOD'
 , 'mediacode' : iI11 . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : o0ooooO0o0O
 , 'title' : i1i
 , 'thumbnail' : I11iII
 }
   if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   self . add_dir ( i1i , sublabel = ii1iii1i , img = I11iII , infoLabels = II111iI111I1I , isFolder = False , params = I1 )
   if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
   if 42 - 42: I1IiiI
   if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
   if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
   if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  if ii1111iII == 1 :
   II111iI111I1I = { 'plot' : '정렬순서를 변경합니다.' }
   I1 = { }
   I1 [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    i1i = '정렬순서변경 : 최신화부터 -> 1회부터'
    I1 [ 'orderby' ] = 'asc'
   else :
    i1i = '정렬순서변경 : 1회부터 -> 최신화부터'
    I1 [ 'orderby' ] = 'desc'
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = II111iI111I1I , isFolder = False , params = I1 )
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
   if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  if oooOo0OOOoo0 :
   if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
   I1 [ 'mode' ] = 'EPISODE'
   I1 [ 'programcode' ] = o0ooooO0o0O
   I1 [ 'page' ] = str ( ii1111iII + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   ii1iii1i = str ( ii1111iII + 1 )
   self . add_dir ( i1i , sublabel = ii1iii1i , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 79 - 79: O0 * i11iIiiIii - IiII / IiII
   if 48 - 48: O0
  if len ( IiI1iiiIii ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
 def dp_setEpOrderby ( self , args ) :
  I1II1 = args . get ( 'orderby' )
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  self . set_winEpisodeOrderby ( I1II1 )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
  if 60 - 60: II111iiii + Oo0Ooo
  if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
  if 49 - 49: II111iiii
 def dp_Movie_List ( self , args ) :
  if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 81 - 81: iII111i + IiII
  I1II1 = args . get ( 'orderby' )
  ii1111iII = int ( args . get ( 'page' ) )
  if 98 - 98: I1IiiI
  o00o0 , oooOo0OOOoo0 = self . TvingObj . GetMovieList ( I1II1 , ii1111iII , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  for O0O0Oo00 in o00o0 :
   i1i = O0O0Oo00 . get ( 'title' )
   I11iII = O0O0Oo00 . get ( 'thumbnail' )
   iIIII = O0O0Oo00 . get ( 'synopsis' )
   if 80 - 80: oO0o + OOooOOo / I11i
   II111iI111I1I = O0O0Oo00 . get ( 'info' )
   II111iI111I1I [ 'plot' ] = '%s\n\n%s' % ( i1i , iIIII )
   if 79 - 79: ooOoO0o
   I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : O0O0Oo00 . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : I11iII
 }
   if 48 - 48: I1Ii111 - o0oOOo0O0Ooo % Ii1I
   self . add_dir ( i1i , sublabel = '' , img = I11iII , infoLabels = II111iI111I1I , isFolder = False , params = I1 )
   if 36 - 36: oO0o - Ii1I . Oo0Ooo - i11iIiiIii - OOooOOo * Oo0Ooo
  if oooOo0OOOoo0 :
   if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
   I1 [ 'mode' ] = 'MOVIE_GROUP'
   I1 [ 'orderby' ] = I1II1
   I1 [ 'page' ] = str ( ii1111iII + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   ii1iii1i = str ( ii1111iII + 1 )
   self . add_dir ( i1i , sublabel = ii1iii1i , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 51 - 51: iIii1I11I1II1 . ooOoO0o + iIii1I11I1II1
  if len ( o00o0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 95 - 95: I1IiiI
  if 46 - 46: OoOoOO00 + OoO0O00
  if 70 - 70: iII111i / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
 def dp_Search_Group ( self , args ) :
  for IiIiI1111I1I in O0o0o00o0Oo0 :
   i1i = IiIiI1111I1I . get ( 'title' )
   if 96 - 96: OoooooooOO + oO0o
   I1 = { 'mode' : IiIiI1111I1I . get ( 'mode' )
 , 'stype' : IiIiI1111I1I . get ( 'stype' )
 , 'page' : '1'
 }
   if 44 - 44: oO0o
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
  if len ( O0o0o00o0Oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
  if 88 - 88: OoOoOO00 / II111iiii
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
  if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
 def dp_Search_List ( self , args ) :
  if 42 - 42: Oo0Ooo
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  iii11I = __addon__ . getSetting ( 'id' )
  ii1111iII = int ( args . get ( 'page' ) )
  IIIIii1I = args . get ( 'stype' )
  if 50 - 50: iII111i + O0 + Ii1I . II111iiii / o0oOOo0O0Ooo
  if 'search_key' in args :
   i1Iii11I1i = args . get ( 'search_key' )
  else :
   i1Iii11I1i = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not i1Iii11I1i : return
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  I11i1II , oooOo0OOOoo0 = self . TvingObj . GetSearchList ( i1Iii11I1i , iii11I , ii1111iII , IIIIii1I , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if len ( I11i1II ) == 0 : return
  if 72 - 72: iIii1I11I1II1 . i1IIi / Oo0Ooo . II111iiii
  for ooo000o000 in I11i1II :
   i1i = ooo000o000 . get ( 'title' )
   I11iII = ooo000o000 . get ( 'thumbnail' )
   iIIII = ooo000o000 . get ( 'synopsis' )
   O0o = ooo000o000 . get ( 'program' )
   if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + IiII
   II111iI111I1I = ooo000o000 . get ( 'info' )
   II111iI111I1I [ 'plot' ] = '%s\n\n%s' % ( i1i , iIIII )
   if 10 - 10: I1Ii111 / ooOoO0o + i11iIiiIii / Ii1I
   if IIIIii1I == 'vod' :
    I1 = { 'mode' : 'EPISODE'
 , 'programcode' : ooo000o000 . get ( 'program' )
 , 'page' : '1'
 }
    iI1 = True
   else :
    I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : ooo000o000 . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : I11iII
 }
    iI1 = False
    if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
   self . add_dir ( i1i , sublabel = '' , img = I11iII , infoLabels = II111iI111I1I , isFolder = iI1 , params = I1 )
   if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if oooOo0OOOoo0 :
   if 5 - 5: Ii1I
   I1 [ 'mode' ] = 'SEARCH'
   I1 [ 'search_key' ] = i1Iii11I1i
   I1 [ 'page' ] = str ( ii1111iII + 1 )
   i1i = '[B]%s >>[/B]' % '다음 페이지'
   ii1iii1i = str ( ii1111iII + 1 )
   self . add_dir ( i1i , sublabel = ii1iii1i , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 46 - 46: IiII
  if len ( I11i1II ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 45 - 45: ooOoO0o
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
 def Delete_Watched_List ( self , stype ) :
  try :
   OooO0oo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( OooO0oo , 'w' ) as o0o0oOoOO0O :
    o0o0oOoOO0O . write ( '' )
  except :
   None
   if 16 - 16: IiII % iIii1I11I1II1 . Ii1I
   if 59 - 59: I1IiiI * II111iiii . O0
   if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
 def dp_WatchList_Delete ( self , args ) :
  IIIIii1I = args . get ( 'stype' )
  if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
  O00oooo0O = xbmcgui . Dialog ( )
  OOO00O0O = O00oooo0O . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if OOO00O0O == False : sys . exit ( )
  if 27 - 27: O0
  self . Delete_Watched_List ( IIIIii1I )
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  xbmc . executebuiltin ( "Container.Refresh" )
  if 28 - 28: i1IIi - iII111i
  if 54 - 54: iII111i - O0 % OOooOOo
  if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
  if 17 - 17: Ii1I - OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
 def Load_Watched_List ( self , stype ) :
  try :
   OooO0oo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( OooO0oo , 'r' ) as o0o0oOoOO0O :
    iIiIIIIIii = o0o0oOoOO0O . readlines ( )
  except :
   iIiIIIIIii = [ ]
   if 58 - 58: o0oOOo0O0Ooo / IiII . OoOoOO00 / OoooooooOO + I1Ii111
  return iIiIIIIIii
  if 86 - 86: I11i * I1IiiI + I11i + II111iiii
  if 8 - 8: I1Ii111 - iII111i / ooOoO0o
  if 96 - 96: OoOoOO00
  if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   OooO0oo = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   IiiIiI111iI = self . Load_Watched_List ( stype )
   if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
   with open ( OooO0oo , 'w' ) as o0o0oOoOO0O :
    OO0ooo0oOO = urllib . urlencode ( in_params )
    OO0ooo0oOO = OO0ooo0oOO . encode ( 'utf-8' ) + '\n'
    o0o0oOoOO0O . write ( OO0ooo0oOO )
    if 97 - 97: I1IiiI / iII111i
    Oooo0 = 0
    for oOO in IiiIiI111iI :
     Oooo = dict ( urlparse . parse_qsl ( oOO ) )
     if 16 - 16: OOooOOo % iII111i . O0 / Oo0Ooo / o0oOOo0O0Ooo
     ooOO0oO0oo00o = in_params . get ( 'code' )
     oOOo0oo0O = Oooo . get ( 'code' )
     if stype == 'vod' and self . get_settings_direct_replay ( ) == True :
      ooOO0oO0oo00o = in_params . get ( 'videoid' )
      oOOo0oo0O = Oooo . get ( 'videoid' ) if oOOo0oo0O != None else '-'
      if 13 - 13: I1IiiI % OoOoOO00 . I1ii11iIi11i / Oo0Ooo % OOooOOo . OoooooooOO
      if 22 - 22: IiII / i11iIiiIii
     if ooOO0oO0oo00o != oOOo0oo0O :
      o0o0oOoOO0O . write ( oOO )
      Oooo0 += 1
      if Oooo0 >= 50 : break
  except :
   None
   if 62 - 62: OoO0O00 / I1ii11iIi11i
   if 7 - 7: OoooooooOO . IiII
   if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
   if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
 def dp_Watch_List ( self , args ) :
  IIIIii1I = args . get ( 'stype' )
  IiII1I11i1I1I = self . get_settings_direct_replay ( )
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  if IIIIii1I == '-' :
   for IiIiI1111I1I in OOooo0000ooo :
    i1i = IiIiI1111I1I . get ( 'title' )
    if 92 - 92: ooOoO0o
    I1 = { 'mode' : IiIiI1111I1I . get ( 'mode' )
 , 'stype' : IiIiI1111I1I . get ( 'stype' )
 }
    if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
    self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if len ( OOooo0000ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
  else :
   iIi1 = self . Load_Watched_List ( IIIIii1I )
   if 21 - 21: I11i
   for OoO00 in iIi1 :
    OO0Ooooo000Oo = dict ( urlparse . parse_qsl ( OoO00 ) )
    if 97 - 97: Ii1I * I1ii11iIi11i / I1IiiI / iIii1I11I1II1 % I11i
    i1i = OO0Ooooo000Oo . get ( 'title' )
    I11iII = OO0Ooooo000Oo . get ( 'img' )
    O00oO0 = OO0Ooooo000Oo . get ( 'videoid' )
    if 97 - 97: I1Ii111 - iIii1I11I1II1
    II111iI111I1I = { }
    II111iI111I1I [ 'plot' ] = i1i
    if 75 - 75: OoooooooOO * IiII
    if IIIIii1I == 'vod' :
     if IiII1I11i1I1I == False or O00oO0 == None :
      I1 = { 'mode' : 'EPISODE'
 , 'programcode' : OO0Ooooo000Oo . get ( 'code' )
 , 'page' : '1'
 }
      iI1 = True
     else :
      I1 = { 'mode' : 'VOD'
 , 'mediacode' : O00oO0
 , 'stype' : 'vod'
 , 'programcode' : OO0Ooooo000Oo . get ( 'code' )
 , 'title' : i1i
 , 'thumbnail' : I11iII
 }
      iI1 = False
    else :
     I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : OO0Ooooo000Oo . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : i1i
 , 'thumbnail' : I11iII
 }
     iI1 = False
     if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
    self . add_dir ( i1i , sublabel = '' , img = I11iII , infoLabels = II111iI111I1I , isFolder = iI1 , params = I1 )
    if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
   II111iI111I1I = { 'plot' : '시청목록을 삭제합니다.' }
   i1i = '*** 시청목록 삭제 ***'
   I1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : IIIIii1I
 }
   self . add_dir ( i1i , sublabel = '' , img = '' , infoLabels = II111iI111I1I , isFolder = False , params = I1 )
   if 69 - 69: O0
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 85 - 85: ooOoO0o / O0
   if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
   if 62 - 62: I1Ii111 . IiII . OoooooooOO
   if 11 - 11: OOooOOo / I11i
   if 73 - 73: i1IIi / i11iIiiIii
 def play_VIDEO ( self , args ) :
  if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 85 - 85: OoOoOO00 + OOooOOo
  I1II = args . get ( 'mediacode' )
  IIIIii1I = args . get ( 'stype' )
  iii1 = self . get_selQuality ( IIIIii1I )
  if 67 - 67: I1IiiI
  OO00OO0O0 , i1I111Ii1i11 = self . TvingObj . GetBroadURL ( I1II , iii1 , IIIIii1I )
  if 81 - 81: OoO0O00
  self . addon_log ( 'qt, stype, url : %s - %s - %s' % ( str ( iii1 ) , IIIIii1I , OO00OO0O0 ) )
  if 99 - 99: oO0o * II111iiii * I1Ii111
  if OO00OO0O0 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
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
  self . addon_log ( I111IiiIi1 , False )
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
 , 'referer' : 'https://www.tving.com/live/player/%s' % I1II
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
    , 'user-agent' : OoOooOOOO
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
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , Oo )
  if 21 - 21: i11iIiiIii / I1Ii111 % OOooOOo * O0 . I11i - iIii1I11I1II1
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
    I1 = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 , 'videoid' : args . get ( 'mediacode' )
    }
    self . Save_Watched_List ( args . get ( 'stype' ) , I1 )
  except :
   None
   if 26 - 26: II111iiii * OoOoOO00
   if 10 - 10: II111iiii . iII111i
   if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
   if 88 - 88: iII111i
   if 19 - 19: II111iiii * IiII + Ii1I
 def logout ( self ) :
  O00oooo0O = xbmcgui . Dialog ( )
  OOO00O0O = O00oooo0O . yesno ( __language__ ( 30910 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if OOO00O0O == False : sys . exit ( )
  if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
  self . wininfo_clear ( )
  if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
  if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
  if os . path . isfile ( i11iiII ) : os . remove ( i11iiII )
  if 67 - 67: I11i - OOooOOo . i1IIi
  self . addon_noti ( __language__ ( 30909 ) . encode ( 'utf-8' ) )
  if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
  if 87 - 87: OoOoOO00
  if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
  if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
 def wininfo_clear ( self ) :
  if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_TOKEN' , '' )
  iII . setProperty ( 'TVING_M_USERINFO' , '' )
  iII . setProperty ( 'TVING_M_UUID' , '' )
  iII . setProperty ( 'TVING_M_LOGINTIME' , '' )
  if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
  if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
  if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
  if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + I1Ii111 . iII111i
 def cookiefile_save ( self ) :
  IiI1iII1II111 = datetime . datetime . now ( )
  IIiI11i1111Ii = IiI1iII1II111 + datetime . timedelta ( days = int ( __addon__ . getSetting ( 'cache_ttl' ) ) )
  if 63 - 63: OOooOOo + ooOoO0o
  iII = xbmcgui . Window ( 10000 )
  O0ooOOO0 = { 'tving_token' : iII . getProperty ( 'TVING_M_TOKEN' )
 , 'tving_userinfo' : iII . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : iII . getProperty ( 'TVING_M_UUID' )
 , 'tving_id' : base64 . standard_b64encode ( __addon__ . getSetting ( 'id' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'tving_pw' : base64 . standard_b64encode ( __addon__ . getSetting ( 'pw' ) . encode ( ) ) . decode ( 'utf-8' )
 , 'tving_logintype' : __addon__ . getSetting ( 'login_type' )
 , 'tving_limitdate' : IIiI11i1111Ii . strftime ( '%Y-%m-%d' )
 }
  if 42 - 42: II111iiii * iII111i * i11iIiiIii - OOooOOo . OoooooooOO
  try :
   with open ( i11iiII , 'w' ) as o0o0oOoOO0O :
    json . dump ( O0ooOOO0 , o0o0oOoOO0O )
  except Exception as oo00o :
   print ( oo00o )
   if 76 - 76: iII111i
   if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
   if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
   if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
 def cookiefile_check ( self ) :
  if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  if 71 - 71: OoooooooOO
  O0ooOOO0 = { }
  try :
   with open ( i11iiII , 'r' ) as o0o0oOoOO0O :
    O0ooOOO0 = json . load ( o0o0oOoOO0O )
  except Exception as oo00o :
   self . wininfo_clear ( )
   return False
   if 33 - 33: I1Ii111
   if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
   if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
  IIiIiiIi = __addon__ . getSetting ( 'id' )
  O000oo = __addon__ . getSetting ( 'pw' )
  I111i1I1 = __addon__ . getSetting ( 'login_type' )
  O0ooOOO0 [ 'tving_id' ] = base64 . standard_b64decode ( O0ooOOO0 [ 'tving_id' ] ) . decode ( 'utf-8' )
  O0ooOOO0 [ 'tving_pw' ] = base64 . standard_b64decode ( O0ooOOO0 [ 'tving_pw' ] ) . decode ( 'utf-8' )
  if IIiIiiIi != O0ooOOO0 [ 'tving_id' ] or O000oo != O0ooOOO0 [ 'tving_pw' ] or I111i1I1 != O0ooOOO0 [ 'tving_logintype' ] :
   self . wininfo_clear ( )
   return False
   if 62 - 62: OOooOOo * I1Ii111 / Oo0Ooo * o0oOOo0O0Ooo
   if 29 - 29: Oo0Ooo % OoO0O00 % IiII . o0oOOo0O0Ooo / OoooooooOO * ooOoO0o
   if 54 - 54: O0
   if 68 - 68: OoO0O00 * o0oOOo0O0Ooo . ooOoO0o % oO0o % I1Ii111
   if 75 - 75: OoOoOO00
   if 34 - 34: O0
   if 80 - 80: i1IIi - Oo0Ooo / OoO0O00 - i11iIiiIii
   if 68 - 68: oO0o - I1ii11iIi11i % O0 % I1Ii111
   if 11 - 11: O0 / OoO0O00 % OOooOOo + o0oOOo0O0Ooo + iIii1I11I1II1
   if 40 - 40: ooOoO0o - OOooOOo . Ii1I * Oo0Ooo % I1Ii111
  O0O = int ( datetime . datetime . now ( ) . strftime ( '%Y%m%d' ) )
  OoOO00OO = O0ooOOO0 [ 'tving_limitdate' ]
  i1I1I = int ( re . sub ( '-' , '' , OoOO00OO ) )
  if 65 - 65: i1IIi . OoooooooOO * Ii1I / IiII
  if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
  if i1I1I < O0O :
   self . wininfo_clear ( )
   return False
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
   if 37 - 37: i11iIiiIii + i1IIi
  iII = xbmcgui . Window ( 10000 )
  iII . setProperty ( 'TVING_M_TOKEN' , O0ooOOO0 [ 'tving_token' ] )
  iII . setProperty ( 'TVING_M_USERINFO' , O0ooOOO0 [ 'tving_userinfo' ] )
  iII . setProperty ( 'TVING_M_UUID' , O0ooOOO0 [ 'tving_uuid' ] )
  iII . setProperty ( 'TVING_M_LOGINTIME' , OoOO00OO )
  if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
  return True
  if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
  if 8 - 8: o0oOOo0O0Ooo
  if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
  if 78 - 78: Ii1I / II111iiii % OoOoOO00
 def tving_main ( self ) :
  oO00OoOO = self . main_params . get ( 'mode' , None )
  if 18 - 18: ooOoO0o - OoOoOO00 % i1IIi + O0 + i11iIiiIii + i1IIi
  self . login_main ( )
  if 91 - 91: OoOoOO00 + ooOoO0o . I1IiiI
  if oO00OoOO is None :
   self . dp_Main_List ( )
   if 71 - 71: iII111i % o0oOOo0O0Ooo / OOooOOo / Oo0Ooo
  elif oO00OoOO in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
   self . dp_Title_Group ( self . main_params )
   if 66 - 66: Oo0Ooo - o0oOOo0O0Ooo * IiII + OoOoOO00 + o0oOOo0O0Ooo - iIii1I11I1II1
  elif oO00OoOO == 'CHANNEL' :
   self . dp_LiveChannel_List ( self . main_params )
   if 17 - 17: oO0o
  elif oO00OoOO in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 22 - 22: I11i + iIii1I11I1II1
   time . sleep ( 0.1 )
   if 24 - 24: OoOoOO00 % i1IIi + iII111i . i11iIiiIii . I1ii11iIi11i
  elif oO00OoOO == 'PROGRAM' :
   self . dp_Program_List ( self . main_params )
   if 17 - 17: I1ii11iIi11i . II111iiii . ooOoO0o / I1ii11iIi11i
  elif oO00OoOO == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 57 - 57: I11i
  elif oO00OoOO == 'MOVIE_GROUP' :
   self . dp_Movie_List ( self . main_params )
   if 67 - 67: OoO0O00 . ooOoO0o
  elif oO00OoOO == 'SEARCH_GROUP' :
   self . dp_Search_Group ( self . main_params )
   if 87 - 87: oO0o % Ii1I
  elif oO00OoOO == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 83 - 83: II111iiii - I11i
  elif oO00OoOO == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
  elif oO00OoOO == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - Ii1I
  elif oO00OoOO == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 51 - 51: OoOoOO00
  elif oO00OoOO == 'LOGOUT' :
   self . logout ( )
   if 14 - 14: IiII % oO0o % Oo0Ooo - i11iIiiIii
   if 53 - 53: Ii1I % Oo0Ooo
   if 59 - 59: OOooOOo % iIii1I11I1II1 . i1IIi + II111iiii * IiII
   if 41 - 41: Ii1I % I1ii11iIi11i
   if 12 - 12: OOooOOo
   if 69 - 69: OoooooooOO + OOooOOo
  else :
   None
   if 26 - 26: Oo0Ooo + OOooOOo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
   if 31 - 31: I11i % OOooOOo * I11i
   if 45 - 45: i1IIi . I1IiiI + OOooOOo - OoooooooOO % ooOoO0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
