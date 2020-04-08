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
class I1Ii11I1Ii1i ( object ) :
 def __init__ ( self ) :
  self . MyCookie = cookielib . LWPCookieJar ( )
  self . Opener = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( self . MyCookie ) )
  self . Opener . addheaders = [ ( 'User-Agent' , i1I1ii1II1iII ) ]
  urllib2 . install_opener ( self . Opener )
  if 67 - 67: iIii1I11I1II1 . I1ii11iIi11i . oO0o / i1IIi % II111iiii - OoOoOO00
  if 91 - 91: OoO0O00 . i11iIiiIii / oO0o % I11i / OoO0O00 - i11iIiiIii
 def RequestCookie ( self , url , params ) :
  II1Iiii1111i = ''
  i1IIi11111i = self . Opener . open ( url , urllib . urlencode ( params ) )
  if 74 - 74: iII111i * IiII
  II1Iiii1111i = i1IIi11111i . info ( ) . getheader ( 'Set-Cookie' )
  if 82 - 82: iIii1I11I1II1 % IiII
  i1IIi11111i . close ( )
  return II1Iiii1111i
  if 86 - 86: OoOoOO00 % I1IiiI
  if 80 - 80: OoooooooOO . I1IiiI
 def Request ( self , url , params = None , cookie = None ) :
  if cookie : self . Opener . addheaders = cookie
  if 87 - 87: oO0o / ooOoO0o + I1Ii111 - ooOoO0o . ooOoO0o / II111iiii
  if params :
   i1IIi11111i = self . Opener . open ( url , urllib . urlencode ( params ) )
  else :
   i1IIi11111i = self . Opener . open ( url )
   if 11 - 11: I1IiiI % o0oOOo0O0Ooo - Oo0Ooo
  oo0O000OoO = i1IIi11111i . read ( )
  i1IIi11111i . close ( )
  if 34 - 34: I11i * I1IiiI
  return oo0O000OoO
  if 31 - 31: II111iiii + OoO0O00 . I1Ii111
  if 68 - 68: I1IiiI - i11iIiiIii - OoO0O00 / OOooOOo - OoO0O00 + i1IIi
  if 48 - 48: OoooooooOO % o0oOOo0O0Ooo . I1IiiI - Ii1I % i1IIi % OoooooooOO
  if 3 - 3: iII111i + O0
  if 42 - 42: OOooOOo / i1IIi + i11iIiiIii - Ii1I
