# -*- coding: utf-8 -*-
__author__ = "NightRain"
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
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
reload ( sys )
sys . setdefaultencoding ( 'utf-8' )
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I
i1I1ii1II1iII = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
oooO0oo0oOOOO = { 'stream50' : 1080 , 'stream40' : 720 , 'stream30' : 480 , 'stream25' : 360 }
if 53 - 53: I11i / Oo0Ooo / II111iiii % Ii1I / OoOoOO00 . ooOoO0o
if 100 - 100: i1IIi
if 27 - 27: IiII * OoooooooOO + I11i * ooOoO0o - i11iIiiIii - iII111i
if 30 - 30: iIii1I11I1II1 * iIii1I11I1II1 . II111iiii - oO0o
if 72 - 72: II111iiii - OoOoOO00
if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
if 8 - 8: o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1 . IiII / IiII % IiII
if 22 - 22: Ii1I . IiII
if 41 - 41: I1Ii111 . ooOoO0o * IiII % i11iIiiIii
if 74 - 74: iII111i * IiII
if 82 - 82: iIii1I11I1II1 % IiII
if 86 - 86: OoOoOO00 % I1IiiI
if 80 - 80: OoooooooOO . I1IiiI
if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
if 58 - 58: i11iIiiIii % I1Ii111
if 54 - 54: OOooOOo % O0 + I1IiiI - iII111i / I11i
if 31 - 31: OoO0O00 + II111iiii
if 13 - 13: OOooOOo * oO0o * I1IiiI
if 55 - 55: II111iiii
if 43 - 43: OoOoOO00 - i1IIi + I1Ii111 + Ii1I
if 17 - 17: o0oOOo0O0Ooo
class o00ooooO0oO ( object ) :
 def __init__ ( self ) :
  self . MyCookie = cookielib . LWPCookieJar ( )
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , i1I1ii1II1iII ) ]
  urllib2 . install_opener ( self . Opener )
  if 63 - 63: OoOoOO00 % i1IIi
  if 66 - 66: Ii1I
 def RequestCookie ( self , url , params ) :
  oo0Ooo0 = ''
  I1I11I1I1I = self . Opener . open ( url , urllib . urlencode ( params ) )
  if 90 - 90: II111iiii + oO0o / o0oOOo0O0Ooo % II111iiii - O0
  oo0Ooo0 = I1I11I1I1I . info ( ) . getheader ( 'Set-Cookie' )
  if 29 - 29: o0oOOo0O0Ooo / iIii1I11I1II1
  I1I11I1I1I . close ( )
  return oo0Ooo0
  if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + I1Ii111 + I1ii11iIi11i
  if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
 def Request ( self , url , params = None , cookie = None ) :
  if cookie : self . Opener . addheaders = cookie
  if 23 - 23: i11iIiiIii + I1IiiI
  if params :
   I1I11I1I1I = self . Opener . open ( url , urllib . urlencode ( params ) )
  else :
   I1I11I1I1I = self . Opener . open ( url )
   if 68 - 68: OoOoOO00 . oO0o . i11iIiiIii
  II = I1I11I1I1I . read ( )
  I1I11I1I1I . close ( )
  if 14 - 14: Oo0Ooo . I1IiiI / Ii1I
  return II
  if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
 def Request2 ( self , url , params = None , cookie = None ) :
  import requests
  I1I11I1I1I = requests . get ( url , headers = cookie , cookies = None )
  if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
  II = I1I11I1I1I . json ( )
  return II
  if 77 - 77: I11i - iIii1I11I1II1
  if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
  if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
  if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
  if 74 - 74: iII111i * O0
