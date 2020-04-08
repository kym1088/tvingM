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
  i1 = xbmcgui . ListItem ( Ii1iIiII1ii1 , thumbnailImage = img )
  if infoLabels : i1 . setInfo ( type = "Video" , infoLabels = infoLabels )
  if not isFolder : i1 . setProperty ( 'IsPlayable' , 'true' )
  if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
  xbmcplugin . addDirectoryItem ( self . _addon_handle , iI1I111Ii111i , i1 , isFolder )
  if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
  if 98 - 98: I1ii11iIi11i / I11i % oO0o . OoOoOO00
  if 91 - 91: oO0o % Oo0Ooo
 def get_selQuality ( self , etype ) :
  try :
   if etype == 'movie' :
    O0O0O0OoOO = 'movie_quality'
   else :
    O0O0O0OoOO = 'selected_quality'
    if 74 - 74: II111iiii
   oO0 = [ 1080 , 720 , 480 , 360 ]
   if 54 - 54: II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + iIii1I11I1II1 * ooOoO0o
   O00O0oOO00O00 = int ( __addon__ . getSetting ( O0O0O0OoOO ) )
   return oO0 [ O00O0oOO00O00 ]
  except :
   None
   if 11 - 11: IiII . I1ii11iIi11i
  return 720
  if 92 - 92: iII111i . I1Ii111
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  if 89 - 89: OoOoOO00
 def dp_Main_List ( self ) :
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
  for i11i1I1 in Oo0oO0ooo :
   Ii1iIiII1ii1 = i11i1I1 . get ( 'title' )
   if 36 - 36: iIii1I11I1II1 / OoOoOO00 * OOooOOo
   O0ii1ii1ii = { 'mode' : i11i1I1 . get ( 'mode' )
 , 'stype' : i11i1I1 . get ( 'stype' )
 , 'orderby' : i11i1I1 . get ( 'orderby' )
 , 'ordernm' : i11i1I1 . get ( 'ordernm' )
 , 'page' : '1'
 }
   if 91 - 91: IiII
   if i11i1I1 . get ( 'mode' ) == 'XXX' :
    O0ii1ii1ii [ 'mode' ] = 'XXX'
    iiIii = False
   else :
    iiIii = True
    if 79 - 79: OoooooooOO / O0
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = iiIii , params = O0ii1ii1ii )
  if len ( Oo0oO0ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
 if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
 if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 if 91 - 91: O0
 if 61 - 61: II111iiii
 if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 if 42 - 42: OoO0O00
 if 67 - 67: I1Ii111 . iII111i . O0
 if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
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
 def login_main ( self ) :
  ( o0O , IiIIii1iII1II , Iii1I1I11iiI1 ) = self . get_settings_login_info ( )
  if 18 - 18: OOooOOo + iII111i - Ii1I . II111iiii + i11iIiiIii
  if 20 - 20: I1Ii111
  if not ( o0O and IiIIii1iII1II ) :
   oO = xbmcgui . Dialog ( )
   Oo0oO00o = oO . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
   if Oo0oO00o == True :
    __addon__ . openSettings ( )
    sys . exit ( )
    if 13 - 13: I11i * Oo0Ooo * ooOoO0o
  iI11iI1IiiIiI = datetime . datetime . now ( ) . strftime ( '%Y-%m-%d' )
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINWAIT' ) == 'TRUE' :
   o0 = 0
   while True :
    o0 += 1
    if 37 - 37: oO0o - I1Ii111 % Oo0Ooo
    time . sleep ( 0.05 )
    if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
    if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == iI11iI1IiiIiI : return
    if o0 > 600 : return
  else :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'TRUE' )
   if 39 - 39: II111iiii / ooOoO0o + I1Ii111 / OoOoOO00
  if xbmcgui . Window ( 10000 ) . getProperty ( 'TVING_M_LOGINTIME' ) == iI11iI1IiiIiI :
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   return
   if 13 - 13: IiII + O0 + iII111i % I1IiiI / o0oOOo0O0Ooo . IiII
   if 86 - 86: oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
  if not self . TvingObj . GetCredential ( o0O , IiIIii1iII1II , Iii1I1I11iiI1 ) :
   self . addon_noti ( __language__ ( 30103 ) . encode ( 'utf8' ) )
   xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
   sys . exit ( )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
  self . set_winCredential ( self . TvingObj . LoadCredential ( ) )
  self . set_winEpisodeOrderby ( 'desc' )
  xbmcgui . Window ( 10000 ) . setProperty ( 'TVING_M_LOGINWAIT' , 'FALSE' )
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
 def dp_Title_Group ( self , args ) :
  oO00oooOOoOo0 = args . get ( 'stype' )
  if oO00oooOOoOo0 == 'live' :
   OoOOoOooooOOo = o00oOoo
  else :
   OoOOoOooooOOo = IiII1I1i1i1ii
   if 87 - 87: I1IiiI
  for oOOOoo0O0oO in OoOOoOooooOOo :
   Ii1iIiII1ii1 = oOOOoo0O0oO . get ( 'title' )
   if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
   if args . get ( 'ordernm' ) != '-' :
    Ii1iIiII1ii1 += '  (' + args . get ( 'ordernm' ) + ')'
    if 44 - 44: Ii1I % OoO0O00 + OoooooooOO - O0 - Ii1I - II111iiii
   O0ii1ii1ii = { 'mode' : oOOOoo0O0oO . get ( 'mode' )
 , 'stype' : oOOOoo0O0oO . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
   if 99 - 99: ooOoO0o . Ii1I + I1Ii111 + OoooooooOO % o0oOOo0O0Ooo
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if len ( OoOOoOooooOOo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 51 - 51: iIii1I11I1II1
  if 34 - 34: oO0o + I1IiiI - oO0o
  if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
  if 59 - 59: OOooOOo % OoOoOO00 . Ii1I * I1ii11iIi11i % I11i
 def dp_LiveChannel_List ( self , args ) :
  if 59 - 59: oO0o - iII111i
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 15 - 15: I1Ii111 . i11iIiiIii . OoooooooOO / OoO0O00 % Ii1I
  oO00oooOOoOo0 = args . get ( 'stype' )
  OooooOOoo0 = int ( args . get ( 'page' ) )
  i1I1IiiIi1i , iiI11ii1I1 = self . TvingObj . GetLiveChannelList ( oO00oooOOoOo0 , OooooOOoo0 )
  if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
  for oOo0OOoO0 in i1I1IiiIi1i :
   Ii1iIiII1ii1 = oOo0OOoO0 . get ( 'title' )
   II = oOo0OOoO0 . get ( 'channel' )
   o0Oo0oO0oOO00 = oOo0OOoO0 . get ( 'thumbnail' )
   oo00OO0000oO = oOo0OOoO0 . get ( 'synopsis' )
   I1II1 = oOo0OOoO0 . get ( 'channelepg' )
   if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
   II1i111Ii1i = { }
   II1i111Ii1i [ 'plot' ] = '%s\n%s\n%s\n\n%s' % ( II , Ii1iIiII1ii1 , I1II1 , oo00OO0000oO )
   if 15 - 15: II111iiii / i1IIi
   O0ii1ii1ii = { 'mode' : 'LIVE'
 , 'mediacode' : oOo0OOoO0 . get ( 'mediacode' )
 , 'stype' : oO00oooOOoOo0
   }
   if 76 - 76: I11i / OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + IiII
   self . add_dir ( II , sublabel = Ii1iIiII1ii1 , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = False , params = O0ii1ii1ii )
   if 71 - 71: I1Ii111 . II111iiii
  if iiI11ii1I1 :
   if 62 - 62: OoooooooOO . I11i
   O0ii1ii1ii [ 'mode' ] = 'CHANNEL'
   O0ii1ii1ii [ 'stype' ] = oO00oooOOoOo0
   O0ii1ii1ii [ 'page' ] = str ( OooooOOoo0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   oOOOoo00 = str ( OooooOOoo0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = oOOOoo00 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
  if len ( i1I1IiiIi1i ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
  if 52 - 52: o0oOOo0O0Ooo + O0 + iII111i + Oo0Ooo % iII111i
  if 75 - 75: I1IiiI . ooOoO0o . O0 * I1Ii111
  if 4 - 4: Ii1I % oO0o * OoO0O00
 def dp_Program_List ( self , args ) :
  if 100 - 100: I1Ii111 * OOooOOo + OOooOOo
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
  oO00oooOOoOo0 = args . get ( 'stype' )
  iII1iIi11i = args . get ( 'orderby' )
  OooooOOoo0 = int ( args . get ( 'page' ) )
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  Ii1Iii1iIi , iiI11ii1I1 = self . TvingObj . GetProgramList ( oO00oooOOoOo0 , iII1iIi11i , OooooOOoo0 , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 82 - 82: I1ii11iIi11i / I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
  for I1III1111iIi in Ii1Iii1iIi :
   Ii1iIiII1ii1 = I1III1111iIi . get ( 'title' )
   o0Oo0oO0oOO00 = I1III1111iIi . get ( 'thumbnail' )
   oo00OO0000oO = I1III1111iIi . get ( 'synopsis' )
   I1i111I = O0OoOoo00o . get ( I1III1111iIi . get ( 'channel' ) )
   if 97 - 97: i1IIi . oO0o / iII111i * O0
   II1i111Ii1i = { }
   II1i111Ii1i [ 'plot' ] = '%s <%s>\n\n%s' % ( Ii1iIiII1ii1 , I1i111I , oo00OO0000oO )
   if 73 - 73: OOooOOo / oO0o
   O0ii1ii1ii = { 'mode' : 'EPISODE'
 , 'programcode' : I1III1111iIi . get ( 'program' )
 , 'page' : '1'
 }
   if 88 - 88: I11i % I1ii11iIi11i
   self . add_dir ( Ii1iIiII1ii1 , sublabel = I1i111I , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = True , params = O0ii1ii1ii )
   if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
  if iiI11ii1I1 :
   if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   O0ii1ii1ii [ 'mode' ] = 'PROGRAM'
   O0ii1ii1ii [ 'stype' ] = oO00oooOOoOo0
   O0ii1ii1ii [ 'orderby' ] = iII1iIi11i
   O0ii1ii1ii [ 'page' ] = str ( OooooOOoo0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   oOOOoo00 = str ( OooooOOoo0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = oOOOoo00 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 10 - 10: iII111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / I1Ii111 / I1ii11iIi11i
  if len ( Ii1Iii1iIi ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 42 - 42: I1IiiI
  if 38 - 38: OOooOOo + II111iiii % ooOoO0o % OoOoOO00 - Ii1I / OoooooooOO
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  if 85 - 85: Ii1I % iII111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 def dp_Episode_List ( self , args ) :
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  iII1i1 = args . get ( 'programcode' )
  OooooOOoo0 = int ( args . get ( 'page' ) )
  if 85 - 85: Ii1I * Oo0Ooo . O0 - i11iIiiIii
  i1I1iIi , iiI11ii1I1 , IIii11Ii1i1I = self . TvingObj . GetEpisodoList ( iII1i1 , OooooOOoo0 , orderby = self . get_winEpisodeOrderby ( ) )
  if 76 - 76: O0 + i1IIi . Oo0Ooo * I1IiiI * Ii1I
  for II1iI1I11I in i1I1iIi :
   Ii1iIiII1ii1 = II1iI1I11I . get ( 'title' )
   o0Oo0oO0oOO00 = II1iI1I11I . get ( 'thumbnail' )
   oo00OO0000oO = II1iI1I11I . get ( 'synopsis' )
   if 78 - 78: II111iiii
   II1i111Ii1i = { }
   II1i111Ii1i [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , oo00OO0000oO )
   if 100 - 100: I1Ii111 + OOooOOo + OOooOOo
   O0ii1ii1ii = { 'mode' : 'VOD'
 , 'mediacode' : II1iI1I11I . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : iII1i1
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : o0Oo0oO0oOO00
 }
   if 9 - 9: I11i % OoooooooOO . oO0o % I11i
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = False , params = O0ii1ii1ii )
   if 32 - 32: i11iIiiIii
   if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
   if 41 - 41: Oo0Ooo
   if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
   if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
  if OooooOOoo0 == 1 :
   II1i111Ii1i = { 'plot' : '정렬순서를 변경합니다.' }
   O0ii1ii1ii = { }
   O0ii1ii1ii [ 'mode' ] = 'ORDER_BY'
   if self . get_winEpisodeOrderby ( ) == 'desc' :
    Ii1iIiII1ii1 = '정렬순서변경 : 최신화부터 -> 1회부터'
    O0ii1ii1ii [ 'orderby' ] = 'asc'
   else :
    Ii1iIiII1ii1 = '정렬순서변경 : 1회부터 -> 최신화부터'
    O0ii1ii1ii [ 'orderby' ] = 'desc'
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = II1i111Ii1i , isFolder = False , params = O0ii1ii1ii )
   if 20 - 20: I1IiiI
   if 95 - 95: iII111i - I1IiiI
  if iiI11ii1I1 :
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
   O0ii1ii1ii [ 'mode' ] = 'EPISODE'
   O0ii1ii1ii [ 'programcode' ] = iII1i1
   O0ii1ii1ii [ 'page' ] = str ( OooooOOoo0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   oOOOoo00 = str ( OooooOOoo0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = oOOOoo00 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  if len ( i1I1iIi ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
  if 41 - 41: i1IIi - I11i - Ii1I
  if 8 - 8: OoO0O00 + I1Ii111 - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
  if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + ooOoO0o
 def dp_setEpOrderby ( self , args ) :
  iII1iIi11i = args . get ( 'orderby' )
  if 44 - 44: II111iiii
  self . set_winEpisodeOrderby ( iII1iIi11i )
  xbmc . executebuiltin ( "Container.Refresh" )
  if 52 - 52: I1ii11iIi11i - Oo0Ooo + I1ii11iIi11i % o0oOOo0O0Ooo
  if 35 - 35: iIii1I11I1II1
  if 42 - 42: I1Ii111 . I1IiiI . i1IIi + OoOoOO00 + OOooOOo + I1IiiI
  if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
 def dp_Movie_List ( self , args ) :
  if 56 - 56: OoO0O00 / oO0o / i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
  iII1iIi11i = args . get ( 'orderby' )
  OooooOOoo0 = int ( args . get ( 'page' ) )
  if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  oooooo0OO , iiI11ii1I1 = self . TvingObj . GetMovieList ( iII1iIi11i , OooooOOoo0 , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if 14 - 14: oO0o / oO0o % ooOoO0o
  for ooO in oooooo0OO :
   Ii1iIiII1ii1 = ooO . get ( 'title' )
   o0Oo0oO0oOO00 = ooO . get ( 'thumbnail' )
   oo00OO0000oO = ooO . get ( 'synopsis' )
   if 6 - 6: iIii1I11I1II1 . ooOoO0o % o0oOOo0O0Ooo
   II1i111Ii1i = { }
   II1i111Ii1i [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , oo00OO0000oO )
   if 50 - 50: iII111i + O0 + Ii1I . II111iiii / o0oOOo0O0Ooo
   O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'mediacode' : ooO . get ( 'moviecode' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : o0Oo0oO0oOO00
 }
   if 17 - 17: Ii1I % iIii1I11I1II1 - iIii1I11I1II1
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = False , params = O0ii1ii1ii )
   if 78 - 78: iII111i + I11i . ooOoO0o - iII111i . Ii1I
  if iiI11ii1I1 :
   if 30 - 30: I1IiiI + OoO0O00 % Ii1I * iII111i / Oo0Ooo - I11i
   O0ii1ii1ii [ 'mode' ] = 'MOVIE_GROUP'
   O0ii1ii1ii [ 'orderby' ] = iII1iIi11i
   O0ii1ii1ii [ 'page' ] = str ( OooooOOoo0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   oOOOoo00 = str ( OooooOOoo0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = oOOOoo00 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 64 - 64: iIii1I11I1II1
  if len ( oooooo0OO ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
  if 21 - 21: Oo0Ooo . II111iiii
  if 54 - 54: II111iiii % II111iiii
  if 86 - 86: O0 % Ii1I * ooOoO0o * iIii1I11I1II1 * i1IIi * I11i
  if 83 - 83: OoOoOO00 % II111iiii - OoOoOO00 + IiII - O0
 def dp_Search_Group ( self , args ) :
  for oOOOoo0O0oO in O0o0o00o0Oo0 :
   Ii1iIiII1ii1 = oOOOoo0O0oO . get ( 'title' )
   if 52 - 52: Oo0Ooo * ooOoO0o
   O0ii1ii1ii = { 'mode' : oOOOoo0O0oO . get ( 'mode' )
 , 'stype' : oOOOoo0O0oO . get ( 'stype' )
 , 'page' : '1'
 }
   if 33 - 33: Ii1I
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
  if len ( O0o0o00o0Oo0 ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if 5 - 5: Ii1I
  if 46 - 46: IiII
 def dp_Search_List ( self , args ) :
  if 45 - 45: ooOoO0o
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  i1iI1 = __addon__ . getSetting ( 'id' )
  OooooOOoo0 = int ( args . get ( 'page' ) )
  oO00oooOOoOo0 = args . get ( 'stype' )
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  if 'search_key' in args :
   OooO0oo = args . get ( 'search_key' )
  else :
   OooO0oo = self . get_keyboard_input ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
   if not OooO0oo : return
   if 89 - 89: Ii1I
  ooOoOO0OoO00o , iiI11ii1I1 = self . TvingObj . GetSearchList ( OooO0oo , i1iI1 , OooooOOoo0 , oO00oooOOoOo0 , premiumyn = self . get_settings_premiumyn ( ) , landyn = self . get_settings_thumbnail_landyn ( ) )
  if len ( ooOoOO0OoO00o ) == 0 : return
  if 11 - 11: Oo0Ooo - I1IiiI * II111iiii . I1ii11iIi11i . oO0o
  for O0OoOO0oo0 in ooOoOO0OoO00o :
   Ii1iIiII1ii1 = O0OoOO0oo0 . get ( 'title' )
   o0Oo0oO0oOO00 = O0OoOO0oo0 . get ( 'thumbnail' )
   oo00OO0000oO = O0OoOO0oo0 . get ( 'synopsis' )
   oOO = O0OoOO0oo0 . get ( 'program' )
   if 53 - 53: I1Ii111 * IiII . Oo0Ooo - Ii1I % Ii1I * i11iIiiIii
   II1i111Ii1i = { }
   II1i111Ii1i [ 'plot' ] = '%s\n\n%s' % ( Ii1iIiII1ii1 , oo00OO0000oO )
   if 7 - 7: O0 . Ii1I
   if oO00oooOOoOo0 == 'vod' :
    O0ii1ii1ii = { 'mode' : 'EPISODE'
 , 'programcode' : O0OoOO0oo0 . get ( 'program' )
 , 'page' : '1'
 }
    iiIii = True
   else :
    O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'mediacode' : O0OoOO0oo0 . get ( 'movie' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : o0Oo0oO0oOO00
 }
    iiIii = False
    if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = iiIii , params = O0ii1ii1ii )
   if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
  if iiI11ii1I1 :
   if 7 - 7: iII111i % O0 . OoOoOO00 + I1IiiI - I11i
   O0ii1ii1ii [ 'mode' ] = 'SEARCH'
   O0ii1ii1ii [ 'search_key' ] = OooO0oo
   O0ii1ii1ii [ 'page' ] = str ( OooooOOoo0 + 1 )
   Ii1iIiII1ii1 = '[B]%s >>[/B]' % '다음 페이지'
   oOOOoo00 = str ( OooooOOoo0 + 1 )
   self . add_dir ( Ii1iIiII1ii1 , sublabel = oOOOoo00 , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if 75 - 75: I11i
  if len ( ooOoOO0OoO00o ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
  if 71 - 71: ooOoO0o
  if 53 - 53: OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
  if 28 - 28: I11i
  if 58 - 58: OoOoOO00
 def Delete_Watched_List ( self , stype ) :
  try :
   iIiiI1iI = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( iIiiI1iI , 'w' ) as IIIi :
    IIIi . write ( '' )
  except :
   None
   if 94 - 94: I1Ii111 - OoO0O00 % OoO0O00 / II111iiii % Oo0Ooo . o0oOOo0O0Ooo
   if 91 - 91: ooOoO0o % ooOoO0o
   if 7 - 7: iII111i / I1ii11iIi11i / i11iIiiIii
   if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
 def dp_WatchList_Delete ( self , args ) :
  oO00oooOOoOo0 = args . get ( 'stype' )
  if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
  oO = xbmcgui . Dialog ( )
  Oo0oO00o = oO . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
  if Oo0oO00o == False : sys . exit ( )
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
  self . Delete_Watched_List ( oO00oooOOoOo0 )
  if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
  xbmc . executebuiltin ( "Container.Refresh" )
  if 97 - 97: I1IiiI / iII111i
  if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
  if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 def Load_Watched_List ( self , stype ) :
  try :
   iIiiI1iI = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   with open ( iIiiI1iI , 'r' ) as IIIi :
    oO0oO0 = IIIi . readlines ( )
  except :
   oO0oO0 = [ ]
   if 14 - 14: iII111i
  return oO0oO0
  if 99 - 99: iII111i
  if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
  if 45 - 45: I1Ii111
  if 83 - 83: OoOoOO00 . OoooooooOO
 def Save_Watched_List ( self , stype , in_params ) :
  try :
   iIiiI1iI = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
   Oo0ooo = self . Load_Watched_List ( stype )
   if 28 - 28: oO0o . II111iiii / I1ii11iIi11i + II111iiii . OoooooooOO . IiII
   with open ( iIiiI1iI , 'w' ) as IIIi :
    O000OOO0OOo = urllib . urlencode ( in_params )
    O000OOO0OOo = O000OOO0OOo . encode ( 'utf-8' ) + '\n'
    IIIi . write ( O000OOO0OOo )
    if 32 - 32: Ii1I * O0
    O00oOo00o0o = 0
    for O00oO0 in Oo0ooo :
     O0Oo00OoOo = dict ( urlparse . parse_qsl ( O00oO0 ) )
     if in_params . get ( 'code' ) != O0Oo00OoOo . get ( 'code' ) :
      IIIi . write ( O00oO0 )
      O00oOo00o0o += 1
      if O00oOo00o0o >= 50 : break
  except :
   None
   if 24 - 24: i11iIiiIii - I1Ii111
   if 21 - 21: I11i
   if 92 - 92: i11iIiiIii / I1Ii111 - iII111i % ooOoO0o * I1Ii111 + Oo0Ooo
   if 11 - 11: OoooooooOO . I1Ii111
 def dp_Watch_List ( self , args ) :
  oO00oooOOoOo0 = args . get ( 'stype' )
  if 80 - 80: OoooooooOO - OOooOOo * Ii1I * I1ii11iIi11i / I1IiiI / OOooOOo
  if oO00oooOOoOo0 == '-' :
   for oOOOoo0O0oO in OOooo0000ooo :
    Ii1iIiII1ii1 = oOOOoo0O0oO . get ( 'title' )
    if 13 - 13: I1Ii111 * ooOoO0o + i11iIiiIii * I1Ii111 - ooOoO0o
    O0ii1ii1ii = { 'mode' : oOOOoo0O0oO . get ( 'mode' )
 , 'stype' : oOOOoo0O0oO . get ( 'stype' )
 }
    if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * IiII
    self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = O0ii1ii1ii )
   if len ( OOooo0000ooo ) > 0 : xbmcplugin . endOfDirectory ( self . _addon_handle )
   if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  else :
   I1IIIiI1I1ii1 = self . Load_Watched_List ( oO00oooOOoOo0 )
   if 30 - 30: O0 * OoooooooOO
   for I1iIIIi1 in I1IIIiI1I1ii1 :
    Iii = dict ( urlparse . parse_qsl ( I1iIIIi1 ) )
    if 19 - 19: I11i % II111iiii / i11iIiiIii / iII111i - OoooooooOO
    Ii1iIiII1ii1 = Iii . get ( 'title' )
    o0Oo0oO0oOO00 = Iii . get ( 'img' )
    if 37 - 37: OOooOOo / OoooooooOO - i11iIiiIii
    II1i111Ii1i = { }
    II1i111Ii1i [ 'plot' ] = Ii1iIiII1ii1
    if 18 - 18: iII111i . I1IiiI
    if oO00oooOOoOo0 == 'vod' :
     O0ii1ii1ii = { 'mode' : 'EPISODE'
 , 'programcode' : Iii . get ( 'code' )
 , 'page' : '1'
 }
     iiIii = True
    else :
     O0ii1ii1ii = { 'mode' : 'MOVIE'
 , 'mediacode' : Iii . get ( 'code' )
 , 'stype' : 'movie'
 , 'title' : Ii1iIiII1ii1
 , 'thumbnail' : o0Oo0oO0oOO00
 }
     iiIii = False
     if 40 - 40: O0 - OoooooooOO - IiII
    self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = o0Oo0oO0oOO00 , infoLabels = II1i111Ii1i , isFolder = iiIii , params = O0ii1ii1ii )
    if 37 - 37: OoOoOO00 / II111iiii / O0
   II1i111Ii1i = { 'plot' : '시청목록을 삭제합니다.' }
   Ii1iIiII1ii1 = '*** 시청목록 삭제 ***'
   O0ii1ii1ii = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : oO00oooOOoOo0
 }
   self . add_dir ( Ii1iIiII1ii1 , sublabel = '' , img = '' , infoLabels = II1i111Ii1i , isFolder = False , params = O0ii1ii1ii )
   if 76 - 76: I1IiiI . ooOoO0o - I1ii11iIi11i - iII111i * OoO0O00
   xbmcplugin . endOfDirectory ( self . _addon_handle , cacheToDisc = False )
   if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
   if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
   if 63 - 63: I1Ii111 / O0 * Oo0Ooo + II111iiii / IiII + Ii1I
   if 63 - 63: OoO0O00 + I1ii11iIi11i . I1Ii111 % I1Ii111
   if 57 - 57: II111iiii
 def play_VIDEO ( self , args ) :
  if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
  self . TvingObj . SaveCredential ( self . get_winCredential ( ) )
  if 28 - 28: oO0o
  ooo000o0ooO0 = args . get ( 'mediacode' )
  oO00oooOOoOo0 = args . get ( 'stype' )
  I1IoOoo000 = self . get_selQuality ( oO00oooOOoOo0 )
  if 87 - 87: OoooooooOO - o0oOOo0O0Ooo / IiII . i11iIiiIii * OoooooooOO
  OO00 , IIiiIIi1 = self . TvingObj . GetBroadURL ( ooo000o0ooO0 , I1IoOoo000 , oO00oooOOoOo0 )
  if 59 - 59: IiII . OOooOOo % II111iiii
  self . addon_log ( 'qt, stype, url : %s - %s - %s' % ( str ( I1IoOoo000 ) , oO00oooOOoOo0 , OO00 ) )
  if 39 - 39: I1ii11iIi11i
  if OO00 == '' :
   self . addon_noti ( __language__ ( 30303 ) . encode ( 'utf8' ) )
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
  self . addon_log ( I1iii , False )
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
   iIi1i = 'mpd'
   i1ii = 'com.widevine.alpha'
   if 68 - 68: OOooOOo * O0 . I11i - II111iiii . ooOoO0o / II111iiii
   iii1 = inputstreamhelper . Helper ( iIi1i , drm = i1ii )
   if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
   if iii1 . check_inputstream ( ) :
    if 88 - 88: iII111i
    iiI11I1i1i1iI = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % ooo000o0ooO0
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
    O0ii1ii1ii = { 'code' : args . get ( 'programcode' ) if args . get ( 'mode' ) == 'VOD' else args . get ( 'mediacode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
    self . Save_Watched_List ( args . get ( 'stype' ) , O0ii1ii1ii )
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
