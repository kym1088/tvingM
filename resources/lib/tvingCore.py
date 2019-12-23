# -*- coding: utf-8 -*-
__author__ = "NightRain"
__email__ = "kym1088@naver.com"
if 64 - 64: i11iIiiIii
import urllib
import urllib2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
import cookielib
import re
import json
import sys
import urlparse
import time
import ctypes
if 73 - 73: II111iiii
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
IiII = { 'stream50' : 1080 , 'stream40' : 720 , 'stream30' : 480 , 'stream25' : 360 }
if 28 - 28: Ii11111i * iiI1i1
if 46 - 46: Ooo0OO0oOO * Ii * I1ii11iIi11i
class o0o ( object ) :
 def __init__ ( self ) :
  self . MyCookie = cookielib . LWPCookieJar ( )
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , IiiIII111iI ) ]
  urllib2 . install_opener ( self . Opener )
  if 60 - 60: I1ii11iIi11i + Ooo0OO0oOO - I11i / i1IIi
  if 40 - 40: I1IiiI / O0 % Ii + O0 * i1IIi
 def RequestCookie ( self , url , params ) :
  I1Ii11I1Ii1i = ''
  Ooo = self . Opener . open ( url , urllib . urlencode ( params ) )
  if 56 - 56: I11i - i1IIi
  I1Ii11I1Ii1i = Ooo . info ( ) . getheader ( 'Set-Cookie' )
  if 64 - 64: Ooo0OO0oOO + Ii11111i
  Ooo . close ( )
  return I1Ii11I1Ii1i
  if 10 - 10: i11iIiiIii / oO0o % II111iiii
  if 75 - 75: i11iIiiIii + iiI1i1 . o0oOOo0O0Ooo * Ii11111i
 def Request ( self , url , params = None , cookie = None ) :
  if cookie : self . Opener . addheaders = cookie
  if 59 - 59: iIii1I11I1II1
  if params :
   Ooo = self . Opener . open ( url , urllib . urlencode ( params ) )
  else :
   Ooo = self . Opener . open ( url )
   if 31 - 31: iiI1i1 % i1IIi * iIii1I11I1II1 / iiI1i1 % oO0o + OoooooooOO
  O00o0o0000o0o = Ooo . read ( )
  Ooo . close ( )
  if 88 - 88: Ii11111i / I1IiiI + i1IIi % OoooooooOO . iiI1i1 / Ii
  return O00o0o0000o0o
  if 28 - 28: Ii + Ooo0OO0oOO - Ii . OoooooooOO
  if 97 - 97: OoO0O00 . I11i
  if 32 - 32: Oo0Ooo - II111iiii - i11iIiiIii % Ooo0OO0oOO
  if 54 - 54: OOooOOo % O0 + I1IiiI - Ii11111i / I11i
  if 31 - 31: OoO0O00 + II111iiii
