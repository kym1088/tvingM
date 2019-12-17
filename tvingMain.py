# -*- coding: utf-8 -*-
__author__ = "NightRain"
__email__ = "kym1088@naver.com"
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
 , { 'title' : '-----------------' , 'mode' : 'XXX' , 'stype' : 'XXX' , 'orderby' : '-' }
 , { 'title' : 'Watched (시청목록)' , 'mode' : 'WATCH' , 'stype' : 'vod' , 'orderby' : '-' }
 , { 'title' : '검색 (VOD)' , 'mode' : 'SEARCH' , 'stype' : 'vod' , 'orderby' : '-' }
 ]
if 100 - 100: i1IIi
I1Ii11I1Ii1i = [
 { 'title' : '실시간 TV' , 'mode' : 'CHANNEL' , 'stype' : 'onair' }
 , { 'title' : 'TVING TV' , 'mode' : 'CHANNEL' , 'stype' : 'tvingtv' }
 ]
if 67 - 67: iIii1I11I1II1 . I1ii11iIi11i . oO0o / i1IIi % II111iiii - OoOoOO00
OOo = [
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
if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111
Oooo0000 = { 'C00551' : 'tvN'
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
if 22 - 22: Ii1I . IiII
from tvingCore import *
if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
if 74 - 74: iII111i * IiII
def oo00o0Oo0oo ( sting ) :
 try :
  i1iII1I1i1i1 = xbmcgui . Dialog ( )
  i1iII1I1i1i1 . notification ( __name__ , sting )
 except :
  None
  if 27 - 27: OoO0O00
  if 73 - 73: o0oOOo0O0Ooo - Oo0Ooo
  if 58 - 58: i11iIiiIii % I1Ii111
def O0OoOoo00o ( string , isDebug = False ) :
 try :
  iiiI11 = string . encode ( 'utf-8' , 'ignore' )
 except :
  iiiI11 = 'addonException: addon_log'
 if isDebug : OOooO = xbmc . LOGDEBUG
 else : OOooO = xbmc . LOGNOTICE
 xbmc . log ( "[%s-%s]: %s" % ( __addonid__ , __version__ , iiiI11 ) , level = OOooO )
 if 58 - 58: OoO0O00 + OoOoOO00 / Ii1I * OoooooooOO
 if 9 - 9: I1IiiI - Ii1I % i1IIi % OoooooooOO
 if 3 - 3: iII111i + O0
 if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
def oo0Ooo0 ( title ) :
 I1I11I1I1I = None
 OooO0OO = xbmc . Keyboard ( )
 OooO0OO . setHeading ( title )
 xbmc . sleep ( 1000 )
 OooO0OO . doModal ( )
 if ( OooO0OO . isConfirmed ( ) ) :
  I1I11I1I1I = OooO0OO . getText ( )
 return I1I11I1I1I
 if 28 - 28: II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
 if 70 - 70: OoO0O00 . OoO0O00 - OoO0O00 / I1ii11iIi11i * OOooOOo
 if 86 - 86: i11iIiiIii + Ii1I + ooOoO0o * I11i + o0oOOo0O0Ooo
def oOoO ( ) :
 oOo = __addon__ . getSetting ( 'id' )
 oOoOoO = __addon__ . getSetting ( 'pw' )
 ii1I = __addon__ . getSetting ( 'login_type' )
 return ( oOo , oOoOoO , ii1I )
 if 76 - 76: O0 / o0oOOo0O0Ooo . I1IiiI * Ii1I - OOooOOo
 if 76 - 76: i11iIiiIii / iIii1I11I1II1 . I1ii11iIi11i % OOooOOo / OoooooooOO % oO0o
 if 75 - 75: iII111i
def oo ( credential ) :
 O0o0Oo = xbmcgui . Window ( 10000 )
 O0o0Oo . setProperty ( 'TVING_TOKEN' , credential . get ( 'tving_token' ) )
 O0o0Oo . setProperty ( 'TVING_USERINFO' , credential . get ( 'poc_userinfo' ) )
 if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
def I11I11i1I ( ) :
 O0o0Oo = xbmcgui . Window ( 10000 )
 ii11i1iIII = {
 'tving_token' : O0o0Oo . getProperty ( 'TVING_TOKEN' )
 , 'poc_userinfo' : O0o0Oo . getProperty ( 'TVING_USERINFO' )
 }
 return ii11i1iIII
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
 if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
def i1iiI11I ( ) :
 iiii = urlparse . parse_qs ( sys . argv [ 2 ] [ 1 : ] )
 for oO0o0O0OOOoo0 in iiii . keys ( ) :
  iiii [ oO0o0O0OOOoo0 ] = iiii [ oO0o0O0OOOoo0 ] [ 0 ]
 return iiii
 if 48 - 48: O0 + O0 - I1ii11iIi11i . ooOoO0o / iIii1I11I1II1
 if 77 - 77: i1IIi % OoOoOO00 - IiII + ooOoO0o
 if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
def iI ( label , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = '' ) :
 o00O = '%s?%s' % ( sys . argv [ 0 ] , urllib . urlencode ( params ) )
 if 69 - 69: oO0o % I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - O0 % OoooooooOO
 if sublabel : Iii111II = '%s < %s >' % ( label , sublabel )
 else : Iii111II = label
 if not img : img = 'DefaultFolder.png'
 if 9 - 9: OoO0O00
 i11 = xbmcgui . ListItem ( Iii111II , thumbnailImage = img )
 if infoLabels : i11 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder : i11 . setProperty ( 'IsPlayable' , 'true' )
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 xbmcplugin . addDirectoryItem ( ii11i1 , o00O , i11 , isFolder )
 if 29 - 29: I1ii11iIi11i % I1IiiI + ooOoO0o / o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 if 42 - 42: Ii1I + oO0o
 if 76 - 76: I1Ii111 - OoO0O00
def oOooOOo00Oo0O ( ) :
 try :
  O00oO = [ 1080 , 720 , 480 , 360 ]
  if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  OoOOOOO = int ( __addon__ . getSetting ( 'selected_quality' ) )
  return O00oO [ OoOOOOO ]
 except :
  None
  if 33 - 33: I1ii11iIi11i % i1IIi
 return 1080
 if 78 - 78: I11i
 if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
 if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
 if 16 - 16: I1IiiI * oO0o % IiII
def Oo000o ( ) :
 ( I11IiI1I11i1i , iI1ii1Ii , oooo000 ) = oOoO ( )
 if 16 - 16: I1ii11iIi11i + OoO0O00 - II111iiii
 if 85 - 85: OoOoOO00 + i1IIi
 if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
 if 75 - 75: oO0o
 if not ( I11IiI1I11i1i and iI1ii1Ii ) :
  i1iII1I1i1i1 = xbmcgui . Dialog ( )
  I1III = i1iII1I1i1i1 . yesno ( __name__ , __language__ ( 30101 ) . encode ( 'utf8' ) , __language__ ( 30102 ) . encode ( 'utf8' ) )
  if I1III == True :
   __addon__ . openSettings ( )
   sys . exit ( )
   if 63 - 63: OOooOOo % oO0o * oO0o * OoO0O00 / I1ii11iIi11i
   if 74 - 74: II111iiii
 if not oO0 . GetCredential ( I11IiI1I11i1i , iI1ii1Ii , oooo000 ) :
  oo00o0Oo0oo ( __language__ ( 30103 ) . encode ( 'utf8' ) )
  sys . exit ( )
  if 54 - 54: II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + iIii1I11I1II1 * ooOoO0o
  if 87 - 87: ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
 for O0ooo0O0oo0 in o0oO0 :
  Iii111II = O0ooo0O0oo0 . get ( 'title' )
  if 91 - 91: iIii1I11I1II1 + I1Ii111
  i1i = { 'mode' : O0ooo0O0oo0 . get ( 'mode' )
 , 'stype' : O0ooo0O0oo0 . get ( 'stype' )
 , 'orderby' : O0ooo0O0oo0 . get ( 'orderby' )
 , 'page' : '1'
 }
  if 46 - 46: I1Ii111 % I11i + OoO0O00 . OoOoOO00 . OoO0O00
  if O0ooo0O0oo0 . get ( 'mode' ) == 'XXX' :
   i1i [ 'mode' ] = 'XXX'
   oO00o0 = False
  else :
   oO00o0 = True
   if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
  iI ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = oO00o0 , params = i1i )
 if len ( o0oO0 ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 )
 if 25 - 25: I1ii11iIi11i
 if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
 oo ( oO0 . LoadCredential ( ) )
 if 13 - 13: OOooOOo / i11iIiiIii
 if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
 if 52 - 52: o0oOOo0O0Ooo
 if 95 - 95: Ii1I
def O0oOO0O ( args ) :
 oO = args . get ( 'stype' )
 if oO == 'live' :
  iIi1IIIi1 = I1Ii11I1Ii1i
 else :
  iIi1IIIi1 = OOo
  if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 for iIIi1i1 in iIi1IIIi1 :
  Iii111II = iIIi1i1 . get ( 'title' )
  if 10 - 10: I11i
  i1i = { 'mode' : iIIi1i1 . get ( 'mode' )
 , 'stype' : iIIi1i1 . get ( 'stype' )
 , 'orderby' : args . get ( 'orderby' )
 , 'page' : '1'
 }
  if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
  iI ( Iii111II , sublabel = '' , img = '' , infoLabels = None , isFolder = True , params = i1i )
 if len ( iIi1IIIi1 ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 )
 if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
 if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
 if 83 - 83: I11i / I1IiiI
 if 34 - 34: IiII
def oOooOO00Oo ( args ) :
 if 6 - 6: oO0o
 oO0 . SaveCredential ( I11I11i1I ( ) )
 if 68 - 68: OoOoOO00 - OoO0O00
 oO = args . get ( 'stype' )
 IIi = int ( args . get ( 'page' ) )
 ooOOoooooo , II1I = oO0 . GetLiveChannelList ( oO , IIi )
 if 84 - 84: IiII . i11iIiiIii . IiII * I1ii11iIi11i - I11i
 for ii in ooOOoooooo :
  Iii111II = ii . get ( 'title' )
  O0o0oOOOoOo = ii . get ( 'channel' )
  II1 = ii . get ( 'thumbnail' )
  I1iiiI1Ii1I = ii . get ( 'synopsis' )
  if 76 - 76: I1Ii111 + oO0o - IiII - OoooooooOO - O0
  iiIiI = { }
  iiIiI [ 'plot' ] = '%s <%s>\n\n%s' % ( Iii111II , O0o0oOOOoOo , I1iiiI1Ii1I )
  if 6 - 6: IiII . oO0o * OoOoOO00 - Ii1I - IiII
  i1i = { 'mode' : 'LIVE'
 , 'mediacode' : ii . get ( 'mediacode' )
 , 'stype' : oO
  }
  if 45 - 45: I1IiiI - OoooooooOO + iIii1I11I1II1 . I1IiiI * I11i
  iI ( Iii111II , sublabel = O0o0oOOOoOo , img = II1 , infoLabels = iiIiI , isFolder = False , params = i1i )
  if 51 - 51: OoO0O00 / OoO0O00
 if II1I :
  if 53 - 53: Oo0Ooo
  i1i [ 'mode' ] = 'CHANNEL'
  i1i [ 'stype' ] = oO
  i1i [ 'page' ] = str ( IIi + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  iI1Iii = str ( IIi + 1 )
  iI ( Iii111II , sublabel = iI1Iii , img = '' , infoLabels = None , isFolder = True , params = i1i )
  if 68 - 68: OOooOOo % I1Ii111
 if len ( ooOOoooooo ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 88 - 88: iIii1I11I1II1 - ooOoO0o + OOooOOo
 if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
 if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + I1Ii111 / OoOoOO00
 if 23 - 23: O0
def o00oO0oOo00 ( args ) :
 if 81 - 81: OoO0O00
 oO0 . SaveCredential ( I11I11i1I ( ) )
 if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + iII111i / OoOoOO00
 oO = args . get ( 'stype' )
 o0OoOO000ooO0 = args . get ( 'orderby' )
 IIi = int ( args . get ( 'page' ) )
 if 56 - 56: iII111i
 oo0oO0oOOoo , II1I = oO0 . GetProgramList ( oO , o0OoOO000ooO0 , IIi )
 if 51 - 51: Oo0Ooo * i11iIiiIii
 for O0oo00o0O in oo0oO0oOOoo :
  Iii111II = O0oo00o0O . get ( 'title' )
  II1 = O0oo00o0O . get ( 'thumbnail' )
  I1iiiI1Ii1I = O0oo00o0O . get ( 'synopsis' )
  i1I1I = Oooo0000 . get ( O0oo00o0O . get ( 'channel' ) )
  if 12 - 12: i11iIiiIii / OoO0O00
  iiIiI = { }
  iiIiI [ 'plot' ] = '%s <%s>\n\n%s' % ( Iii111II , i1I1I , I1iiiI1Ii1I )
  if 80 - 80: I1Ii111 . i11iIiiIii - o0oOOo0O0Ooo
  i1i = { 'mode' : 'EPISODE'
 , 'programcode' : O0oo00o0O . get ( 'program' )
 , 'page' : '1'
 }
  if 25 - 25: OoO0O00
  iI ( Iii111II , sublabel = i1I1I , img = II1 , infoLabels = iiIiI , isFolder = True , params = i1i )
  if 62 - 62: OOooOOo + O0
 if II1I :
  if 98 - 98: o0oOOo0O0Ooo
  i1i [ 'mode' ] = 'PROGRAM'
  i1i [ 'stype' ] = oO
  i1i [ 'orderby' ] = o0OoOO000ooO0
  i1i [ 'page' ] = str ( IIi + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  iI1Iii = str ( IIi + 1 )
  iI ( Iii111II , sublabel = iI1Iii , img = '' , infoLabels = None , isFolder = True , params = i1i )
  if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
 if len ( oo0oO0oOOoo ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 78 - 78: i11iIiiIii / iII111i - Ii1I / OOooOOo + oO0o
 if 82 - 82: Ii1I
 if 46 - 46: OoooooooOO . i11iIiiIii
 if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
def oO0O0OO0O ( args ) :
 if 81 - 81: oO0o . o0oOOo0O0Ooo % O0 / I1IiiI - oO0o
 oO0 . SaveCredential ( I11I11i1I ( ) )
 if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * I1Ii111 * O0
 o00oO0oo0OO = args . get ( 'programcode' )
 IIi = int ( args . get ( 'page' ) )
 if 57 - 57: I1Ii111 % Ii1I + o0oOOo0O0Ooo - Oo0Ooo
 o0O , II1I = oO0 . GetEpisodoList ( o00oO0oo0OO , IIi )
 if 39 - 39: II111iiii / ooOoO0o + I1Ii111 / OoOoOO00
 for I1Ii11i in o0O :
  Iii111II = I1Ii11i . get ( 'title' )
  II1 = I1Ii11i . get ( 'thumbnail' )
  I1iiiI1Ii1I = I1Ii11i . get ( 'synopsis' )
  if 35 - 35: o0oOOo0O0Ooo
  iiIiI = { }
  iiIiI [ 'plot' ] = '%s\n\n%s' % ( Iii111II , I1iiiI1Ii1I )
  if 90 - 90: I1Ii111 % Ii1I - iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % I1ii11iIi11i
  i1i = { 'mode' : 'VOD'
 , 'mediacode' : I1Ii11i . get ( 'episode' )
 , 'stype' : 'vod'
 , 'programcode' : o00oO0oo0OO
 , 'title' : Iii111II
 , 'thumbnail' : II1
 }
  if 37 - 37: oO0o - I1IiiI . I11i * Ii1I - iII111i
  iI ( Iii111II , sublabel = '' , img = II1 , infoLabels = iiIiI , isFolder = False , params = i1i )
  if 8 - 8: OoO0O00 - I1IiiI % Ii1I * OoooooooOO - OoO0O00 * I1Ii111
 if II1I :
  if 6 - 6: OoooooooOO
  i1i [ 'mode' ] = 'EPOSODE'
  i1i [ 'programcode' ] = o00oO0oo0OO
  i1i [ 'page' ] = str ( IIi + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  iI1Iii = str ( IIi + 1 )
  iI ( Iii111II , sublabel = iI1Iii , img = '' , infoLabels = None , isFolder = True , params = i1i )
  if 17 - 17: I1IiiI % I1Ii111
 if len ( o0O ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
 if 90 - 90: oO0o / iIii1I11I1II1 - o0oOOo0O0Ooo / OoooooooOO - OoooooooOO * OOooOOo
 if 73 - 73: I1ii11iIi11i * i11iIiiIii % oO0o . I1ii11iIi11i
 if 66 - 66: oO0o + oO0o + ooOoO0o / iII111i + OOooOOo
 if 30 - 30: O0
def iIi1 ( args ) :
 if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
 oO0 . SaveCredential ( I11I11i1I ( ) )
 if 62 - 62: OoooooooOO * I1IiiI
 oOOOoo0O0oO = __addon__ . getSetting ( 'id' )
 IIi = int ( args . get ( 'page' ) )
 if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
 if 'search_key' in args :
  I1IIIiIiI1 = args . get ( 'search_key' )
 else :
  I1IIIiIiI1 = oo0Ooo0 ( __language__ ( 30003 ) . encode ( 'utf-8' ) )
  if not I1IIIiIiI1 : return
  if 28 - 28: iIii1I11I1II1 % Oo0Ooo * I1IiiI % Ii1I * o0oOOo0O0Ooo / o0oOOo0O0Ooo
 iIIII , II1I = oO0 . GetSearchList ( I1IIIiIiI1 , oOOOoo0O0oO , IIi )
 if len ( iIIII ) == 0 : return
 if 33 - 33: ooOoO0o . II111iiii % iII111i + o0oOOo0O0Ooo
 for oO00O000oO0 in iIIII :
  Iii111II = oO00O000oO0 . get ( 'title' )
  II1 = oO00O000oO0 . get ( 'thumbnail' )
  I1iiiI1Ii1I = oO00O000oO0 . get ( 'synopsis' )
  O0OoOO0o = oO00O000oO0 . get ( 'program' )
  if 69 - 69: I1Ii111
  iiIiI = { }
  iiIiI [ 'plot' ] = '%s\n\n%s' % ( Iii111II , I1iiiI1Ii1I )
  if 11 - 11: I1IiiI
  i1i = { 'mode' : 'EPISODE'
 , 'programcode' : oO00O000oO0 . get ( 'program' )
 , 'page' : '1'
 }
  if 16 - 16: Ii1I + IiII * O0 % i1IIi . I1IiiI
  iI ( Iii111II , sublabel = '' , img = II1 , infoLabels = iiIiI , isFolder = True , params = i1i )
  if 67 - 67: OoooooooOO / I1IiiI * Ii1I + I11i
 if II1I :
  if 65 - 65: OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii / i1IIi
  i1i [ 'mode' ] = 'SEARCH'
  i1i [ 'search_key' ] = I1IIIiIiI1
  i1i [ 'page' ] = str ( IIi + 1 )
  Iii111II = '[B]%s >>[/B]' % '다음 페이지'
  iI1Iii = str ( IIi + 1 )
  iI ( Iii111II , sublabel = iI1Iii , img = '' , infoLabels = None , isFolder = True , params = i1i )
  if 71 - 71: I1Ii111 + Ii1I
 if len ( iIIII ) > 0 : xbmcplugin . endOfDirectory ( ii11i1 )
 if 28 - 28: OOooOOo
 if 38 - 38: ooOoO0o % II111iiii % I11i / OoO0O00 + OoOoOO00 / i1IIi
 if 54 - 54: iIii1I11I1II1 % I1ii11iIi11i - OOooOOo / oO0o - OoO0O00 . I11i
 if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
def IiII111i1i11 ( stype ) :
 try :
  i111iIi1i1II1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( i111iIi1i1II1 , 'w' ) as oooO :
   oooO . write ( '' )
 except :
  None
  if 26 - 26: Ii1I % I1ii11iIi11i
  if 76 - 76: IiII * iII111i
  if 52 - 52: OOooOOo
  if 19 - 19: I1IiiI
def i11i ( args ) :
 oO = args . get ( 'stype' )
 if 73 - 73: OOooOOo
 i1iII1I1i1i1 = xbmcgui . Dialog ( )
 I1III = i1iII1I1i1i1 . yesno ( __name__ , __language__ ( 30201 ) . encode ( 'utf8' ) , __language__ ( 30202 ) . encode ( 'utf8' ) )
 if I1III == False : sys . exit ( )
 if 70 - 70: iIii1I11I1II1
 IiII111i1i11 ( oO )
 if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
 xbmc . executebuiltin ( "Container.Refresh" )
 if 92 - 92: i1IIi - iIii1I11I1II1
 if 16 - 16: OoO0O00 - OoOoOO00 - OOooOOo - i1IIi / Ii1I
 if 88 - 88: OoO0O00
 if 71 - 71: I1ii11iIi11i
def IIiiIiiI ( stype ) :
 try :
  i111iIi1i1II1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  with open ( i111iIi1i1II1 , 'r' ) as oooO :
   IIIIiI11I11 = oooO . readlines ( )
 except :
  IIIIiI11I11 = [ ]
  if 58 - 58: I1IiiI
 return IIIIiI11I11
 if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
 if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 if 23 - 23: i11iIiiIii
 if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
def o0ooooO0o0O ( stype , in_params ) :
 try :
  i111iIi1i1II1 = xbmc . translatePath ( os . path . join ( __profile__ , 'watchedlist_%s.txt' % stype ) )
  iiIi11iI1iii = IIiiIiiI ( stype )
  if 67 - 67: O0 / I1Ii111
  with open ( i111iIi1i1II1 , 'w' ) as oooO :
   OOO0000oO = urllib . urlencode ( in_params )
   OOO0000oO = OOO0000oO . encode ( 'utf-8' ) + '\n'
   oooO . write ( OOO0000oO )
   if 15 - 15: OoOoOO00 % I1IiiI * I11i
   O0OoooO0 = 0
   for ooo0O0o00O in iiIi11iI1iii :
    I1i11 = dict ( urlparse . parse_qsl ( ooo0O0o00O ) )
    if in_params . get ( 'code' ) != I1i11 . get ( 'code' ) :
     oooO . write ( ooo0O0o00O )
     O0OoooO0 += 1
     if O0OoooO0 >= 50 : break
 except :
  None
  if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
  if 52 - 52: ooOoO0o . iII111i + I1Ii111
  if 38 - 38: i1IIi - II111iiii . I1Ii111
  if 58 - 58: I1IiiI . iII111i + OoOoOO00
def O00OO ( args ) :
 oO = args . get ( 'stype' )
 if 17 - 17: I11i / I1Ii111 + oO0o - i11iIiiIii . iII111i
 if oO == 'vod' :
  OO0o0oOOO0O = IIiiIiiI ( oO )
  if 49 - 49: I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
  for o000ooooO0o in OO0o0oOOO0O :
   iI1i11 = dict ( urlparse . parse_qsl ( o000ooooO0o ) )
   if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
   Iii111II = iI1i11 . get ( 'title' )
   II1 = iI1i11 . get ( 'img' )
   if 86 - 86: o0oOOo0O0Ooo
   iiIiI = { }
   iiIiI [ 'plot' ] = Iii111II
   if 5 - 5: IiII * OoOoOO00
   i1i = { 'mode' : 'EPISODE'
 , 'programcode' : iI1i11 . get ( 'code' )
 , 'page' : '1'
 }
   oO00o0 = True
   if 5 - 5: I1Ii111
   iI ( Iii111II , sublabel = '' , img = II1 , infoLabels = iiIiI , isFolder = oO00o0 , params = i1i )
   if 90 - 90: I1Ii111 . ooOoO0o / Ii1I - I11i
  iiIiI = { 'plot' : '시청목록을 삭제합니다.' }
  Iii111II = '*** 시청목록 삭제 ***'
  i1i = { 'mode' : 'MYVIEW_REMOVE'
 , 'stype' : oO
 }
  if 40 - 40: OoooooooOO
  iI ( Iii111II , sublabel = '' , img = '' , infoLabels = iiIiI , isFolder = False , params = i1i )
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
  xbmcplugin . endOfDirectory ( ii11i1 , cacheToDisc = False )
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
  if 60 - 60: II111iiii + Oo0Ooo
def I1IiIiiIiIII ( args ) :
 if 8 - 8: oO0o / I1ii11iIi11i
 oO0 . SaveCredential ( I11I11i1I ( ) )
 if 20 - 20: I1IiiI
 o0oO000oo = args . get ( 'mediacode' )
 oO = args . get ( 'stype' )
 o00o0 = oOooOOo00Oo0O ( )
 if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 O0O0Oo00 , oOoO00o = oO0 . GetBroadURL ( o0oO000oo , o00o0 , oO )
 if 100 - 100: o0oOOo0O0Ooo + OOooOOo * o0oOOo0O0Ooo
 if 80 - 80: o0oOOo0O0Ooo * O0 - Ii1I
 if 66 - 66: i11iIiiIii - OOooOOo * Oo0Ooo
 OooOOOO = O0O0Oo00 . find ( 'Policy=' )
 if OooOOOO != - 1 :
  iIIIiiI1i1i = O0O0Oo00 . split ( '?' ) [ 0 ]
  if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
  ii1I1i1iiiI = dict ( urlparse . parse_qsl ( urlparse . urlsplit ( O0O0Oo00 ) . query ) )
  ii1I1i1iiiI = urllib . urlencode ( ii1I1i1iiiI )
  ii1I1i1iiiI = ii1I1i1iiiI . replace ( '&' , ';' )
  ii1I1i1iiiI = ii1I1i1iiiI . replace ( 'Policy' , 'CloudFront-Policy' )
  ii1I1i1iiiI = ii1I1i1iiiI . replace ( 'Signature' , 'CloudFront-Signature' )
  ii1I1i1iiiI = ii1I1i1iiiI . replace ( 'Key-Pair-Id' , 'CloudFront-Key-Pair-Id' )
  if 96 - 96: OoooooooOO + oO0o
  iiII1i11i = '%s|Cookie=%s' % ( iIIIiiI1i1i , ii1I1i1iiiI )
 else :
  iiII1i11i = O0O0Oo00
  if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
  if 85 - 85: I11i % oO0o / iIii1I11I1II1 . iIii1I11I1II1
 O0OoOoo00o ( iiII1i11i , False )
 if oOoO00o != '' :
  oo00o0Oo0oo ( __language__ ( 30302 ) . encode ( 'utf8' ) )
  return
  if 31 - 31: o0oOOo0O0Ooo % OoO0O00
 iI1I = xbmcgui . ListItem ( path = iiII1i11i )
 if 100 - 100: iIii1I11I1II1 + OoOoOO00 / Oo0Ooo . i11iIiiIii
 if 14 - 14: o0oOOo0O0Ooo * OOooOOo + iII111i + O0 + i11iIiiIii
 if oOoO00o != '' :
  oOoO0 = oOoO00o
  Oo0 = 'https://cj.drmkeyserver.com/widevine_license'
  if 83 - 83: i11iIiiIii % o0oOOo0O0Ooo % ooOoO0o
  if 11 - 11: II111iiii % OoO0O00 * iII111i + ooOoO0o + Ii1I
  II1Iiiiii = 'mpd'
  ii1ii111 = 'com.widevine.alpha'
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  IIII1 = inputstreamhelper . Helper ( II1Iiiiii , drm = ii1ii111 )
  if 10 - 10: I1Ii111 / ooOoO0o + i11iIiiIii / Ii1I
  if IIII1 . check_inputstream ( ) :
   if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
   oOOO0oo0 = { 'origin' : 'https://www.tving.com'
 , 'pragma' : 'no-cache'
 , 'referer' : 'https://www.tving.com/live/player/%s' % o0oO000oo
 , 'sec-fetch-mode' : 'cors'
 , 'sec-fetch-site' : 'same-site'
 , 'user-agent' : USER_AGENT

   }
   if 46 - 46: IiII
   ii1iIi1iIiI1i = Oo0 + '?' + oOoO0 + '|' + urllib . urlencode ( oOOO0oo0 ) + '|R{SSM}|'
   if 40 - 40: i1IIi % OOooOOo
   iI1I . setProperty ( 'inputstreamaddon' , IIII1 . inputstream_addon )
   if 71 - 71: OoOoOO00
   iI1I . setProperty ( 'inputstream.adaptive.manifest_type' , II1Iiiiii )
   iI1I . setProperty ( 'inputstream.adaptive.license_type' , ii1ii111 )
   if 14 - 14: i11iIiiIii % OOooOOo
   iI1I . setProperty ( 'inputstream.adaptive.license_key' , ii1iIi1iIiI1i )
   if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
   if 14 - 14: o0oOOo0O0Ooo . OOooOOo . I11i + OoooooooOO - OOooOOo + IiII
   iI1I . setMimeType ( 'application/dash+xml' )
   iI1I . setContentLookup ( False )
   if 9 - 9: Ii1I
   if 59 - 59: I1IiiI * II111iiii . O0
 xbmcplugin . setResolvedUrl ( ii11i1 , True , iI1I )
 if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
 if args . get ( 'mode' ) in [ 'VOD' ] and args . get ( 'title' ) :
  i1i = { 'code' : args . get ( 'programcode' )
 , 'img' : args . get ( 'thumbnail' )
 , 'title' : args . get ( 'title' )
 }
  o0ooooO0o0O ( args . get ( 'stype' ) , i1i )
  if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
  if 27 - 27: O0
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
  if 28 - 28: i1IIi - iII111i
  if 54 - 54: iII111i - O0 % OOooOOo
oO0 = i11i1I1 ( )
ii11i1 = int ( sys . argv [ 1 ] )
if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
i1i = i1iiI11I ( )
I11ii1i1 = i1i . get ( 'mode' , None )
if 78 - 78: iII111i
if I11ii1i1 is None :
 Oo000o ( )
 oo ( oO0 . LoadCredential ( ) )
 if 28 - 28: I11i
elif I11ii1i1 in [ 'LIVE_GROUP' , 'VOD_GROUP' ] :
 O0oOO0O ( i1i )
 if 58 - 58: OoOoOO00
elif I11ii1i1 == 'CHANNEL' :
 oOooOO00Oo ( i1i )
 if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
elif I11ii1i1 in [ 'LIVE' , 'VOD' ] :
 I1IiIiiIiIII ( i1i )
 xbmc . sleep ( 200 )
 if 73 - 73: i11iIiiIii - IiII
elif I11ii1i1 == 'PROGRAM' :
 o00oO0oOo00 ( i1i )
 if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
elif I11ii1i1 == 'EPISODE' :
 oO0O0OO0O ( i1i )
 if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
elif I11ii1i1 == 'SEARCH' :
 iIi1 ( i1i )
 if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
elif I11ii1i1 == 'WATCH' :
 O00OO ( i1i )
 if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
elif I11ii1i1 == 'MYVIEW_REMOVE' :
 i11i ( i1i )
 if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
else :
 None
 if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
 if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
 if 97 - 97: I1IiiI / iII111i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
