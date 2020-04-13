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
 , { 'title' : '검색 (VOD,영화)' , 'mode' : 'SEARCH_GROUP' , 'stype' : '-' , 'orderby' : '-' , 'ordernm' : '-' }
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
  self . TvingObj = oo0Ooo0 ( )
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
   if 13 - 13: I1Ii111 % OoOoOO00 - i11iIiiIii . I1IiiI + II111iiii
 def get_settings_thumbnail_landyn ( self ) :
  II111ii1II1i = int ( __addon__ . getSetting ( 'thumbnail_way' ) )
  if II111ii1II1i == 0 :
   return True
  else :
   return False
   if 59 - 59: O0 + I1IiiI + IiII % I1IiiI
   if 70 - 70: iII111i * I1ii11iIi11i
   if 46 - 46: ooOoO0o / OoO0O00
   if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + Ii1I + Ii1I - o0oOOo0O0Ooo / I1Ii111
 def set_winCredential ( self , credential ) :
  I1I = xbmcgui . Window ( 10000 )
  I1I . setProperty ( 'TVING_M_TOKEN' , credential . get ( 'tving_token' ) )
  I1I . setProperty ( 'TVING_M_USERINFO' , credential . get ( 'poc_userinfo' ) )
  I1I . setProperty ( 'TVING_M_UUID' , credential . get ( 'tving_uuid' ) )
  if 24 - 24: I1ii11iIi11i
  I1I . setProperty ( 'TVING_M_LOGINTIME' , datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' ) )
  if 56 - 56: ooOoO0o
  if 92 - 92: iII111i . I11i + o0oOOo0O0Ooo
 def get_winCredential ( self ) :
  I1I = xbmcgui . Window ( 10000 )
  IiII1I11i1I1I = {
 'tving_token' : I1I . getProperty ( 'TVING_M_TOKEN' )
 , 'poc_userinfo' : I1I . getProperty ( 'TVING_M_USERINFO' )
 , 'tving_uuid' : I1I . getProperty ( 'TVING_M_UUID' )
 }
  return IiII1I11i1I1I
  if 83 - 83: I1ii11iIi11i / ooOoO0o
 def set_winEpisodeOrderby ( self , orderby ) :
  I1I = xbmcgui . Window ( 10000 )
  I1I . setProperty ( 'TVING_M_ORDERBY' , orderby )
  if 49 - 49: o0oOOo0O0Ooo
 def get_winEpisodeOrderby ( self ) :
  I1I = xbmcgui . Window ( 10000 )
  return I1I . getProperty ( 'TVING_M_ORDERBY' )
  if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
  if 78 - 78: I11i
  if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
  if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
 def add_dir ( self , label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
  iI1I111Ii111i = '%s?%s' % ( self . _addon_url , urllib . urlencode ( params ) )
  if 7 - 7: ooOoO0o * OoO0O00 % oO0o . IiII
  if sublabel : Ii1iIiII1ii1 = '%s < %s >' % ( label , sublabel )
  else : Ii1iIiII1ii1 = label
  if not img : img = 'DefaultFolder.png'
  if 62 - 62: iIii1I11I1II1 * OoOoOO00
  if 26 - 26: iII111i . I1Ii111
  oOOOOo0 = xbmcgui . ListItem ( Ii1iIiII1ii1 )
  oOOOOo0 . setArt ( { 'thumbnailImage' : img , 'icon' : img , 'poster' : img } )
  if 20 - 20: i1IIi + I1ii11iIi11i - ooOoO0o
  if infoLabels : oOOOOo0 . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : oOOOOo0 . setProperty ( 'IsPlayable' , 'true' )
  if 30 - 30: II111iiii - OOooOOo - i11iIiiIii % OoOoOO00 - II111iiii * Ii1I
  xbmcplugin . addDirectoryItem ( self . _addon_handle , iI1I111Ii111i , oOOOOo0 , isFolder )
  if 61 - 61: oO0o - I11i % OOooOOo
  if 84 - 84: oO0o * OoO0O00 / I11i - O0
  if 30 - 30: iIii1I11I1II1 / ooOoO0o - I1Ii111 - II111iiii % iII111i
 def get_selQuality ( self , etype ) :
  try :
   IIi1i11111 = 'selected_quality'
   if 81 - 81: i11iIiiIii % OoOoOO00 - OOooOOo
   if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
   if 92 - 92: iII111i . I1Ii111
   if 31 - 31: I1Ii111 . OoOoOO00 / O0
   if 89 - 89: OoOoOO00
   if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
   if 4 - 4: ooOoO0o + O0 * OOooOOo
   OOoo0O = [ 1080 , 720 , 480 , 360 ]
   if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
   o0oo = int ( __addon__ . getSetting ( IIi1i11111 ) )
   return OOoo0O [ o0oo ]
  except :
   None
   if 91 - 91: IiII
  return 720
  if 15 - 15: II111iiii
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
  if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
 def dp_Main_List ( self ) :
  if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
  for oOiIi1IIIi1 in Oo0oO0ooo :
   Ii1iIiII1ii1 = oOiIi1IIIi1 . get ( 'title' )
   if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
   iIIi1i1 = { 'mode' : oOiIi1IIIi1 . get ( 'mode' )
 , 'stype' : oOiIi1IIIi1 . get ( 'stype' )
 , 'orderby' : oOiIi1IIIi1 . get ( 'orderby' )
 , 'ordernm' : oOiIi1IIIi1 . get ( 'ordernm' )
 , 'page' : '1'
 }
   if 10 - 10: I11i
   if oOiIi1IIIi1 . get ( 'mode' ) == 'XXX' :
    iIIi1i1 [ 'mode' ] = 'XXX'
    OOooOO000 = False
   else :
    OOooOO000 = True
    if 97 - 97: I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = OOooOO000 , params = iIIi1i1 )
  if len ( Oo0oO0ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
 if 57 - 57: oO0o . I11i . i1IIi
 if 42 - 42: I11i + I1ii11iIi11i % O0
 if 6 - 6: oO0o
 if 68 - 68: OoOoOO00 - OoO0O00
 if 28 - 28: OoO0O00 . OOooOOo / OOooOOo + Oo0Ooo . I1ii11iIi11i
 if 1 - 1: iIii1I11I1II1 / II111iiii
 if 33 - 33: I11i
 if 18 - 18: o0oOOo0O0Ooo % iII111i * O0
 if 87 - 87: i11iIiiIii
 if 93 - 93: I1ii11iIi11i - OoO0O00 % i11iIiiIii . iII111i / iII111i - I1Ii111
 if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 if 91 - 91: iII111i % i1IIi % iIii1I11I1II1
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
 def login_main ( self ) :
  ( O0OO0O , OO , OoOoO ) = self . get_settings_login_info ( )
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  if not ( O0OO0O and OO ) :
   oO = xbmcgui . Dialog ( )
   o0 = oO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if o0 == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 37 - 37: oO0o - I1Ii111 % Oo0Ooo
  OOOoo0OO = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 57 - 57: OoO0O00 / ooOoO0o
  if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
   I111I1Iiii1i = 0
   while True :
    I111I1Iiii1i += 1
    if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
    time . sleep ( 0.05 )
    if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
    if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == OOOoo0OO : return
    if I111I1Iiii1i > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == OOOoo0OO :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   return
   if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  if not self . TvingObj . GetCredential ( O0OO0O , OO , OoOoO ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
   if 63 - 63: OoOoOO00 * iII111i
  self . set_winCredential ( self . TvingObj . LoadCredential ( ) )
  self . set_winEpisodeOrderby ( 'desc' )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  if 69 - 69: O0 . OoO0O00
  if 49 - 49: I1IiiI - I11i
  if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
  if 62 - 62: OoooooooOO * I1IiiI
 def dp_Title_Group ( self , args ) :
  oOOOoo0O0oO = args . get ( 'stype' )
  if oOOOoo0O0oO == 'live' :
   iIII1I111III = o00oOoo
  else :
   iIII1I111III = IiII1I1i1i1ii
   if 20 - 20: o0oOOo0O0Ooo . II111iiii % OOooOOo * iIii1I11I1II1
  for oO00oOOoooO in iIII1I111III :
   Ii1iIiII1ii1 = oO00oOOoooO . get ( 'title' )
   if 46 - 46: I1IiiI - OoooooooOO - I11i * II111iiii
   if args . get ( 'ordernm' ) != '-' :
    Ii1iIiII1ii1 += '  (' + args . get ( 'ordernm' ) + ')'
    if 34 - 34: I11i - iII111i / OOooOOo + I1ii11iIi11i * Ii1I
   iIIi1i1 = { 'mode' : oO00oOOoooO . get ( 'mode' )
 , 'stype' : oO00oOOoooO . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
   if 73 - 73: OoOoOO00 . Ii1I * I1ii11iIi11i % I1ii11iIi11i % OoooooooOO
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if len ( iIII1I111III ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
  if 32 - 32: OOooOOo
  if 42 - 42: IiII * O0 % i1IIi . OOooOOo / o0oOOo0O0Ooo
  if 32 - 32: I1IiiI * Oo0Ooo
 def dp_LiveChannel_List ( self , args ) :
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 29 - 29: I1IiiI % I1IiiI
  oOOOoo0O0oO = args . get ( 'stype' )
  Oo0O0 = int ( args . get ( 'page' ) )
  Ooo0OOoOoO0 , oOo0OOoO0 = self . TvingObj . GetLiveChannelList ( oOOOoo0O0oO , Oo0O0 )
  if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
  for IiII111i1i11 in Ooo0OOoOoO0 :
   Ii1iIiII1ii1 = IiII111i1i11 . get ( 'title' )
   i111iIi1i1II1 = IiII111i1i11 . get ( 'channel' )
   oooO = IiII111i1i11 . get ( 'thumbnail' )
   i1I1i111Ii = IiII111i1i11 . get ( 'synopsis' )
   ooo = IiII111i1i11 . get ( 'channelepg' )
   if 27 - 27: ooOoO0o % I1IiiI
   o0oooOO00 = IiII111i1i11 . get ( 'info' )
   o0oooOO00 [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( i111iIi1i1II1 , Ii1iIiII1ii1 , ooo , i1I1i111Ii )
   if 32 - 32: I1Ii111
   iIIi1i1 = { 'mode' : 'LIVE'
 , 'mediacode' : IiII111i1i11 . get ( 'mediacode' )
 , 'stype' : oOOOoo0O0oO
   }
   if 30 - 30: iIii1I11I1II1 / I11i . OoO0O00 - o0oOOo0O0Ooo
   self . add_dir ( i111iIi1i1II1 , sublabel = Ii1iIiII1ii1 , img = oooO , infoLabels = o0oooOO00 , isFolder = False , params = iIIi1i1 )
   if 48 - 48: i1IIi - Ii1I / O0 * OoO0O00
  if oOo0OOoO0 :
   if 71 - 71: I1ii11iIi11i
   iIIi1i1 [ 'mode' ] = 'CHANNEL'
   iIIi1i1 [ 'stype' ] = oOOOoo0O0oO
   iIIi1i1 [ 'page' ] = str ( Oo0O0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   IIiiIiiI = str ( Oo0O0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 10 - 10: OoOoOO00 % OoOoOO00 - OoOoOO00 . iII111i
  if len ( Ooo0OOoOoO0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  if 23 - 23: i11iIiiIii
 def dp_Program_List ( self , args ) :
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  oOOOoo0O0oO = args . get ( 'stype' )
  Ii1Iii1iIi = args . get ( 'orderby' )
  Oo0O0 = int ( args . get ( 'page' ) )
  if 82 - 82: I1ii11iIi11i / I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
  I1III1111iIi , oOo0OOoO0 = self . TvingObj . GetProgramList ( oOOOoo0O0oO , Ii1Iii1iIi , Oo0O0 , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 38 - 38: iII111i + I11i / I1Ii111 % ooOoO0o - I1ii11iIi11i
  for iI11 in I1III1111iIi :
   Ii1iIiII1ii1 = iI11 . get ( 'title' )
   oooO = iI11 . get ( 'thumbnail' )
   i1I1i111Ii = iI11 . get ( 'synopsis' )
   Ii1Io0OO0o0o00o = O0OoOoo00o . get ( iI11 . get ( 'channel' ) )
   if 100 - 100: oO0o / I1Ii111 / I1ii11iIi11i
   o0oooOO00 = iI11 . get ( 'info' )
   o0oooOO00 [ 'studio' ] = Ii1Io0OO0o0o00o
   o0oooOO00 [ 'plot' ] = '%s <%s>\n\n%s' % ( Ii1iIiII1ii1 , Ii1Io0OO0o0o00o , i1I1i111Ii )
   if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   iIIi1i1 = { 'mode' : 'EPISODE'
 , 'programcode' : iI11 . get ( 'program' )
 , 'page' : '1'
 }
   if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
   self . add_dir ( Ii1iIiII1ii1 , sublabel = Ii1Io0OO0o0o00o , img = oooO , infoLabels = o0oooOO00 , isFolder = True , params = iIIi1i1 )
   if 42 - 42: I1IiiI
  if oOo0OOoO0 :
   if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
   iIIi1i1 [ 'mode' ] = 'PROGRAM'
   iIIi1i1 [ 'stype' ] = oOOOoo0O0oO
   iIIi1i1 [ 'orderby' ] = Ii1Iii1iIi
   iIIi1i1 [ 'page' ] = str ( Oo0O0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   IIiiIiiI = str ( Oo0O0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  if len ( I1III1111iIi ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
 def dp_Episode_List ( self , args ) :
  if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
  i1 = args . get ( 'programcode' )
  Oo0O0 = int ( args . get ( 'page' ) )
  if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
  ii1 , oOo0OOoO0 , I1i11 = self . TvingObj . GetEpisodoList ( i1 , Oo0O0 , orderby = self . get_winEpisodeOrderby ( ) )
  if 51 - 51: OoO0O00 . I1IiiI * ooOoO0o % Ii1I + II111iiii . ooOoO0o
  for iI1IiI11ii1I1 in ii1 :
   Ii1iIiII1ii1 = iI1IiI11ii1I1 . get ( 'title' )
   IIiiIiiI = iI1IiI11ii1I1 . get ( 'subtitle' )
   oooO = iI1IiI11ii1I1 . get ( 'thumbnail' )
   i1I1i111Ii = iI1IiI11ii1I1 . get ( 'synopsis' )
   if 32 - 32: i11iIiiIii
   o0oooOO00 = iI1IiI11ii1I1 . get ( 'info' )
   o0oooOO00 [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , i1I1i111Ii )
   if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
   iIIi1i1 = { 'mode' : 'VOD'
 , 'mediacode' : iI1IiI11ii1I1 . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : i1
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : oooO
 }
   if 41 - 41: Oo0Ooo
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = oooO , infoLabels = o0oooOO00 , isFolder = False , params = iIIi1i1 )
   if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
   if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   if 20 - 20: I1IiiI
   if 95 - 95: iII111i - I1IiiI
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
  if Oo0O0 == 1 :
   o0oooOO00 = { 'plot' : '정렬순서를 변경합니다.' }
   iIIi1i1 = { }
   iIIi1i1 [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    Ii1iIiII1ii1 = '정렬순서변경 : 최신화부터 -> 1회부터'
    iIIi1i1 [ 'orderby' ] = 'asc'
   else :
    Ii1iIiII1ii1 = '정렬순서변경 : 1회부터 -> 최신화부터'
    iIIi1i1 [ 'orderby' ] = 'desc'
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = o0oooOO00 , isFolder = False , params = iIIi1i1 )
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  if oOo0OOoO0 :
   if 41 - 41: i1IIi - I11i - Ii1I
   iIIi1i1 [ 'mode' ] = 'EPISODE'
   iIIi1i1 [ 'programcode' ] = i1
   iIIi1i1 [ 'page' ] = str ( Oo0O0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   IIiiIiiI = str ( Oo0O0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  if len ( ii1 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
  if 44 - 44: II111iiii
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  if 35 - 35: iIii1I11I1II1
 def dp_setEpOrderby ( self , args ) :
  Ii1Iii1iIi = args . get ( 'orderby' )
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  self . set_winEpisodeOrderby ( Ii1Iii1iIi )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
 def dp_Movie_List ( self , args ) :
  if 71 - 71: O0 - iIii1I11I1II1
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  Ii1Iii1iIi = args . get ( 'orderby' )
  Oo0O0 = int ( args . get ( 'page' ) )
  if 42 - 42: Oo0Ooo
  II1IIiiIiI , oOo0OOoO0 = self . TvingObj . GetMovieList ( Ii1Iii1iIi , Oo0O0 , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 1 - 1: iII111i
  for O0O0Ooo in II1IIiiIiI :
   Ii1iIiII1ii1 = O0O0Ooo . get ( 'title' )
   oooO = O0O0Ooo . get ( 'thumbnail' )
   i1I1i111Ii = O0O0Ooo . get ( 'synopsis' )
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   o0oooOO00 = O0O0Ooo . get ( 'info' )
   o0oooOO00 [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , i1I1i111Ii )
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   iIIi1i1 = { 'mode' : 'MOVIE'
 , 'mediacode' : O0O0Ooo . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : oooO
 }
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = oooO , infoLabels = o0oooOO00 , isFolder = False , params = iIIi1i1 )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  if oOo0OOoO0 :
   if 17 - 17: i1IIi
   iIIi1i1 [ 'mode' ] = 'MOVIE_GROUP'
   iIIi1i1 [ 'orderby' ] = Ii1Iii1iIi
   iIIi1i1 [ 'page' ] = str ( Oo0O0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   IIiiIiiI = str ( Oo0O0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 21 - 21: Oo0Ooo
  if len ( II1IIiiIiI ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
 def dp_Search_Group ( self , args ) :
  for oO00oOOoooO in O0o0o00o0Oo0 :
   Ii1iIiII1ii1 = oO00oOOoooO . get ( 'title' )
   if 54 - 54: i1IIi + II111iiii
   iIIi1i1 = { 'mode' : oO00oOOoooO . get ( 'mode' )
 , 'stype' : oO00oOOoooO . get ( 'stype' )
 , 'page' : '1'
 }
   if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
  if len ( O0o0o00o0Oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 5 - 5: Ii1I
  if 46 - 46: IiII
  if 45 - 45: ooOoO0o
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
 def dp_Search_List ( self , args ) :
  if 17 - 17: OOooOOo / OOooOOo / I11i
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  OooO0oo = __addon__ . getSetting ( 'id' )
  Oo0O0 = int ( args . get ( 'page' ) )
  oOOOoo0O0oO = args . get ( 'stype' )
  if 89 - 89: Ii1I
  if 'search_key' in args :
   ooOoOO0OoO00o = args . get ( 'search_key' )
  else :
   ooOoOO0OoO00o = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not ooOoOO0OoO00o : return
   if 11 - 11: Oo0Ooo - I1IiiI * II111iiii . I1ii11iIi11i . oO0o
  O0OoOO0oo0 , oOo0OOoO0 = self . TvingObj . GetSearchList ( ooOoOO0OoO00o , OooO0oo , Oo0O0 , oOOOoo0O0oO , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if len ( O0OoOO0oo0 ) == 0 : return
  if 96 - 96: OoOoOO00 . o0oOOo0O0Ooo - ooOoO0o
  for O0O in O0OoOO0oo0 :
   Ii1iIiII1ii1 = O0O . get ( 'title' )
   oooO = O0O . get ( 'thumbnail' )
   i1I1i111Ii = O0O . get ( 'synopsis' )
   I11iiiii1II = O0O . get ( 'program' )
   if 51 - 51: O0 % oO0o - II111iiii
   o0oooOO00 = O0O . get ( 'info' )
   o0oooOO00 [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , i1I1i111Ii )
   if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
   if oOOOoo0O0oO == 'vod' :
    iIIi1i1 = { 'mode' : 'EPISODE'
 , 'programcode' : O0O . get ( 'program' )
 , 'page' : '1'
 }
    OOooOO000 = True
   else :
    iIIi1i1 = { 'mode' : 'MOVIE'
 , 'mediacode' : O0O . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : oooO
 }
    OOooOO000 = False
    if 7 - 7: iII111i % O0 . OoOoOO00 + I1IiiI - I11i
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = oooO , infoLabels = o0oooOO00 , isFolder = OOooOO000 , params = iIIi1i1 )
   if 75 - 75: I11i
  if oOo0OOoO0 :
   if 71 - 71: ooOoO0o
   iIIi1i1 [ 'mode' ] = 'SEARCH'
   iIIi1i1 [ 'search_key' ] = ooOoOO0OoO00o
   iIIi1i1 [ 'page' ] = str ( Oo0O0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   IIiiIiiI = str ( Oo0O0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = IIiiIiiI , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if 53 - 53: OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
  if len ( O0OoOO0oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 28 - 28: I11i
  if 58 - 58: OoOoOO00
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  if 73 - 73: i11iIiiIii - IiII
 def Delete_Watched_List ( self , stype ) :
  try :
   ii11I1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( ii11I1 , 'w' ) as oO0oo :
    oO0oo . write ( '' )
  except :
   None
   if 38 - 38: OoooooooOO * ooOoO0o % O0 * OoOoOO00
   if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
   if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
   if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
 def dp_WatchList_Delete ( self , args ) :
  oOOOoo0O0oO = args . get ( 'stype' )
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  oO = xbmcgui . Dialog ( )
  o0 = oO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if o0 == False : sys . exit ( )
  if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
  self . Delete_Watched_List ( oOOOoo0O0oO )
  if 74 - 74: O0 / i1IIi
  xbmc . executebuiltin ( "Container.Refresh" )
  if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
  if 31 - 31: OoooooooOO . OOooOOo
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
  if 100 - 100: OoO0O00
 def Load_Watched_List ( self , stype ) :
  try :
   ii11I1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( ii11I1 , 'r' ) as oO0oo :
    II1i = oO0oo . readlines ( )
  except :
   II1i = [ ]
   if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
  return II1i
  if 3 - 3: I1Ii111
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   ii11I1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   oOOoo = self . Load_Watched_List ( stype )
   if 14 - 14: o0oOOo0O0Ooo * oO0o
   with open ( ii11I1 , 'w' ) as oO0oo :
    O0OOO0OOooo00 = urllib . urlencode ( in_params )
    O0OOO0OOooo00 = O0OOO0OOooo00 . encode ( 'utf-8' ) + '\n'
    oO0oo . write ( O0OOO0OOooo00 )
    if 6 - 6: Ii1I - ooOoO0o * OOooOOo . iII111i / O0 * ooOoO0o
    II11iI111i1 = 0
    for Oo00OoOo in oOOoo :
     ii1ii111 = dict ( urlparse . parse_qsl ( Oo00OoOo ) )
     if in_params . get ( 'code' ) != ii1ii111 . get ( 'code' ) :
      oO0oo . write ( Oo00OoOo )
      II11iI111i1 += 1
      if II11iI111i1 >= 50 : break
  except :
   None
   if 33 - 33: I1ii11iIi11i
   if 92 - 92: IiII * Oo0Ooo * Oo0Ooo * I1IiiI . iIii1I11I1II1
   if 16 - 16: ooOoO0o % OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / OoooooooOO
   if 31 - 31: I11i . I1Ii111 * ooOoO0o + i11iIiiIii * oO0o
 def dp_Watch_List ( self , args ) :
  oOOOoo0O0oO = args . get ( 'stype' )
  if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * I11i
  if oOOOoo0O0oO == '-' :
   for oO00oOOoooO in OOooo0000ooo :
    Ii1iIiII1ii1 = oO00oOOoooO . get ( 'title' )
    if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . ooOoO0o % IiII
    iIIi1i1 = { 'mode' : oO00oOOoooO . get ( 'mode' )
 , 'stype' : oO00oOOoooO . get ( 'stype' )
 }
    if 50 - 50: iIii1I11I1II1 - IiII + OOooOOo
    self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = iIIi1i1 )
   if len ( OOooo0000ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 69 - 69: O0
  else :
   o0ooO = self . Load_Watched_List ( oOOOoo0O0oO )
   if 74 - 74: O0 * oO0o - i11iIiiIii + I1Ii111
   for Iii in o0ooO :
    I1iiiiI1iI = dict ( urlparse . parse_qsl ( Iii ) )
    if 43 - 43: oO0o - OoooooooOO
    Ii1iIiII1ii1 = I1iiiiI1iI . get ( 'title' )
    oooO = I1iiiiI1iI . get ( 'img' )
    if 3 - 3: O0 / iII111i
    o0oooOO00 = { }
    o0oooOO00 [ 'plot' ] = Ii1iIiII1ii1
    if 31 - 31: OOooOOo + o0oOOo0O0Ooo . OoooooooOO
    if oOOOoo0O0oO == 'vod' :
     iIIi1i1 = { 'mode' : 'EPISODE'
 , 'programcode' : I1iiiiI1iI . get ( 'code' )
 , 'page' : '1'
 }
     OOooOO000 = True
    else :
     iIIi1i1 = { 'mode' : 'MOVIE'
 , 'mediacode' : I1iiiiI1iI . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : oooO
 }
     OOooOO000 = False
     if 89 - 89: II111iiii + i1IIi + II111iiii
    self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = oooO , infoLabels = o0oooOO00 , isFolder = OOooOO000 , params = iIIi1i1 )
    if 7 - 7: O0 % o0oOOo0O0Ooo + I1ii11iIi11i * iII111i - iII111i
   o0oooOO00 = { 'plot' : '시청목록을 삭제합니다.' }
   Ii1iIiII1ii1 = '*** 시청목록 삭제 ***'
   iIIi1i1 = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : oOOOoo0O0oO
 }
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = o0oooOO00 , isFolder = False , params = iIIi1i1 )
   if 42 - 42: OoOoOO00 * OoOoOO00 * I1Ii111 . I11i
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 51 - 51: OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o * iIii1I11I1II1 % OoO0O00
   if 99 - 99: oO0o * II111iiii * I1Ii111
   if 92 - 92: Oo0Ooo
   if 40 - 40: OoOoOO00 / IiII
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
 def play_VIDEO ( self , args ) :
  if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 61 - 61: II111iiii
  Ii1ii111i1 = args . get ( 'mediacode' )
  oOOOoo0O0oO = args . get ( 'stype' )
  i1i1i1I = self . get_selQuality ( oOOOoo0O0oO )
  if 83 - 83: oO0o + OoooooooOO
  I111IiiIi1 , o00o = self . TvingObj . GetBroadURL ( Ii1ii111i1 , i1i1i1I , oOOOoo0O0oO )
  if 46 - 46: II111iiii % o0oOOo0O0Ooo % iIii1I11I1II1 - Oo0Ooo . OoooooooOO - IiII
  self . addon_log ( 'qt, stype, url : %s - %s - %s' % ( str ( i1i1i1I ) , oOOOoo0O0oO , I111IiiIi1 ) )
  if 59 - 59: IiII . OOooOOo % II111iiii
  if I111IiiIi1 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
   return
   if 39 - 39: I1ii11iIi11i
   if 97 - 97: OOooOOo - OoO0O00 / Ii1I . i11iIiiIii % oO0o * oO0o
   if 1 - 1: I1IiiI % ooOoO0o
  oOoO00 = I111IiiIi1 . find ( 'Policy=' )
  if oOoO00 != - 1 :
   iI1IIIii = I111IiiIi1 . split ( '?' ) [ 0 ]
   if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
   O0O0oOOo0O = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( I111IiiIi1 ) . query ) )
   O0O0oOOo0O = urllib . urlencode ( O0O0oOOo0O )
   O0O0oOOo0O = O0O0oOOo0O . replace ( '&' , ';' )
   O0O0oOOo0O = O0O0oOOo0O . replace ( 'Policy' , 'CloudFront-Policy' )
   O0O0oOOo0O = O0O0oOOo0O . replace ( 'Signature' , 'CloudFront-Signature' )
   O0O0oOOo0O = O0O0oOOo0O . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
   if 19 - 19: o0oOOo0O0Ooo / I1Ii111 % o0oOOo0O0Ooo % iII111i * IiII
   ii1oOoO0o0ooo = '%s|Cookie=%s' % ( iI1IIIii , O0O0oOOo0O )
  else :
   ii1oOoO0o0ooo = I111IiiIi1
   if 86 - 86: I1ii11iIi11i * O0 * IiII
   if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
  self . addon_log ( ii1oOoO0o0ooo , False )
  if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
  if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
  if 2 - 2: OoooooooOO % OOooOOo
  if 63 - 63: I1IiiI % iIii1I11I1II1
  I1ii = xbmcgui . ListItem ( path = ii1oOoO0o0ooo )
  if 73 - 73: IiII + I1IiiI * Oo0Ooo * OoooooooOO
  if 95 - 95: i1IIi + iIii1I11I1II1 % I1ii11iIi11i % Oo0Ooo / i11iIiiIii - IiII
  if o00o != '' :
   I1 = o00o
   O0iIi1IiII = 'https://cj.drmkeyserver.com/widevine_license'
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
 , 'referer' : 'https://www.tving.com/live/player/%s' % Ii1ii111i1
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
    , 'user-agent' : OoOooOOOO
 , 'AcquireLicenseAssertion' : I1
 , 'Host' : 'cj.drmkeyserver.com'
 }
    OoOOo000o0 = O0iIi1IiII + '|' + urllib . urlencode ( iiI11I1i1i1iI ) + '|R{SSM}|'
    if 12 - 12: II111iiii . I11i / OOooOOo
    I1ii . setProperty ( 'inputstreamaddon' , iii1 . inputstream_addon )
    if 77 - 77: ooOoO0o - I1IiiI % I11i - O0
    I1ii . setProperty ( 'inputstream.adaptive.manifest_type' , iIi1i )
    I1ii . setProperty ( 'inputstream.adaptive.license_type' , i1ii )
    if 67 - 67: OOooOOo + Oo0Ooo
    I1ii . setProperty ( 'inputstream.adaptive.license_key' , OoOOo000o0 )
    if 84 - 84: O0 * OoooooooOO - IiII * IiII
    if 8 - 8: ooOoO0o / i1IIi . oO0o
    if 41 - 41: iII111i + OoO0O00
    if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
    if 56 - 56: O0
  xbmcplugin . setResolvedUrl ( self . _addon_handle , True , I1ii )
  if 61 - 61: o0oOOo0O0Ooo / OOooOOo / Oo0Ooo * O0
  try :
   if args . get ( 'mode' ) in [ 'VOD' , 'MOVIE' ] and args . get ( 'title' ) :
    iIIi1i1 = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
    self . Save_Watched_List ( args . get ( 'stype' ) , iIIi1i1 )
  except :
   None
   if 23 - 23: oO0o - OOooOOo + I11i
   if 12 - 12: I1IiiI / ooOoO0o % o0oOOo0O0Ooo / i11iIiiIii % OoooooooOO
   if 15 - 15: iIii1I11I1II1 % OoooooooOO - Oo0Ooo * Ii1I + I11i
   if 11 - 11: iII111i * Ii1I - OoOoOO00
   if 66 - 66: OoOoOO00 . i11iIiiIii - iII111i * o0oOOo0O0Ooo + OoooooooOO * I1ii11iIi11i
   if 74 - 74: Oo0Ooo
 def tving_main ( self ) :
  OO000o00 = self . main_params . get ( 'mode' , None )
  if 46 - 46: OoO0O00
  self . login_main ( )
  if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
  if OO000o00 is None :
   self . dp_Main_List ( )
   if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
  elif OO000o00 in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
   self . dp_Title_Group ( self . main_params )
   if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
  elif OO000o00 == 'CHANNEL' :
   self . dp_LiveChannel_List ( self . main_params )
   if 68 - 68: OoooooooOO % II111iiii
  elif OO000o00 in [ 'LIVE' , 'VOD' , 'MOVIE' ] :
   self . play_VIDEO ( self . main_params )
   if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
   time . sleep ( 0.1 )
   if 24 - 24: II111iiii % I1Ii111 - ooOoO0o + I1IiiI * I1ii11iIi11i
  elif OO000o00 == 'PROGRAM' :
   self . dp_Program_List ( self . main_params )
   if 2 - 2: Ii1I - IiII
  elif OO000o00 == 'EPISODE' :
   self . dp_Episode_List ( self . main_params )
   if 83 - 83: oO0o % o0oOOo0O0Ooo % Ii1I - II111iiii * OOooOOo / OoooooooOO
  elif OO000o00 == 'MOVIE_GROUP' :
   self . dp_Movie_List ( self . main_params )
   if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
  elif OO000o00 == 'SEARCH_GROUP' :
   self . dp_Search_Group ( self . main_params )
   if 71 - 71: OoooooooOO
  elif OO000o00 == 'SEARCH' :
   self . dp_Search_List ( self . main_params )
   if 33 - 33: I1Ii111
  elif OO000o00 == 'WATCH' :
   self . dp_Watch_List ( self . main_params )
   if 62 - 62: I1ii11iIi11i + Ii1I + i1IIi / OoooooooOO
  elif OO000o00 == 'MYVIEW_REMOVE' :
   self . dp_WatchList_Delete ( self . main_params )
   if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
  elif OO000o00 == 'ORDER_BY' :
   self . dp_setEpOrderby ( self . main_params )
   if 22 - 22: ooOoO0o - ooOoO0o % OOooOOo . I1Ii111 + oO0o
  else :
   None
   if 63 - 63: I1IiiI % I1Ii111 * o0oOOo0O0Ooo + I1Ii111 / Oo0Ooo % iII111i
   if 45 - 45: IiII
   if 20 - 20: OoooooooOO * o0oOOo0O0Ooo * O0 . OOooOOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