class i11IiIiiIIIII ( object ) :
 def __init__ ( self ) :
  self . SESSION = o0o ( )
  self . TVING_TOKEN = ''
  self . POC_USERINFO = ''
  self . APIKEY = '1e7952d0917d6aab1f0293a063697610'
  self . NETWORKCODE = 'CSND0900'
  self . OSCODE = 'CSOD0900'
  self . TELECODE = 'CSCD0900'
  self . SCREENCODE = 'CSSD0100'
  self . LIVE_LIMIT = 23
  self . VOD_LIMIT = 20
  self . EPISODE_LIMIT = 30
  self . SEARCH_LIMIT = 80
  self . MOVIE_LIMIT = 18
  self . API_DOMAIN = 'https://api.tving.com'
  self . IMG_DOMAIN = 'https://image.tving.com'
  self . SEARCH_DOMAIN = 'https://search.tving.com'
  self . LOGIN_DOMAIN = 'https://user.tving.com'
  self . URL_DOMAIN = 'https://www.tving.com'
  if 22 - 22: Ii1I * O0 / o0oOOo0O0Ooo
  if 64 - 64: Ii1I % i1IIi % OoooooooOO
 def getDeviceStr ( self ) :
  i1iIIi1 = [ ]
  i1iIIi1 . append ( 'Windows' )
  i1iIIi1 . append ( 'Chrome' )
  i1iIIi1 . append ( 'ko-KR' )
  i1iIIi1 . append ( 'undefined' )
  i1iIIi1 . append ( '24' )
  i1iIIi1 . append ( u'한국 표준시' )
  i1iIIi1 . append ( 'undefined' )
  i1iIIi1 . append ( 'undefined' )
  i1iIIi1 . append ( 'data:image/png;base64,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CZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAT+H9FJng/hy/8wAAAAAElFTkSuQmCC' )
  if 50 - 50: i11iIiiIii - Ii1I
  if 78 - 78: OoO0O00
  Iii1I111 = ''
  for OO0O0O00OooO in i1iIIi1 :
   Iii1I111 += OO0O0O00OooO + '|'
  return Iii1I111
  if 77 - 77: II111iiii - II111iiii . I1IiiI / o0oOOo0O0Ooo
  if 14 - 14: I11i % O0
 def murmurhash3_32 ( self , device_str , hash_int ) :
  def IiI1I1 ( val , n ) :
   OoO000 = ctypes . c_int32 ( val )
   OoO000 . value <<= n
   return OoO000 . value
   if 42 - 42: oO0o - i1IIi / i11iIiiIii + OOooOOo + OoO0O00
  def iIi ( val , n ) :
   return val >> n if val >= 0 else ( val + 0x100000000 ) >> n
   if 40 - 40: oO0o . OoOoOO00 . Oo0Ooo . i1IIi
  I11iii = len ( device_str )
  OO0O00 = I11iii & 3
  ii1 = I11iii - OO0O00
  o0oO0o00oo = hash_int
  if 32 - 32: Oo0Ooo * O0 % oO0o % Ii1I . iiI1i1
  o0OOOOO00o0O0 = 0
  for o0o0OOO0o0 in range ( 0 , ii1 , 4 ) :
   ooOOOo0oo0O0 = ord ( device_str [ o0o0OOO0o0 ] )
   o0 = ord ( device_str [ o0o0OOO0o0 + 1 ] )
   I11II1i = ord ( device_str [ o0o0OOO0o0 + 2 ] )
   IIIII = ord ( device_str [ o0o0OOO0o0 + 3 ] )
   if 75 - 75: II111iiii % II111iiii
   iI1 = ctypes . c_int32 ( ooOOOo0oo0O0 & 255 | IiI1I1 ( ( o0 & 255 ) , 8 ) | IiI1I1 ( ( I11II1i & 255 ) , 16 ) | IiI1I1 ( ( IIIII & 255 ) , 24 ) ) . value
   iI1 = ctypes . c_int32 ( 3432918353 * ( iI1 & 65535 ) + IiI1I1 ( ( 3432918353 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
   iI1 = ctypes . c_int32 ( IiI1I1 ( iI1 , 15 ) | iIi ( iI1 , 17 ) ) . value
   iI1 = ctypes . c_int32 ( 461845907 * ( iI1 & 65535 ) + IiI1I1 ( ( 461845907 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
   o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ iI1 ) . value
   o0oO0o00oo = ctypes . c_int32 ( IiI1I1 ( o0oO0o00oo , 13 ) | iIi ( o0oO0o00oo , 19 ) ) . value
   o0oO0o00oo = ctypes . c_int32 ( 5 * ( o0oO0o00oo & 65535 ) + IiI1I1 ( ( 5 * iIi ( o0oO0o00oo , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
   o0oO0o00oo = ctypes . c_int32 ( ( o0oO0o00oo & 65535 ) + 27492 + IiI1I1 ( ( iIi ( o0oO0o00oo , 16 ) + 58964 & 65535 ) , 16 ) ) . value
   o0OOOOO00o0O0 = o0o0OOO0o0 + 4
   if 19 - 19: I11i + Ii
  iI1 = 0
  if OO0O00 == 3 :
   iI1 = ctypes . c_int32 ( iI1 ^ IiI1I1 ( ( ord ( device_str [ o0OOOOO00o0O0 + 2 ] ) & 255 ) , 16 ) ) . value
   iI1 = ctypes . c_int32 ( iI1 ^ IiI1I1 ( ( ord ( device_str [ o0OOOOO00o0O0 + 1 ] ) & 255 ) , 8 ) ) . value
   iI1 = ctypes . c_int32 ( iI1 ^ ( ord ( device_str [ o0OOOOO00o0O0 ] ) & 255 ) ) . value
   iI1 = ctypes . c_int32 ( 3432918353 * ( iI1 & 65535 ) + IiI1I1 ( ( 3432918353 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
   iI1 = ctypes . c_int32 ( IiI1I1 ( iI1 , 15 ) | iIi ( iI1 , 17 ) ) . value
   o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ ( 461845907 * ( iI1 & 65535 ) + IiI1I1 ( ( 461845907 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) ) . value
  elif OO0O00 == 2 :
   iI1 = ctypes . c_int32 ( iI1 ^ IiI1I1 ( ( ord ( device_str [ o0OOOOO00o0O0 + 1 ] ) & 255 ) , 8 ) ) . value
  elif OO0O00 == 1 :
   iI1 = ctypes . c_int32 ( iI1 ^ ( ord ( device_str [ o0OOOOO00o0O0 ] ) & 255 ) ) . value
   iI1 = ctypes . c_int32 ( 3432918353 * ( iI1 & 65535 ) + IiI1I1 ( ( 3432918353 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
   iI1 = ctypes . c_int32 ( IiI1I1 ( iI1 , 15 ) | iIi ( iI1 , 17 ) ) . value
   o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ ( 461845907 * ( iI1 & 65535 ) + IiI1I1 ( ( 461845907 * iIi ( iI1 , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) ) . value
   if 53 - 53: OoooooooOO . i1IIi
  o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ I11iii ) . value
  o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ iIi ( o0oO0o00oo , 16 ) ) . value
  o0oO0o00oo = ctypes . c_int32 ( 2246822507 * ( o0oO0o00oo & 65535 ) + IiI1I1 ( ( 2246822507 * iIi ( o0oO0o00oo , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
  o0oO0o00oo = ctypes . c_int32 ( o0oO0o00oo ^ iIi ( o0oO0o00oo , 13 ) ) . value
  o0oO0o00oo = ctypes . c_int32 ( 3266489909 * ( o0oO0o00oo & 65535 ) + IiI1I1 ( ( 3266489909 * iIi ( o0oO0o00oo , 16 ) & 65535 ) , 16 ) & ctypes . c_int32 ( 4294967295 ) . value ) . value
  if 18 - 18: o0oOOo0O0Ooo
  o0oO0o00oo = iIi ( ( o0oO0o00oo ^ iIi ( o0oO0o00oo , 16 ) ) , 0 )
  return o0oO0o00oo
  if 28 - 28: OOooOOo - iiI1i1 . iiI1i1 + OoOoOO00 - OoooooooOO + O0
  if 95 - 95: OoO0O00 % oO0o . O0
 def SaveCredential ( self , login_params ) :
  self . TVING_TOKEN = login_params . get ( 'tving_token' )
  self . POC_USERINFO = login_params . get ( 'poc_userinfo' )
  if 15 - 15: Ii / Ii1I . Ii1I - i1IIi
 def LoadCredential ( self ) :
  o00oOO0 = {
 'tving_token' : self . TVING_TOKEN
 , 'poc_userinfo' : self . POC_USERINFO
 }
  return o00oOO0
  if 95 - 95: OOooOOo / OoooooooOO
 def GetDefaultParams ( self ) :
  iI = { 'apiKey' : self . APIKEY
 , 'networkCode' : self . NETWORKCODE
 , 'osCode' : self . OSCODE
 , 'teleCode' : self . TELECODE
 , 'screenCode' : self . SCREENCODE
 }
  return iI
  if 60 - 60: I11i / I11i
 def GetNoCache ( self , timetype = 1 ) :
  if timetype == 1 :
   return int ( time . time ( ) )
  else :
   return int ( time . time ( ) * 1000 )
   if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - Ooo0OO0oOO
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  oo0 = domain + path
  if query1 :
   oo0 += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   oo0 += '&%s' % urllib . urlencode ( query2 )
  return oo0
  if 57 - 57: OOooOOo . OOooOOo
  if 95 - 95: O0 + OoO0O00 . II111iiii / O0
  if 97 - 97: Ii - OOooOOo * i11iIiiIii / OoOoOO00 % Ooo0OO0oOO - OoooooooOO
  if 59 - 59: O0 + I1IiiI + iiI1i1 % I1IiiI
  if 70 - 70: Ii11111i * I1ii11iIi11i
 def GetCredential ( self , user_id , user_pw , login_type ) :
  i1II1 = False
  if 66 - 66: OoooooooOO + Ii1I + Ii1I - i1IIi
  try :
   O0o0Ooo = self . LOGIN_DOMAIN + '/pc/user/doLogin.tving'
   if 56 - 56: Ii . OoOoOO00 * Ii11111i . OoOoOO00
   iI = { 'userId' : user_id
 , 'password' : user_pw
 , 'loginType' : '10' if login_type == '0' else '20'
 , 'autoLogin' : 'false'
 , 'cjOneCookie' : ''
 , 'kaptcha' : ''

   , 'returnUrl' : ''
 , 'csite' : ''
 }
   if 72 - 72: Ii11111i / i1IIi * Oo0Ooo - Ooo0OO0oOO
   I1Ii11I1Ii1i = self . SESSION . RequestCookie ( O0o0Ooo , iI )
   if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / Ii
   if 49 - 49: o0oOOo0O0Ooo
   if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
   for o00OO00OoO in I1Ii11I1Ii1i . split ( ',' ) :
    o00OO00OoO = o00OO00OoO . strip ( )
    if o00OO00OoO . startswith ( '_tving_token' ) :
     OOOO0OOoO0O0 = o00OO00OoO . split ( ';' ) [ 0 ]
     OOOO0OOoO0O0 = OOOO0OOoO0O0 . split ( '=' ) [ 1 ]
     if 65 - 65: iiI1i1 * I1IiiI + Ii1I % i11iIiiIii * oO0o . Ooo0OO0oOO
    if o00OO00OoO . startswith ( 'POC_USERINFO' ) :
     OoO0O00IIiII = o00OO00OoO . split ( ';' ) [ 0 ]
     OoO0O00IIiII = OoO0O00IIiII . split ( '=' ) [ 1 ]
     if 80 - 80: iiI1i1 . oO0o
   if OOOO0OOoO0O0 : i1II1 = True
   if 25 - 25: OoOoOO00 . II111iiii / Ii11111i . OOooOOo * OoO0O00 . I1IiiI
  except Exception as Oo0oOOo :
   OOOO0OOoO0O0 = OoO0O00IIiII = ''
   if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
  o00oOO0 = {
 'tving_token' : OOOO0OOoO0O0
 , 'poc_userinfo' : OoO0O00IIiII
 }
  self . SaveCredential ( o00oOO0 )
  if 75 - 75: oO0o
  return i1II1
  if 50 - 50: Ii1I / Oo0Ooo - oO0o - I11i % Ii11111i - oO0o
  if 91 - 91: OoO0O00 / I11i - II111iiii . I11i
 def GetBroadURL ( self , mediacode , sel_quality , stype ) :
  i1I11i1I = ''
  Oo0o00 = ''
  O0O0oOO00O00o = '2357846534'
  if 24 - 24: iiI1i1
  if 57 - 57: O0 / Ooo0OO0oOO % OoO0O00 / Ooo0OO0oOO . OoOoOO00 / O0
  if 89 - 89: OoOoOO00
  try :
   if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + Ii
   if stype != 'tvingtv' :
    if 4 - 4: Ii + O0 * OOooOOo
    OOoo0O = '/v2/media/stream/info'
    if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
    o0oo = self . GetDefaultParams ( )
    oooooOoo0ooo = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'noCache' : str ( self . GetNoCache ( 1 ) )
 , 'callingFrom' : 'HTML5'
 , 'adReq' : 'none'
 , 'ooc' : ''
 }
    oooooOoo0ooo [ 'deviceId' ] = O0O0oOO00O00o
    if 6 - 6: I11i - Ii1I + iIii1I11I1II1 - Ooo0OO0oOO - i11iIiiIii
    oo0 = self . makeurl ( self . API_DOMAIN , OOoo0O , o0oo , oooooOoo0ooo )
    if 79 - 79: OoOoOO00 - O0 * OoO0O00 + OoOoOO00 % O0 * O0
    I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
    if 61 - 61: II111iiii
    Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
    O0OOO = json . loads ( Ooo )
    if 10 - 10: OOooOOo * I11i % OoOoOO00 / I1IiiI / OoOoOO00
    if not ( 'stream' in O0OOO [ 'body' ] ) : return None
    iIIi1i1 = O0OOO [ 'body' ] [ 'stream' ]
    if 10 - 10: I11i
    if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
    if 'drm_license_assertion' in iIIi1i1 :
     Oo0o00 = iIIi1i1 [ 'drm_license_assertion' ]
    else :
     print O0OOO [ 'body' ] [ 'stream' ]
     OOOOoOoo0O0O0 = iIIi1i1 [ 'broadcast' ] [ 'broad_url' ]
     if 85 - 85: oO0o % i11iIiiIii - Ii11111i * OoooooooOO / I1IiiI % I1IiiI
    IIiIi1iI = iIIi1i1 [ 'quality' ]
    if 35 - 35: Ii1I % O0 - O0
    IiIIIi1iIi = [ ]
    for ooOOoooooo in IIiIi1iI :
     if ooOOoooooo [ 'active' ] == 'Y' :
      IiIIIi1iIi . append ( { IiII . get ( ooOOoooooo [ 'code' ] ) : ooOOoooooo [ 'code' ] } )
      if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % Ii11111i * iiI1i1 . i11iIiiIii
    III1Iiii1I11 = self . CheckQuality ( sel_quality , IiIIIi1iIi )
    if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
   else :
    for o00oooO0Oo , o0O0OOO0Ooo in IiII . items ( ) :
     if o0O0OOO0Ooo == sel_quality :
      III1Iiii1I11 = o00oooO0Oo
      if 45 - 45: O0 / o0oOOo0O0Ooo
      if 32 - 32: Ii11111i . iiI1i1 . iiI1i1
      if 62 - 62: I1ii11iIi11i + iiI1i1 % Ii11111i + OOooOOo
      if 33 - 33: O0 . iiI1i1 . I1IiiI
      if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
      if 29 - 29: I1ii11iIi11i + oO0o % O0
   OOoo0O = '/streaming/info'
   o0oo = self . GetDefaultParams ( )
   if stype == 'onair' : o0oo [ 'osCode' ] = 'CSOD0400'
   if 10 - 10: I11i / Ooo0OO0oOO - I1IiiI * iIii1I11I1II1 - I1IiiI
   if 97 - 97: I1ii11iIi11i + I1IiiI * Ii1I + OOooOOo % Ii11111i
   if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + Ooo0OO0oOO / OoOoOO00
   i1 = {
 'isTrusted' : 'false'
 , 'NONE' : '0'
 , 'CAPTURING_PHASE' : '1'
 , 'AT_TARGET' : '2'
 , 'BUBBLING_PHASE' : '3'
 , 'type' : 'oocCreate'
 , 'eventPhase' : '0'
 , 'bubbles' : 'false'
 , 'cancelable' : 'false'
 , 'defaultPrevented' : 'false'
 , 'composed' : 'false'
 , 'timeStamp' : '2158.7350000045262'
 , 'returnValue' : 'true'
 , 'cancelBubble' : 'false'
 }
   if 11 - 11: iiI1i1 * I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii11111i
   OOO = self . makeOocUrl ( i1 )
   oo0OOo0 = urllib . quote ( OOO )
   if 47 - 47: Ooo0OO0oOO + OoOoOO00 * Oo0Ooo / Ii - Ii11111i % iIii1I11I1II1
   if 26 - 26: I1ii11iIi11i * Ii11111i . II111iiii * Ii1I
   if 28 - 28: OoO0O00 . i1IIi * I1IiiI + O0 . i1IIi - Ii
   oooooOoo0ooo = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'callingFrom' : 'HTML5'
 , 'streamCode' : III1Iiii1I11
   , 'adReq' : 'none'
 , 'ooc' : OOO
 }
   oooooOoo0ooo [ 'deviceId' ] = O0O0oOO00O00o
   if 38 - 38: Ooo0OO0oOO
   oo0 = self . URL_DOMAIN + OOoo0O
   Ooo00o0Oooo = o0oo
   Ooo00o0Oooo . update ( oooooOoo0ooo )
   if 84 - 84: o0oOOo0O0Ooo % II111iiii . i11iIiiIii / OoO0O00
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s; %s=%s'
 % ( '_tving_token' , self . TVING_TOKEN
 , 'onClickEvent2' , oo0OOo0
 , 'POC_USERINFO' , self . POC_USERINFO
 )
 )
 , ( 'origin' , 'https://www.tving.com' )
 , ( 'Referer' , 'https://www.tving.com/vod/player/' + mediacode )
 ]
   if 80 - 80: Ooo0OO0oOO . i11iIiiIii - o0oOOo0O0Ooo
   Ooo = self . SESSION . Request ( oo0 , params = Ooo00o0Oooo , cookie = I1Ii11I1Ii1i )
   if 25 - 25: OoO0O00
   O0OOO = json . loads ( Ooo )
   if 62 - 62: OOooOOo + O0
   if 98 - 98: o0oOOo0O0Ooo
   if Oo0o00 != '' :
    Oo0o00 = O0OOO [ 'stream' ] [ 'drm_license_assertion' ]
    i1I11i1I = O0OOO [ 'stream' ] [ 'broadcast' ] [ 'widevine' ] [ 'broad_url' ] + '&' + str ( self . GetNoCache ( 2 ) )
   else :
    if not ( 'broad_url' in O0OOO [ 'stream' ] [ 'broadcast' ] ) : return i1I11i1I , Oo0o00
    i1I11i1I = O0OOO [ 'stream' ] [ 'broadcast' ] [ 'broad_url' ]
    if 51 - 51: Oo0Ooo - oO0o + II111iiii * Ii1I . I11i + oO0o
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 78 - 78: i11iIiiIii / Ii11111i - Ii1I / OOooOOo + oO0o
  return i1I11i1I , Oo0o00
  if 82 - 82: Ii1I
  if 46 - 46: OoooooooOO . i11iIiiIii
 def CheckQuality ( self , sel_qt , qt_list ) :
  for OOo0oO00ooO00 in qt_list :
   if sel_qt >= OOo0oO00ooO00 . keys ( ) [ 0 ] : return OOo0oO00ooO00 . get ( OOo0oO00ooO00 . keys ( ) [ 0 ] )
   oOO0O00oO0Ooo = OOo0oO00ooO00 . get ( OOo0oO00ooO00 . keys ( ) [ 0 ] )
  return oOO0O00oO0Ooo
  if 67 - 67: OoO0O00 - OOooOOo
  if 36 - 36: iiI1i1
 def makeOocUrl ( self , ooc_params ) :
  oo0 = ''
  for o00oooO0Oo , o0O0OOO0Ooo in ooc_params . items ( ) :
   oo0 += "%s=%s^" % ( o00oooO0Oo , o0O0OOO0Ooo )
  return oo0
  if 36 - 36: Ii / O0 * Oo0Ooo - OOooOOo % iIii1I11I1II1 * oO0o
  if 79 - 79: O0
 def GetLiveChannelList ( self , stype , page_int ) :
  oOO00O = [ ]
  OOOoo0OO = False
  if 57 - 57: OoO0O00 / Ii
  try :
   OOoo0O = '/v2/media/lives'
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * OOooOOo . I1IiiI * I1IiiI
   if stype == 'onair' :
    I111I1Iiii1i = 'CPCS0100,CPCS0400'
   else :
    I111I1Iiii1i = 'CPCS0300'
    if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
   o0oo = self . GetDefaultParams ( )
   oooooOoo0ooo = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . LIVE_LIMIT )
 , 'order' : 'rating'
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'channelType' : I111I1Iiii1i

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
   oo0 = self . makeurl ( self . API_DOMAIN , OOoo0O , oooooOoo0ooo , o0oo )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 33 - 33: Ooo0OO0oOO + Ii11111i * oO0o / iIii1I11I1II1 - I1IiiI
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   O0OOO = json . loads ( Ooo )
   if 54 - 54: Ooo0OO0oOO / OOooOOo . oO0o % Ii11111i
   if not ( 'result' in O0OOO [ 'body' ] ) : return oOO00O , OOOoo0OO
   Oo = O0OOO [ 'body' ] [ 'result' ]
   if 65 - 65: Ii1I - oO0o + oO0o + II111iiii
   if 96 - 96: OOooOOo % O0 / O0
   for ooOOoooooo in Oo :
    iIi1 = OoOOoOooooOOo = oOo0O = oo0O0 = ''
    if 22 - 22: OoOoOO00 . OOooOOo * OoOoOO00
    O000OOO = ooOOoooooo [ 'live_code' ]
    iIi1 = ooOOoooooo [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 20 - 20: o0oOOo0O0Ooo . II111iiii % OOooOOo * iIii1I11I1II1
    if ooOOoooooo [ 'schedule' ] [ 'episode' ] != None :
     OoOOoOooooOOo = ooOOoooooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     OoOOoOooooOOo = OoOOoOooooOOo + ', ' + str ( ooOOoooooo [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if ooOOoooooo [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      oOo0O = ooOOoooooo [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     oo0O0 = ooOOoooooo [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     OoOOoOooooOOo = ooOOoooooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if ooOOoooooo [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      oOo0O = ooOOoooooo [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     oo0O0 = ooOOoooooo [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 98 - 98: I1IiiI % Ii1I * OoooooooOO
    if oOo0O == '' :
     oOo0O = ooOOoooooo [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if oOo0O != '' : oOo0O = self . IMG_DOMAIN + oOo0O
    if 51 - 51: iIii1I11I1II1 . OoOoOO00 / oO0o + o0oOOo0O0Ooo
    if 33 - 33: Ii . II111iiii % Ii11111i + o0oOOo0O0Ooo
    oO00O000oO0 = { 'channel' : unicode ( iIi1 )
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'mediacode' : O000OOO
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 }
    if 79 - 79: I11i - OoooooooOO - oO0o - iIii1I11I1II1 * OOooOOo
    oOO00O . append ( oO00O000oO0 )
    if 4 - 4: i11iIiiIii . OoooooooOO / OoO0O00 % Ooo0OO0oOO % I11i * O0
   if O0OOO [ 'body' ] [ 'has_more' ] == 'Y' : OOOoo0OO = True
   if 14 - 14: OOooOOo / o0oOOo0O0Ooo
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 32 - 32: I1IiiI * Oo0Ooo
  return oOO00O , OOOoo0OO
  if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / Ii / II111iiii
  if 29 - 29: I1IiiI % I1IiiI
 def GetProgramList ( self , stype , orderby , page_int ) :
  oOO00O = [ ]
  OOOoo0OO = False
  if 94 - 94: iIii1I11I1II1 / Oo0Ooo % Ii11111i * Ii11111i * II111iiii
  try :
   OOoo0O = '/v2/media/episodes'
   if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
   o0oo = self . GetDefaultParams ( )
   oooooOoo0ooo = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . VOD_LIMIT )
 , 'order' : orderby
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'lastFrequency' : 'y'
 , 'personal' : 'N'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if stype != 'all' : oooooOoo0ooo [ 'multiCategoryCode' ] = stype
   if 62 - 62: OOooOOo / oO0o - OoO0O00 . I11i
   oo0 = self . makeurl ( self . API_DOMAIN , OOoo0O , oooooOoo0ooo , o0oo )
   if 11 - 11: I1ii11iIi11i . OoO0O00 * iiI1i1 * OoooooooOO + Ii
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 33 - 33: O0 * o0oOOo0O0Ooo - Ooo0OO0oOO % Ooo0OO0oOO
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   O0OOO = json . loads ( Ooo )
   if 18 - 18: Ooo0OO0oOO / Oo0Ooo * Ooo0OO0oOO + Ooo0OO0oOO * i11iIiiIii * I1ii11iIi11i
   if not ( 'result' in O0OOO [ 'body' ] ) : return oOO00O , OOOoo0OO
   Oo = O0OOO [ 'body' ] [ 'result' ]
   if 11 - 11: Ii / OoOoOO00 - iiI1i1 * OoooooooOO + OoooooooOO . OoOoOO00
   if 26 - 26: Ii1I % I1ii11iIi11i
   for ooOOoooooo in Oo :
    o00Oo0oooooo = ooOOoooooo [ 'program' ] [ 'code' ]
    OoOOoOooooOOo = ooOOoooooo [ 'program' ] [ 'name' ] [ 'ko' ]
    oOo0O = self . IMG_DOMAIN + ooOOoooooo [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    oo0O0 = ooOOoooooo [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    O0oO0 = ooOOoooooo [ 'program' ] [ 'channel_code' ]
    if 7 - 7: I1IiiI
    oO00O000oO0 = { 'program' : o00Oo0oooooo
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 , 'channel' : O0oO0
 }
    if 41 - 41: I11i * iIii1I11I1II1 / II111iiii * oO0o
    oOO00O . append ( oO00O000oO0 )
    if 22 - 22: OoooooooOO
    if 75 - 75: o0oOOo0O0Ooo + o0oOOo0O0Ooo + i1IIi - i1IIi
   if O0OOO [ 'body' ] [ 'has_more' ] == 'Y' : OOOoo0OO = True
   if 76 - 76: OoO0O00 . O0 % O0 - o0oOOo0O0Ooo - iIii1I11I1II1 - I1IiiI
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 53 - 53: i1IIi
  return oOO00O , OOOoo0OO
  if 59 - 59: o0oOOo0O0Ooo
  if 81 - 81: OoOoOO00 - OoOoOO00 . Ii11111i
 def GetEpisodoList ( self , program_code , page_int ) :
  oOO00O = [ ]
  OOOoo0OO = False
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
  try :
   OOoo0O = '/v2/media/frequency/program/' + program_code
   if 7 - 7: O0 * i11iIiiIii * Ii1I + Ii % OoO0O00 - Ii
   o0oo = self . GetDefaultParams ( )
   oooooOoo0ooo = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   oo0 = self . makeurl ( self . API_DOMAIN , OOoo0O , oooooOoo0ooo , o0oo )
   if 23 - 23: i11iIiiIii
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   O0OOO = json . loads ( Ooo )
   if 81 - 81: iiI1i1 % i1IIi . iIii1I11I1II1
   if not ( 'result' in O0OOO [ 'body' ] ) : return oOO00O , OOOoo0OO
   Oo = O0OOO [ 'body' ] [ 'result' ]
   if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / iiI1i1
   I11iI = int ( O0OOO [ 'body' ] [ 'total_count' ] )
   ooOoo = int ( I11iI // self . EPISODE_LIMIT ) + 1
   I1III1111iIi = ( I11iI - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   if 38 - 38: Ii11111i + I11i / Ooo0OO0oOO % Ii - I1ii11iIi11i
   for iI11 in range ( self . EPISODE_LIMIT ) :
    if I1III1111iIi - iI11 < 0 : break
    Ii1Io0OO0o0o00o = Oo [ I1III1111iIi - iI11 ] [ 'episode' ] [ 'code' ]
    OoOOoOooooOOo = Oo [ I1III1111iIi - iI11 ] [ 'vod_name' ] [ 'ko' ]
    if Oo [ I1III1111iIi - iI11 ] [ 'episode' ] [ 'image' ] != [ ] :
     oOo0O = self . IMG_DOMAIN + Oo [ I1III1111iIi - iI11 ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     oOo0O = self . IMG_DOMAIN + Oo [ I1III1111iIi - iI11 ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    oo0O0 = Oo [ I1III1111iIi - iI11 ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 100 - 100: oO0o / Ooo0OO0oOO / I1ii11iIi11i
    oO00O000oO0 = { 'episode' : Ii1Io0OO0o0o00o
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 }
    if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
    oOO00O . append ( oO00O000oO0 )
    if 10 - 10: Ii11111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / Ooo0OO0oOO / I1ii11iIi11i
   if ooOoo > page_int : OOOoo0OO = True
   if 42 - 42: I1IiiI
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 38 - 38: OOooOOo + II111iiii % Ii % OoOoOO00 - Ii1I / OoooooooOO
  return oOO00O , OOOoo0OO
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  if 85 - 85: Ii1I % Ii11111i + I11i / o0oOOo0O0Ooo . oO0o + OOooOOo
 def GetMovieList ( self , orderby , page_int ) :
  oOO00O = [ ]
  OOOoo0OO = False
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
  try :
   OOoo0O = '/v2/media/movies'
   if 28 - 28: Ii11111i . Ii11111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / Ii11111i
   o0oo = self . GetDefaultParams ( )
   oooooOoo0ooo = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : '338723'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 27 - 27: OoO0O00 + Ii - i1IIi
   oo0 = self . makeurl ( self . API_DOMAIN , OOoo0O , oooooOoo0ooo , o0oo )
   if 69 - 69: iiI1i1 - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 79 - 79: O0 * i11iIiiIii - iiI1i1 / iiI1i1
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   O0OOO = json . loads ( Ooo )
   if 48 - 48: O0
   if not ( 'result' in O0OOO [ 'body' ] ) : return oOO00O , OOOoo0OO
   Oo = O0OOO [ 'body' ] [ 'result' ]
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
   if 25 - 25: iiI1i1 + Ii1I / Ii . o0oOOo0O0Ooo % O0 * OoO0O00
   for ooOOoooooo in Oo :
    o0O0oo0OO0O = ooOOoooooo [ 'movie' ] [ 'code' ]
    OoOOoOooooOOo = ooOOoooooo [ 'movie' ] [ 'name' ] [ 'ko' ]
    oOo0O = self . IMG_DOMAIN + ooOOoooooo [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    oo0O0 = ooOOoooooo [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 68 - 68: oO0o . I11i % OoooooooOO . I11i
    oO00O000oO0 = { 'moviecode' : o0O0oo0OO0O
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 }
    if 64 - 64: iIii1I11I1II1 / I1IiiI . II111iiii + OoooooooOO . OoO0O00
    oOO00O . append ( oO00O000oO0 )
    if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
    if 39 - 39: O0 + Ooo0OO0oOO
   if O0OOO [ 'body' ] [ 'has_more' ] == 'Y' : OOOoo0OO = True
   if 91 - 91: OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoOoOO00 + O0
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 26 - 26: I1ii11iIi11i - OoooooooOO
  return oOO00O , OOOoo0OO
  if 11 - 11: I1IiiI * oO0o
  if 81 - 81: Ii11111i + iiI1i1
 def GetSearchList ( self , search_key , userid , page_int , stype ) :
  o0oo0 = [ ]
  OOOoo0OO = False
  if 97 - 97: OoOoOO00 % I1ii11iIi11i
  try :
   OOoo0O = '/search/getSearch.jsp'
   if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   o0oo = self . GetDefaultParams ( )
   oooooOoo0ooo = { 'kwd' : search_key
 , 'notFoundText' : search_key
 , 'userid' : userid
 , 'siteName' : 'TVING_WEB'
 , 'category' : 'PROGRAM' if stype == 'vod' else 'VODMV'
   , 'pageNum' : str ( page_int )
 , 'pageSize' : str ( self . SEARCH_LIMIT )
 , 'indexType' : 'both'
 , 'methodType' : 'allwordthruindex'
 , 'payFree' : 'ALL'
 , 'runTime' : 'ALL'
 , 'grade' : 'ALL'
 , 'genre' : 'ALL'
 , 'screen' : self . SCREENCODE
 , 'os' : self . OSCODE
 , 'network' : self . NETWORKCODE
 , 'sort1' : 'NO'
 , 'sort2' : 'NO'
 , 'sort3' : 'NO'
 , 'type1' : 'desc'
 , 'type2' : 'desc'
 , 'type3' : 'desc'
 , 'fixedType' : 'Y'
 , 'spcMethod' : 'someword'
 , 'spcSize' : '0'
 , 'schReqCnt' : '0'
   , 'vodBCReqCnt' : '0'
   , 'programReqCnt' : self . SEARCH_LIMIT
 , 'vodMVReqCnt' : '0'
   , 'smrclipReqCnt' : '0'
   , 'pickClipReqCnt' : '0'
   , 'aloneReqCnt' : '0'
   , 'cSocialClipCnt' : '0'
 , 'boardReqCnt' : '0'
 , 'talkReqCnt' : '0'
 , 'nowTime' : ''
 , 'mode' : 'normal'
 , 'adult_yn' : ''
 , 'reKwd' : ''
 , 'xwd' : ''

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 55 - 55: Ii - I11i + II111iiii + Ii11111i % Ii1I
   oo0 = self . makeurl ( self . SEARCH_DOMAIN , OOoo0O , oooooOoo0ooo , None )
   if 41 - 41: i1IIi - I11i - Ii1I
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 8 - 8: OoO0O00 + Ooo0OO0oOO - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   O0OOO = json . loads ( Ooo )
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Ii
   if stype == 'vod' :
    if not ( 'programRsb' in O0OOO ) : return o0oo0 , OOOoo0OO
    iIIII = O0OOO [ 'programRsb' ] [ 'dataList' ]
    iIIIiiI1i1i = int ( O0OOO [ 'programRsb' ] [ 'count' ] )
    if 32 - 32: OoOoOO00 / OoO0O00 + OOooOOo
    if 32 - 32: iIii1I11I1II1 % Ii11111i
    for ooOOoooooo in iIIII :
     o00Oo0oooooo = ooOOoooooo [ 'mast_cd' ]
     OoOOoOooooOOo = ooOOoooooo [ 'mast_nm' ]
     oOo0O = self . IMG_DOMAIN + ooOOoooooo [ 'web_url' ]
     oo0O0 = ooOOoooooo [ 'mast_synop' ]
     if 65 - 65: Ii . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
     oO00O000oO0 = { 'program' : o00Oo0oooooo
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 }
     if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
     o0oo0 . append ( oO00O000oO0 )
   else :
    if not ( 'vodMVRsb' in O0OOO ) : return o0oo0 , OOOoo0OO
    Iii1iiIi1II = O0OOO [ 'vodMVRsb' ] [ 'dataList' ]
    iIIIiiI1i1i = int ( O0OOO [ 'vodMVRsb' ] [ 'count' ] )
    if 60 - 60: I1IiiI - oO0o * I11i % II111iiii
    if 62 - 62: iIii1I11I1II1
    for ooOOoooooo in Iii1iiIi1II :
     o00Oo0oooooo = ooOOoooooo [ 'mast_cd' ]
     OoOOoOooooOOo = ooOOoooooo [ 'mast_nm' ]
     oOo0O = self . IMG_DOMAIN + ooOOoooooo [ 'web_url' ]
     oo0O0 = ooOOoooooo [ 'mast_synop' ]
     if 12 - 12: OOooOOo / o0oOOo0O0Ooo
     for iiI1I1 in ooOOoooooo [ 'bill' ] :
      if iiI1I1 == '338723' :
       oO00O000oO0 = { 'movie' : o00Oo0oooooo
 , 'title' : unicode ( OoOOoOooooOOo )
 , 'thumbnail' : oOo0O
 , 'synopsis' : unicode ( oo0O0 )
 }
       if 56 - 56: I1IiiI . O0 + Oo0Ooo
       o0oo0 . append ( oO00O000oO0 )
       if 1 - 1: Ii11111i
       if 97 - 97: OOooOOo + Ii11111i + O0 + i11iIiiIii
       if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
       if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . Ii11111i % Ii11111i + i11iIiiIii
  except Exception as Oo0oOOo :
   print ( Oo0oOOo )
   if 72 - 72: iIii1I11I1II1 * Ii1I % Ii / OoO0O00
  return o0oo0 , OOOoo0OO
  if 35 - 35: Ii + i1IIi % I1ii11iIi11i % I11i + oO0o
  if 17 - 17: i1IIi
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