class oOOo0oo ( object ) :
 def __init__ ( self ) :
  self . SESSION = o00ooooO0oO ( )
  self . TVING_TOKEN = ''
  self . POC_USERINFO = ''
  self . TVING_UUID = '-'
  self . APIKEY = '1e7952d0917d6aab1f0293a063697610'
  self . NETWORKCODE = 'CSND0900'
  self . OSCODE = 'CSOD0900'
  self . TELECODE = 'CSCD0900'
  self . SCREENCODE = 'CSSD0100'
  self . LIVE_LIMIT = 30
  self . VOD_LIMIT = 30
  self . EPISODE_LIMIT = 40
  self . SEARCH_LIMIT = 80
  self . MOVIE_LIMIT = 30
  self . API_DOMAIN = 'https://api.tving.com'
  self . IMG_DOMAIN = 'https://image.tving.com'
  self . SEARCH_DOMAIN = 'https://search.tving.com'
  self . LOGIN_DOMAIN = 'https://user.tving.com'
  self . URL_DOMAIN = 'https://www.tving.com'
  self . MOVIE_LITE = '338723'
  self . MOVIE_PREMIUM = '1513561'
  if 80 - 80: I11i * i11iIiiIii / I1Ii111
  if 9 - 9: Ii1I + oO0o % Ii1I + i1IIi . OOooOOo
 def getDeviceStr ( self ) :
  III1i1i = [ ]
  III1i1i . append ( 'Windows' )
  III1i1i . append ( 'Chrome' )
  III1i1i . append ( 'ko-KR' )
  III1i1i . append ( 'undefined' )
  III1i1i . append ( '24' )
  III1i1i . append ( u'한국 표준시' )
  III1i1i . append ( 'undefined' )
  III1i1i . append ( 'undefined' )
  III1i1i . append ( 'data:image/png;base64,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CZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAT+H9FJng/hy/8wAAAAAElFTkSuQmCC' )
  if 26 - 26: OoooooooOO
  if 12 - 12: OoooooooOO % OoOoOO00 / ooOoO0o % o0oOOo0O0Ooo
  iiii = ''
  for oO0o0O0OOOoo0 in III1i1i :
   iiii += oO0o0O0OOOoo0 + '|'
  return iiii
 if 48 - 48: O0 + O0 - I1ii11iIi11i . ooOoO0o / iIii1I11I1II1
 if 77 - 77: i1IIi % OoOoOO00 - IiII + ooOoO0o
 if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
 if 18 - 18: i11iIiiIii
 if 46 - 46: i1IIi / I11i % OOooOOo + I1Ii111
 if 79 - 79: I1Ii111 - o0oOOo0O0Ooo + I1Ii111 - iII111i
 if 8 - 8: I1IiiI
 if 75 - 75: iIii1I11I1II1 / OOooOOo % o0oOOo0O0Ooo * OoOoOO00
 if 9 - 9: OoO0O00
 if 33 - 33: ooOoO0o . iII111i
 if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
 if 50 - 50: I1IiiI
 if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
 if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
 if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
 if 16 - 16: O0 - I1Ii111 * iIii1I11I1II1 + iII111i
 if 50 - 50: II111iiii - ooOoO0o * I1ii11iIi11i / I1Ii111 + o0oOOo0O0Ooo
 if 88 - 88: Ii1I / I1Ii111 + iII111i - II111iiii / ooOoO0o - OoOoOO00
 if 15 - 15: I1ii11iIi11i + OoOoOO00 - OoooooooOO / OOooOOo
 if 58 - 58: i11iIiiIii % I11i
 if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
 if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
 if 16 - 16: I1IiiI * oO0o % IiII
 if 86 - 86: I1IiiI + Ii1I % i11iIiiIii * oO0o . ooOoO0o * I11i
 if 44 - 44: oO0o
 if 88 - 88: I1Ii111 % Ii1I . II111iiii
 if 38 - 38: o0oOOo0O0Ooo
 if 57 - 57: O0 / oO0o * I1Ii111 / OoOoOO00 . II111iiii
 if 26 - 26: iII111i
 if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - iII111i / OoooooooOO
 if 39 - 39: I1ii11iIi11i / ooOoO0o - II111iiii
 if 98 - 98: I1ii11iIi11i / I11i % oO0o . OoOoOO00
 if 91 - 91: oO0o % Oo0Ooo
 if 64 - 64: I11i % iII111i - I1Ii111 - oO0o
 if 31 - 31: I11i - II111iiii . I11i
 if 18 - 18: o0oOOo0O0Ooo
 if 98 - 98: iII111i * iII111i / iII111i + I11i
 if 34 - 34: ooOoO0o
 if 15 - 15: I11i * ooOoO0o * Oo0Ooo % i11iIiiIii % OoOoOO00 - OOooOOo
 if 68 - 68: I1Ii111 % i1IIi . IiII . I1ii11iIi11i
 if 92 - 92: iII111i . I1Ii111
 if 31 - 31: I1Ii111 . OoOoOO00 / O0
 if 89 - 89: OoOoOO00
 if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + ooOoO0o
 if 4 - 4: ooOoO0o + O0 * OOooOOo
 if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
 if 25 - 25: I1ii11iIi11i
 if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
 if 13 - 13: OOooOOo / i11iIiiIii
 if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
 if 52 - 52: o0oOOo0O0Ooo
 if 95 - 95: Ii1I
 if 87 - 87: ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
 if 91 - 91: O0
 if 61 - 61: II111iiii
 if 64 - 64: ooOoO0o / OoOoOO00 - O0 - I11i
 if 86 - 86: I11i % OoOoOO00 / I1IiiI / OoOoOO00
 if 42 - 42: OoO0O00
 if 67 - 67: I1Ii111 . iII111i . O0
 if 10 - 10: I1ii11iIi11i % I1ii11iIi11i - iIii1I11I1II1 / OOooOOo + Ii1I
 def SaveCredential ( self , login_params ) :
  self . TVING_TOKEN = login_params . get ( 'tving_token' )
  self . POC_USERINFO = login_params . get ( 'poc_userinfo' )
  self . TVING_UUID = login_params . get ( 'tving_uuid' )
  if 87 - 87: oO0o * I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
 def LoadCredential ( self ) :
  I1111IIi = {
 'tving_token' : self . TVING_TOKEN
 , 'poc_userinfo' : self . POC_USERINFO
 , 'tving_uuid' : self . TVING_UUID
 }
  return I1111IIi
  if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
 def GetDefaultParams ( self ) :
  I1 = { 'apiKey' : self . APIKEY
 , 'networkCode' : self . NETWORKCODE
 , 'osCode' : self . OSCODE
 , 'teleCode' : self . TELECODE
 , 'screenCode' : self . SCREENCODE
 }
  return I1
  if 22 - 22: Oo0Ooo + Ii1I % I1ii11iIi11i
 def GetNoCache ( self , timetype = 1 ) :
  if timetype == 1 :
   return int ( time . time ( ) )
  else :
   return int ( time . time ( ) * 1000 )
   if 9 - 9: OoooooooOO
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  OOOOo = domain + path
  if query1 :
   OOOOo += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   OOOOo += '&%s' % urllib . urlencode ( query2 )
  return OOOOo
  if 76 - 76: OoO0O00
  if 29 - 29: OOooOOo + Oo0Ooo . i11iIiiIii - i1IIi / iIii1I11I1II1
  if 26 - 26: I11i . OoooooooOO
  if 39 - 39: iII111i - O0 % i11iIiiIii * I1Ii111 . IiII
  if 58 - 58: OoO0O00 % i11iIiiIii . iII111i / oO0o
 def GetCredential ( self , user_id , user_pw , login_type ) :
  O0o = False
  OoOooO = '-'
  if 12 - 12: I1IiiI * iII111i % i1IIi % iIii1I11I1II1
  try :
   IIi1I11I1II = self . LOGIN_DOMAIN + '/pc/user/doLogin.tving'
   if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
   I1 = { 'userId' : user_id
 , 'password' : user_pw
 , 'loginType' : '10' if login_type == '0' else '20'
 , 'autoLogin' : 'false'
 , 'cjOneCookie' : ''
 , 'kaptcha' : ''

   , 'returnUrl' : ''
 , 'csite' : ''
 }
   if 84 - 84: IiII
   oo0Ooo0 = self . SESSION . RequestCookie ( IIi1I11I1II , I1 )
   if 86 - 86: OoOoOO00 - Ii1I - OoO0O00 * iII111i
   if 66 - 66: OoooooooOO + O0
   if 11 - 11: I11i + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   for i1Iii1i1I in oo0Ooo0 . split ( ',' ) :
    i1Iii1i1I = i1Iii1i1I . strip ( )
    if i1Iii1i1I . startswith ( '_tving_token' ) :
     OOoO00 = i1Iii1i1I . split ( ';' ) [ 0 ]
     OOoO00 = OOoO00 . split ( '=' ) [ 1 ]
     if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
    if i1Iii1i1I . startswith ( 'POC_USERINFO' ) :
     OOOOOoo0 = i1Iii1i1I . split ( ';' ) [ 0 ]
     OOOOOoo0 = OOOOOoo0 . split ( '=' ) [ 1 ]
     if 49 - 49: O0 . iII111i
   if OOoO00 : O0o = True
   if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
   OoOooO = self . GetDeviceList ( OOoO00 , OOOOOoo0 )
   if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   if 54 - 54: OoOoOO00 % iII111i
  except Exception as IIiII111iiI1I :
   OOoO00 = OOOOOoo0 = ''
   OoOooO = '-'
   if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * I1Ii111 + OoOoOO00 / I1IiiI
  I1111IIi = {
 'tving_token' : OOoO00
 , 'poc_userinfo' : OOOOOoo0
 , 'tving_uuid' : OoOooO
 }
  self . SaveCredential ( I1111IIi )
  if 3 - 3: o0oOOo0O0Ooo
  return O0o
  if 24 - 24: i11iIiiIii + iII111i * Ii1I - II111iiii . OOooOOo % iIii1I11I1II1
  if 71 - 71: O0 . iII111i / o0oOOo0O0Ooo
 def GetBroadURL ( self , mediacode , sel_quality , stype ) :
  Ooo = ''
  iIi1IiIiiII = ''
  ii1iII1II = self . TVING_UUID
  if 48 - 48: II111iiii * Ii1I . I11i + oO0o
  OoO0o = self . TVING_TOKEN
  oO0o0Ooooo = self . POC_USERINFO
  if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
  if 87 - 87: Oo0Ooo . IiII
  if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
  if 55 - 55: OOooOOo . I1IiiI
  if 61 - 61: Oo0Ooo % IiII . Oo0Ooo
  if 100 - 100: I1Ii111 * O0
  if 64 - 64: OOooOOo % iIii1I11I1II1 * oO0o
  try :
   if stype != 'tvingtv' :
    if 79 - 79: O0
    oOO00O = '/v2/media/stream/info'
    if 77 - 77: Oo0Ooo - i1IIi - I11i . OoOoOO00
    IiI1i = self . GetDefaultParams ( )
    o0O = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'noCache' : str ( self . GetNoCache ( 1 ) )
 , 'callingFrom' : 'HTML5'
 , 'adReq' : 'none'
 , 'ooc' : ''
 }
    o0O [ 'deviceId' ] = ii1iII1II
    if 90 - 90: OOooOOo . I1IiiI * I1IiiI
    OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , IiI1i , o0O )
    if 7 - 7: IiII * I1Ii111 % Ii1I - o0oOOo0O0Ooo
    oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , OoO0o , 'POC_USERINFO' , oO0o0Ooooo ) )
 ]
    if 13 - 13: Ii1I . i11iIiiIii
    I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
    oOOoo00O00o = json . loads ( I1I11I1I1I )
    if 98 - 98: OOooOOo + IiII + oO0o % OoooooooOO
    if not ( 'stream' in oOOoo00O00o [ 'body' ] ) : return Ooo , iIi1IiIiiII
    oooooo0O000o = oOOoo00O00o [ 'body' ] [ 'stream' ]
    if 64 - 64: I1IiiI . o0oOOo0O0Ooo - I1Ii111 / OoooooooOO
    if 66 - 66: iII111i - iII111i - i11iIiiIii . I1ii11iIi11i - OOooOOo
    if 'drm_license_assertion' in oooooo0O000o :
     iIi1IiIiiII = oooooo0O000o [ 'drm_license_assertion' ]
    else :
     if 77 - 77: OoOoOO00 - II111iiii - ooOoO0o
     IiiiIIiIi1 = oooooo0O000o [ 'broadcast' ] [ 'broad_url' ]
     if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
    oooOo0OOOoo0 = oooooo0O000o [ 'quality' ]
    if 51 - 51: Oo0Ooo / OoOoOO00 . OOooOOo * o0oOOo0O0Ooo + OoO0O00 * IiII
    OOOoOo = [ ]
    for O00o0 in oooOo0OOOoo0 :
     if O00o0 [ 'active' ] == 'Y' :
      OOOoOo . append ( { oooO0oo0oOOOO . get ( O00o0 [ 'code' ] ) : O00o0 [ 'code' ] } )
      if 40 - 40: I1Ii111 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
    iIiIi11iI = self . CheckQuality ( sel_quality , OOOoOo )
    if 83 - 83: II111iiii % Oo0Ooo % ooOoO0o % I1ii11iIi11i
   else :
    for OoO000O0Oo , Oo0o0oooo0O0 in oooO0oo0oOOOO . items ( ) :
     if Oo0o0oooo0O0 == sel_quality :
      iIiIi11iI = OoO000O0Oo
      if 93 - 93: O0 % i1IIi . OOooOOo / I1IiiI - I1Ii111 / I1IiiI
      if 36 - 36: oO0o % oO0o % i1IIi / i1IIi - ooOoO0o
  except Exception as IIiII111iiI1I :
   for OoO000O0Oo , Oo0o0oooo0O0 in oooO0oo0oOOOO . items ( ) :
    if Oo0o0oooo0O0 == sel_quality :
     iIiIi11iI = OoO000O0Oo
   return Ooo , iIi1IiIiiII
   if 30 - 30: I11i / I1IiiI
  print ii1iII1II , iIiIi11iI
  if 35 - 35: II111iiii % OOooOOo . ooOoO0o + ooOoO0o % II111iiii % II111iiii
  if 72 - 72: II111iiii + i1IIi + o0oOOo0O0Ooo
  try :
   if 94 - 94: oO0o . i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
   oOO00O = '/streaming/info'
   IiI1i = self . GetDefaultParams ( )
   if stype == 'onair' : IiI1i [ 'osCode' ] = 'CSOD0400'
   if 72 - 72: Ii1I
   if 1 - 1: OoO0O00 * IiII * OoooooooOO + ooOoO0o
   if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
   I11I = {
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
   if 50 - 50: I1Ii111 * i11iIiiIii * iIii1I11I1II1 - II111iiii * o0oOOo0O0Ooo * OoOoOO00
   OoooOoo = self . makeOocUrl ( I11I )
   O0o000Oo = urllib . quote ( OoooOoo )
   if 67 - 67: I1IiiI . i1IIi
   if 27 - 27: ooOoO0o % I1IiiI
   if 73 - 73: OOooOOo
   o0O = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'callingFrom' : 'HTML5'
 , 'streamCode' : iIiIi11iI
   , 'adReq' : 'none'
 , 'ooc' : OoooOoo
 }
   o0O [ 'deviceId' ] = ii1iII1II
   if 70 - 70: iIii1I11I1II1
   OOOOo = self . URL_DOMAIN + oOO00O
   i11ii1iI = IiI1i
   i11ii1iI . update ( o0O )
   if 22 - 22: OoooooooOO
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s; %s=%s'
 % ( '_tving_token' , OoO0o
 , 'onClickEvent2' , O0o000Oo
 , 'POC_USERINFO' , oO0o0Ooooo
 )
 )
 , ( 'origin' , 'https://www.tving.com' )
 , ( 'Referer' , 'https://www.tving.com/vod/player/' + mediacode )
 ]
   if 75 - 75: o0oOOo0O0Ooo + o0oOOo0O0Ooo + i1IIi - i1IIi
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = i11ii1iI , cookie = oo0Ooo0 )
   if 76 - 76: OoO0O00 . O0 % O0 - o0oOOo0O0Ooo - iIii1I11I1II1 - I1IiiI
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 53 - 53: i1IIi
   if 59 - 59: o0oOOo0O0Ooo
   if iIi1IiIiiII != '' :
    iIi1IiIiiII = oOOoo00O00o [ 'stream' ] [ 'drm_license_assertion' ]
    Ooo = oOOoo00O00o [ 'stream' ] [ 'broadcast' ] [ 'widevine' ] [ 'broad_url' ]
   else :
    if not ( 'broad_url' in oOOoo00O00o [ 'stream' ] [ 'broadcast' ] ) : return Ooo , iIi1IiIiiII
    Ooo = oOOoo00O00o [ 'stream' ] [ 'broadcast' ] [ 'broad_url' ]
    if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
  return Ooo , iIi1IiIiiII
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
 def CheckQuality ( self , sel_qt , qt_list ) :
  for ii in qt_list :
   if sel_qt >= ii . keys ( ) [ 0 ] : return ii . get ( ii . keys ( ) [ 0 ] )
   O0oOo00o = ii . get ( ii . keys ( ) [ 0 ] )
  return O0oOo00o
  if 81 - 81: IiII % i1IIi . iIii1I11I1II1
  if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
 def makeOocUrl ( self , ooc_params ) :
  OOOOo = ''
  for OoO000O0Oo , Oo0o0oooo0O0 in ooc_params . items ( ) :
   OOOOo += "%s=%s^" % ( OoO000O0Oo , Oo0o0oooo0O0 )
  return OOOOo
  if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
  if 31 - 31: OOooOOo
 def GetLiveChannelList ( self , stype , page_int ) :
  i1 = [ ]
  OOO0000oO = False
  if 15 - 15: OoOoOO00 % I1IiiI * I11i
  try :
   oOO00O = '/v2/media/lives'
   if 81 - 81: ooOoO0o - iIii1I11I1II1 - i1IIi / I1Ii111 - O0 * I11i
   if stype == 'onair' :
    iI1i11II1i = 'CPCS0100,CPCS0400'
   else :
    iI1i11II1i = 'CPCS0300'
    if 96 - 96: I1Ii111
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . LIVE_LIMIT )
 , 'order' : 'rating'
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'channelType' : iI1i11II1i

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 97 - 97: ooOoO0o
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 48 - 48: i1IIi - I1Ii111
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 56 - 56: o0oOOo0O0Ooo + II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 84 - 84: OoO0O00 + i1IIi - II111iiii . I1ii11iIi11i * OoooooooOO + I1IiiI
   if not ( 'result' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'result' ]
   if 50 - 50: OoooooooOO % I11i
   if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
   for O00o0 in II1i11I :
    oOO0OOOo = { }
    oOO0OOOo [ 'mediatype' ] = 'video'
    if 56 - 56: o0oOOo0O0Ooo
    I1OooooO0oOOOO = o0O00oOOoo = i1I1iIi = IIii11Ii1i1I = ''
    Oooo0O = oo00O0oO0O0 = ''
    if 96 - 96: i11iIiiIii % ooOoO0o / OoOoOO00
    I1IiI11 = O00o0 [ 'live_code' ]
    I1OooooO0oOOOO = O00o0 [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 9 - 9: I11i
    if O00o0 [ 'schedule' ] [ 'episode' ] != None :
     o0O00oOOoo = O00o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     o0O00oOOoo = o0O00oOOoo + ', ' + str ( O00o0 [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if O00o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      i1I1iIi = O00o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     IIii11Ii1i1I = O00o0 [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     o0O00oOOoo = O00o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if O00o0 [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      i1I1iIi = O00o0 [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     IIii11Ii1i1I = O00o0 [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 64 - 64: iIii1I11I1II1 / I1IiiI . II111iiii + OoooooooOO . OoO0O00
     if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
    oOO0OOOo [ 'title' ] = O00o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
    oOO0OOOo [ 'studio' ] = I1OooooO0oOOOO
    try :
     ii111I = [ ]
     for iiI in O00o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'actor' ) : ii111I . append ( iiI )
     if ii111I [ 0 ] != '' and ii111I [ 0 ] != u'없음' : oOO0OOOo [ 'cast' ] = ii111I
    except :
     None
    try :
     iIiiiII = [ ]
     if O00o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      iIiiiII . append ( O00o0 [ 'schedule' ] [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
     if O00o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      iIiiiII . append ( O00o0 [ 'schedule' ] [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
     if iIiiiII [ 0 ] != '' : oOO0OOOo [ 'genre' ] = iIiiiII
    except :
     None
     if 20 - 20: I1IiiI
     if 95 - 95: iII111i - I1IiiI
     if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
     if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
    if i1I1iIi == '' :
     i1I1iIi = O00o0 [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if i1I1iIi != '' : i1I1iIi = self . IMG_DOMAIN + i1I1iIi
    if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
    Oooo0O = str ( O00o0 [ 'schedule' ] [ 'broadcast_start_time' ] ) [ 8 : 12 ]
    oo00O0oO0O0 = str ( O00o0 [ 'schedule' ] [ 'broadcast_end_time' ] ) [ 8 : 12 ]
    if 41 - 41: i1IIi - I11i - Ii1I
    III11I1 = { 'channel' : unicode ( I1OooooO0oOOOO )
 , 'title' : unicode ( o0O00oOOoo )
 , 'mediacode' : I1IiI11
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : unicode ( IIii11Ii1i1I )
 , 'channelepg' : ' [%s:%s ~ %s:%s]' % ( Oooo0O [ 0 : 2 ] , Oooo0O [ 2 : ] , oo00O0oO0O0 [ 0 : 2 ] , oo00O0oO0O0 [ 2 : ] )
 , 'info' : oOO0OOOo
 }
    if 36 - 36: oO0o - Ii1I . Oo0Ooo - i11iIiiIii - OOooOOo * Oo0Ooo
    i1 . append ( III11I1 )
    if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
   if oOOoo00O00o [ 'body' ] [ 'has_more' ] == 'Y' : OOO0000oO = True
   if 51 - 51: iIii1I11I1II1 . ooOoO0o + iIii1I11I1II1
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 95 - 95: I1IiiI
  return i1 , OOO0000oO
  if 46 - 46: OoOoOO00 + OoO0O00
  if 70 - 70: iII111i / iIii1I11I1II1
 def GetProgramList ( self , stype , orderby , page_int , landyn = False ) :
  i1 = [ ]
  OOO0000oO = False
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
  try :
   oOO00O = '/v2/media/episodes'
   if 96 - 96: OoooooooOO + oO0o
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : str ( page_int )
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
   if stype != 'all' : o0O [ 'multiCategoryCode' ] = stype
   if 44 - 44: oO0o
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 88 - 88: OoOoOO00 / II111iiii
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
   if not ( 'result' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'result' ]
   if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
   if 42 - 42: Oo0Ooo
   for O00o0 in II1i11I :
    II1IIiiIiI = O00o0 [ 'program' ] [ 'code' ]
    o0O00oOOoo = O00o0 [ 'program' ] [ 'name' ] [ 'ko' ]
    if 1 - 1: iII111i
    i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    O0O0Ooo = 'CAIP0200' if landyn else 'CAIP0900'
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
    for IIii11I1i1I in O00o0 [ 'program' ] [ 'image' ] :
     if IIii11I1i1I [ 'code' ] == O0O0Ooo :
      i1I1iIi = self . IMG_DOMAIN + IIii11I1i1I [ 'url' ]
      break
      if 99 - 99: iII111i
    IIii11Ii1i1I = O00o0 [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    oOO0O00o0OO0O = O00o0 [ 'program' ] [ 'channel_code' ]
    if 17 - 17: i1IIi
    oOO0OOOo = { }
    oOO0OOOo [ 'title' ] = unicode ( o0O00oOOoo )
    oOO0OOOo [ 'mediatype' ] = 'episode'
    try :
     ii111I = [ ]
     for iiI in O00o0 . get ( 'program' ) . get ( 'actor' ) : ii111I . append ( iiI )
     if ii111I [ 0 ] != '' and ii111I [ 0 ] != '-' : oOO0OOOo [ 'cast' ] = ii111I
    except :
     None
    try :
     iiIi1i = [ ]
     for I1i11111i1i11 in O00o0 . get ( 'program' ) . get ( 'director' ) : iiIi1i . append ( I1i11111i1i11 )
     if iiIi1i [ 0 ] != '' and iiIi1i [ 0 ] != '-' : oOO0OOOo [ 'director' ] = iiIi1i
    except :
     None
     if 77 - 77: I1ii11iIi11i + OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
    iIiiiII = [ ]
    if O00o0 . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
     iIiiiII . append ( O00o0 [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
    if O00o0 . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
     iIiiiII . append ( O00o0 [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
    if iIiiiII [ 0 ] != '' : oOO0OOOo [ 'genre' ] = iIiiiII
    if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
    try :
     if O00o0 . get ( 'program' ) . get ( 'product_year' ) : oOO0OOOo [ 'year' ] = O00o0 [ 'program' ] [ 'product_year' ]
     if 'broad_dt' in O00o0 . get ( 'program' ) :
      ooo0OOO = O00o0 . get ( 'program' ) . get ( 'broad_dt' )
      oOO0OOOo [ 'aired' ] = '%s-%s-%s' % ( ooo0OOO [ : 4 ] , ooo0OOO [ 4 : 6 ] , ooo0OOO [ 6 : ] )
    except :
     None
     if 49 - 49: i11iIiiIii % Ii1I . OoOoOO00
     if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * OOooOOo
    III11I1 = { 'program' : II1IIiiIiI
 , 'title' : unicode ( o0O00oOOoo )
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : unicode ( IIii11Ii1i1I )
 , 'channel' : oOO0O00o0OO0O
 , 'info' : oOO0OOOo
 }
    if 26 - 26: OoooooooOO * I1IiiI + OOooOOo
    i1 . append ( III11I1 )
    if 24 - 24: i11iIiiIii % iIii1I11I1II1 + OOooOOo / i11iIiiIii
    if 70 - 70: OoO0O00 * O0 . I11i + I1IiiI . IiII
   if oOOoo00O00o [ 'body' ] [ 'has_more' ] == 'Y' : OOO0000oO = True
   if 14 - 14: iIii1I11I1II1 % iIii1I11I1II1 * i11iIiiIii - OoO0O00 - I11i
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 63 - 63: OoO0O00
  return i1 , OOO0000oO
  if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % ooOoO0o + iIii1I11I1II1 / O0 / I1ii11iIi11i
  if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
 def GetEpisodoList ( self , program_code , page_int , orderby = 'desc' ) :
  i1 = [ ]
  OOO0000oO = False
  if 75 - 75: IiII . ooOoO0o
  if 50 - 50: OoOoOO00
  if 60 - 60: ooOoO0o * iIii1I11I1II1 * I1ii11iIi11i * Oo0Ooo
  if 69 - 69: Ii1I * O0 . i11iIiiIii / Ii1I . o0oOOo0O0Ooo
  if 63 - 63: I11i + o0oOOo0O0Ooo . II111iiii - I1IiiI
  if 52 - 52: o0oOOo0O0Ooo % Oo0Ooo
  if 64 - 64: O0 % I11i % O0 * OoO0O00 . oO0o + I1IiiI
  try :
   oOO00O = '/v2/media/frequency/program/' + program_code
   if 75 - 75: I11i . OoooooooOO % o0oOOo0O0Ooo * I11i % OoooooooOO
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 13 - 13: IiII / i11iIiiIii % II111iiii % I11i . I1ii11iIi11i
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 8 - 8: OoOoOO00 + Oo0Ooo - II111iiii
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 39 - 39: I1Ii111
   if not ( 'result' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'result' ]
   if 86 - 86: I11i * I1IiiI + I11i + II111iiii
   i1i111iI = int ( oOOoo00O00o [ 'body' ] [ 'total_count' ] )
   if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
   IiiIiI111iI = int ( i1i111iI // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if orderby == 'desc' :
    OOo = ( i1i111iI - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    OOo = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 50 - 50: ooOoO0o
   for o0O0O0ooo0oOO in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     oo000 = OOo - o0O0O0ooo0oOO
     if oo000 < 0 : break
    else :
     oo000 = OOo + o0O0O0ooo0oOO
     if oo000 >= i1i111iI : break
     if 32 - 32: i1IIi . Ii1I
    oOO = II1i11I [ oo000 ] [ 'episode' ] [ 'code' ]
    o0O00oOOoo = II1i11I [ oo000 ] [ 'vod_name' ] [ 'ko' ]
    Oooo = ''
    try :
     ooo0OOO = str ( II1i11I [ oo000 ] [ 'episode' ] [ 'broadcast_date' ] )
     Oooo = '%s-%s-%s' % ( ooo0OOO [ : 4 ] , ooo0OOO [ 4 : 6 ] , ooo0OOO [ 6 : ] )
    except :
     None
    if II1i11I [ oo000 ] [ 'episode' ] [ 'image' ] != [ ] :
     i1I1iIi = self . IMG_DOMAIN + II1i11I [ oo000 ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     i1I1iIi = self . IMG_DOMAIN + II1i11I [ oo000 ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    IIii11Ii1i1I = II1i11I [ oo000 ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 16 - 16: OOooOOo % iII111i . O0 / Oo0Ooo / o0oOOo0O0Ooo
    oOO0OOOo = { }
    oOO0OOOo [ 'mediatype' ] = 'episode'
    try :
     oOO0OOOo [ 'title' ] = unicode ( II1i11I [ oo000 ] [ 'program' ] [ 'name' ] [ 'ko' ] )
     oOO0OOOo [ 'aired' ] = Oooo
     oOO0OOOo [ 'studio' ] = II1i11I [ oo000 ] [ 'channel' ] [ 'name' ] [ 'ko' ]
     if 'frequency' in II1i11I [ oo000 ] [ 'episode' ] : oOO0OOOo [ 'episode' ] = II1i11I [ oo000 ] [ 'episode' ] [ 'frequency' ]
    except :
     None
     if 68 - 68: i11iIiiIii * OoO0O00
    III11I1 = { 'episode' : oOO
 , 'title' : unicode ( o0O00oOOoo )
 , 'subtitle' : Oooo
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : unicode ( IIii11Ii1i1I )
 , 'info' : oOO0OOOo
 }
    if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
    i1 . append ( III11I1 )
    if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   if IiiIiI111iI > page_int : OOO0000oO = True
   if 45 - 45: I1Ii111
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 83 - 83: OoOoOO00 . OoooooooOO
  return i1 , OOO0000oO , IiiIiI111iI
  if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
  if 62 - 62: OoO0O00 / I1ii11iIi11i
 def GetMovieList ( self , orderby , page_int , premiumyn = False , landyn = False ) :
  i1 = [ ]
  OOO0000oO = False
  if 7 - 7: OoooooooOO . IiII
  if premiumyn == True :
   O000OOO0OOo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   O000OOO0OOo = self . MOVIE_LITE
   if 32 - 32: Ii1I * O0
  try :
   oOO00O = '/v2/media/movies'
   if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : O000OOO0OOo
   # ooOoO0o . iII111i / Oo0Ooo % iII111i * I1ii11iIi11i / iII111i
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 70 - 70: I11i . I1ii11iIi11i * OoooooooOO - IiII * I1IiiI + OoOoOO00
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 92 - 92: I11i . I1Ii111
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 85 - 85: I1ii11iIi11i . I1Ii111
   if not ( 'result' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'result' ]
   if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
   if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
   for O00o0 in II1i11I :
    ii111I11iI = O00o0 [ 'movie' ] [ 'code' ]
    o0O00oOOoo = O00o0 [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( )
    o0O00oOOoo += u' (%s년)' % ( O00o0 . get ( 'movie' ) . get ( 'product_year' ) )
    i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    O0O0Ooo = 'CAIM0400' if landyn else 'CAIM2100'
    if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * I11i
    for IIii11I1i1I in O00o0 [ 'movie' ] [ 'image' ] :
     if IIii11I1i1I [ 'code' ] == O0O0Ooo :
      i1I1iIi = self . IMG_DOMAIN + IIii11I1i1I [ 'url' ]
      break
      if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . ooOoO0o % IiII
    IIii11Ii1i1I = O00o0 [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 50 - 50: iIii1I11I1II1 - IiII + OOooOOo
    oOO0OOOo = { }
    oOO0OOOo [ 'mediatype' ] = 'movie'
    oOO0OOOo [ 'title' ] = unicode ( O00o0 [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( ) )
    oOO0OOOo [ 'year' ] = O00o0 . get ( 'movie' ) . get ( 'product_year' )
    try :
     ii111I = [ ]
     for iiI in O00o0 . get ( 'movie' ) . get ( 'actor' ) : ii111I . append ( iiI )
     if ii111I [ 0 ] != '' : oOO0OOOo [ 'cast' ] = ii111I
    except :
     None
    try :
     iiIi1i = [ ]
     for I1i11111i1i11 in O00o0 . get ( 'movie' ) . get ( 'director' ) : iiIi1i . append ( I1i11111i1i11 )
     if iiIi1i [ 0 ] != '' : oOO0OOOo [ 'director' ] = iiIi1i
    except :
     None
    try :
     iIiiiII = [ ]
     if O00o0 . get ( 'movie' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      iIiiiII . append ( O00o0 [ 'movie' ] [ 'category1_name' ] [ 'ko' ] )
     if O00o0 . get ( 'movie' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      iIiiiII . append ( O00o0 [ 'movie' ] [ 'category2_name' ] [ 'ko' ] )
     if iIiiiII [ 0 ] != '' : oOO0OOOo [ 'genre' ] = iIiiiII
    except :
     None
    try :
     if 'release_date' in O00o0 . get ( 'movie' ) :
      ooo0OOO = str ( O00o0 . get ( 'movie' ) . get ( 'release_date' ) )
      oOO0OOOo [ 'aired' ] = '%s-%s-%s' % ( ooo0OOO [ : 4 ] , ooo0OOO [ 4 : 6 ] , ooo0OOO [ 6 : ] )
    except :
     None
    try :
     if 'duration' in O00o0 . get ( 'movie' ) : oOO0OOOo [ 'duration' ] = O00o0 . get ( 'movie' ) . get ( 'duration' )
    except :
     None
     if 69 - 69: O0
     if 85 - 85: ooOoO0o / O0
    III11I1 = { 'moviecode' : ii111I11iI
 , 'title' : unicode ( o0O00oOOoo )
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : unicode ( IIii11Ii1i1I )
 , 'info' : oOO0OOOo
 }
    if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
    if premiumyn == True :
     o0 = False
     for Iii in O00o0 [ 'billing_package_id' ] :
      if Iii == self . MOVIE_LITE :
       o0 = True
       break
     if o0 == False :
      III11I1 [ 'title' ] = unicode ( III11I1 [ 'title' ] + ' [Premium]' )
      if 19 - 19: I11i % II111iiii / i11iIiiIii / iII111i - OoooooooOO
    i1 . append ( III11I1 )
    if 37 - 37: OOooOOo / OoooooooOO - i11iIiiIii
    if 18 - 18: iII111i . I1IiiI
   if oOOoo00O00o [ 'body' ] [ 'has_more' ] == 'Y' : OOO0000oO = True
   if 40 - 40: O0 - OoooooooOO - IiII
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 37 - 37: OoOoOO00 / II111iiii / O0
  return i1 , OOO0000oO
  if 76 - 76: I1IiiI . ooOoO0o - I1ii11iIi11i - iII111i * OoO0O00
  if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
 def GetMovieListGenre ( self , genre , page_int , premiumyn = False ) :
  i1 = [ ]
  OOO0000oO = False
  if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
  if premiumyn == True :
   O000OOO0OOo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   O000OOO0OOo = self . MOVIE_LITE
   if 63 - 63: I1Ii111 / O0 * Oo0Ooo + II111iiii / IiII + Ii1I
  try :
   oOO00O = '/v2/media/movie/curation/' + genre
   if 63 - 63: OoO0O00 + I1ii11iIi11i . I1Ii111 % I1Ii111
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'productPackageCode' : O000OOO0OOo
   # II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 61 - 61: II111iiii
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 90 - 90: iII111i
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 31 - 31: OOooOOo + O0
   if not ( 'movies' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'movies' ]
   if 87 - 87: ooOoO0o
   if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
   for O00o0 in II1i11I :
    ii111I11iI = O00o0 [ 'code' ]
    o0O00oOOoo = O00o0 [ 'name' ] [ 'ko' ]
    i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'image' ] [ 0 ] [ 'url' ]
    for IIii11I1i1I in O00o0 [ 'image' ] :
     if IIii11I1i1I [ 'code' ] == 'CAIM2100' :
      i1I1iIi = self . IMG_DOMAIN + IIii11I1i1I [ 'url' ]
    IIii11Ii1i1I = O00o0 [ 'story' ] [ 'ko' ]
    if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
    III11I1 = { 'moviecode' : ii111I11iI
 , 'title' : unicode ( o0O00oOOoo . strip ( ) )
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : unicode ( IIii11Ii1i1I )
 }
    if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
    if premiumyn == True :
     o0 = False
     for Iii in O00o0 [ 'billing_package_id' ] :
      if Iii == self . MOVIE_LITE :
       o0 = True
       break
     if o0 == False :
      III11I1 [ 'title' ] = unicode ( III11I1 [ 'title' ] + ' [Premium]' )
      if 13 - 13: Oo0Ooo
    i1 . append ( III11I1 )
    if 60 - 60: I1ii11iIi11i * I1IiiI
    if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
    if 41 - 41: Ii1I
    if 77 - 77: I1Ii111
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
  return i1 , OOO0000oO
  if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
  if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
 def GetMovieGenre ( self ) :
  i1 = [ ]
  OOO0000oO = False
  if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
  try :
   oOO00O = '/v2/media/movie/curations'
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'movieViewType' : 'sma'
 , 'curationSection' : 'view0002'
   , 'order' : 'curation_code'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O , IiI1i )
   if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 95 - 95: IiII
   if not ( 'result' in oOOoo00O00o [ 'body' ] ) : return i1 , OOO0000oO
   II1i11I = oOOoo00O00o [ 'body' ] [ 'result' ]
   if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
   if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
   for O00o0 in II1i11I :
    III = O00o0 [ 'curation_code' ]
    IiiIii = O00o0 [ 'curation_name' ]
    if 84 - 84: oO0o % i1IIi
    III11I1 = { 'curation_code' : III
 , 'curation_name' : unicode ( IiiIii )
 }
    i1 . append ( III11I1 )
    if 70 - 70: Oo0Ooo . OoooooooOO - iII111i
    if 30 - 30: I1ii11iIi11i % I1IiiI
    if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 59 - 59: OOooOOo + i11iIiiIii
  return i1 , OOO0000oO
  if 88 - 88: i11iIiiIii - ooOoO0o
  if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
 def GetSearchList ( self , search_key , userid , page_int , stype , premiumyn = False , landyn = False ) :
  OOOoO = [ ]
  OOO0000oO = False
  if 14 - 14: I11i . iIii1I11I1II1 . OoooooooOO . II111iiii / o0oOOo0O0Ooo
  try :
   oOO00O = '/search/getSearch.jsp'
   if 21 - 21: i11iIiiIii / i1IIi + I1IiiI * OOooOOo . I1Ii111
   IiI1i = self . GetDefaultParams ( )
   o0O = { 'kwd' : search_key
 , 'notFoundText' : search_key
 , 'userid' : userid
 , 'siteName' : 'TVING_WEB'
 , 'category' : 'TOTAL'
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
   , 'programReqCnt' : str ( self . SEARCH_LIMIT )
 , 'vodMVReqCnt' : str ( self . SEARCH_LIMIT )
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
   if 84 - 84: O0 . I11i - II111iiii . ooOoO0o / II111iiii
   OOOOo = self . makeurl ( self . SEARCH_DOMAIN , oOO00O , o0O , None )
   if 47 - 47: OoooooooOO
   if 4 - 4: I1IiiI % I11i
   if 10 - 10: IiII . OoooooooOO - OoO0O00 + IiII - O0
   if 82 - 82: ooOoO0o + II111iiii
   if 39 - 39: oO0o % iIii1I11I1II1 % O0 % OoooooooOO * I1ii11iIi11i + iII111i
   if 68 - 68: Oo0Ooo + i11iIiiIii
   if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + I1IiiI / OOooOOo % Ii1I
   if 58 - 58: OOooOOo * o0oOOo0O0Ooo + O0 % OOooOOo
   if 25 - 25: Oo0Ooo % I1ii11iIi11i * ooOoO0o
   if 6 - 6: iII111i . IiII * OoOoOO00 . i1IIi
   oo0Ooo0 = {
 'User-Agent' : i1I1ii1II1iII
 , 'Cookie' : '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO )
 }
   oOOoo00O00o = self . SESSION . Request2 ( OOOOo , params = None , cookie = oo0Ooo0 )
   if 98 - 98: i1IIi
   if 65 - 65: OoOoOO00 / OoO0O00 % IiII
   if stype == 'vod' :
    if not ( 'programRsb' in oOOoo00O00o ) : return OOOoO , OOO0000oO
    if 45 - 45: OoOoOO00
    oOooOO = oOOoo00O00o [ 'programRsb' ] [ 'dataList' ]
    I11IiIIII1i = int ( oOOoo00O00o [ 'programRsb' ] [ 'count' ] )
    if 76 - 76: iII111i + ooOoO0o
    if 30 - 30: i11iIiiIii % iIii1I11I1II1 . I11i % iIii1I11I1II1
    for O00o0 in oOooOO :
     II1IIiiIiI = O00o0 [ 'mast_cd' ]
     o0O00oOOoo = O00o0 [ 'mast_nm' ]
     i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'web_url' ]
     if landyn == False :
      i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'web_url4' ]
      if 62 - 62: Oo0Ooo * OoOoOO00
      if 79 - 79: OoO0O00 . iII111i * Ii1I - OOooOOo + ooOoO0o
      if 14 - 14: i11iIiiIii - iII111i * OoOoOO00
     oOO0OOOo = { }
     oOO0OOOo [ 'title' ] = O00o0 [ 'mast_nm' ]
     oOO0OOOo [ 'mediatype' ] = 'episode'
     if 51 - 51: I1ii11iIi11i / iIii1I11I1II1 % oO0o + o0oOOo0O0Ooo * ooOoO0o + I1Ii111
     try :
      if O00o0 . get ( 'actor' ) != '' and O00o0 . get ( 'actor' ) != '-' : oOO0OOOo [ 'cast' ] = O00o0 . get ( 'actor' ) . split ( ',' )
      if O00o0 . get ( 'director' ) != '' and O00o0 . get ( 'director' ) != '-' : oOO0OOOo [ 'director' ] = O00o0 . get ( 'director' ) . split ( ',' )
      if O00o0 . get ( 'cate_nm' ) != '' : oOO0OOOo [ 'genre' ] = O00o0 . get ( 'cate_nm' ) . split ( '/' )
      if 'targetage' in O00o0 : oOO0OOOo [ 'mpaa' ] = O00o0 . get ( 'targetage' )
     except :
      None
     try :
      if 'broad_dt' in O00o0 :
       ooo0OOO = O00o0 . get ( 'broad_dt' )
       oOO0OOOo [ 'aired' ] = '%s-%s-%s' % ( ooo0OOO [ : 4 ] , ooo0OOO [ 4 : 6 ] , ooo0OOO [ 6 : ] )
     except :
      None
      if 77 - 77: ooOoO0o * OoOoOO00
     III11I1 = { 'program' : II1IIiiIiI
 , 'title' : unicode ( o0O00oOOoo )
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : ''
     , 'info' : oOO0OOOo
 }
     if 14 - 14: I11i % I11i / IiII
     OOOoO . append ( III11I1 )
   else :
    if not ( 'vodMVRsb' in oOOoo00O00o ) : return OOOoO , OOO0000oO
    OoOoO00O0 = oOOoo00O00o [ 'vodMVRsb' ] [ 'dataList' ]
    I11IiIIII1i = int ( oOOoo00O00o [ 'vodMVRsb' ] [ 'count' ] )
    if 51 - 51: iIii1I11I1II1 / OoOoOO00 + OOooOOo - I11i + iII111i
    if 29 - 29: o0oOOo0O0Ooo % iIii1I11I1II1 . OoooooooOO % OoooooooOO % II111iiii / iII111i
    for O00o0 in OoOoO00O0 :
     II1IIiiIiI = O00o0 [ 'mast_cd' ]
     o0O00oOOoo = O00o0 [ 'mast_nm' ] . strip ( )
     i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'web_url' ]
     if 70 - 70: i11iIiiIii % iII111i
     if 11 - 11: IiII % I1ii11iIi11i % Ii1I / II111iiii % I1Ii111 - Oo0Ooo
     if landyn == False :
      i1I1iIi = self . IMG_DOMAIN + O00o0 [ 'web_url5' ]
      if 96 - 96: I1ii11iIi11i / II111iiii . Ii1I - iII111i * I11i * oO0o
      if 76 - 76: Ii1I - II111iiii * OOooOOo / OoooooooOO
      if 18 - 18: OoO0O00 + iIii1I11I1II1 - II111iiii - I1IiiI
     ooo = False
     OOOO0oooo = False
     for Iii in O00o0 [ 'bill' ] :
      if Iii == self . MOVIE_LITE : OOOO0oooo = True
      elif Iii == self . MOVIE_PREMIUM : ooo = True
      if 51 - 51: O0 - i1IIi / I1IiiI
     oOO0OOOo = { }
     oOO0OOOo [ 'title' ] = unicode ( o0O00oOOoo )
     oOO0OOOo [ 'mediatype' ] = 'movie'
     if 37 - 37: o0oOOo0O0Ooo % ooOoO0o
     try :
      if O00o0 . get ( 'actor' ) != '' : oOO0OOOo [ 'cast' ] = O00o0 . get ( 'actor' ) . split ( ',' )
      if 83 - 83: OOooOOo . I1Ii111 + oO0o - OOooOOo * I1Ii111 / I1Ii111
      if O00o0 . get ( 'cate_nm' ) != '' : oOO0OOOo [ 'genre' ] = O00o0 . get ( 'cate_nm' ) . split ( '/' )
      if O00o0 . get ( 'runtime_sec' ) != '' : oOO0OOOo [ 'duration' ] = O00o0 . get ( 'runtime_sec' )
      if 'grade_nm' in O00o0 : oOO0OOOo [ 'mpaa' ] = O00o0 . get ( 'grade_nm' )
     except :
      None
     try :
      ooo0OOO = O00o0 . get ( 'broad_dt' )
      if data_str != '' :
       oOO0OOOo [ 'aired' ] = '%s-%s-%s' % ( ooo0OOO [ : 4 ] , ooo0OOO [ 4 : 6 ] , ooo0OOO [ 6 : ] )
       oOO0OOOo [ 'year' ] = ooo0OOO [ : 4 ]
     except :
      None
      if 39 - 39: I1Ii111 / Oo0Ooo % OoO0O00 % i11iIiiIii
      if 90 - 90: I1Ii111 - OoooooooOO
     if OOOO0oooo or ( premiumyn == True and ooo ) :
      III11I1 = { 'movie' : II1IIiiIiI
 , 'title' : unicode ( o0O00oOOoo )
 , 'thumbnail' : i1I1iIi
 , 'synopsis' : ''
      , 'info' : oOO0OOOo
 }
      if OOOO0oooo == False : III11I1 [ 'title' ] = unicode ( III11I1 [ 'title' ] + ' [Premium]' )
      OOOoO . append ( III11I1 )
      if 96 - 96: O0 . Ii1I % OoO0O00 * iIii1I11I1II1
      if 54 - 54: Ii1I * I1Ii111 - OoooooooOO % I1IiiI + O0
      if 6 - 6: I1ii11iIi11i - II111iiii / oO0o + i11iIiiIii + OOooOOo
      if 54 - 54: Ii1I - I11i - I1Ii111 . iIii1I11I1II1
  except Exception as IIiII111iiI1I :
   if 79 - 79: Ii1I . OoO0O00
   print ( IIiII111iiI1I )
   if 40 - 40: o0oOOo0O0Ooo + Oo0Ooo . o0oOOo0O0Ooo % ooOoO0o
  return OOOoO , OOO0000oO
  if 15 - 15: Ii1I * Oo0Ooo % I1ii11iIi11i * iIii1I11I1II1 - i11iIiiIii
  if 60 - 60: I1IiiI * I1Ii111 % OoO0O00 + oO0o
 def GetDeviceList ( self , tving_token , poc_userinfo ) :
  i1 = [ ]
  ii1iII1II = '-'
  if 52 - 52: i1IIi
  try :
   oOO00O = '/v1/user/device/list'
   if 84 - 84: Ii1I / IiII
   if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / OOooOOo
   o0O = { 'apiKey' : '4263d7d76161f4a19a9efe9ca7903ec4'
 , 'model' : 'PC'
 }
   if 11 - 11: I1IiiI * oO0o + I1ii11iIi11i / I1ii11iIi11i
   OOOOo = self . makeurl ( self . API_DOMAIN , oOO00O , o0O )
   if 37 - 37: i11iIiiIii + i1IIi
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , tving_token , 'POC_USERINFO' , poc_userinfo ) )
 ]
   if 23 - 23: iII111i + I11i . OoOoOO00 * I1IiiI + I1ii11iIi11i
   I1I11I1I1I = self . SESSION . Request ( OOOOo , params = None , cookie = oo0Ooo0 )
   oOOoo00O00o = json . loads ( I1I11I1I1I )
   if 18 - 18: IiII * o0oOOo0O0Ooo . IiII / O0
   if 8 - 8: o0oOOo0O0Ooo
   i1 = oOOoo00O00o [ 'body' ]
   if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * ooOoO0o - OoOoOO00
   for O00o0 in i1 :
    if O00o0 [ 'model' ] == 'PC' :
     ii1iII1II = O00o0 [ 'uuid' ]
     if 78 - 78: Ii1I / II111iiii % OoOoOO00
     if 52 - 52: OOooOOo - iII111i * oO0o
  except Exception as IIiII111iiI1I :
   print ( IIiII111iiI1I )
   if 17 - 17: OoooooooOO + OOooOOo * I11i * OoOoOO00
  return ii1iII1II
  if 36 - 36: O0 + Oo0Ooo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