class oo0Ooo0 ( object ) :
 def __init__ ( self ) :
  self . SESSION = I1Ii11I1Ii1i ( )
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
  self . MOVIE_LITE = '338723'
  self . MOVIE_PREMIUM = '1513561'
  if 46 - 46: ooOoO0o % ooOoO0o - oO0o * o0oOOo0O0Ooo % iII111i
  if 55 - 55: OoOoOO00 % i1IIi / Ii1I - oO0o - O0 / II111iiii
 def getDeviceStr ( self ) :
  iii11iII = [ ]
  iii11iII . append ( 'Windows' )
  iii11iII . append ( 'Chrome' )
  iii11iII . append ( 'ko-KR' )
  iii11iII . append ( 'undefined' )
  iii11iII . append ( '24' )
  iii11iII . append ( u'한국 표준시' )
  iii11iII . append ( 'undefined' )
  iii11iII . append ( 'undefined' )
  iii11iII . append ( 'data:image/png;base64,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CZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAT+H9FJng/hy/8wAAAAAElFTkSuQmCC' )
  if 42 - 42: I1Ii111 + I1ii11iIi11i
  if 70 - 70: Oo0Ooo % Oo0Ooo . IiII % OoO0O00 * o0oOOo0O0Ooo % oO0o
  iiI1IiI = ''
  for II in iii11iII :
   iiI1IiI += II + '|'
  return iiI1IiI
 if 57 - 57: oO0o
 if 14 - 14: Oo0Ooo . I1IiiI / Ii1I
 if 38 - 38: II111iiii % i11iIiiIii . ooOoO0o - OOooOOo + Ii1I
 if 66 - 66: OoooooooOO * OoooooooOO . OOooOOo . i1IIi - OOooOOo
 if 77 - 77: I11i - iIii1I11I1II1
 if 82 - 82: i11iIiiIii . OOooOOo / Oo0Ooo * O0 % oO0o % iIii1I11I1II1
 if 78 - 78: iIii1I11I1II1 - Ii1I * OoO0O00 + o0oOOo0O0Ooo + iII111i + iII111i
 if 11 - 11: iII111i - OoO0O00 % ooOoO0o % iII111i / OoOoOO00 - OoO0O00
 if 74 - 74: iII111i * O0
 if 89 - 89: oO0o + Oo0Ooo
 if 3 - 3: i1IIi / I1IiiI % I11i * i11iIiiIii / O0 * I11i
 if 49 - 49: oO0o % Ii1I + i1IIi . I1IiiI % I1ii11iIi11i
 if 48 - 48: I11i + I11i / II111iiii / iIii1I11I1II1
 if 20 - 20: o0oOOo0O0Ooo
 if 77 - 77: OoOoOO00 / I11i
 if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
 if 28 - 28: OOooOOo - IiII . IiII + OoOoOO00 - OoooooooOO + O0
 if 95 - 95: OoO0O00 % oO0o . O0
 if 15 - 15: ooOoO0o / Ii1I . Ii1I - i1IIi
 if 53 - 53: IiII + I1IiiI * oO0o
 if 61 - 61: i1IIi * OOooOOo / OoooooooOO . i11iIiiIii . OoOoOO00
 if 60 - 60: I11i / I11i
 if 46 - 46: Ii1I * OOooOOo - OoO0O00 * oO0o - I1Ii111
 if 83 - 83: OoooooooOO
 if 31 - 31: II111iiii - OOooOOo . I1Ii111 % OoOoOO00 - O0
 if 4 - 4: II111iiii / ooOoO0o . iII111i
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
 def SaveCredential ( self , login_params ) :
  self . TVING_TOKEN = login_params . get ( 'tving_token' )
  self . POC_USERINFO = login_params . get ( 'poc_userinfo' )
  self . TVING_UUID = login_params . get ( 'tving_uuid' )
  if 4 - 4: ooOoO0o + O0 * OOooOOo
 def LoadCredential ( self ) :
  OOoo0O = {
 'tving_token' : self . TVING_TOKEN
 , 'poc_userinfo' : self . POC_USERINFO
 , 'tving_uuid' : self . TVING_UUID
 }
  return OOoo0O
  if 67 - 67: i11iIiiIii - i1IIi % I1ii11iIi11i . O0
 def GetDefaultParams ( self ) :
  o0oo = { 'apiKey' : self . APIKEY
 , 'networkCode' : self . NETWORKCODE
 , 'osCode' : self . OSCODE
 , 'teleCode' : self . TELECODE
 , 'screenCode' : self . SCREENCODE
 }
  return o0oo
  if 91 - 91: IiII
 def GetNoCache ( self , timetype = 1 ) :
  if timetype == 1 :
   return int ( time . time ( ) )
  else :
   return int ( time . time ( ) * 1000 )
   if 15 - 15: II111iiii
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  Ii = domain + path
  if query1 :
   Ii += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   Ii += '&%s' % urllib . urlencode ( query2 )
  return Ii
  if 79 - 79: OoooooooOO / O0
  if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . I1Ii111
  if 5 - 5: o0oOOo0O0Ooo * ooOoO0o + OoOoOO00 . OOooOOo + OoOoOO00
  if 91 - 91: O0
  if 61 - 61: II111iiii
 def GetCredential ( self , user_id , user_pw , login_type ) :
  O0OOO = False
  II11iIiIIIiI = '-'
  if 67 - 67: I1Ii111 . iII111i . O0
  try :
   IIIIiiII111 = self . LOGIN_DOMAIN + '/pc/user/doLogin.tving'
   if 97 - 97: I1ii11iIi11i + OOooOOo / iIii1I11I1II1 / iII111i
   o0oo = { 'userId' : user_id
 , 'password' : user_pw
 , 'loginType' : '10' if login_type == '0' else '20'
 , 'autoLogin' : 'false'
 , 'cjOneCookie' : ''
 , 'kaptcha' : ''

   , 'returnUrl' : ''
 , 'csite' : ''
 }
   if 37 - 37: iII111i - ooOoO0o * oO0o % i11iIiiIii - I1Ii111
   II1Iiii1111i = self . SESSION . RequestCookie ( IIIIiiII111 , o0oo )
   if 83 - 83: I11i / I1IiiI
   if 34 - 34: IiII
   if 57 - 57: oO0o . I11i . i1IIi
   for i11Iii in II1Iiii1111i . split ( ',' ) :
    i11Iii = i11Iii . strip ( )
    if i11Iii . startswith ( '_tving_token' ) :
     IiIIIi1iIi = i11Iii . split ( ';' ) [ 0 ]
     IiIIIi1iIi = IiIIIi1iIi . split ( '=' ) [ 1 ]
     if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
    if i11Iii . startswith ( 'POC_USERINFO' ) :
     iii = i11Iii . split ( ';' ) [ 0 ]
     iii = iii . split ( '=' ) [ 1 ]
     if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
   if IiIIIi1iIi : O0OOO = True
   if 2 - 2: I1ii11iIi11i * I11i - iIii1I11I1II1 + I1IiiI . oO0o % iII111i
   II11iIiIIIiI = self . GetDeviceList ( IiIIIi1iIi , iii )
   if 92 - 92: iII111i
   if 25 - 25: Oo0Ooo - I1IiiI / OoooooooOO / o0oOOo0O0Ooo
  except Exception as II111iiiI1Ii :
   IiIIIi1iIi = iii = ''
   II11iIiIIIiI = '-'
   if 78 - 78: Ii1I % I1Ii111 + I1ii11iIi11i
  OOoo0O = {
 'tving_token' : IiIIIi1iIi
 , 'poc_userinfo' : iii
 , 'tving_uuid' : II11iIiIIIiI
 }
  self . SaveCredential ( OOoo0O )
  if 64 - 64: oO0o * O0 . I1IiiI + II111iiii
  return O0OOO
  if 6 - 6: OoOoOO00 / iII111i . IiII . IiII
  if 62 - 62: I1ii11iIi11i + IiII % iII111i + OOooOOo
 def GetBroadURL ( self , mediacode , sel_quality , stype ) :
  iiioOooOOOoOo = ''
  i1Iii1i1I = ''
  OOoO00 = self . TVING_UUID
  if 40 - 40: I1IiiI * Ii1I + OOooOOo % iII111i
  OOOOOoo0 = self . TVING_TOKEN
  ii1 = self . POC_USERINFO
  if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
  if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
  if 54 - 54: OoOoOO00 % iII111i
  if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
  if 88 - 88: iII111i . II111iiii * II111iiii % I1Ii111
  if 15 - 15: i1IIi * I1IiiI + i11iIiiIii
  if 6 - 6: ooOoO0o / i11iIiiIii + iII111i * oO0o
  try :
   if stype != 'tvingtv' :
    if 80 - 80: II111iiii
    O0O = '/v2/media/stream/info'
    if 1 - 1: II111iiii
    OOooooO0Oo = self . GetDefaultParams ( )
    OO = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'noCache' : str ( self . GetNoCache ( 1 ) )
 , 'callingFrom' : 'HTML5'
 , 'adReq' : 'none'
 , 'ooc' : ''
 }
    OO [ 'deviceId' ] = OOoO00
    if 25 - 25: OoO0O00
    Ii = self . makeurl ( self . API_DOMAIN , O0O , OOooooO0Oo , OO )
    if 62 - 62: OOooOOo + O0
    II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , OOOOOoo0 , 'POC_USERINFO' , ii1 ) )
 ]
    if 98 - 98: o0oOOo0O0Ooo
    i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
    OOOO0oo0 = json . loads ( i1IIi11111i )
    if 35 - 35: Ii1I - I1IiiI % o0oOOo0O0Ooo . OoooooooOO % Ii1I
    if not ( 'stream' in OOOO0oo0 [ 'body' ] ) : return iiioOooOOOoOo , i1Iii1i1I
    I1i1Iiiii = OOOO0oo0 [ 'body' ] [ 'stream' ]
    if 94 - 94: o0oOOo0O0Ooo * Ii1I / Oo0Ooo / Ii1I
    if 87 - 87: Oo0Ooo . IiII
    if 'drm_license_assertion' in I1i1Iiiii :
     i1Iii1i1I = I1i1Iiiii [ 'drm_license_assertion' ]
    else :
     if 75 - 75: ooOoO0o + OoOoOO00 + o0oOOo0O0Ooo * I11i % oO0o . iII111i
     oO = I1i1Iiiii [ 'broadcast' ] [ 'broad_url' ]
     if 31 - 31: OOooOOo + i11iIiiIii + Oo0Ooo * ooOoO0o
    IiII111iI1ii1 = I1i1Iiiii [ 'quality' ]
    if 37 - 37: oO0o - I1Ii111 % Oo0Ooo
    OOOoo0OO = [ ]
    for oO0o0 in IiII111iI1ii1 :
     if oO0o0 [ 'active' ] == 'Y' :
      OOOoo0OO . append ( { oooO0oo0oOOOO . get ( oO0o0 [ 'code' ] ) : oO0o0 [ 'code' ] } )
      if 50 - 50: IiII
    Ii11iIi = self . CheckQuality ( sel_quality , OOOoo0OO )
    if 55 - 55: I11i * oO0o * o0oOOo0O0Ooo % i1IIi . Ii1I . i11iIiiIii
   else :
    for oOOoo00O00o , O0O00Oo in oooO0oo0oOOOO . items ( ) :
     if O0O00Oo == sel_quality :
      Ii11iIi = oOOoo00O00o
      if 97 - 97: O0 * OoooooooOO . OoooooooOO
      if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
  except Exception as II111iiiI1Ii :
   for oOOoo00O00o , O0O00Oo in oooO0oo0oOOOO . items ( ) :
    if O0O00Oo == sel_quality :
     Ii11iIi = oOOoo00O00o
   return iiioOooOOOoOo , i1Iii1i1I
   if 54 - 54: I1Ii111 / OOooOOo . oO0o % iII111i
  print OOoO00 , Ii11iIi
  if 57 - 57: i11iIiiIii . I1ii11iIi11i - Ii1I - oO0o + OoOoOO00
  if 63 - 63: OoOoOO00 * iII111i
  try :
   if 69 - 69: O0 . OoO0O00
   O0O = '/streaming/info'
   OOooooO0Oo = self . GetDefaultParams ( )
   if stype == 'onair' : OOooooO0Oo [ 'osCode' ] = 'CSOD0400'
   if 49 - 49: I1IiiI - I11i
   if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
   if 62 - 62: OoooooooOO * I1IiiI
   oOOOoo0O0oO = {
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
   if 6 - 6: OOooOOo * o0oOOo0O0Ooo + iII111i
   I1IIIiIiI1 = self . makeOocUrl ( oOOOoo0O0oO )
   Ii1I1I11iI = urllib . quote ( I1IIIiIiI1 )
   if 51 - 51: iIii1I11I1II1
   if 34 - 34: oO0o + I1IiiI - oO0o
   if 17 - 17: II111iiii % iII111i + I11i - iII111i / OOooOOo + ooOoO0o
   OO = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'callingFrom' : 'HTML5'
 , 'streamCode' : Ii11iIi
   , 'adReq' : 'none'
 , 'ooc' : I1IIIiIiI1
 }
   OO [ 'deviceId' ] = OOoO00
   if 59 - 59: OOooOOo % OoOoOO00 . Ii1I * I1ii11iIi11i % I11i
   Ii = self . URL_DOMAIN + O0O
   oO0o0o0oo = OOooooO0Oo
   oO0o0o0oo . update ( OO )
   if 32 - 32: OOooOOo
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s; %s=%s'
 % ( '_tving_token' , OOOOOoo0
 , 'onClickEvent2' , Ii1I1I11iI
 , 'POC_USERINFO' , ii1
 )
 )
 , ( 'origin' , 'https://www.tving.com' )
 , ( 'Referer' , 'https://www.tving.com/vod/player/' + mediacode )
 ]
   if 42 - 42: IiII * O0 % i1IIi . OOooOOo / o0oOOo0O0Ooo
   i1IIi11111i = self . SESSION . Request ( Ii , params = oO0o0o0oo , cookie = II1Iiii1111i )
   if 32 - 32: I1IiiI * Oo0Ooo
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 78 - 78: OOooOOo - OoooooooOO - I1ii11iIi11i / ooOoO0o / II111iiii
   if 29 - 29: I1IiiI % I1IiiI
   if i1Iii1i1I != '' :
    i1Iii1i1I = OOOO0oo0 [ 'stream' ] [ 'drm_license_assertion' ]
    iiioOooOOOoOo = OOOO0oo0 [ 'stream' ] [ 'broadcast' ] [ 'widevine' ] [ 'broad_url' ]
   else :
    if not ( 'broad_url' in OOOO0oo0 [ 'stream' ] [ 'broadcast' ] ) : return iiioOooOOOoOo , i1Iii1i1I
    iiioOooOOOoOo = OOOO0oo0 [ 'stream' ] [ 'broadcast' ] [ 'broad_url' ]
    if 94 - 94: iIii1I11I1II1 / Oo0Ooo % iII111i * iII111i * II111iiii
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 29 - 29: OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / OOooOOo * iIii1I11I1II1
  return iiioOooOOOoOo , i1Iii1i1I
  if 62 - 62: OOooOOo / oO0o - OoO0O00 . I11i
  if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
 def CheckQuality ( self , sel_qt , qt_list ) :
  for IiII111i1i11 in qt_list :
   if sel_qt >= IiII111i1i11 . keys ( ) [ 0 ] : return IiII111i1i11 . get ( IiII111i1i11 . keys ( ) [ 0 ] )
   i111iIi1i1II1 = IiII111i1i11 . get ( IiII111i1i11 . keys ( ) [ 0 ] )
  return i111iIi1i1II1
  if 86 - 86: iIii1I11I1II1 / OoOoOO00 . II111iiii
  if 19 - 19: I1ii11iIi11i % OoooooooOO % IiII * o0oOOo0O0Ooo % O0
 def makeOocUrl ( self , ooc_params ) :
  Ii = ''
  for oOOoo00O00o , O0O00Oo in ooc_params . items ( ) :
   Ii += "%s=%s^" % ( oOOoo00O00o , O0O00Oo )
  return Ii
  if 67 - 67: I1IiiI . i1IIi
  if 27 - 27: ooOoO0o % I1IiiI
 def GetLiveChannelList ( self , stype , page_int ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 67 - 67: Ii1I / IiII
  try :
   O0O = '/v2/media/lives'
   if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
   if stype == 'onair' :
    OoO = 'CPCS0100,CPCS0400'
   else :
    OoO = 'CPCS0300'
    if 12 - 12: O0 - o0oOOo0O0Ooo
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . LIVE_LIMIT )
 , 'order' : 'rating'
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'channelType' : OoO

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 73 - 73: I11i % i11iIiiIii - I1IiiI
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 68 - 68: iII111i - I1IiiI / I1Ii111 / I11i
   if 12 - 12: Ii1I + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . I11i
   for oO0o0 in ii :
    Iii1iI = IiI1iiiIii = I1III1111iIi = I1i111I = ''
    Ooo = Oo0oo0O0o00O = ''
    if 48 - 48: ooOoO0o / I1Ii111 . iIii1I11I1II1 * OoOoOO00 * oO0o / i1IIi
    OOOOoOOo0O0 = oO0o0 [ 'live_code' ]
    Iii1iI = oO0o0 [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 92 - 92: I1ii11iIi11i + iIii1I11I1II1 / II111iiii
    if oO0o0 [ 'schedule' ] [ 'episode' ] != None :
     IiI1iiiIii = oO0o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     IiI1iiiIii = IiI1iiiIii + ', ' + str ( oO0o0 [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if oO0o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      I1III1111iIi = oO0o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     I1i111I = oO0o0 [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     IiI1iiiIii = oO0o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if oO0o0 [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      I1III1111iIi = oO0o0 [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     I1i111I = oO0o0 [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 94 - 94: OoooooooOO + Oo0Ooo / OoOoOO00 * OOooOOo
    if I1III1111iIi == '' :
     I1III1111iIi = oO0o0 [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if I1III1111iIi != '' : I1III1111iIi = self . IMG_DOMAIN + I1III1111iIi
    if 69 - 69: ooOoO0o % oO0o
    Ooo = str ( oO0o0 [ 'schedule' ] [ 'broadcast_start_time' ] ) [ 8 : 12 ]
    Oo0oo0O0o00O = str ( oO0o0 [ 'schedule' ] [ 'broadcast_end_time' ] ) [ 8 : 12 ]
    if 50 - 50: OoooooooOO % I11i
    IIii1111 = { 'channel' : unicode ( Iii1iI )
 , 'title' : unicode ( IiI1iiiIii )
 , 'mediacode' : OOOOoOOo0O0
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 , 'channelepg' : ' [%s:%s ~ %s:%s]' % ( Ooo [ 0 : 2 ] , Ooo [ 2 : ] , Oo0oo0O0o00O [ 0 : 2 ] , Oo0oo0O0o00O [ 2 : ] )
 }
    if 42 - 42: I11i / o0oOOo0O0Ooo . oO0o + oO0o % OoOoOO00 + i11iIiiIii
    o0oooOO00 . append ( IIii1111 )
    if 56 - 56: o0oOOo0O0Ooo
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
  return o0oooOO00 , iiIiii1IIIII
  if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
  if 79 - 79: O0 * i11iIiiIii - IiII / IiII
 def GetProgramList ( self , stype , orderby , page_int , landyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 48 - 48: O0
  try :
   O0O = '/v2/media/episodes'
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
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
   if stype != 'all' : OO [ 'multiCategoryCode' ] = stype
   if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 19 - 19: OoO0O00 - Oo0Ooo . O0
   if 60 - 60: II111iiii + Oo0Ooo
   for oO0o0 in ii :
    I1IiIiiIiIII = oO0o0 [ 'program' ] [ 'code' ]
    IiI1iiiIii = oO0o0 [ 'program' ] [ 'name' ] [ 'ko' ]
    if 8 - 8: oO0o / I1ii11iIi11i
    I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    i1iI1 = 'CAIP0200' if landyn else 'CAIP0900'
    if 33 - 33: IiII % iIii1I11I1II1 * I1IiiI
    for o00o0 in oO0o0 [ 'program' ] [ 'image' ] :
     if o00o0 [ 'code' ] == i1iI1 :
      I1III1111iIi = self . IMG_DOMAIN + o00o0 [ 'url' ]
      break
      if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
    I1i111I = oO0o0 [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    O0O0Oo00 = oO0o0 [ 'program' ] [ 'channel_code' ]
    if 80 - 80: oO0o + OOooOOo / I11i
    IIii1111 = { 'program' : I1IiIiiIiIII
 , 'title' : unicode ( IiI1iiiIii )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 , 'channel' : O0O0Oo00
 }
    if 79 - 79: ooOoO0o
    o0oooOO00 . append ( IIii1111 )
    if 48 - 48: I1Ii111 - o0oOOo0O0Ooo % Ii1I
    if 36 - 36: oO0o - Ii1I . Oo0Ooo - i11iIiiIii - OOooOOo * Oo0Ooo
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - Ii1I + I1ii11iIi11i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 51 - 51: iIii1I11I1II1 . ooOoO0o + iIii1I11I1II1
  return o0oooOO00 , iiIiii1IIIII
  if 95 - 95: I1IiiI
  if 46 - 46: OoOoOO00 + OoO0O00
 def GetEpisodoList ( self , program_code , page_int , orderby = 'desc' ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 70 - 70: iII111i / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
  if 96 - 96: OoooooooOO + oO0o
  if 44 - 44: oO0o
  if 20 - 20: I11i + Ii1I / O0 % iIii1I11I1II1
  if 88 - 88: OoOoOO00 / II111iiii
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
  try :
   O0O = '/v2/media/frequency/program/' + program_code
   if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 42 - 42: Oo0Ooo
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 46 - 46: Oo0Ooo
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 1 - 1: iII111i
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
   oOoO0 = int ( OOOO0oo0 [ 'body' ] [ 'total_count' ] )
   if 77 - 77: iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   Oo00o0OO0O00o = int ( oOoO0 // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if orderby == 'desc' :
    O0Oooo = ( oOoO0 - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    O0Oooo = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 21 - 21: Oo0Ooo
   for I1ii1 in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     O00 = O0Oooo - I1ii1
     if O00 < 0 : break
    else :
     O00 = O0Oooo + I1ii1
     if O00 >= oOoO0 : break
     if 92 - 92: iIii1I11I1II1 * i1IIi * iII111i % OOooOOo % I1ii11iIi11i + II111iiii
    i1iIi1I1i = ii [ O00 ] [ 'episode' ] [ 'code' ]
    IiI1iiiIii = ii [ O00 ] [ 'vod_name' ] [ 'ko' ]
    if ii [ O00 ] [ 'episode' ] [ 'image' ] != [ ] :
     I1III1111iIi = self . IMG_DOMAIN + ii [ O00 ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     I1III1111iIi = self . IMG_DOMAIN + ii [ O00 ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    I1i111I = ii [ O00 ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 1 - 1: I11i % OOooOOo + O0 + i1IIi - OoO0O00
    IIii1111 = { 'episode' : i1iIi1I1i
 , 'title' : unicode ( IiI1iiiIii )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 }
    if 22 - 22: I1IiiI % I1ii11iIi11i
    o0oooOO00 . append ( IIii1111 )
    if 57 - 57: OOooOOo + O0 . Ii1I
   if Oo00o0OO0O00o > page_int : iiIiii1IIIII = True
   if 46 - 46: IiII
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 45 - 45: ooOoO0o
  return o0oooOO00 , iiIiii1IIIII , Oo00o0OO0O00o
  if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
  if 17 - 17: OOooOOo / OOooOOo / I11i
 def GetMovieList ( self , orderby , page_int , premiumyn = False , landyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
  if premiumyn == True :
   OooO0oo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   OooO0oo = self . MOVIE_LITE
   if 89 - 89: Ii1I
  try :
   O0O = '/v2/media/movies'
   if 76 - 76: ooOoO0o
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : OooO0oo
   # o0oOOo0O0Ooo
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 1 - 1: I11i + OoooooooOO - OOooOOo + IiII
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 9 - 9: Ii1I
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 59 - 59: I1IiiI * II111iiii . O0
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
   if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
   for oO0o0 in ii :
    i1 = oO0o0 [ 'movie' ] [ 'code' ]
    IiI1iiiIii = oO0o0 [ 'movie' ] [ 'name' ] [ 'ko' ]
    I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    i1iI1 = 'CAIM0400' if landyn else 'CAIM2100'
    if 51 - 51: OoO0O00 - O0 % oO0o - II111iiii
    for o00o0 in oO0o0 [ 'movie' ] [ 'image' ] :
     if o00o0 [ 'code' ] == i1iI1 :
      I1III1111iIi = self . IMG_DOMAIN + o00o0 [ 'url' ]
      break
      if 31 - 31: iII111i / Oo0Ooo - iII111i - OOooOOo
    I1i111I = oO0o0 [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 7 - 7: iII111i % O0 . OoOoOO00 + I1IiiI - I11i
    IIii1111 = { 'moviecode' : i1
 , 'title' : unicode ( IiI1iiiIii . strip ( ) )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 }
    if 75 - 75: I11i
    if premiumyn == True :
     oO00oo0o00o0o = False
     for IiIIIIIi in oO0o0 [ 'billing_package_id' ] :
      if IiIIIIIi == self . MOVIE_LITE :
       oO00oo0o00o0o = True
       break
     if oO00oo0o00o0o == False :
      IIii1111 [ 'title' ] = unicode ( IIii1111 [ 'title' ] + ' [Premium]' )
      if 11 - 11: i1IIi % i11iIiiIii - i1IIi * OoOoOO00
    o0oooOO00 . append ( IIii1111 )
    if 39 - 39: I1Ii111
    if 86 - 86: I11i * I1IiiI + I11i + II111iiii
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 8 - 8: I1Ii111 - iII111i / ooOoO0o
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 96 - 96: OoOoOO00
  return o0oooOO00 , iiIiii1IIIII
  if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - Ii1I
  if 20 - 20: i1IIi % OoO0O00 . I1IiiI / IiII * i11iIiiIii * OOooOOo
 def GetMovieListGenre ( self , genre , page_int , premiumyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / ooOoO0o . O0 % I1Ii111
  if premiumyn == True :
   OooO0oo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   OooO0oo = self . MOVIE_LITE
   if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . iII111i
  try :
   O0O = '/v2/media/movie/curation/' + genre
   if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'productPackageCode' : OooO0oo
   # II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 100 - 100: OoO0O00
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   if not ( 'movies' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'movies' ]
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   if 45 - 45: I1Ii111
   for oO0o0 in ii :
    i1 = oO0o0 [ 'code' ]
    IiI1iiiIii = oO0o0 [ 'name' ] [ 'ko' ]
    I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'image' ] [ 0 ] [ 'url' ]
    for o00o0 in oO0o0 [ 'image' ] :
     if o00o0 [ 'code' ] == 'CAIM2100' :
      I1III1111iIi = self . IMG_DOMAIN + o00o0 [ 'url' ]
    I1i111I = oO0o0 [ 'story' ] [ 'ko' ]
    if 83 - 83: OoOoOO00 . OoooooooOO
    IIii1111 = { 'moviecode' : i1
 , 'title' : unicode ( IiI1iiiIii . strip ( ) )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 }
    if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
    if premiumyn == True :
     oO00oo0o00o0o = False
     for IiIIIIIi in oO0o0 [ 'billing_package_id' ] :
      if IiIIIIIi == self . MOVIE_LITE :
       oO00oo0o00o0o = True
       break
     if oO00oo0o00o0o == False :
      IIii1111 [ 'title' ] = unicode ( IIii1111 [ 'title' ] + ' [Premium]' )
      if 62 - 62: OoO0O00 / I1ii11iIi11i
    o0oooOO00 . append ( IIii1111 )
    if 7 - 7: OoooooooOO . IiII
    if 53 - 53: Ii1I % Ii1I * o0oOOo0O0Ooo + OoOoOO00
    if 92 - 92: OoooooooOO + i1IIi / Ii1I * O0
    if 100 - 100: ooOoO0o % iIii1I11I1II1 * II111iiii - iII111i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 92 - 92: ooOoO0o
  return o0oooOO00 , iiIiii1IIIII
  if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
  if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
 def GetMovieGenre ( self ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  try :
   O0O = '/v2/media/movie/curations'
   if 92 - 92: I11i . I1Ii111
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'movieViewType' : 'sma'
 , 'curationSection' : 'view0002'
   , 'order' : 'curation_code'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 85 - 85: I1ii11iIi11i . I1Ii111
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 18 - 18: iIii1I11I1II1 % I11i
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
   if 75 - 75: OoooooooOO * IiII
   for oO0o0 in ii :
    I1Iiiiiii = oO0o0 [ 'curation_code' ]
    I1IIIiI1I1ii1 = oO0o0 [ 'curation_name' ]
    if 30 - 30: O0 * OoooooooOO
    IIii1111 = { 'curation_code' : I1Iiiiiii
 , 'curation_name' : unicode ( I1IIIiI1I1ii1 )
 }
    o0oooOO00 . append ( IIii1111 )
    if 38 - 38: IiII - I1ii11iIi11i . OoOoOO00 - I1Ii111 . OoooooooOO
    if 89 - 89: iIii1I11I1II1
    if 21 - 21: I11i % I11i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 27 - 27: i11iIiiIii / I1ii11iIi11i
  return o0oooOO00 , iiIiii1IIIII
  if 84 - 84: Oo0Ooo
  if 43 - 43: oO0o - OoooooooOO
 def GetSearchList ( self , search_key , userid , page_int , stype , premiumyn = False , landyn = False ) :
  ii1iI = [ ]
  iiIiii1IIIII = False
  if 49 - 49: o0oOOo0O0Ooo . IiII / OoO0O00 + II111iiii
  try :
   O0O = '/search/getSearch.jsp'
   if 47 - 47: O0 / Ii1I
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'kwd' : search_key
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
   if 67 - 67: I1IiiI
   Ii = self . makeurl ( self . SEARCH_DOMAIN , O0O , OO , None )
   if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
   if stype == 'vod' :
    if not ( 'programRsb' in OOOO0oo0 ) : return ii1iI , iiIiii1IIIII
    oOooO0 = OOOO0oo0 [ 'programRsb' ] [ 'dataList' ]
    OOOoO000 = int ( OOOO0oo0 [ 'programRsb' ] [ 'count' ] )
    if 57 - 57: II111iiii
    if 54 - 54: Oo0Ooo + oO0o + i11iIiiIii
    for oO0o0 in oOooO0 :
     I1IiIiiIiIII = oO0o0 [ 'mast_cd' ]
     IiI1iiiIii = oO0o0 [ 'mast_nm' ]
     I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'web_url' ]
     if landyn == False :
      I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'web_url4' ]
      if 28 - 28: oO0o
     I1i111I = oO0o0 [ 'mast_synop' ]
     if 70 - 70: IiII
     IIii1111 = { 'program' : I1IiIiiIiIII
 , 'title' : unicode ( IiI1iiiIii )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 }
     if 34 - 34: I1Ii111 % IiII
     ii1iI . append ( IIii1111 )
   else :
    if not ( 'vodMVRsb' in OOOO0oo0 ) : return ii1iI , iiIiii1IIIII
    IiI1i = OOOO0oo0 [ 'vodMVRsb' ] [ 'dataList' ]
    OOOoO000 = int ( OOOO0oo0 [ 'vodMVRsb' ] [ 'count' ] )
    if 87 - 87: ooOoO0o
    if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
    for oO0o0 in IiI1i :
     I1IiIiiIiIII = oO0o0 [ 'mast_cd' ]
     IiI1iiiIii = oO0o0 [ 'mast_nm' ]
     I1III1111iIi = self . IMG_DOMAIN + oO0o0 [ 'web_url' ]
     if landyn :
      I1III1111iIi = I1III1111iIi . replace ( 'CAIM2100' , 'CAIM0400' )
      if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
     I1i111I = oO0o0 [ 'mast_synop' ]
     if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
     iIi1II = False
     I1iIiI11I1 = False
     for IiIIIIIi in oO0o0 [ 'bill' ] :
      if IiIIIIIi == self . MOVIE_LITE : I1iIiI11I1 = True
      elif IiIIIIIi == self . MOVIE_PREMIUM : iIi1II = True
      if 27 - 27: Ii1I . i11iIiiIii % I1Ii111
     if I1iIiI11I1 or ( premiumyn == True and iIi1II ) :
      IIii1111 = { 'movie' : I1IiIiiIiIII
 , 'title' : unicode ( IiI1iiiIii . strip ( ) )
 , 'thumbnail' : I1III1111iIi
 , 'synopsis' : unicode ( I1i111I )
 }
      if I1iIiI11I1 == False : IIii1111 [ 'title' ] = unicode ( IIii1111 [ 'title' ] + ' [Premium]' )
      ii1iI . append ( IIii1111 )
      if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
      if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
      if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
      if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
  return ii1iI , iiIiii1IIIII
  if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
 def GetDeviceList ( self , tving_token , poc_userinfo ) :
  o0oooOO00 = [ ]
  OOoO00 = '-'
  if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
  try :
   O0O = '/v1/user/device/list'
   if 95 - 95: IiII
   if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
   OO = { 'apiKey' : '4263d7d76161f4a19a9efe9ca7903ec4'
 , 'model' : 'PC'
 }
   if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO )
   if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , tving_token , 'POC_USERINFO' , poc_userinfo ) )
 ]
   if 2 - 2: OoooooooOO % OOooOOo
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 63 - 63: I1IiiI % iIii1I11I1II1
   if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
   o0oooOO00 = OOOO0oo0 [ 'body' ]
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   for oO0o0 in o0oooOO00 :
    if oO0o0 [ 'model' ] == 'PC' :
     OOoO00 = oO0o0 [ 'uuid' ]
     if 59 - 59: OOooOOo + i11iIiiIii
     if 88 - 88: i11iIiiIii - ooOoO0o
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  return OOoO00
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
