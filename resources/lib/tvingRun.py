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
if 45 - 45: I1Ii111 + Ii1I
from tvingCore import *
if 17 - 17: o0oOOo0O0Ooo
if 64 - 64: Ii1I % i1IIi % OoooooooOO
class i1iIIi1 ( object ) :
 def __init__ ( self , in_addonurl , in_handle , in_params ) :
  if 50 - 50: i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  if 18 - 18: O0 - iII111i / iII111i + ooOoO0o % ooOoO0o - IiII
  if 62 - 62: iII111i - IiII - OoOoOO00 % i1IIi / oO0o
  self . _addon_url = in_addonurl
  self . _addon_handle = in_handle
  self . main_params = in_params
  self . TvingObj = oOOo0oo ( )
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  if 14 - 14: I11i % O0
  if 41 - 41: i1IIi + I1Ii111 + OOooOOo - IiII
 def addon_noti ( self , sting ) :
  try :
   oO = xbmcgui . Dialog ( )
   if 76 - 76: OoO0O00 * o0oOOo0O0Ooo % i1IIi - OoO0O00 / I1IiiI . OOooOOo
   oO . notification ( __addonname__ , sting )
  except :
   None
   if 41 - 41: OoOoOO00
   if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
   if 6 - 6: I1IiiI / Oo0Ooo % Ii1I
 def addon_log ( self , string , isDebug = False ) :
  try :
   oo = string . encode ( 'utf-8' , 'ignore' )
  except :
   oo = 'addonException: addon_log'
  if isDebug : OO0O00 = xbmc . LOGDEBUG
  else : OO0O00 = xbmc . LOGNOTICE
  xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , oo ) , level = OO0O00 )
  if 20 - 20: OoooooooOO
  if 13 - 13: i1IIi - Ii1I % oO0o / iIii1I11I1II1 % iII111i
  if 97 - 97: i11iIiiIii
  if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . IiII
 def get_keyboard_input ( self , title ) :
  o0OOOOO00o0O0 = None
  o0o0OOO0o0 = xbmc . Keyboard ( )
  o0o0OOO0o0 . setHeading ( title )
  xbmc . sleep ( 1000 )
  o0o0OOO0o0 . doModal ( )
  if ( o0o0OOO0o0 . isConfirmed ( ) ) :
   o0OOOOO00o0O0 = o0o0OOO0o0 . getText ( )
  return o0OOOOO00o0O0
  if 84 - 84: IiII
  if 25 - 25: Oo0Ooo - IiII . OoooooooOO
  if 22 - 22: IiII + II111iiii % I1Ii111 . I11i . OoOoOO00
  if 76 - 76: OoOoOO00 - O0 % OOooOOo / I1ii11iIi11i / OoOoOO00
 def get_settings_login_info ( self ) :
  oo0oooooO0 = __addon__ . getSetting ( 'id' )
  i11Iiii = __addon__ . getSetting ( 'pw' )
  iI = __addon__ . getSetting ( 'login_type' )
  return ( oo0oooooO0 , i11Iiii , iI )
  if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
  if 95 - 95: OoO0O00 % oO0o . O0
  if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
  if 53 - 53: IiII + I1IiiI * oO0o
 def get_settings_premiumyn ( self ) :
  OooOooooOOoo0 = __addon__ . getSetting ( 'premium_movieyn' )
  if OooOooooOOoo0 == 'false' :
   return False
  else :
   return True
   if 71 - 71: I1Ii111 % oO0o % OOooOOo
   if 94 - 94: oO0o - iII111i * O0
   if 17 - 17: I1ii11iIi11i % II111iiii
 def get_settings_direct_replay ( self ) :
  I1IIiiIiii = int ( __addon__ . getSetting ( 'direct_replay' ) )
  if I1IIiiIiii == 0 :
   return False
  else :
   return True
   if 97 - 97: ooOoO0o - OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - OoooooooOO
   if 59 - 59: O0 + I1IiiI + IiII % I1IiiI
   if 70 - 70: iII111i * I1ii11iIi11i
 def get_settings_thumbnail_landyn ( self ) :
  i1II1 = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if i1II1 == 0 :
   return True
  else :
   return False
   if 66 - 66: OoooooooOO + Ii1I + Ii1I - i1IIi
   if 55 - 55: OOooOOo + ooOoO0o . i1IIi - I1ii11iIi11i . O0 - ooOoO0o
   if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
   if 28 - 28: i1IIi * Oo0Ooo - o0oOOo0O0Ooo * IiII * Ii1I / OoO0O00
 def set_winCredential ( self , credential ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  OooO0OoOOOO . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
  OooO0OoOOOO . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
  OooO0OoOOOO . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
  if 46 - 46: OOooOOo / I1ii11iIi11i
  OooO0OoOOOO . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 24 - 24: I11i . iII111i % OOooOOo + ooOoO0o % OoOoOO00
  if 4 - 4: IiII - OoO0O00 * OoOoOO00 - I11i
 def get_winCredential ( self ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  II1 = {
 'tving_token' : OooO0OoOOOO . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : OooO0OoOOOO . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : OooO0OoOOOO . getProperty ( 'TVING_M_UUID' )
 }
  return II1
  if 34 - 34: IiII - IiII * I1IiiI + Ii1I % IiII
 def set_winEpisodeOrderby ( self , orderby ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  OooO0OoOOOO . setProperty ( 'TVING_M_ORDERBY' , orderby )
  if 4 - 4: oO0o
 def get_winEpisodeOrderby ( self ) :
  OooO0OoOOOO = xbmcgui . Window ( 10000 )
  return OooO0OoOOOO . getProperty ( 'TVING_M_ORDERBY' )
  if 93 - 93: OoO0O00 % oO0o . OoO0O00 * I1Ii111 % Ii1I . II111iiii
  if 38 - 38: o0oOOo0O0Ooo
  if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
  if 26 - 26: iII111i
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  OOO = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
  if sublabel : Oo0OoO00oOO0o = '%s < %s >' % ( label , sublabel )
  else : Oo0OoO00oOO0o = label
  if not img : img = 'DefaultFolder.png'
  if 80 - 80: oO0o + OOooOOo - OOooOOo % iII111i
  if 63 - 63: I1IiiI - I1ii11iIi11i + O0 % I11i / iIii1I11I1II1 / o0oOOo0O0Ooo
  O0o0O00Oo0o0 = xbmcgui . ListItem ( Oo0OoO00oOO0o )
  O0o0O00Oo0o0 . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 87 - 87: ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  if infoLabels : O0o0O00Oo0o0 . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : O0o0O00Oo0o0 . setProperty ( 'IsPlayable' , 'true' )
  if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
  xbmcplugin . addDirectoryItem ( self . _addon_handle , OOO , O0o0O00Oo0o0 , isFolder )
  if 92 - 92: iII111i . I1Ii111
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  if 89 - 89: OoOoOO00
 def get_selQuality ( self , etype ) :
  try :
   OO0oOoOO0oOO0 = 'selected_quality'
   if 86 - 86: OOooOOo
   if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
   if 25 - 25: I1ii11iIi11i
   if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
   if 13 - 13: OOooOOo / i11iIiiIii
   if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
   if 52 - 52: o0oOOo0O0Ooo
   o0OO0oOO0O0 = [ 1080 , 720 , 480 , 360 ]
   if 8 - 8: oO0o
   iIi1IIIi1 = int ( __addon__ . getSetting ( OO0oOoOO0oOO0 ) )
   return o0OO0oOO0O0 [ iIi1IIIi1 ]
  except :
   None
   if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
  return 720
  if 42 - 42: OoO0O00
  if 67 - 67: I1Ii111 . iII111i . O0
  if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 def dp_Main_List ( self ) :
  if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
  for I1111IIi in Oo0oO0ooo :
   Oo0OoO00oOO0o = I1111IIi . get ( 'title' )
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
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = iI1 , params = I1 )
  if len ( Oo0oO0ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
 if 31 - 31: II111iiii . I1IiiI
 if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
 if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
 if 92 - 92: iII111i
 if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
 if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
 if 20 - 20: OOooOOo % Ii1I / Ii1I + Ii1I
 if 45 - 45: oO0o - IiII - OoooooooOO - OoO0O00 . II111iiii / O0
 if 51 - 51: O0 + iII111i
 if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
 if 48 - 48: O0
 if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
 if 41 - 41: Ii1I - O0 - O0
 if 68 - 68: OOooOOo % I1Ii111
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
 if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
 if 80 - 80: II111iiii
 if 83 - 83: I11i . i11iIiiIii + II111iiii . o0oOOo0O0Ooo * I11i
 if 53 - 53: II111iiii
 if 31 - 31: OoO0O00
 if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
 if 25 - 25: OoO0O00
 if 62 - 62: OOooOOo + O0
 if 98 - 98: o0oOOo0O0Ooo
 if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
 if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
 if 82 - 82: Ii1I
 if 46 - 46: OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
 if 87 - 87: Oo0Ooo . IiII
 if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
 if 55 - 55: OOooOOo . I1IiiI
 if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
 if 100 - 100: I1Ii111 * O0
 if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 if 79 - 79: O0
 if 78 - 78: I1ii11iIi11i + OOooOOo - I1Ii111
 if 38 - 38: o0oOOo0O0Ooo - oO0o + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
 def login_main ( self ) :
  ( oO0o0 , iI1Ii11iIiI1 , OO0Oooo0oOO0O ) = self . get_settings_login_info ( )
  if 62 - 62: I1IiiI
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  if not ( oO0o0 and iI1Ii11iIiI1 ) :
   oO = xbmcgui . Dialog ( )
   Oo0O0oooo = oO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if Oo0O0oooo == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  O0oO = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
  if 66 - 66: oO0o + oO0o + ooOoO0o / iII111i + OOooOOo
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
   iIii1111iII = 0
   while True :
    iIii1111iII += 1
    if 32 - 32: i1IIi / II111iiii . Oo0Ooo
    time . sleep ( 0.05 )
    if 62 - 62: OoooooooOO * I1IiiI
    if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == O0oO : return
    if iIii1111iII > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
   if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == O0oO :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   return
   if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
   if 97 - 97: O0 + OoOoOO00
  if not self . TvingObj . GetCredential ( oO0o0 , iI1Ii11iIiI1 , OO0Oooo0oOO0O ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
   if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
  self . set_winCredential ( self . TvingObj . LoadCredential ( ) )
  self . set_winEpisodeOrderby ( 'desc' )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  if 77 - 77: OOooOOo * iIii1I11I1II1
  if 98 - 98: I1IiiI % Ii1I * OoooooooOO
  if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
  if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
 def dp_Title_Group ( self , args ) :
  oO00O000oO0 = args . get ( 'stype' )
  if oO00O000oO0 == 'live' :
   O0OoOO0o = o00oOoo
  else :
   O0OoOO0o = IiII1I1i1i1ii
   if 69 - 69: I1Ii111
  for ii1I1 in O0OoOO0o :
   Oo0OoO00oOO0o = ii1I1 . get ( 'title' )
   if 93 - 93: O0 % i1IIi . OOooOOo / I1IiiI - I1Ii111 / I1IiiI
   if args . get ( 'ordernm' ) != '-' :
    Oo0OoO00oOO0o += '  (' + args . get ( 'ordernm' ) + ')'
    if 36 - 36: oO0o % oO0o % i1IIi / i1IIi - ooOoO0o
   I1 = { 'mode' : ii1I1 . get ( 'mode' )
 , 'stype' : ii1I1 . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
   if 30 - 30: I11i / I1IiiI
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
  if len ( O0OoOO0o ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
  if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
  if 72 - 72: Ii1I
 def dp_LiveChannel_List ( self , args ) :
  if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
  oO00O000oO0 = args . get ( 'stype' )
  I11I = int ( args . get ( 'page' ) )
  I11iIi1i1II11 , iiI = self . TvingObj . GetLiveChannelList ( oO00O000oO0 , I11I )
  if 26 - 26: Ii1I % I1ii11iIi11i
  for o00Oo0oooooo in I11iIi1i1II11 :
   Oo0OoO00oOO0o = o00Oo0oooooo . get ( 'title' )
   O0oO0 = o00Oo0oooooo . get ( 'channel' )
   iII11 = o00Oo0oooooo . get ( 'thumbnail' )
   iiIiii1IIIII = o00Oo0oooooo . get ( 'synopsis' )
   o00o = o00Oo0oooooo . get ( 'channelepg' )
   if 45 - 45: I1ii11iIi11i . o0oOOo0O0Ooo . I1ii11iIi11i - I1IiiI . o0oOOo0O0Ooo
   iiI1IIIi = o00Oo0oooooo . get ( 'info' )
   iiI1IIIi [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( O0oO0 , Oo0OoO00oOO0o , o00o , iiIiii1IIIII )
   if 47 - 47: Oo0Ooo % I11i % i11iIiiIii - O0 + ooOoO0o
   I1 = { 'mode' : 'LIVE'
 , 'mediacode' : o00Oo0oooooo . get ( 'mediacode' )
 , 'stype' : oO00O000oO0
   }
   if 94 - 94: I1Ii111
   self . add_dir ( O0oO0 , sublabel = Oo0OoO00oOO0o , img = iII11 , infoLabels = iiI1IIIi , isFolder = False , params = I1 )
   if 4 - 4: Ii1I % oO0o * OoO0O00
  if iiI :
   if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
   I1 [ 'mode' ] = 'CHANNEL'
   I1 [ 'stype' ] = oO00O000oO0
   I1 [ 'page' ] = str ( I11I + 1 )
   Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
   OoOO0o = str ( I11I + 1 )
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 1 - 1: II111iiii
  if len ( I11iIi1i1II11 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
  if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
  if 5 - 5: i1IIi + IiII / o0oOOo0O0Ooo . iII111i / I11i
  if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
 def dp_Program_List ( self , args ) :
  if 7 - 7: I1Ii111 * OoO0O00 - ooOoO0o + OOooOOo * I1IiiI % OoO0O00
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 15 - 15: OoOoOO00 % I1IiiI * I11i
  oO00O000oO0 = args . get ( 'stype' )
  O0OoooO0 = args . get ( 'orderby' )
  I11I = int ( args . get ( 'page' ) )
  if 85 - 85: I11i
  iI1i11II1i , iiI = self . TvingObj . GetProgramList ( oO00O000oO0 , O0OoooO0 , I11I , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 96 - 96: I1Ii111
  for oOoOo0O0OOOoO in iI1i11II1i :
   Oo0OoO00oOO0o = oOoOo0O0OOOoO . get ( 'title' )
   iII11 = oOoOo0O0OOOoO . get ( 'thumbnail' )
   iiIiii1IIIII = oOoOo0O0OOOoO . get ( 'synopsis' )
   iI11IIIiii1II = O0OoOoo00o . get ( oOoOo0O0OOOoO . get ( 'channel' ) )
   if 16 - 16: iII111i + OoOoOO00
   iiI1IIIi = oOoOo0O0OOOoO . get ( 'info' )
   iiI1IIIi [ 'studio' ] = iI11IIIiii1II
   iiI1IIIi [ 'plot' ] = '%s <%s>\n\n%s' % ( Oo0OoO00oOO0o , iI11IIIiii1II , iiIiii1IIIII )
   if 66 - 66: iII111i / oO0o * OoooooooOO + OoooooooOO % I11i
   I1 = { 'mode' : 'EPISODE'
 , 'programcode' : oOoOo0O0OOOoO . get ( 'program' )
 , 'page' : '1'
 }
   if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
   self . add_dir ( Oo0OoO00oOO0o , sublabel = iI11IIIiii1II , img = iII11 , infoLabels = iiI1IIIi , isFolder = True , params = I1 )
   if 71 - 71: o0oOOo0O0Ooo
  if iiI :
   if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
   I1 [ 'mode' ] = 'PROGRAM'
   I1 [ 'stype' ] = oO00O000oO0
   I1 [ 'orderby' ] = O0OoooO0
   I1 [ 'page' ] = str ( I11I + 1 )
   Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
   OoOO0o = str ( I11I + 1 )
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 53 - 53: i11iIiiIii * iII111i
  if len ( iI1i11II1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
  if 38 - 38: ooOoO0o - OOooOOo / iII111i
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
  if 86 - 86: o0oOOo0O0Ooo
 def dp_Episode_List ( self , args ) :
  if 5 - 5: IiII * OoOoOO00
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 5 - 5: I1Ii111
  O0I11Iiii1I = args . get ( 'programcode' )
  I11I = int ( args . get ( 'page' ) )
  if 90 - 90: iIii1I11I1II1 % ooOoO0o
  OoO0O00O0oo0O , iiI , I1IiI11 = self . TvingObj . GetEpisodoList ( O0I11Iiii1I , I11I , orderby = self . get_winEpisodeOrderby ( ) )
  if 9 - 9: I11i
  for OoooO in OoO0O00O0oo0O :
   Oo0OoO00oOO0o = OoooO . get ( 'title' )
   OoOO0o = OoooO . get ( 'subtitle' )
   iII11 = OoooO . get ( 'thumbnail' )
   iiIiii1IIIII = OoooO . get ( 'synopsis' )
   if 27 - 27: OoooooooOO
   iiI1IIIi = OoooO . get ( 'info' )
   iiI1IIIi [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , iiIiii1IIIII )
   if 45 - 45: i11iIiiIii + O0 + I1IiiI - Oo0Ooo
   I1 = { 'mode' : 'VOD'
 , 'mediacode' : OoooO . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : O0I11Iiii1I
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : iII11
 }
   if 30 - 30: I1Ii111 . ooOoO0o * I1ii11iIi11i
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = iII11 , infoLabels = iiI1IIIi , isFolder = False , params = I1 )
   if 17 - 17: I1IiiI . O0 + OoO0O00
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   if 20 - 20: I1IiiI
   if 95 - 95: iII111i - I1IiiI
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if I11I == 1 :
   iiI1IIIi = { 'plot' : '정렬순서를 변경합니다.' }
   I1 = { }
   I1 [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    Oo0OoO00oOO0o = '정렬순서변경 : 최신화부터 -> 1회부터'
    I1 [ 'orderby' ] = 'asc'
   else :
    Oo0OoO00oOO0o = '정렬순서변경 : 1회부터 -> 최신화부터'
    I1 [ 'orderby' ] = 'desc'
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = iiI1IIIi , isFolder = False , params = I1 )
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
   if 41 - 41: i1IIi - I11i - Ii1I
  if iiI :
   if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   I1 [ 'mode' ] = 'EPISODE'
   I1 [ 'programcode' ] = O0I11Iiii1I
   I1 [ 'page' ] = str ( I11I + 1 )
   Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
   OoOO0o = str ( I11I + 1 )
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
   if 44 - 44: II111iiii
  if len ( OoO0O00O0oo0O ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = True )
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  if 35 - 35: iIii1I11I1II1
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
 def dp_setEpOrderby ( self , args ) :
  O0OoooO0 = args . get ( 'orderby' )
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  self . set_winEpisodeOrderby ( O0OoooO0 )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  if 71 - 71: O0 - iIii1I11I1II1
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
 def dp_Movie_List ( self , args ) :
  if 42 - 42: Oo0Ooo
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  O0OoooO0 = args . get ( 'orderby' )
  I11I = int ( args . get ( 'page' ) )
  if 46 - 46: Oo0Ooo
  i1II1I1Iii1 , iiI = self . TvingObj . GetMovieList ( O0OoooO0 , I11I , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 30 - 30: OoooooooOO - OoOoOO00
  for Ooo00O0o in i1II1I1Iii1 :
   Oo0OoO00oOO0o = Ooo00O0o . get ( 'title' )
   iII11 = Ooo00O0o . get ( 'thumbnail' )
   iiIiii1IIIII = Ooo00O0o . get ( 'synopsis' )
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
   iiI1IIIi = Ooo00O0o . get ( 'info' )
   iiI1IIIi [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , iiIiii1IIIII )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
   I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : Ooo00O0o . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : iII11
 }
   if 17 - 17: i1IIi
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = iII11 , infoLabels = iiI1IIIi , isFolder = False , params = I1 )
   if 21 - 21: Oo0Ooo
  if iiI :
   if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
   I1 [ 'mode' ] = 'MOVIE_GROUP'
   I1 [ 'orderby' ] = O0OoooO0
   I1 [ 'page' ] = str ( I11I + 1 )
   Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
   OoOO0o = str ( I11I + 1 )
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  if len ( i1II1I1Iii1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
  if 54 - 54: i1IIi + II111iiii
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
 def dp_Search_Group ( self , args ) :
  for ii1I1 in O0o0o00o0Oo0 :
   Oo0OoO00oOO0o = ii1I1 . get ( 'title' )
   if 5 - 5: Ii1I
   I1 = { 'mode' : ii1I1 . get ( 'mode' )
 , 'stype' : ii1I1 . get ( 'stype' )
 , 'page' : '1'
 }
   if 46 - 46: IiII
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
  if len ( O0o0o00o0Oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 45 - 45: ooOoO0o
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  if 17 - 17: OOooOOo / OOooOOo / I11i
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
 def dp_Search_List ( self , args ) :
  if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
  iII1iiiiIII = __addon__ . getSetting ( 'id' )
  I11I = int ( args . get ( 'page' ) )
  oO00O000oO0 = args . get ( 'stype' )
  if 78 - 78: OOooOOo * o0oOOo0O0Ooo / I11i - O0 / IiII
  if 'search_key' in args :
   oOO = args . get ( 'search_key' )
  else :
   oOO = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not oOO : return
   if 53 - 53: I1Ii111 * IiII . Oo0Ooo - Ii1I % Ii1I * i11iIiiIii
  ii , iiI = self . TvingObj . GetSearchList ( oOO , iII1iiiiIII , I11I , oO00O000oO0 , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if len ( ii ) == 0 : return
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  for ii1III11 in ii :
   Oo0OoO00oOO0o = ii1III11 . get ( 'title' )
   iII11 = ii1III11 . get ( 'thumbnail' )
   iiIiii1IIIII = ii1III11 . get ( 'synopsis' )
   I1iiIIIi11 = ii1III11 . get ( 'program' )
   if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
   iiI1IIIi = ii1III11 . get ( 'info' )
   iiI1IIIi [ 'plot' ] = '%s\n\n%s' % ( Oo0OoO00oOO0o , iiIiii1IIIII )
   if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
   if oO00O000oO0 == 'vod' :
    I1 = { 'mode' : 'EPISODE'
 , 'programcode' : ii1III11 . get ( 'program' )
 , 'page' : '1'
 }
    iI1 = True
   else :
    I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : ii1III11 . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : iII11
 }
    iI1 = False
    if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = iII11 , infoLabels = iiI1IIIi , isFolder = iI1 , params = I1 )
   if 51 - 51: IiII
  if iiI :
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
   I1 [ 'mode' ] = 'SEARCH'
   I1 [ 'search_key' ] = oOO
   I1 [ 'page' ] = str ( I11I + 1 )
   Oo0OoO00oOO0o = '[B]%s >>[/B]' % '다음 페이지'
   OoOO0o = str ( I11I + 1 )
   self . add_dir ( Oo0OoO00oOO0o , sublabel = OoOO0o , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
  if len ( ii ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 def Delete_Watched_List ( self , stype ) :
  try :
   O0ooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( O0ooo0 , 'w' ) as I1iii11 :
    I1iii11 . write ( '' )
  except :
   None
   if 74 - 74: O0 / i1IIi
   if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
   if 31 - 31: OoooooooOO . OOooOOo
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 def dp_WatchList_Delete ( self , args ) :
  oO00O000oO0 = args . get ( 'stype' )
  if 100 - 100: OoO0O00
  oO = xbmcgui . Dialog ( )
  Oo0O0oooo = oO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if Oo0O0oooo == False : sys . exit ( )
  if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
  self . Delete_Watched_List ( oO00O000oO0 )
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
  xbmc . executebuiltin ( "Container.Refresh" )
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if 62 - 62: OoO0O00 / I1ii11iIi11i
 def Load_Watched_List ( self , stype ) :
  try :
   O0ooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( O0ooo0 , 'r' ) as I1iii11 :
    ii1 = I1iii11 . readlines ( )
  except :
   ii1 = [ ]
   if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
  return ii1
  if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
  if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  if 92 - 92: ooOoO0o
  if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   O0ooo0 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   Oo00OoOo = self . Load_Watched_List ( stype )
   if 24 - 24: i11iIiiIii - I1Ii111
   with open ( O0ooo0 , 'w' ) as I1iii11 :
    i11iiI1111 = urllib . urlencode ( in_params )
    i11iiI1111 = i11iiI1111 . encode ( 'utf-8' ) + '\n'
    I1iii11 . write ( i11iiI1111 )
    if 97 - 97: Oo0Ooo * I1IiiI . iIii1I11I1II1
    I1Ii1111iIi = 0
    for I11 in Oo00OoOo :
     o0oO00oO0o0o0 = dict ( urlparse . parse_qsl ( I11 ) )
     if 17 - 17: I11i . IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
     I1IIIiI1I1ii1 = in_params . get ( 'code' )
     iiiI1I1iIIIi1 = o0oO00oO0o0o0 . get ( 'code' )
     if stype == 'vod' and self . get_settings_direct_replay ( ) == True :
      I1IIIiI1I1ii1 = in_params . get ( 'videoid' )
      iiiI1I1iIIIi1 = o0oO00oO0o0o0 . get ( 'videoid' ) if iiiI1I1iIIIi1 != None else '-'
      if 17 - 17: iIii1I11I1II1 . OoooooooOO / I11i % II111iiii % i1IIi / i11iIiiIii
      if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
     if I1IIIiI1I1ii1 != iiiI1I1iIIIi1 :
      I1iii11 . write ( I11 )
      I1Ii1111iIi += 1
      if I1Ii1111iIi >= 50 : break
  except :
   None
   if 85 - 85: OoOoOO00 + OOooOOo
   if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
   if 27 - 27: Ii1I
   if 67 - 67: I1IiiI
 def dp_Watch_List ( self , args ) :
  oO00O000oO0 = args . get ( 'stype' )
  I1IIiiIiii = self . get_settings_direct_replay ( )
  if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
  if oO00O000oO0 == '-' :
   for ii1I1 in OOooo0000ooo :
    Oo0OoO00oOO0o = ii1I1 . get ( 'title' )
    if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
    I1 = { 'mode' : ii1I1 . get ( 'mode' )
 , 'stype' : ii1I1 . get ( 'stype' )
 }
    if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
    self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = I1 )
   if len ( OOooo0000ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 92 - 92: Oo0Ooo
  else :
   iI11I = self . Load_Watched_List ( oO00O000oO0 )
   if 53 - 53: iIii1I11I1II1 + Ii1I - I1Ii111
   for OoO in iI11I :
    iIIiii = dict ( urlparse . parse_qsl ( OoO ) )
    if 61 - 61: IiII . i1IIi / I1Ii111 % i11iIiiIii * iII111i
    Oo0OoO00oOO0o = iIIiii . get ( 'title' )
    iII11 = iIIiii . get ( 'img' )
    i1i1i1I = iIIiii . get ( 'videoid' )
    if 83 - 83: oO0o + OoooooooOO
    iiI1IIIi = { }
    iiI1IIIi [ 'plot' ] = Oo0OoO00oOO0o
    if 22 - 22: Ii1I % iII111i * OoooooooOO - o0oOOo0O0Ooo / iIii1I11I1II1
    if oO00O000oO0 == 'vod' :
     if I1IIiiIiii == False or i1i1i1I == None :
      I1 = { 'mode' : 'EPISODE'
 , 'programcode' : iIIiii . get ( 'code' )
 , 'page' : '1'
 }
      iI1 = True
     else :
      I1 = { 'mode' : 'VOD'
 , 'mediacode' : i1i1i1I
 , 'stype' : 'vod'
 , 'programcode' : iIIiii . get ( 'code' )
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : iII11
 }
      iI1 = False
    else :
     I1 = { 'mode' : 'MOVIE'
 , 'mediacode' : iIIiii . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : Oo0OoO00oOO0o
 , 'thumbnail' : iII11
 }
     iI1 = False
     if 86 - 86: OoooooooOO . iII111i % OoOoOO00 / I11i * iII111i / o0oOOo0O0Ooo
    self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = iII11 , infoLabels = iiI1IIIi , isFolder = iI1 , params = I1 )
    if 64 - 64: i11iIiiIii
   iiI1IIIi = { 'plot' : '시청목록을 삭제합니다.' }
   Oo0OoO00oOO0o = '*** 시청목록 삭제 ***'
   I1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : oO00O000oO0
 }
   self . add_dir ( Oo0OoO00oOO0o , sublabel = '' , img = '' , infoLabels = iiI1IIIi , isFolder = False , params = I1 )
   if 38 - 38: IiII / I1IiiI - IiII . I11i
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 69 - 69: OoooooooOO + I1ii11iIi11i
   if 97 - 97: OOooOOo - OoO0O00 / Ii1I . i11iIiiIii % oO0o * oO0o
   if 1 - 1: I1IiiI % ooOoO0o
   if 65 - 65: I1IiiI + OoOoOO00 / OOooOOo
   if 83 - 83: o0oOOo0O0Ooo . iII111i - Oo0Ooo
 def play_VIDEO ( self , args ) :
  if 65 - 65: iIii1I11I1II1 / ooOoO0o . IiII - II111iiii
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 72 - 72: iIii1I11I1II1 / IiII % iII111i % OOooOOo - I11i % OOooOOo
  oOo0Oo0 = args . get ( 'mediacode' )
  oO00O000oO0 = args . get ( 'stype' )
  I11I111iiii = self . get_selQuality ( oO00O000oO0 )
  if 81 - 81: OOooOOo / O0 + I11i + Ii1I / I1IiiI
  iI1I1i1I1Iii , oOO0 = self . TvingObj . GetBroadURL ( oOo0Oo0 , I11I111iiii , oO00O000oO0 )
  if 46 - 46: Ii1I % OoOoOO00
  self . addon_log ( 'qt, stype, url : %s - %s - %s' % ( str ( I11I111iiii ) , oO00O000oO0 , iI1I1i1I1Iii ) )
  if 64 - 64: i11iIiiIii - II111iiii
  if iI1I1i1I1Iii == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 77 - 77: OoOoOO00 % Ii1I
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   if 2 - 2: OoooooooOO % OOooOOo
  oOoOOo0oo0 = iI1I1i1I1Iii . find ( 'Policy=' )
  if oOoOOo0oo0 != - 1 :
   o0O0Oo00Oo0o = iI1I1i1I1Iii . split ( '?' ) [ 0 ]
   if 74 - 74: Oo0Ooo / i11iIiiIii - II111iiii * o0oOOo0O0Ooo
   IIi1IIIIi = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( iI1I1i1I1Iii ) . query ) )
   IIi1IIIIi = urllib . urlencode ( IIi1IIIIi )
   IIi1IIIIi = IIi1IIIIi . replace ( '&' , ';' )
   IIi1IIIIi = IIi1IIIIi . replace ( 'Policy' , 'CloudFront-Policy' )
   IIi1IIIIi = IIi1IIIIi . replace ( 'Signature' , 'CloudFront-Signature' )
   IIi1IIIIi = IIi1IIIIi . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
   if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
   Iii = '%s|Cookie=%s' % ( o0O0Oo00Oo0o , IIi1IIIIi )
  else :
   Iii = iI1I1i1I1Iii
   if 20 - 20: o0oOOo0O0Ooo / i1IIi
   if 71 - 71: OoOoOO00 . i1IIi
  self . addon_log ( Iii , False )
  if 94 - 94: OOooOOo . I1Ii111
  if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
  if 47 - 47: OoooooooOO
  if 4 - 4: I1IiiI % I11i
  I1oOO0o0 = xbmcgui . ListItem ( path = Iii )
  if 19 - 19: II111iiii * IiII + Ii1I
  if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
  if oOO0 != '' :
   ii111i = oOO0
   oooo00 = 'https://cj.drmkeyserver.com/widevine_license'
   if 77 - 77: ooOoO0o - I1IiiI % I11i - O0
   o0O0O0 = 'mpd'
   I11oo0ooOO = 'com.widevine.alpha'
   if 24 - 24: OoO0O00 % OoO0O00 * iIii1I11I1II1
   III = inputstreamhelper . Helper ( o0O0O0 , drm = I11oo0ooOO )
   if 1 - 1: oO0o
   if III . check_inputstream ( ) :
    if 62 - 62: i1IIi - OOooOOo
    ooIII1i1iI1 = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % oOo0Oo0
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
    , 'user-agent' : OoOooOOOO
 , 'AcquireLicenseAssertion' : ii111i
 , 'Host' : 'cj.drmkeyserver.com'
 }
    o0ooo00o = oooo00 + '|' + urllib . urlencode ( ooIII1i1iI1 ) + '|R{SSM}|'
    if 62 - 62: Oo0Ooo * OoOoOO00
    I1oOO0o0 . setProperty ( 'inputstreamaddon' , III . inputstream_addon )
    if 79 - 79: OoO0O00 . iII111i * Ii1I - OOooOOo + ooOoO0o
    I1oOO0o0 . setProperty ( 'inputstream.adaptive.manifest_type' , o0O0O0 )
    I1oOO0o0 . setProperty ( 'inputstream.adaptive.license_type' , I11oo0ooOO )
    if 14 - 14: i11iIiiIii - iII111i * OoOoOO00
    I1oOO0o0 . setProperty ( 'inputstream.adaptive.license_key' , o0ooo00o )
    if 51 - 51: I1ii11iIi11i / iIii1I11I1II1 % oO0o + o0oOOo0O0Ooo * ooOoO0o + I1Ii111
    if 77 - 77: ooOoO0o * OoOoOO00
    if 14 - 14: I11i % I11i / IiII
    if 72 - 72: i1IIi - II111iiii - OOooOOo + OOooOOo * o0oOOo0O0Ooo * OOooOOo
    if 33 - 33: Oo0Ooo
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , I1oOO0o0 )
  if 49 - 49: OoO0O00 % iII111i % iII111i / iII111i
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
   if 53 - 53: iIii1I11I1II1
   if 68 - 68: OoooooooOO % II111iiii
   if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
   if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
   if 2 - 2: Ii1I - IiII
   if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
 def tving_main ( self ) :
  IIIiIi = self . main_params . get ( 'mode' , None )
  if 34 - 34: OoooooooOO . O0 / oO0o * OoOoOO00 - I1ii11iIi11i
  self . login_main ( )
  if 36 - 36: i1IIi / O0 / OoO0O00 - O0 - i1IIi
  if IIIiIi is None :
   self . dp_Main_List ( )
   if 22 - 22: i1IIi + Ii1I
  elif IIIiIi in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
   self . dp_Title_Group ( self . main_params )
   if 54 - 54: ooOoO0o % OOooOOo . I1Ii111 + oO0o - OOooOOo * I1IiiI
  elif IIIiIi == 'CHANNEL' :
   self . dp_LiveChannel_List ( self . main_params )
   if 92 - 92: o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % OoO0O00 % IiII . OoooooooOO
  elif IIIiIi in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 52 - 52: ooOoO0o / i11iIiiIii - OOooOOo . IiII % iIii1I11I1II1 + o0oOOo0O0Ooo
   time . sleep ( 0.1 )
   if 71 - 71: oO0o % I11i * OoOoOO00 . O0 / Ii1I . I1ii11iIi11i
  elif IIIiIi == 'PROGRAM' :
   self . dp_Program_List ( self . main_params )
   if 58 - 58: Oo0Ooo / oO0o
  elif IIIiIi == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 44 - 44: OOooOOo
  elif IIIiIi == 'MOVIE_GROUP' :
   self . dp_Movie_List ( self . main_params )
   if 54 - 54: Ii1I - I11i - I1Ii111 . iIii1I11I1II1
  elif IIIiIi == 'SEARCH_GROUP' :
   self . dp_Search_Group ( self . main_params )
   if 79 - 79: Ii1I . OoO0O00
  elif IIIiIi == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % ooOoO0o
  elif IIIiIi == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  elif IIIiIi == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 60 - 60: I1IiiI * I1Ii111 % OoO0O00 + oO0o
  elif IIIiIi == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 52 - 52: i1IIi
  else :
   None
   if 84 - 84: Ii1I / IiII
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
