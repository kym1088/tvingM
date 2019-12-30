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
  self . TVING_UUID = '-'
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
  self . TVING_UUID = login_params . get ( 'tving_uuid' )
  if 15 - 15: Ii / Ii1I . Ii1I - i1IIi
 def LoadCredential ( self ) :
  o00oOO0 = {
 'tving_token' : self . TVING_TOKEN
 , 'poc_userinfo' : self . POC_USERINFO
 , 'tving_uuid' : self . TVING_UUID
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
  OoO0O0 = '-'
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
  try :
   Ii11Ii1I = self . LOGIN_DOMAIN + '/pc/user/doLogin.tving'
   if 72 - 72: Ii11111i / i1IIi * Oo0Ooo - Ooo0OO0oOO
   iI = { 'userId' : user_id
 , 'password' : user_pw
 , 'loginType' : '10' if login_type == '0' else '20'
 , 'autoLogin' : 'false'
 , 'cjOneCookie' : ''
 , 'kaptcha' : ''

   , 'returnUrl' : ''
 , 'csite' : ''
 }
   if 51 - 51: II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % I1ii11iIi11i / Ii
   I1Ii11I1Ii1i = self . SESSION . RequestCookie ( Ii11Ii1I , iI )
   if 49 - 49: o0oOOo0O0Ooo
   if 35 - 35: OoOoOO00 - OoooooooOO / I1ii11iIi11i % i1IIi
   if 78 - 78: I11i
   for OO00Oo in I1Ii11I1Ii1i . split ( ',' ) :
    OO00Oo = OO00Oo . strip ( )
    if OO00Oo . startswith ( '_tving_token' ) :
     O0OOO0OOoO0O = OO00Oo . split ( ';' ) [ 0 ]
     O0OOO0OOoO0O = O0OOO0OOoO0O . split ( '=' ) [ 1 ]
     if 70 - 70: iiI1i1 * Oo0Ooo * I11i / Ii1I
    if OO00Oo . startswith ( 'POC_USERINFO' ) :
     oO = OO00Oo . split ( ';' ) [ 0 ]
     oO = oO . split ( '=' ) [ 1 ]
     if 93 - 93: OoO0O00 % oO0o . OoO0O00 * Ooo0OO0oOO % Ii1I . II111iiii
   if O0OOO0OOoO0O : i1II1 = True
   if 38 - 38: o0oOOo0O0Ooo
   OoO0O0 = self . GetDeviceList ( O0OOO0OOoO0O , oO )
   if 57 - 57: O0 / oO0o * Ooo0OO0oOO / OoOoOO00 . II111iiii
   if 26 - 26: Ii11111i
  except Exception as OOO :
   O0OOO0OOoO0O = oO = ''
   OoO0O0 = '-'
   if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
  o00oOO0 = {
 'tving_token' : O0OOO0OOoO0O
 , 'poc_userinfo' : oO
 , 'tving_uuid' : OoO0O0
 }
  self . SaveCredential ( o00oOO0 )
  if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
  return i1II1
  if 75 - 75: oO0o
  if 50 - 50: Ii1I / Oo0Ooo - oO0o - I11i % Ii11111i - oO0o
 def GetBroadURL ( self , mediacode , sel_quality , stype ) :
  OOO0o = ''
  IiI1 = ''
  Oo0O00Oo0o0 = self . TVING_UUID
  if 87 - 87: Ii * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
  O0ooo0O0oo0 = self . TVING_TOKEN
  oo0oOo = self . POC_USERINFO
  if 89 - 89: OoOoOO00
  if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + Ii
  if 4 - 4: Ii + O0 * OOooOOo
  if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
  if 25 - 25: I1ii11iIi11i
  if 7 - 7: i1IIi / I1IiiI * Ooo0OO0oOO . iiI1i1 . iIii1I11I1II1
  if 13 - 13: OOooOOo / i11iIiiIii
  try :
   if stype != 'tvingtv' :
    if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
    o0o00OO0 = '/v2/media/stream/info'
    if 7 - 7: OOooOOo + Ooo0OO0oOO + O0
    IiO0OOO = self . GetDefaultParams ( )
    II11iIiIIIiI = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'noCache' : str ( self . GetNoCache ( 1 ) )
 , 'callingFrom' : 'HTML5'
 , 'adReq' : 'none'
 , 'ooc' : ''
 }
    II11iIiIIIiI [ 'deviceId' ] = Oo0O00Oo0o0
    if 67 - 67: Ooo0OO0oOO . Ii11111i . O0
    oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , IiO0OOO , II11iIiIIIiI )
    if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
    I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , O0ooo0O0oo0 , 'POC_USERINFO' , oo0oOo ) )
 ]
    if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / Ii11111i
    Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
    I1111IIi = json . loads ( Ooo )
    if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
    if not ( 'stream' in I1111IIi [ 'body' ] ) : return OOO0o , IiI1
    I1 = I1111IIi [ 'body' ] [ 'stream' ]
    if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
    if 9 - 9: OoooooooOO
    if 'drm_license_assertion' in I1 :
     IiI1 = I1 [ 'drm_license_assertion' ]
    else :
     if 62 - 62: OOooOOo / OoO0O00 + Ii1I / OoO0O00 . II111iiii
     ooOOoooooo = I1 [ 'broadcast' ] [ 'broad_url' ]
     if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % Ii11111i * iiI1i1 . i11iIiiIii
    III1Iiii1I11 = I1 [ 'quality' ]
    if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
    o00oooO0Oo = [ ]
    for o0O0OOO0Ooo in III1Iiii1I11 :
     if o0O0OOO0Ooo [ 'active' ] == 'Y' :
      o00oooO0Oo . append ( { IiII . get ( o0O0OOO0Ooo [ 'code' ] ) : o0O0OOO0Ooo [ 'code' ] } )
      if 45 - 45: O0 / o0oOOo0O0Ooo
    i1 = self . CheckQuality ( sel_quality , o00oooO0Oo )
    if 8 - 8: oO0o * OoOoOO00 - Ii1I - OoO0O00 * OOooOOo % I1IiiI
   else :
    for ii , oOooOOOoOo in IiII . items ( ) :
     if oOooOOOoOo == sel_quality :
      i1 = ii
      if 41 - 41: Ii1I - O0 - O0
      if 68 - 68: OOooOOo % Ooo0OO0oOO
  except Exception as OOO :
   for ii , oOooOOOoOo in IiII . items ( ) :
    if oOooOOOoOo == sel_quality :
     i1 = ii
   return OOO0o , IiI1
   if 88 - 88: iIii1I11I1II1 - Ii + OOooOOo
  print Oo0O00Oo0o0 , i1
  if 40 - 40: I1IiiI * Ii1I + OOooOOo % Ii11111i
  if 74 - 74: oO0o - Oo0Ooo + OoooooooOO + Ooo0OO0oOO / OoOoOO00
  try :
   if 23 - 23: O0
   o0o00OO0 = '/streaming/info'
   IiO0OOO = self . GetDefaultParams ( )
   if stype == 'onair' : IiO0OOO [ 'osCode' ] = 'CSOD0400'
   if 85 - 85: Ii1I
   if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + Ii1I % OoooooooOO % OoO0O00
   if 42 - 42: OoO0O00 / I11i / o0oOOo0O0Ooo + Ii11111i / OoOoOO00
   o0OoOO000ooO0 = {
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
   if 56 - 56: Ii11111i
   oo0oO0oOOoo = self . makeOocUrl ( o0OoOO000ooO0 )
   oOo00O0oo00o0 = urllib . quote ( oo0oO0oOOoo )
   if 45 - 45: O0
   if 26 - 26: I11i - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
   if 91 - 91: o0oOOo0O0Ooo . iIii1I11I1II1 / oO0o + i1IIi
   II11iIiIIIiI = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'callingFrom' : 'HTML5'
 , 'streamCode' : i1
   , 'adReq' : 'none'
 , 'ooc' : oo0oO0oOOoo
 }
   II11iIiIIIiI [ 'deviceId' ] = Oo0O00Oo0o0
   if 42 - 42: Ii . o0oOOo0O0Ooo . Ii - I1ii11iIi11i
   oo0 = self . URL_DOMAIN + o0o00OO0
   i1ii1I1I1 = IiO0OOO
   i1ii1I1I1 . update ( II11iIiIIIiI )
   if 74 - 74: o0oOOo0O0Ooo . Ii11111i
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s; %s=%s'
 % ( '_tving_token' , O0ooo0O0oo0
 , 'onClickEvent2' , oOo00O0oo00o0
 , 'POC_USERINFO' , oo0oOo
 )
 )
 , ( 'origin' , 'https://www.tving.com' )
 , ( 'Referer' , 'https://www.tving.com/vod/player/' + mediacode )
 ]
   if 18 - 18: OOooOOo + Ii11111i - Ii1I . II111iiii + i11iIiiIii
   Ooo = self . SESSION . Request ( oo0 , params = i1ii1I1I1 , cookie = I1Ii11I1Ii1i )
   if 20 - 20: Ooo0OO0oOO
   I1111IIi = json . loads ( Ooo )
   if 52 - 52: II111iiii - OoooooooOO % Ii1I + I1IiiI * Oo0Ooo . iiI1i1
   if 75 - 75: Ii + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . Ii11111i
   if IiI1 != '' :
    IiI1 = I1111IIi [ 'stream' ] [ 'drm_license_assertion' ]
    OOO0o = I1111IIi [ 'stream' ] [ 'broadcast' ] [ 'widevine' ] [ 'broad_url' ] + '&' + str ( self . GetNoCache ( 2 ) )
   else :
    if not ( 'broad_url' in I1111IIi [ 'stream' ] [ 'broadcast' ] ) : return OOO0o , IiI1
    OOO0o = I1111IIi [ 'stream' ] [ 'broadcast' ] [ 'broad_url' ]
    if 55 - 55: OOooOOo . I1IiiI
  except Exception as OOO :
   print ( OOO )
   if 61 - 61: Oo0Ooo % iiI1i1 . Oo0Ooo
  return OOO0o , IiI1
  if 100 - 100: Ooo0OO0oOO * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
 def CheckQuality ( self , sel_qt , qt_list ) :
  for o0iI11I1II in qt_list :
   if sel_qt >= o0iI11I1II . keys ( ) [ 0 ] : return o0iI11I1II . get ( o0iI11I1II . keys ( ) [ 0 ] )
   Ii1IIiI1i = o0iI11I1II . get ( o0iI11I1II . keys ( ) [ 0 ] )
  return Ii1IIiI1i
  if 92 - 92: iiI1i1 . iiI1i1 + OoO0O00
  if 9 - 9: I1IiiI * O0 + iiI1i1 - I11i * Ooo0OO0oOO
 def makeOocUrl ( self , ooc_params ) :
  oo0 = ''
  for ii , oOooOOOoOo in ooc_params . items ( ) :
   oo0 += "%s=%s^" % ( ii , oOooOOOoOo )
  return oo0
  if 64 - 64: iIii1I11I1II1 - iIii1I11I1II1 / i11iIiiIii % Oo0Ooo - Ii11111i
  if 56 - 56: I1IiiI . I11i * Ii1I - Ii11111i
 def GetLiveChannelList ( self , stype , page_int ) :
  II1I11Ii1 = [ ]
  Iii1I11 = False
  if 85 - 85: I1ii11iIi11i - iIii1I11I1II1
  try :
   o0o00OO0 = '/v2/media/lives'
   if 31 - 31: OoooooooOO - OoooooooOO * I11i - oO0o
   if stype == 'onair' :
    OooOOO0OOOO = 'CPCS0100,CPCS0400'
   else :
    OooOOO0OOOO = 'CPCS0300'
    if 29 - 29: Ii11111i + II111iiii % O0 . OoOoOO00 + oO0o / I1IiiI
   IiO0OOO = self . GetDefaultParams ( )
   II11iIiIIIiI = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . LIVE_LIMIT )
 , 'order' : 'rating'
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'channelType' : OooOOO0OOOO

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 72 - 72: Ii * Oo0Ooo . I1IiiI - II111iiii + i1IIi
   oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , II11iIiIIIiI , IiO0OOO )
   if 10 - 10: oO0o + i1IIi
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 87 - 87: I1IiiI
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
   if not ( 'result' in I1111IIi [ 'body' ] ) : return II1I11Ii1 , Iii1I11
   i1OOoO = I1111IIi [ 'body' ] [ 'result' ]
   if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * I11i * Ii1I
   if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
   for o0O0OOO0Ooo in i1OOoO :
    o0o0O0O00oOOo = iIIIiIi = OO0O0 = I11I11 = ''
    if 69 - 69: OoOoOO00
    OO0OoOO0o0o = o0O0OOO0Ooo [ 'live_code' ]
    o0o0O0O00oOOo = o0O0OOO0Ooo [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 95 - 95: i11iIiiIii
    if o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] != None :
     iIIIiIi = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     iIIIiIi = iIIIiIi + ', ' + str ( o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      OO0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     I11I11 = o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     iIIIiIi = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      OO0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     I11I11 = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 32 - 32: OOooOOo
    if OO0O0 == '' :
     OO0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if OO0O0 != '' : OO0O0 = self . IMG_DOMAIN + OO0O0
    if 42 - 42: iiI1i1 * O0 % i1IIi . OOooOOo / o0oOOo0O0Ooo
    if 32 - 32: I1IiiI * Oo0Ooo
    O0OooOo0o = { 'channel' : unicode ( o0o0O0O00oOOo )
 , 'title' : unicode ( iIIIiIi )
 , 'mediacode' : OO0OoOO0o0o
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 }
    if 29 - 29: I1IiiI % I1IiiI
    II1I11Ii1 . append ( O0OooOo0o )
    if 94 - 94: iIii1I11I1II1 / Oo0Ooo % Ii11111i * Ii11111i * II111iiii
   if I1111IIi [ 'body' ] [ 'has_more' ] == 'Y' : Iii1I11 = True
   if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
  except Exception as OOO :
   print ( OOO )
   if 62 - 62: OOooOOo / oO0o - OoO0O00 . I11i
  return II1I11Ii1 , Iii1I11
  if 11 - 11: I1ii11iIi11i . OoO0O00 * iiI1i1 * OoooooooOO + Ii
  if 33 - 33: O0 * o0oOOo0O0Ooo - Ooo0OO0oOO % Ooo0OO0oOO
 def GetProgramList ( self , stype , orderby , page_int ) :
  II1I11Ii1 = [ ]
  Iii1I11 = False
  if 18 - 18: Ooo0OO0oOO / Oo0Ooo * Ooo0OO0oOO + Ooo0OO0oOO * i11iIiiIii * I1ii11iIi11i
  try :
   o0o00OO0 = '/v2/media/episodes'
   if 11 - 11: Ii / OoOoOO00 - iiI1i1 * OoooooooOO + OoooooooOO . OoOoOO00
   IiO0OOO = self . GetDefaultParams ( )
   II11iIiIIIiI = { 'pageNo' : str ( page_int )
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
   if stype != 'all' : II11iIiIIIiI [ 'multiCategoryCode' ] = stype
   if 26 - 26: Ii1I % I1ii11iIi11i
   oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , II11iIiIIIiI , IiO0OOO )
   if 76 - 76: iiI1i1 * Ii11111i
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 52 - 52: OOooOOo
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 19 - 19: I1IiiI
   if not ( 'result' in I1111IIi [ 'body' ] ) : return II1I11Ii1 , Iii1I11
   i1OOoO = I1111IIi [ 'body' ] [ 'result' ]
   if 25 - 25: Ii1I / Ii
   if 31 - 31: OOooOOo . O0 % I1IiiI . o0oOOo0O0Ooo + iiI1i1
   for o0O0OOO0Ooo in i1OOoO :
    o0ooo0 = o0O0OOO0Ooo [ 'program' ] [ 'code' ]
    iIIIiIi = o0O0OOO0Ooo [ 'program' ] [ 'name' ] [ 'ko' ]
    OO0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    for oOOOoo00 in o0O0OOO0Ooo [ 'program' ] [ 'image' ] :
     if oOOOoo00 [ 'code' ] == 'CAIP0900' :
      OO0O0 = self . IMG_DOMAIN + oOOOoo00 [ 'url' ]
    I11I11 = o0O0OOO0Ooo [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    iiIiIIIiiI = o0O0OOO0Ooo [ 'program' ] [ 'channel_code' ]
    if 12 - 12: O0 - o0oOOo0O0Ooo
    O0OooOo0o = { 'program' : o0ooo0
 , 'title' : unicode ( iIIIiIi )
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 , 'channel' : iiIiIIIiiI
 }
    if 81 - 81: OoOoOO00 - OoOoOO00 . Ii11111i
    II1I11Ii1 . append ( O0OooOo0o )
    if 73 - 73: I11i % i11iIiiIii - I1IiiI
    if 7 - 7: O0 * i11iIiiIii * Ii1I + Ii % OoO0O00 - Ii
   if I1111IIi [ 'body' ] [ 'has_more' ] == 'Y' : Iii1I11 = True
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
  except Exception as OOO :
   print ( OOO )
   if 23 - 23: i11iIiiIii
  return II1I11Ii1 , Iii1I11
  if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
  if 81 - 81: iiI1i1 % i1IIi . iIii1I11I1II1
 def GetEpisodoList ( self , program_code , page_int , orderby = 'desc' ) :
  II1I11Ii1 = [ ]
  Iii1I11 = False
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / iiI1i1
  if 6 - 6: Ii11111i / I1IiiI % OOooOOo - I1IiiI
  if 31 - 31: OOooOOo
  if 23 - 23: Ooo0OO0oOO . iiI1i1
  if 92 - 92: OoOoOO00 + Ooo0OO0oOO * Ii1I % I1IiiI
  if 42 - 42: Oo0Ooo
  if 76 - 76: I1IiiI * Ii11111i % Ooo0OO0oOO
  try :
   o0o00OO0 = '/v2/media/frequency/program/' + program_code
   if 57 - 57: iIii1I11I1II1 - i1IIi / Ooo0OO0oOO - O0 * OoooooooOO % II111iiii
   IiO0OOO = self . GetDefaultParams ( )
   II11iIiIIIiI = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 68 - 68: OoooooooOO * I11i % OoOoOO00 - iiI1i1
   oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , II11iIiIIIiI , IiO0OOO )
   if 34 - 34: Ooo0OO0oOO . iIii1I11I1II1 * OoOoOO00 * oO0o / Ooo0OO0oOO / I1ii11iIi11i
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 10 - 10: Ii11111i + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / Ooo0OO0oOO / I1ii11iIi11i
   if not ( 'result' in I1111IIi [ 'body' ] ) : return II1I11Ii1 , Iii1I11
   i1OOoO = I1111IIi [ 'body' ] [ 'result' ]
   if 42 - 42: I1IiiI
   II1i11I = int ( I1111IIi [ 'body' ] [ 'total_count' ] )
   ii1I1IIii11 = int ( II1i11I // self . EPISODE_LIMIT ) + 1
   if orderby == 'desc' :
    O0o0oO = ( II1i11I - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    O0o0oO = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 38 - 38: oO0o % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
   for oo0000ooooO0o in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     iI1i11 = O0o0oO - oo0000ooooO0o
     if iI1i11 < 0 : break
    else :
     iI1i11 = O0o0oO + oo0000ooooO0o
     if iI1i11 >= II1i11I : break
     if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / Ii1I + I1ii11iIi11i
    ooo00Ooo = i1OOoO [ iI1i11 ] [ 'episode' ] [ 'code' ]
    iIIIiIi = i1OOoO [ iI1i11 ] [ 'vod_name' ] [ 'ko' ]
    if i1OOoO [ iI1i11 ] [ 'episode' ] [ 'image' ] != [ ] :
     OO0O0 = self . IMG_DOMAIN + i1OOoO [ iI1i11 ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     OO0O0 = self . IMG_DOMAIN + i1OOoO [ iI1i11 ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    I11I11 = i1OOoO [ iI1i11 ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
    O0OooOo0o = { 'episode' : ooo00Ooo
 , 'title' : unicode ( iIIIiIi )
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 }
    if 25 - 25: iiI1i1 + Ii1I / Ii . o0oOOo0O0Ooo % O0 * OoO0O00
    II1I11Ii1 . append ( O0OooOo0o )
    if 84 - 84: Ii % Ii1I + i11iIiiIii
   if ii1I1IIii11 > page_int : Iii1I11 = True
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  except Exception as OOO :
   print ( OOO )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
  return II1I11Ii1 , Iii1I11 , ii1I1IIii11
  if 19 - 19: OoO0O00 - Oo0Ooo . O0
  if 60 - 60: II111iiii + Oo0Ooo
 def GetMovieList ( self , orderby , page_int , premiumyn = False ) :
  II1I11Ii1 = [ ]
  Iii1I11 = False
  if 9 - 9: Ii * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
  if premiumyn == True :
   iiIIi = '338723,1513561'
  else :
   iiIIi = '338723'
   if 11 - 11: I1IiiI * oO0o
  try :
   o0o00OO0 = '/v2/media/movies'
   if 81 - 81: Ii11111i + iiI1i1
   IiO0OOO = self . GetDefaultParams ( )
   II11iIiIIIiI = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : iiIIi
   # I1IiiI . i1IIi * Ii / II111iiii * OoOoOO00 % I1ii11iIi11i
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 25 - 25: Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , II11iIiIIIiI , IiO0OOO )
   if 55 - 55: Ii - I11i + II111iiii + Ii11111i % Ii1I
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 41 - 41: i1IIi - I11i - Ii1I
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 8 - 8: OoO0O00 + Ooo0OO0oOO - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * oO0o
   if not ( 'result' in I1111IIi [ 'body' ] ) : return II1I11Ii1 , Iii1I11
   i1OOoO = I1111IIi [ 'body' ] [ 'result' ]
   if 9 - 9: Oo0Ooo - i11iIiiIii - OOooOOo * Ii1I + Ii
   if 44 - 44: II111iiii
   for o0O0OOO0Ooo in i1OOoO :
    OOOO0OOO = o0O0OOO0Ooo [ 'movie' ] [ 'code' ]
    iIIIiIi = o0O0OOO0Ooo [ 'movie' ] [ 'name' ] [ 'ko' ]
    OO0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    for oOOOoo00 in o0O0OOO0Ooo [ 'movie' ] [ 'image' ] :
     if oOOOoo00 [ 'code' ] == 'CAIM2100' :
      OO0O0 = self . IMG_DOMAIN + oOOOoo00 [ 'url' ]
    I11I11 = o0O0OOO0Ooo [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 3 - 3: OoO0O00
    O0OooOo0o = { 'moviecode' : OOOO0OOO
 , 'title' : unicode ( iIIIiIi . strip ( ) )
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 }
    if 97 - 97: Ooo0OO0oOO
    if premiumyn == True :
     iiIII1i = False
     for I1I in o0O0OOO0Ooo [ 'billing_package_id' ] :
      if I1I == '338723' :
       iiIII1i = True
       break
     if iiIII1i == False :
      O0OooOo0o [ 'title' ] = unicode ( O0OooOo0o [ 'title' ] + ' [Premium]' )
      if 68 - 68: Ii
    II1I11Ii1 . append ( O0OooOo0o )
    if 25 - 25: I1ii11iIi11i . Ii
    if 24 - 24: oO0o / i11iIiiIii + oO0o
   if I1111IIi [ 'body' ] [ 'has_more' ] == 'Y' : Iii1I11 = True
   if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
  except Exception as OOO :
   print ( OOO )
   if 88 - 88: OoOoOO00 / II111iiii
  return II1I11Ii1 , Iii1I11
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - Ii11111i + oO0o
  if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
 def GetSearchList ( self , search_key , userid , page_int , stype , premiumyn = False ) :
  iiI1I1 = [ ]
  Iii1I11 = False
  if 56 - 56: I1IiiI . O0 + Oo0Ooo
  try :
   o0o00OO0 = '/search/getSearch.jsp'
   if 1 - 1: Ii11111i
   IiO0OOO = self . GetDefaultParams ( )
   II11iIiIIIiI = { 'kwd' : search_key
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
   if 97 - 97: OOooOOo + Ii11111i + O0 + i11iIiiIii
   oo0 = self . makeurl ( self . SEARCH_DOMAIN , o0o00OO0 , II11iIiIIIiI , None )
   if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . Ii11111i % Ii11111i + i11iIiiIii
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 72 - 72: iIii1I11I1II1 * Ii1I % Ii / OoO0O00
   if stype == 'vod' :
    if not ( 'programRsb' in I1111IIi ) : return iiI1I1 , Iii1I11
    I11i1II = I1111IIi [ 'programRsb' ] [ 'dataList' ]
    OooiiIi1i = int ( I1111IIi [ 'programRsb' ] [ 'count' ] )
    if 27 - 27: OOooOOo * Ii . Ooo0OO0oOO % iiI1i1 * iiI1i1 . i1IIi
    if 72 - 72: OOooOOo % I1ii11iIi11i + OoO0O00 / oO0o + iiI1i1
    for o0O0OOO0Ooo in I11i1II :
     o0ooo0 = o0O0OOO0Ooo [ 'mast_cd' ]
     iIIIiIi = o0O0OOO0Ooo [ 'mast_nm' ]
     OO0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url' ]
     I11I11 = o0O0OOO0Ooo [ 'mast_synop' ]
     if 10 - 10: Ooo0OO0oOO / Ii + i11iIiiIii / Ii1I
     O0OooOo0o = { 'program' : o0ooo0
 , 'title' : unicode ( iIIIiIi )
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 }
     if 74 - 74: OOooOOo + O0 + i1IIi - i1IIi + II111iiii
     iiI1I1 . append ( O0OooOo0o )
   else :
    if not ( 'vodMVRsb' in I1111IIi ) : return iiI1I1 , Iii1I11
    oOOO0oo0 = I1111IIi [ 'vodMVRsb' ] [ 'dataList' ]
    OooiiIi1i = int ( I1111IIi [ 'vodMVRsb' ] [ 'count' ] )
    if 46 - 46: iiI1i1
    if 45 - 45: Ii
    for o0O0OOO0Ooo in oOOO0oo0 :
     o0ooo0 = o0O0OOO0Ooo [ 'mast_cd' ]
     iIIIiIi = o0O0OOO0Ooo [ 'mast_nm' ]
     OO0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url' ]
     I11I11 = o0O0OOO0Ooo [ 'mast_synop' ]
     if 21 - 21: oO0o . Ooo0OO0oOO . OOooOOo / Oo0Ooo / Ooo0OO0oOO
     i1iI1 = False
     ii1I1IiiI1ii1i = False
     for I1I in o0O0OOO0Ooo [ 'bill' ] :
      if I1I == '338723' : ii1I1IiiI1ii1i = True
      elif I1I == '1513561' : i1iI1 = True
      if 78 - 78: Ii . o0oOOo0O0Ooo . OOooOOo . I11i + oO0o
     if ii1I1IiiI1ii1i or ( premiumyn == True and i1iI1 ) :
      O0OooOo0o = { 'movie' : o0ooo0
 , 'title' : unicode ( iIIIiIi . strip ( ) )
 , 'thumbnail' : OO0O0
 , 'synopsis' : unicode ( I11I11 )
 }
      if ii1I1IiiI1ii1i == False : O0OooOo0o [ 'title' ] = unicode ( O0OooOo0o [ 'title' ] + ' [Premium]' )
      iiI1I1 . append ( O0OooOo0o )
      if 16 - 16: iiI1i1 % iIii1I11I1II1 . Ii1I
      if 59 - 59: I1IiiI * II111iiii . O0
      if 56 - 56: Ii1I - Ii11111i % I1IiiI - o0oOOo0O0Ooo
      if 51 - 51: O0 / Ii * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  except Exception as OOO :
   print ( OOO )
   if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + Ii % i11iIiiIii % O0
  return iiI1I1 , Iii1I11
  if 27 - 27: O0
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
 def GetDeviceList ( self , tving_token , poc_userinfo ) :
  II1I11Ii1 = [ ]
  Oo0O00Oo0o0 = '-'
  if 28 - 28: i1IIi - Ii11111i
  try :
   o0o00OO0 = '/v1/user/device/list'
   if 54 - 54: Ii11111i - O0 % OOooOOo
   if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
   II11iIiIIIiI = { 'apiKey' : '4263d7d76161f4a19a9efe9ca7903ec4'
 , 'model' : 'PC'
 }
   if 17 - 17: Ii1I - OoooooooOO % Ii1I . iiI1i1 / i11iIiiIii % Ii11111i
   oo0 = self . makeurl ( self . API_DOMAIN , o0o00OO0 , II11iIiIIIiI )
   if 28 - 28: I11i
   I1Ii11I1Ii1i = [
 ( 'User-Agent' , IiiIII111iI )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , tving_token , 'POC_USERINFO' , poc_userinfo ) )
 ]
   if 58 - 58: OoOoOO00
   Ooo = self . SESSION . Request ( oo0 , params = None , cookie = I1Ii11I1Ii1i )
   I1111IIi = json . loads ( Ooo )
   if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
   if 73 - 73: i11iIiiIii - iiI1i1
   II1I11Ii1 = I1111IIi [ 'body' ]
   if 25 - 25: OoooooooOO + iiI1i1 * I1ii11iIi11i
   for o0O0OOO0Ooo in II1I11Ii1 :
    if o0O0OOO0Ooo [ 'model' ] == 'PC' :
     Oo0O00Oo0o0 = o0O0OOO0Ooo [ 'uuid' ]
     if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + Ooo0OO0oOO
     if 18 - 18: Ii * OoOoOO00 . Ii11111i / I1ii11iIi11i / i11iIiiIii
  except Exception as OOO :
   print ( OOO )
   if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  return Oo0O00Oo0o0
  if 91 - 91: i11iIiiIii / i1IIi + Ii11111i + Ii * i11iIiiIii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
