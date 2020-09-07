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
 def SaveCredential ( self , login_params ) :
  self . TVING_TOKEN = login_params . get ( 'tving_token' )
  self . POC_USERINFO = login_params . get ( 'poc_userinfo' )
  self . TVING_UUID = login_params . get ( 'tving_uuid' )
  if 31 - 31: I11i - i1IIi * OOooOOo / OoooooooOO
 def LoadCredential ( self ) :
  iI = {
 'tving_token' : self . TVING_TOKEN
 , 'poc_userinfo' : self . POC_USERINFO
 , 'tving_uuid' : self . TVING_UUID
 }
  return iI
  if 60 - 60: I11i / I11i
 def GetDefaultParams ( self ) :
  I1II1III11iii = { 'apiKey' : self . APIKEY
 , 'networkCode' : self . NETWORKCODE
 , 'osCode' : self . OSCODE
 , 'teleCode' : self . TELECODE
 , 'screenCode' : self . SCREENCODE
 }
  return I1II1III11iii
  if 75 - 75: iIii1I11I1II1 / OOooOOo % o0oOOo0O0Ooo * OoOoOO00
 def GetNoCache ( self , timetype = 1 ) :
  if timetype == 1 :
   return int ( time . time ( ) )
  else :
   return int ( time . time ( ) * 1000 )
   if 9 - 9: OoO0O00
 def makeurl ( self , domain , path , query1 = None , query2 = None ) :
  i11 = domain + path
  if query1 :
   i11 += '?%s' % urllib . urlencode ( query1 )
  if query2 :
   i11 += '&%s' % urllib . urlencode ( query2 )
  return i11
  if 58 - 58: OOooOOo * i11iIiiIii / OoOoOO00 % I1Ii111 - I1ii11iIi11i / oO0o
  if 50 - 50: I1IiiI
  if 34 - 34: I1IiiI * II111iiii % iII111i * OoOoOO00 - I1IiiI
  if 33 - 33: o0oOOo0O0Ooo + OOooOOo * OoO0O00 - Oo0Ooo / oO0o % Ii1I
  if 21 - 21: OoO0O00 * iIii1I11I1II1 % oO0o * i1IIi
 def GetCredential ( self , user_id , user_pw , login_type ) :
  Ii11Ii1I = False
  O00oO = '-'
  if 39 - 39: IiII - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  try :
   OoOOOOO = self . LOGIN_DOMAIN + '/pc/user/doLogin.tving'
   if 33 - 33: I1ii11iIi11i % i1IIi
   I1II1III11iii = { 'userId' : user_id
 , 'password' : user_pw
 , 'loginType' : '10' if login_type == '0' else '20'
 , 'autoLogin' : 'false'
 , 'cjOneCookie' : ''
 , 'kaptcha' : ''

   , 'returnUrl' : ''
 , 'csite' : ''
 }
   if 78 - 78: I11i
   oo0Ooo0 = self . SESSION . RequestCookie ( OoOOOOO , I1II1III11iii )
   if 71 - 71: OOooOOo + ooOoO0o % i11iIiiIii + I1ii11iIi11i - IiII
   if 88 - 88: OoOoOO00 - OoO0O00 % OOooOOo
   if 16 - 16: I1IiiI * oO0o % IiII
   for Oo000o in oo0Ooo0 . split ( ',' ) :
    Oo000o = Oo000o . strip ( )
    if Oo000o . startswith ( '_tving_token' ) :
     I11IiI1I11i1i = Oo000o . split ( ';' ) [ 0 ]
     I11IiI1I11i1i = I11IiI1I11i1i . split ( '=' ) [ 1 ]
     if 38 - 38: o0oOOo0O0Ooo
    if Oo000o . startswith ( 'POC_USERINFO' ) :
     Oo0O = Oo000o . split ( ';' ) [ 0 ]
     Oo0O = Oo0O . split ( '=' ) [ 1 ]
     if 25 - 25: OoOoOO00 . II111iiii / iII111i . OOooOOo * OoO0O00 . I1IiiI
   if I11IiI1I11i1i : Ii11Ii1I = True
   if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
   O00oO = self . GetDeviceList ( I11IiI1I11i1i , Oo0O )
   if 58 - 58: II111iiii * OOooOOo * I1ii11iIi11i / OOooOOo
   if 75 - 75: oO0o
  except Exception as I1III :
   I11IiI1I11i1i = Oo0O = ''
   O00oO = '-'
   if 63 - 63: OOooOOo % oO0o * oO0o * OoO0O00 / I1ii11iIi11i
  iI = {
 'tving_token' : I11IiI1I11i1i
 , 'poc_userinfo' : Oo0O
 , 'tving_uuid' : O00oO
 }
  self . SaveCredential ( iI )
  if 74 - 74: II111iiii
  return Ii11Ii1I
  if 75 - 75: o0oOOo0O0Ooo . ooOoO0o
  if 54 - 54: II111iiii % OoOoOO00 % I11i % iIii1I11I1II1 + iIii1I11I1II1 * ooOoO0o
 def GetBroadURL ( self , mediacode , sel_quality , stype ) :
  O00O0oOO00O00 = ''
  i1 = ''
  Oo00 = self . TVING_UUID
  if 31 - 31: I1Ii111 . OoOoOO00 / O0
  o000O0o = self . TVING_TOKEN
  iI1iII1 = self . POC_USERINFO
  if 86 - 86: OOooOOo
  if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * oO0o - i11iIiiIii - Ii1I
  if 25 - 25: I1ii11iIi11i
  if 7 - 7: i1IIi / I1IiiI * I1Ii111 . IiII . iIii1I11I1II1
  if 13 - 13: OOooOOo / i11iIiiIii
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % Ii1I
  if 52 - 52: o0oOOo0O0Ooo
  try :
   if stype != 'tvingtv' :
    if 95 - 95: Ii1I
    O0oOO0O = '/v2/media/stream/info'
    if 91 - 91: O0
    oOOo0 = self . GetDefaultParams ( )
    oo00O00oO = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'noCache' : str ( self . GetNoCache ( 1 ) )
 , 'callingFrom' : 'HTML5'
 , 'adReq' : 'none'
 , 'ooc' : ''
 }
    oo00O00oO [ 'deviceId' ] = Oo00
    if 23 - 23: OoO0O00 + OoO0O00 . OOooOOo
    i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oOOo0 , oo00O00oO )
    if 38 - 38: I1Ii111
    oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , o000O0o , 'POC_USERINFO' , iI1iII1 ) )
 ]
    if 7 - 7: O0 . iII111i % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
    I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
    I111IIIiIii = json . loads ( I1I11I1I1I )
    if 85 - 85: I1ii11iIi11i % iII111i % ooOoO0o
    if not ( 'stream' in I111IIIiIii [ 'body' ] ) : return O00O0oOO00O00 , i1
    Oo00oo0oO = I111IIIiIii [ 'body' ] [ 'stream' ]
    if 1 - 1: OoO0O00 - oO0o . I11i . OoO0O00 / Oo0Ooo + I11i
    if 78 - 78: O0 . oO0o . II111iiii % OOooOOo
    if 'drm_license_assertion' in Oo00oo0oO :
     i1 = Oo00oo0oO [ 'drm_license_assertion' ]
    else :
     if 49 - 49: Ii1I / OoO0O00 . II111iiii
     ooOOoooooo = Oo00oo0oO [ 'broadcast' ] [ 'broad_url' ]
     if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % iII111i * IiII . i11iIiiIii
    III1Iiii1I11 = Oo00oo0oO [ 'quality' ]
    if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
    o00oooO0Oo = [ ]
    for o0O0OOO0Ooo in III1Iiii1I11 :
     if o0O0OOO0Ooo [ 'active' ] == 'Y' :
      o00oooO0Oo . append ( { oooO0oo0oOOOO . get ( o0O0OOO0Ooo [ 'code' ] ) : o0O0OOO0Ooo [ 'code' ] } )
      if 45 - 45: O0 / o0oOOo0O0Ooo
    i1IIIII11I1IiI = self . CheckQuality ( sel_quality , o00oooO0Oo )
    if 16 - 16: iIii1I11I1II1
   else :
    for oOooOOOoOo , i1Iii1i1I in oooO0oo0oOOOO . items ( ) :
     if i1Iii1i1I == sel_quality :
      i1IIIII11I1IiI = oOooOOOoOo
      if 91 - 91: I1ii11iIi11i + I1IiiI . OOooOOo * I1ii11iIi11i + I1IiiI * Oo0Ooo
      if 80 - 80: iII111i % OOooOOo % oO0o - Oo0Ooo + Oo0Ooo
  except Exception as I1III :
   for oOooOOOoOo , i1Iii1i1I in oooO0oo0oOOOO . items ( ) :
    if i1Iii1i1I == sel_quality :
     i1IIIII11I1IiI = oOooOOOoOo
   return O00O0oOO00O00 , i1
   if 19 - 19: OoOoOO00 * i1IIi
  print Oo00 , i1IIIII11I1IiI
  if 14 - 14: iII111i
  if 11 - 11: IiII * I1IiiI . iIii1I11I1II1 % OoooooooOO + iII111i
  try :
   if 78 - 78: OoO0O00 . OOooOOo + OoO0O00 / I11i / OoO0O00
   O0oOO0O = '/streaming/info'
   oOOo0 = self . GetDefaultParams ( )
   if stype == 'onair' : oOOo0 [ 'osCode' ] = 'CSOD0400'
   if 54 - 54: OoOoOO00 % iII111i
   if 37 - 37: OoOoOO00 * Oo0Ooo / ooOoO0o - iII111i % II111iiii . oO0o
   if 88 - 88: iII111i . II111iiii * II111iiii % I1Ii111
   iiIIiiIi1Ii11 = {
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
   if 65 - 65: II111iiii . OOooOOo % I11i . i11iIiiIii + O0
   I1IiiiiI = self . makeOocUrl ( iiIIiiIi1Ii11 )
   o0O = urllib . quote ( I1IiiiiI )
   if 2 - 2: iIii1I11I1II1 / oO0o + OoO0O00 / OOooOOo
   if 9 - 9: o0oOOo0O0Ooo . ooOoO0o - Oo0Ooo - oO0o + II111iiii * i11iIiiIii
   if 79 - 79: oO0o % I11i % I1IiiI
   oo00O00oO = { 'info' : 'Y'
 , 'mediaCode' : mediacode
 , 'callingFrom' : 'HTML5'
 , 'streamCode' : i1IIIII11I1IiI
   , 'adReq' : 'none'
 , 'ooc' : I1IiiiiI
 }
   oo00O00oO [ 'deviceId' ] = Oo00
   if 5 - 5: OoooooooOO % OoOoOO00 % oO0o % iII111i
   i11 = self . URL_DOMAIN + O0oOO0O
   Iiiii1I = oOOo0
   Iiiii1I . update ( oo00O00oO )
   if 99 - 99: Ii1I / Oo0Ooo / IiII % I1IiiI
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s; %s=%s'
 % ( '_tving_token' , o000O0o
 , 'onClickEvent2' , o0O
 , 'POC_USERINFO' , iI1iII1
 )
 )
 , ( 'origin' , 'https://www.tving.com' )
 , ( 'Referer' , 'https://www.tving.com/vod/player/' + mediacode )
 ]
   if 13 - 13: I11i * Oo0Ooo * ooOoO0o
   I1I11I1I1I = self . SESSION . Request ( i11 , params = Iiiii1I , cookie = oo0Ooo0 )
   if 50 - 50: o0oOOo0O0Ooo * I11i % O0
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 61 - 61: I1IiiI - OOooOOo . oO0o / OOooOOo + Oo0Ooo
   if 5 - 5: ooOoO0o + ooOoO0o / O0 * Oo0Ooo - OOooOOo % ooOoO0o
   if i1 != '' :
    i1 = I111IIIiIii [ 'stream' ] [ 'drm_license_assertion' ]
    O00O0oOO00O00 = I111IIIiIii [ 'stream' ] [ 'broadcast' ] [ 'widevine' ] [ 'broad_url' ]
   else :
    if not ( 'broad_url' in I111IIIiIii [ 'stream' ] [ 'broadcast' ] ) : return O00O0oOO00O00 , i1
    O00O0oOO00O00 = I111IIIiIii [ 'stream' ] [ 'broadcast' ] [ 'broad_url' ]
    if 15 - 15: i11iIiiIii % Ii1I . Oo0Ooo + I1ii11iIi11i
  except Exception as I1III :
   print ( I1III )
   if 61 - 61: Oo0Ooo * I1ii11iIi11i % Oo0Ooo - i1IIi - iIii1I11I1II1
  return O00O0oOO00O00 , i1
  if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
  if 100 - 100: OoOoOO00 * iIii1I11I1II1
 def CheckQuality ( self , sel_qt , qt_list ) :
  for oOo00oOoO000 in qt_list :
   if sel_qt >= oOo00oOoO000 . keys ( ) [ 0 ] : return oOo00oOoO000 . get ( oOo00oOoO000 . keys ( ) [ 0 ] )
   OOooo0oOO0O = oOo00oOoO000 . get ( oOo00oOoO000 . keys ( ) [ 0 ] )
  return OOooo0oOO0O
  if 62 - 62: I1IiiI
  if 100 - 100: Ii1I - O0 % oO0o * OOooOOo + I1IiiI
 def makeOocUrl ( self , ooc_params ) :
  i11 = ''
  for oOooOOOoOo , i1Iii1i1I in ooc_params . items ( ) :
   i11 += "%s=%s^" % ( oOooOOOoOo , i1Iii1i1I )
  return i11
  if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
  if 33 - 33: I1Ii111 + iII111i * oO0o / iIii1I11I1II1 - I1IiiI
 def GetLiveChannelList ( self , stype , page_int ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 63 - 63: OoOoOO00 * iII111i
  try :
   O0oOO0O = '/v2/media/lives'
   if 69 - 69: O0 . OoO0O00
   if stype == 'onair' :
    ii1111iII = 'CPCS0100,CPCS0400'
   else :
    ii1111iII = 'CPCS0300'
    if 32 - 32: i1IIi / II111iiii . Oo0Ooo
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . LIVE_LIMIT )
 , 'order' : 'rating'
 , 'adult' : 'all'
 , 'free' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'channelType' : ii1111iII

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 62 - 62: OoooooooOO * I1IiiI
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 50 - 50: I1Ii111 . o0oOOo0O0Ooo
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 97 - 97: O0 + OoOoOO00
   if not ( 'result' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'result' ]
   if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
   if 77 - 77: OOooOOo * iIii1I11I1II1
   for o0O0OOO0Ooo in OO0O000 :
    oO00oOOoooO = { }
    oO00oOOoooO [ 'mediatype' ] = 'video'
    if 46 - 46: I1IiiI - OoooooooOO - I11i * II111iiii
    I1i1I11I = OoO000O0Oo = Oo0o0oooo0O0 = OooooOOoo0 = ''
    i1I1IiiIi1i = iiI11ii1I1 = ''
    if 82 - 82: II111iiii % I11i / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / I1Ii111
    oOo0OOoO0 = o0O0OOO0Ooo [ 'live_code' ]
    I1i1I11I = o0O0OOO0Ooo [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 11 - 11: I1ii11iIi11i . OoO0O00 * IiII * OoooooooOO + ooOoO0o
    if o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] != None :
     OoO000O0Oo = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     OoO000O0Oo = OoO000O0Oo + ', ' + str ( o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      Oo0o0oooo0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     OooooOOoo0 = o0O0OOO0Ooo [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     OoO000O0Oo = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      Oo0o0oooo0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     OooooOOoo0 = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 33 - 33: O0 * o0oOOo0O0Ooo - I1Ii111 % I1Ii111
     if 18 - 18: I1Ii111 / Oo0Ooo * I1Ii111 + I1Ii111 * i11iIiiIii * I1ii11iIi11i
    oO00oOOoooO [ 'title' ] = o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
    oO00oOOoooO [ 'studio' ] = I1i1I11I
    try :
     I1II1 = [ ]
     for oooO in o0O0OOO0Ooo . get ( 'schedule' ) . get ( 'program' ) . get ( 'actor' ) : I1II1 . append ( oooO )
     if I1II1 [ 0 ] != '' and I1II1 [ 0 ] != u'없음' : oO00oOOoooO [ 'cast' ] = I1II1
    except :
     None
    try :
     i1I1i111Ii = [ ]
     if o0O0OOO0Ooo . get ( 'schedule' ) . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      i1I1i111Ii . append ( o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
     if o0O0OOO0Ooo . get ( 'schedule' ) . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      i1I1i111Ii . append ( o0O0OOO0Ooo [ 'schedule' ] [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
     if i1I1i111Ii [ 0 ] != '' : oO00oOOoooO [ 'genre' ] = i1I1i111Ii
    except :
     None
     if 67 - 67: I1IiiI . i1IIi
     if 27 - 27: ooOoO0o % I1IiiI
     if 73 - 73: OOooOOo
     if 70 - 70: iIii1I11I1II1
    if Oo0o0oooo0O0 == '' :
     Oo0o0oooo0O0 = o0O0OOO0Ooo [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if Oo0o0oooo0O0 != '' : Oo0o0oooo0O0 = self . IMG_DOMAIN + Oo0o0oooo0O0
    if 31 - 31: IiII - I1IiiI % iIii1I11I1II1
    i1I1IiiIi1i = str ( o0O0OOO0Ooo [ 'schedule' ] [ 'broadcast_start_time' ] ) [ 8 : 12 ]
    iiI11ii1I1 = str ( o0O0OOO0Ooo [ 'schedule' ] [ 'broadcast_end_time' ] ) [ 8 : 12 ]
    if 92 - 92: i1IIi - iIii1I11I1II1
    IIIIIIii1 = { 'channel' : unicode ( I1i1I11I )
 , 'title' : unicode ( OoO000O0Oo )
 , 'mediacode' : oOo0OOoO0
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : unicode ( OooooOOoo0 )
 , 'channelepg' : ' [%s:%s ~ %s:%s]' % ( i1I1IiiIi1i [ 0 : 2 ] , i1I1IiiIi1i [ 2 : ] , iiI11ii1I1 [ 0 : 2 ] , iiI11ii1I1 [ 2 : ] )
 , 'info' : oO00oOOoooO
 }
    if 88 - 88: OoO0O00
    O0oO . append ( IIIIIIii1 )
    if 71 - 71: I1ii11iIi11i
   if I111IIIiIii [ 'body' ] [ 'has_more' ] == 'Y' : OO0ooOOO0OOO = True
   if 7 - 7: I1ii11iIi11i - I1IiiI . iIii1I11I1II1 - i1IIi
  except Exception as I1III :
   print ( I1III )
   if 59 - 59: o0oOOo0O0Ooo
  return O0oO , OO0ooOOO0OOO
  if 81 - 81: OoOoOO00 - OoOoOO00 . iII111i
  if 73 - 73: I11i % i11iIiiIii - I1IiiI
 def GetProgramList ( self , stype , orderby , page_int , landyn = False ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 7 - 7: O0 * i11iIiiIii * Ii1I + ooOoO0o % OoO0O00 - ooOoO0o
  try :
   O0oOO0O = '/v2/media/episodes'
   if 39 - 39: Oo0Ooo * OOooOOo % OOooOOo - OoooooooOO + o0oOOo0O0Ooo - I11i
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : str ( page_int )
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
   if stype != 'all' : oo00O00oO [ 'multiCategoryCode' ] = stype
   if 23 - 23: i11iIiiIii
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 30 - 30: o0oOOo0O0Ooo - i1IIi % II111iiii + I11i * iIii1I11I1II1
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 81 - 81: IiII % i1IIi . iIii1I11I1II1
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 4 - 4: i11iIiiIii % OoO0O00 % i1IIi / IiII
   if not ( 'result' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'result' ]
   if 6 - 6: iII111i / I1IiiI % OOooOOo - I1IiiI
   if 31 - 31: OOooOOo
   for o0O0OOO0Ooo in OO0O000 :
    i1OOO0000oO = o0O0OOO0Ooo [ 'program' ] [ 'code' ]
    OoO000O0Oo = o0O0OOO0Ooo [ 'program' ] [ 'name' ] [ 'ko' ]
    if 15 - 15: OoOoOO00 % I1IiiI * I11i
    Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    O0OoooO0 = 'CAIP0200' if landyn else 'CAIP0900'
    if 85 - 85: I11i
    for iI1i11II1i in o0O0OOO0Ooo [ 'program' ] [ 'image' ] :
     if iI1i11II1i [ 'code' ] == O0OoooO0 :
      Oo0o0oooo0O0 = self . IMG_DOMAIN + iI1i11II1i [ 'url' ]
      break
      if 96 - 96: I1Ii111
    OooooOOoo0 = o0O0OOO0Ooo [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    oOoOo0O0OOOoO = o0O0OOO0Ooo [ 'program' ] [ 'channel_code' ]
    if 50 - 50: ooOoO0o
    oO00oOOoooO = { }
    oO00oOOoooO [ 'title' ] = unicode ( OoO000O0Oo )
    oO00oOOoooO [ 'mediatype' ] = 'episode'
    try :
     I1II1 = [ ]
     for oooO in o0O0OOO0Ooo . get ( 'program' ) . get ( 'actor' ) : I1II1 . append ( oooO )
     if I1II1 [ 0 ] != '' and I1II1 [ 0 ] != '-' : oO00oOOoooO [ 'cast' ] = I1II1
    except :
     None
    try :
     IIIIiii1IIii = [ ]
     for II1i11I in o0O0OOO0Ooo . get ( 'program' ) . get ( 'director' ) : IIIIiii1IIii . append ( II1i11I )
     if IIIIiii1IIii [ 0 ] != '' and IIIIiii1IIii [ 0 ] != '-' : oO00oOOoooO [ 'director' ] = IIIIiii1IIii
    except :
     None
     if 50 - 50: OoooooooOO % I11i
    i1I1i111Ii = [ ]
    if o0O0OOO0Ooo . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
     i1I1i111Ii . append ( o0O0OOO0Ooo [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
    if o0O0OOO0Ooo . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
     i1I1i111Ii . append ( o0O0OOO0Ooo [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
    if i1I1i111Ii [ 0 ] != '' : oO00oOOoooO [ 'genre' ] = i1I1i111Ii
    if 49 - 49: oO0o - i11iIiiIii . I1Ii111 * Ii1I % iII111i + i1IIi
    try :
     if o0O0OOO0Ooo . get ( 'program' ) . get ( 'product_year' ) : oO00oOOoooO [ 'year' ] = o0O0OOO0Ooo [ 'program' ] [ 'product_year' ]
     if 'broad_dt' in o0O0OOO0Ooo . get ( 'program' ) :
      oOO0OOOo = o0O0OOO0Ooo . get ( 'program' ) . get ( 'broad_dt' )
      oO00oOOoooO [ 'aired' ] = '%s-%s-%s' % ( oOO0OOOo [ : 4 ] , oOO0OOOo [ 4 : 6 ] , oOO0OOOo [ 6 : ] )
    except :
     None
     if 56 - 56: o0oOOo0O0Ooo
     if 28 - 28: iII111i . iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
    IIIIIIii1 = { 'program' : i1OOO0000oO
 , 'title' : unicode ( OoO000O0Oo )
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : unicode ( OooooOOoo0 )
 , 'channel' : oOoOo0O0OOOoO
 , 'info' : oO00oOOoooO
 }
    if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
    O0oO . append ( IIIIIIii1 )
    if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
    if 79 - 79: O0 * i11iIiiIii - IiII / IiII
   if I111IIIiIii [ 'body' ] [ 'has_more' ] == 'Y' : OO0ooOOO0OOO = True
   if 48 - 48: O0
  except Exception as I1III :
   print ( I1III )
   if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
  return O0oO , OO0ooOOO0OOO
  if 25 - 25: IiII + Ii1I / ooOoO0o . o0oOOo0O0Ooo % O0 * OoO0O00
  if 84 - 84: ooOoO0o % Ii1I + i11iIiiIii
 def GetEpisodoList ( self , program_code , page_int , orderby = 'desc' ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 28 - 28: Oo0Ooo + OoO0O00 * OOooOOo % oO0o . I11i % O0
  try :
   O0oOO0O = '/v2/media/frequency/program/' + program_code
   if 16 - 16: I11i - iIii1I11I1II1 / I1IiiI . II111iiii + iIii1I11I1II1
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 19 - 19: OoO0O00 - Oo0Ooo . O0
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 60 - 60: II111iiii + Oo0Ooo
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 9 - 9: ooOoO0o * OoooooooOO - iIii1I11I1II1 + OoOoOO00 / OoO0O00 . OoO0O00
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 49 - 49: II111iiii
   if not ( 'result' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'result' ]
   if 25 - 25: OoooooooOO - I1IiiI . I1IiiI * oO0o
   o000oo = int ( I111IIIiIii [ 'body' ] [ 'total_count' ] )
   if 95 - 95: ooOoO0o / ooOoO0o
   IIiI1Ii = int ( o000oo // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if orderby == 'desc' :
    O0O0O0Oo = ( o000oo - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    O0O0O0Oo = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 70 - 70: OoO0O00 % oO0o + OOooOOo / Ii1I % O0
   for oO00O0 in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     IIi1IIIi = O0O0O0Oo - oO00O0
     if IIi1IIIi < 0 : break
    else :
     IIi1IIIi = O0O0O0Oo + oO00O0
     if IIi1IIIi >= o000oo : break
     if 99 - 99: Ii1I + OoO0O00 * II111iiii . o0oOOo0O0Ooo - I1ii11iIi11i
    o0OOOo = OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'code' ]
    OoO000O0Oo = OO0O000 [ IIi1IIIi ] [ 'vod_name' ] [ 'ko' ]
    ii1iiIiIII1ii = ''
    try :
     oOO0OOOo = str ( OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'broadcast_date' ] )
     ii1iiIiIII1ii = '%s-%s-%s' % ( oOO0OOOo [ : 4 ] , oOO0OOOo [ 4 : 6 ] , oOO0OOOo [ 6 : ] )
    except :
     None
    if OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'image' ] != [ ] :
     Oo0o0oooo0O0 = self . IMG_DOMAIN + OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     Oo0o0oooo0O0 = self . IMG_DOMAIN + OO0O000 [ IIi1IIIi ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    OooooOOoo0 = OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 82 - 82: iII111i
    oO00oOOoooO = { }
    oO00oOOoooO [ 'mediatype' ] = 'episode'
    try :
     oO00oOOoooO [ 'title' ] = unicode ( OO0O000 [ IIi1IIIi ] [ 'program' ] [ 'name' ] [ 'ko' ] )
     oO00oOOoooO [ 'aired' ] = ii1iiIiIII1ii
     oO00oOOoooO [ 'studio' ] = OO0O000 [ IIi1IIIi ] [ 'channel' ] [ 'name' ] [ 'ko' ]
     if 'frequency' in OO0O000 [ IIi1IIIi ] [ 'episode' ] : oO00oOOoooO [ 'episode' ] = OO0O000 [ IIi1IIIi ] [ 'episode' ] [ 'frequency' ]
    except :
     None
     if 65 - 65: ooOoO0o . OoooooooOO / I1ii11iIi11i . i1IIi * OoO0O00
    IIIIIIii1 = { 'episode' : o0OOOo
 , 'title' : unicode ( OoO000O0Oo )
 , 'subtitle' : ii1iiIiIII1ii
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : unicode ( OooooOOoo0 )
 , 'info' : oO00oOOoooO
 }
    if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - I11i
    O0oO . append ( IIIIIIii1 )
    if 21 - 21: O0 % IiII . I1IiiI / II111iiii + IiII
   if IIiI1Ii > page_int : OO0ooOOO0OOO = True
   if 53 - 53: oO0o - I1IiiI - oO0o * iII111i
  except Exception as I1III :
   print ( I1III )
   if 71 - 71: O0 - iIii1I11I1II1
  return O0oO , OO0ooOOO0OOO , IIiI1Ii
  if 12 - 12: OOooOOo / o0oOOo0O0Ooo
  if 42 - 42: Oo0Ooo
 def GetMovieList ( self , orderby , page_int , premiumyn = False , landyn = False ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 19 - 19: oO0o % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  if premiumyn == True :
   iii11I = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   iii11I = self . MOVIE_LITE
   if 50 - 50: iII111i + O0 + Ii1I . II111iiii / o0oOOo0O0Ooo
  try :
   O0oOO0O = '/v2/media/movies'
   if 17 - 17: Ii1I % iIii1I11I1II1 - iIii1I11I1II1
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : iii11I
   # Oo0Ooo % i11iIiiIii % o0oOOo0O0Ooo % iIii1I11I1II1 * iII111i
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 76 - 76: OoO0O00 * I1IiiI
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 82 - 82: Ii1I * iII111i / I1ii11iIi11i
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 36 - 36: OoooooooOO - i1IIi . O0 / II111iiii + o0oOOo0O0Ooo
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 33 - 33: II111iiii / ooOoO0o * O0 % Ii1I * I1Ii111
   if not ( 'result' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'result' ]
   if 100 - 100: IiII . I11i / Ii1I % OoOoOO00 % II111iiii - OoO0O00
   if 46 - 46: O0 * II111iiii - Oo0Ooo * ooOoO0o
   for o0O0OOO0Ooo in OO0O000 :
    i11IIIiIiIi = o0O0OOO0Ooo [ 'movie' ] [ 'code' ]
    OoO000O0Oo = o0O0OOO0Ooo [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( )
    OoO000O0Oo += u' (%s년)' % ( o0O0OOO0Ooo . get ( 'movie' ) . get ( 'product_year' ) )
    Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    O0OoooO0 = 'CAIM0400' if landyn else 'CAIM2100'
    if 27 - 27: I1ii11iIi11i + OoOoOO00 - OOooOOo + O0 . Ii1I
    for iI1i11II1i in o0O0OOO0Ooo [ 'movie' ] [ 'image' ] :
     if iI1i11II1i [ 'code' ] == O0OoooO0 :
      Oo0o0oooo0O0 = self . IMG_DOMAIN + iI1i11II1i [ 'url' ]
      break
      if 46 - 46: IiII
    OooooOOoo0 = o0O0OOO0Ooo [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 45 - 45: ooOoO0o
    oO00oOOoooO = { }
    oO00oOOoooO [ 'mediatype' ] = 'movie'
    oO00oOOoooO [ 'title' ] = unicode ( o0O0OOO0Ooo [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( ) )
    oO00oOOoooO [ 'year' ] = o0O0OOO0Ooo . get ( 'movie' ) . get ( 'product_year' )
    try :
     I1II1 = [ ]
     for oooO in o0O0OOO0Ooo . get ( 'movie' ) . get ( 'actor' ) : I1II1 . append ( oooO )
     if I1II1 [ 0 ] != '' : oO00oOOoooO [ 'cast' ] = I1II1
    except :
     None
    try :
     IIIIiii1IIii = [ ]
     for II1i11I in o0O0OOO0Ooo . get ( 'movie' ) . get ( 'director' ) : IIIIiii1IIii . append ( II1i11I )
     if IIIIiii1IIii [ 0 ] != '' : oO00oOOoooO [ 'director' ] = IIIIiii1IIii
    except :
     None
    try :
     i1I1i111Ii = [ ]
     if o0O0OOO0Ooo . get ( 'movie' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      i1I1i111Ii . append ( o0O0OOO0Ooo [ 'movie' ] [ 'category1_name' ] [ 'ko' ] )
     if o0O0OOO0Ooo . get ( 'movie' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      i1I1i111Ii . append ( o0O0OOO0Ooo [ 'movie' ] [ 'category2_name' ] [ 'ko' ] )
     if i1I1i111Ii [ 0 ] != '' : oO00oOOoooO [ 'genre' ] = i1I1i111Ii
    except :
     None
    try :
     if 'release_date' in o0O0OOO0Ooo . get ( 'movie' ) :
      oOO0OOOo = str ( o0O0OOO0Ooo . get ( 'movie' ) . get ( 'release_date' ) )
      oO00oOOoooO [ 'aired' ] = '%s-%s-%s' % ( oOO0OOOo [ : 4 ] , oOO0OOOo [ 4 : 6 ] , oOO0OOOo [ 6 : ] )
    except :
     None
    try :
     if 'duration' in o0O0OOO0Ooo . get ( 'movie' ) : oO00oOOoooO [ 'duration' ] = o0O0OOO0Ooo . get ( 'movie' ) . get ( 'duration' )
    except :
     None
     if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
     if 17 - 17: OOooOOo / OOooOOo / I11i
    IIIIIIii1 = { 'moviecode' : i11IIIiIiIi
 , 'title' : unicode ( OoO000O0Oo )
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : unicode ( OooooOOoo0 )
 , 'info' : oO00oOOoooO
 }
    if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
    if premiumyn == True :
     OooO0oo = False
     for o0o0oOoOO0O in o0O0OOO0Ooo [ 'billing_package_id' ] :
      if o0o0oOoOO0O == self . MOVIE_LITE :
       OooO0oo = True
       break
     if OooO0oo == False :
      IIIIIIii1 [ 'title' ] = unicode ( IIIIIIii1 [ 'title' ] + ' [Premium]' )
      if 16 - 16: IiII % iIii1I11I1II1 . Ii1I
    O0oO . append ( IIIIIIii1 )
    if 59 - 59: I1IiiI * II111iiii . O0
    if 56 - 56: Ii1I - iII111i % I1IiiI - o0oOOo0O0Ooo
   if I111IIIiIii [ 'body' ] [ 'has_more' ] == 'Y' : OO0ooOOO0OOO = True
   if 51 - 51: O0 / ooOoO0o * iIii1I11I1II1 + I1ii11iIi11i + o0oOOo0O0Ooo
  except Exception as I1III :
   print ( I1III )
   if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * OOooOOo + ooOoO0o % i11iIiiIii % O0
  return O0oO , OO0ooOOO0OOO
  if 27 - 27: O0
  if 79 - 79: o0oOOo0O0Ooo - I11i + o0oOOo0O0Ooo . oO0o
 def GetMovieListGenre ( self , genre , page_int , premiumyn = False ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 28 - 28: i1IIi - iII111i
  if premiumyn == True :
   iii11I = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   iii11I = self . MOVIE_LITE
   if 54 - 54: iII111i - O0 % OOooOOo
  try :
   O0oOO0O = '/v2/media/movie/curation/' + genre
   if 73 - 73: O0 . OoOoOO00 + I1IiiI - I11i % I11i . I11i
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'productPackageCode' : iii11I
   # ooOoO0o
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 53 - 53: OoooooooOO % Ii1I . IiII / i11iIiiIii % iII111i
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 28 - 28: I11i
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 58 - 58: OoOoOO00
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
   if not ( 'movies' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'movies' ]
   if 73 - 73: i11iIiiIii - IiII
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
   for o0O0OOO0Ooo in OO0O000 :
    i11IIIiIiIi = o0O0OOO0Ooo [ 'code' ]
    OoO000O0Oo = o0O0OOO0Ooo [ 'name' ] [ 'ko' ]
    Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'image' ] [ 0 ] [ 'url' ]
    for iI1i11II1i in o0O0OOO0Ooo [ 'image' ] :
     if iI1i11II1i [ 'code' ] == 'CAIM2100' :
      Oo0o0oooo0O0 = self . IMG_DOMAIN + iI1i11II1i [ 'url' ]
    OooooOOoo0 = o0O0OOO0Ooo [ 'story' ] [ 'ko' ]
    if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
    IIIIIIii1 = { 'moviecode' : i11IIIiIiIi
 , 'title' : unicode ( OoO000O0Oo . strip ( ) )
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : unicode ( OooooOOoo0 )
 }
    if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
    if premiumyn == True :
     OooO0oo = False
     for o0o0oOoOO0O in o0O0OOO0Ooo [ 'billing_package_id' ] :
      if o0o0oOoOO0O == self . MOVIE_LITE :
       OooO0oo = True
       break
     if OooO0oo == False :
      IIIIIIii1 [ 'title' ] = unicode ( IIIIIIii1 [ 'title' ] + ' [Premium]' )
      if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
    O0oO . append ( IIIIIIii1 )
    if 91 - 91: i11iIiiIii / i1IIi + iII111i + ooOoO0o * i11iIiiIii
    if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + I11i * I1Ii111 . IiII
    if 52 - 52: ooOoO0o + O0 . iII111i . I1ii11iIi11i . OoO0O00
    if 97 - 97: I1IiiI / iII111i
  except Exception as I1III :
   print ( I1III )
   if 71 - 71: II111iiii / i1IIi . I1ii11iIi11i % OoooooooOO . OoOoOO00
  return O0oO , OO0ooOOO0OOO
  if 41 - 41: i1IIi * II111iiii / OoooooooOO . OOooOOo
  if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
 def GetMovieGenre ( self ) :
  O0oO = [ ]
  OO0ooOOO0OOO = False
  if 100 - 100: OoO0O00
  try :
   O0oOO0O = '/v2/media/movie/curations'
   if 46 - 46: OoOoOO00 / iIii1I11I1II1 % iII111i . iIii1I11I1II1 * iII111i
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'movieViewType' : 'sma'
 , 'curationSection' : 'view0002'
   , 'order' : 'curation_code'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 38 - 38: I1ii11iIi11i - iII111i / O0 . I1Ii111
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO , oOOo0 )
   if 45 - 45: I1Ii111
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 83 - 83: OoOoOO00 . OoooooooOO
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
   if not ( 'result' in I111IIIiIii [ 'body' ] ) : return O0oO , OO0ooOOO0OOO
   OO0O000 = I111IIIiIii [ 'body' ] [ 'result' ]
   if 62 - 62: OoO0O00 / I1ii11iIi11i
   if 7 - 7: OoooooooOO . IiII
   for o0O0OOO0Ooo in OO0O000 :
    O000OOO0OOo = o0O0OOO0Ooo [ 'curation_code' ]
    i1i1I111iIi1 = o0O0OOO0Ooo [ 'curation_name' ]
    if 92 - 92: ooOoO0o
    IIIIIIii1 = { 'curation_code' : O000OOO0OOo
 , 'curation_name' : unicode ( i1i1I111iIi1 )
 }
    O0oO . append ( IIIIIIii1 )
    if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
    if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
    if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  except Exception as I1III :
   print ( I1III )
   if 92 - 92: I11i . I1Ii111
  return O0oO , OO0ooOOO0OOO
  if 85 - 85: I1ii11iIi11i . I1Ii111
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
 def GetSearchList ( self , search_key , userid , page_int , stype , premiumyn = False , landyn = False ) :
  O000 = [ ]
  OO0ooOOO0OOO = False
  if 79 - 79: OoooooooOO - I1IiiI
  try :
   O0oOO0O = '/search/getSearch.jsp'
   if 69 - 69: I11i
   oOOo0 = self . GetDefaultParams ( )
   oo00O00oO = { 'kwd' : search_key
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
   if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
   i11 = self . makeurl ( self . SEARCH_DOMAIN , O0oOO0O , oo00O00oO , None )
   if 75 - 75: OoooooooOO * IiII
   oo0Ooo0 = {
 'User-Agent' : i1I1ii1II1iII
 , 'Cookie' : '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO )
 }
   I111IIIiIii = self . SESSION . Request2 ( i11 , params = None , cookie = oo0Ooo0 )
   if 9 - 9: IiII - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   if 39 - 39: IiII * Oo0Ooo + iIii1I11I1II1 - IiII + OOooOOo
   if stype == 'vod' :
    if not ( 'programRsb' in I111IIIiIii ) : return O000 , OO0ooOOO0OOO
    if 69 - 69: O0
    o0ooO = I111IIIiIii [ 'programRsb' ] [ 'dataList' ]
    OoOOOo0o0ooo = int ( I111IIIiIii [ 'programRsb' ] [ 'count' ] )
    if 19 - 19: I11i % II111iiii / i11iIiiIii / iII111i - OoooooooOO
    if 37 - 37: OOooOOo / OoooooooOO - i11iIiiIii
    for o0O0OOO0Ooo in o0ooO :
     i1OOO0000oO = o0O0OOO0Ooo [ 'mast_cd' ]
     OoO000O0Oo = o0O0OOO0Ooo [ 'mast_nm' ]
     Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url' ]
     if landyn == False :
      Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url4' ]
      if 18 - 18: iII111i . I1IiiI
      if 40 - 40: O0 - OoooooooOO - IiII
      if 37 - 37: OoOoOO00 / II111iiii / O0
     oO00oOOoooO = { }
     oO00oOOoooO [ 'title' ] = o0O0OOO0Ooo [ 'mast_nm' ]
     oO00oOOoooO [ 'mediatype' ] = 'episode'
     if 76 - 76: I1IiiI . ooOoO0o - I1ii11iIi11i - iII111i * OoO0O00
     try :
      if o0O0OOO0Ooo . get ( 'actor' ) != '' and o0O0OOO0Ooo . get ( 'actor' ) != '-' : oO00oOOoooO [ 'cast' ] = o0O0OOO0Ooo . get ( 'actor' ) . split ( ',' )
      if o0O0OOO0Ooo . get ( 'director' ) != '' and o0O0OOO0Ooo . get ( 'director' ) != '-' : oO00oOOoooO [ 'director' ] = o0O0OOO0Ooo . get ( 'director' ) . split ( ',' )
      if o0O0OOO0Ooo . get ( 'cate_nm' ) != '' : oO00oOOoooO [ 'genre' ] = o0O0OOO0Ooo . get ( 'cate_nm' ) . split ( '/' )
      if 'targetage' in o0O0OOO0Ooo : oO00oOOoooO [ 'mpaa' ] = o0O0OOO0Ooo . get ( 'targetage' )
     except :
      None
     try :
      if 'broad_dt' in o0O0OOO0Ooo :
       oOO0OOOo = o0O0OOO0Ooo . get ( 'broad_dt' )
       oO00oOOoooO [ 'aired' ] = '%s-%s-%s' % ( oOO0OOOo [ : 4 ] , oOO0OOOo [ 4 : 6 ] , oOO0OOOo [ 6 : ] )
     except :
      None
      if 54 - 54: IiII + O0 + I11i * I1Ii111 - OOooOOo % oO0o
     IIIIIIii1 = { 'program' : i1OOO0000oO
 , 'title' : unicode ( OoO000O0Oo )
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : ''
     , 'info' : oO00oOOoooO
 }
     if 13 - 13: ooOoO0o / iII111i * OoO0O00 . OoO0O00 * ooOoO0o
     O000 . append ( IIIIIIii1 )
   else :
    if not ( 'vodMVRsb' in I111IIIiIii ) : return O000 , OO0ooOOO0OOO
    O00oOiI11I = I111IIIiIii [ 'vodMVRsb' ] [ 'dataList' ]
    OoOOOo0o0ooo = int ( I111IIIiIii [ 'vodMVRsb' ] [ 'count' ] )
    if 53 - 53: iIii1I11I1II1 + Ii1I - I1Ii111
    if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
    for o0O0OOO0Ooo in O00oOiI11I :
     i1OOO0000oO = o0O0OOO0Ooo [ 'mast_cd' ]
     OoO000O0Oo = o0O0OOO0Ooo [ 'mast_nm' ] . strip ( )
     Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url' ]
     if 61 - 61: II111iiii
     if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
     if landyn == False :
      Oo0o0oooo0O0 = self . IMG_DOMAIN + o0O0OOO0Ooo [ 'web_url5' ]
      if 90 - 90: iII111i
      if 31 - 31: OOooOOo + O0
      if 87 - 87: ooOoO0o
      if 45 - 45: OoO0O00 / OoooooooOO - iII111i / Ii1I % IiII
     oO00oOOoooO = { }
     oO00oOOoooO [ 'title' ] = unicode ( OoO000O0Oo )
     oO00oOOoooO [ 'mediatype' ] = 'movie'
     if 83 - 83: I1IiiI . iIii1I11I1II1 - IiII * i11iIiiIii
     try :
      if o0O0OOO0Ooo . get ( 'actor' ) != '' : oO00oOOoooO [ 'cast' ] = o0O0OOO0Ooo . get ( 'actor' ) . split ( ',' )
      if 20 - 20: i1IIi * I1Ii111 + II111iiii % o0oOOo0O0Ooo % oO0o
      if o0O0OOO0Ooo . get ( 'cate_nm' ) != '' : oO00oOOoooO [ 'genre' ] = o0O0OOO0Ooo . get ( 'cate_nm' ) . split ( '/' )
      if o0O0OOO0Ooo . get ( 'runtime_sec' ) != '' : oO00oOOoooO [ 'duration' ] = o0O0OOO0Ooo . get ( 'runtime_sec' )
      if 'grade_nm' in o0O0OOO0Ooo : oO00oOOoooO [ 'mpaa' ] = o0O0OOO0Ooo . get ( 'grade_nm' )
     except :
      None
     try :
      oOO0OOOo = o0O0OOO0Ooo . get ( 'broad_dt' )
      if data_str != '' :
       oO00oOOoooO [ 'aired' ] = '%s-%s-%s' % ( oOO0OOOo [ : 4 ] , oOO0OOOo [ 4 : 6 ] , oOO0OOOo [ 6 : ] )
       oO00oOOoooO [ 'year' ] = oOO0OOOo [ : 4 ]
     except :
      None
      if 13 - 13: Oo0Ooo
      if 60 - 60: I1ii11iIi11i * I1IiiI
      if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
     if True :
      IIIIIIii1 = { 'movie' : i1OOO0000oO
 , 'title' : unicode ( OoO000O0Oo )
 , 'thumbnail' : Oo0o0oooo0O0
 , 'synopsis' : ''
      , 'info' : oO00oOOoooO
 }
      if 41 - 41: Ii1I
      O000 . append ( IIIIIIii1 )
      if 77 - 77: I1Ii111
      if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
      if 38 - 38: OoOoOO00 / iII111i % Oo0Ooo
      if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
  except Exception as I1III :
   if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
   print ( I1III )
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
  return O000 , OO0ooOOO0OOO
  if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
 def GetDeviceList ( self , tving_token , poc_userinfo ) :
  O0oO = [ ]
  Oo00 = '-'
  if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
  try :
   O0oOO0O = '/v1/user/device/list'
   if 95 - 95: IiII
   if 51 - 51: II111iiii + IiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
   oo00O00oO = { 'apiKey' : '4263d7d76161f4a19a9efe9ca7903ec4'
 , 'model' : 'PC'
 }
   if 72 - 72: oO0o + oO0o / II111iiii . OoooooooOO % Ii1I
   i11 = self . makeurl ( self . API_DOMAIN , O0oOO0O , oo00O00oO )
   if 49 - 49: oO0o . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
   oo0Ooo0 = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , tving_token , 'POC_USERINFO' , poc_userinfo ) )
 ]
   if 2 - 2: OoooooooOO % OOooOOo
   I1I11I1I1I = self . SESSION . Request ( i11 , params = None , cookie = oo0Ooo0 )
   I111IIIiIii = json . loads ( I1I11I1I1I )
   if 63 - 63: I1IiiI % iIii1I11I1II1
   if 39 - 39: iII111i / II111iiii / I1ii11iIi11i % I1IiiI
   O0oO = I111IIIiIii [ 'body' ]
   if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
   for o0O0OOO0Ooo in O0oO :
    if o0O0OOO0Ooo [ 'model' ] == 'PC' :
     Oo00 = o0O0OOO0Ooo [ 'uuid' ]
     if 59 - 59: OOooOOo + i11iIiiIii
     if 88 - 88: i11iIiiIii - ooOoO0o
  except Exception as I1III :
   print ( I1III )
   if 67 - 67: OOooOOo . Oo0Ooo + OoOoOO00 - OoooooooOO
  return Oo00
  if 70 - 70: OOooOOo / II111iiii - iIii1I11I1II1 - iII111i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
