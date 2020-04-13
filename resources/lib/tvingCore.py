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
  iii11iII . append ( 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAATtklEQVR4Xu2be1hVdbrHvwvEDYKICuItMxUDFXVQQZuevIRp5uNRvIXXYcwNdp7H0eZkk9qZTlqaXbxMKWxSRxvTGkJOUz7HS+atFCVT8ZIpZAgqoiYgyBZhnee39l6bxWaLGBj+pi9/iXtd3vV53/XZ7+9dCwX8IQESIAFJCCiSxMkw65CAaoZah4eT5lCKBax3abLlOlAmUPIE/pLwKaxfQo37PAgEKKwHIQu/cgwU1q8MnKerMwIUVp2hlOdAFJY8uWKklQlUFdbk9d7wLPkEijrMsOmfYIldof3+XGIg3Mp3QVVmIdG8FdMtq7T/TzTPqBVc/bzACu24zj/mhJlQlRDHeVzFqSrxtY6jVhchx86/hrBy4YsoxGElPkIPZN8RzFZ0xVDM1D73xw3swNJqt68NYc6wakPvwdi3srBi43tAVXYAWOBCULs0GTgLq66u416EVSGrrY44K/YHSjzH4cMpRXUV2r/bce63sISsBuDPuAKfagV0FG0xHmZ8DIsmKSGvWRiHXXgHgSioc+wUVp0j/dUPWCEsJwlMO4Fm7iV4Q1HRpsTq7Xv1SrswT9ONhKSk/35LdFhBnVLfHDRwzVMHDoxpfvTYU5lms7lQRG9JTBBfp8vtV3IFihqJhLijdtElA9gCYKH98+9R7jYAVtMNvaszmYowdMj737QMzFia0AdJDiL2Dis21nwmvzAgdNPGhf2gqOOnzYw77xynj++VpE0D82Kq0HTuyowdmZB1udtL2j6KGg39M9FBKmqc/VhLAIxwdJc1Sdd0yxAAIx2dX+Xj2a7/g+m5qK6ztX1JuGYn9nXV5Ro70oovIn9XncwMTEQ8ntCuJhiXHMIQAklBT6zChppcqbaNfqxoHMJhtEOi70pkhl3CY6eBoIuVDyO2FT/i+Ic7APuC3PAt2qFj+TVEHy+osn2Ng7jDhhRWbQnW//4VwrIV9cdCArGxcU3UMvxJUfB1Qm+8qxXiIXQoBxaWWBtdW7d+6ZPOwtJuSNtNMsTR4YibVVGXaTel+LEtJTO1z8WPWHoCWdq+9hs2IPDHtaNGLYpUyrHjTsIqKWnUQcTg7f3z/omT/nJLUfGDHqcuWnH4Mk/MXd0V17RzVXRglc7nOL+r7lJcj7gHdanoslGVoS6XrcZ82vZd7hCf+MyZj+P3shh4uq91xKJvC7yiCb/M/VK17IycjfITy2u38kta16wqk7SYJ6/3HuZ16IY4xSewYDV+r3U24t/esGIFBlX6XV+yGUVWXdn+HY9hLL7FWQTgD75jMKm3BT7uxRh0vLKwimDCOJgxBCfwdKud2BMCPHEKePfiRKBDFnq334sRaUBAHTZaFFb9C6e2EVQIy170oaHbRvV77NNZRgnoJ4k9jCdKraZZ27bH9vLyvPFXY4c1deqssh9/DBu5Z9+kZ0RHFZuGFwAMzMt7ONTdvfR66W2vV1NS5izSRDdoTX9VwZn8n1tOKLnpHRDQ4tzuq3ntX9u6Pfbd4cPfLW3a9FK5/Zxf6SKy3+whosNSVbS0fBC/oU3r07uDH93X5OSp/rh4McjRzYk4UY44uCE+IQx7tGMZbupps6eXiq7MWuIdIjpHrSPbtGCZEPbAgWuWBAWl9igr8/C4crndaHeP0t3JQ7PGmQ9hifWWd0Te5fZ9GzYsSgpscU6wS64k1cpdUsXcD8D4bYHPZV8MfvPrfRMnCHGI4ykKQrTYVBS6AfNX9UGmLlw9tub+WYfLyzy+/PAfb0bfiV3m2fC3d+7+w7qoqNfT/ZtnnRNsoCorUe4WFRs3faLGqw/mCC7ii6hxln9UHnwQXp6FwuM9sffi7zVhbY2w4qKfjbxnKRzCEN3PwYDGeCX1Ve2zmsyZ4iMa40u/1hhQmANPzxuajIwdli6smdiJoogT2nGjUoVhB+GUqRkeD09CSA4QllnbEq/Yn8KqO5b1daQqwho5csnLgS0yxlW62Y3R2WdYzh3WsxPmef50rvv4/fvHeXUP3YEmfrk4eHAkrFZvREQkr+0asssvOWVe9wD/cwuF6FQ3FHy86bVzpbc8B0VHzzuvAgVrVr/fuSYdln4D6l1f3tV2DZKT54213fzKFpczLHs3M6D/6tjOIanzUY4CS0LiO14++Z9FjVyYVaZ63BDLTE1YnVKfuXnT7+iH/3hTdIjPx06PexIqep/5od8yXQwB/lleULHOIaw7zOB0cecXBlzRl7HieKqCznoHKLYRv0PFW+fPd/vs2rXWXVJTR4uruTImauE6X7/Lwdu2xYbqXxLO7NzdS69aLJbGPbpv69C3b9LVz7fMOpuT3SVg2izzPG25XI4duXkdb1utXutPn36scWZmLww3pWFM+BqUwh3LD74At84ZCPTLxoKDPyHCegE7QoFcP2DkQcDbCm3Jtj8IQKkHktJisKxgS7XD8Y9CmmJRZhyWNPsAF0Ly7iisONN2FIR/j8DrQGS6XVhohcERtmWokFhd/VBYdUWy/o5TZUn4zLDlH7RtczJM/8avElo1wjqf1W1EUVHTKRHhyWPghrWO7gbA1H2N3ktPjxxbWOj/khCW1p0kJrQWS8g/xszcq7iVBW3c+PpD3o1/ttxtSagLS8Smdw2Kgoa3b3uYLlx8tO+1q61fS31u29uVYrcLa8rk/9ro5VUwTLu+hMQiMRsaOHDN6rZtTo39aldM16CgA692DkqNzL3c8ZOUlDkvPtTu2MtPP/3+BG2JmpC4VyzNIsI/Xd2jx7Z+CrDRVYdl8rwxTJvDtcwQy1Fbl2hfcvfsufXPEX2SxfCmcndWsdy0CbdRcSe943uk/ZHhxq7WmV0DU0n7zZtf3lF6y2vxyBGLTx5MG9Xm5In+c2NnmG/esno+v3nz3N7Xrwd2BKB1fcvNg1Sx1PvP0FX42e+2JqXdnRvgI79gJB38Ix6xFlYZfIsBeSRmw79VBmK6rUUT3KyyzDPy1gfqS1v9rVphRZqOoEX4Xkc3pc+1RoduQEEjCqv+1PBgnrnK0D2i76e5Pbtv9awkLOOTQVU54mroLpaEZzP6RN8uNS3SbmYFDY2XLGTy3XdP96ipsFK/GfPI0fTBXzieAhqG7tnZIcO++GK21bmTmrLHd1J+fsA7nl5FeU2aXtpXaYZlXxJOnvTSRi/v6621z1bEPySkICTSretO867dU3+nC6uwoNm6jzYunhkUdOCfYgmrCTghPl/Mg4I6pb7okK7xwQAAfUl39MiQhqmpUTGOGZadoZBdz57bwip1sPpQXVGf1x5QAHj2q4C1Nwr8x4globv77UJjh+VKWPu/Gb0sPf2pzUOHvpdXXNSkw57dU3uJ5WDelXZ9kz+d762zEl2pT0ZgRq6HF3ohC82LyzVhFZuAz3oD+R4N8HV5Z0QdL8bEi+e0eZZ47cB5hpXnC2wJg8thuoj/bsIS22hyMlkdy79HM21zLbFMdA89QWE9mM6o16iqvNYg5kJ9I5Iy/Fucn611SBWysg3LTVafOz0lzMkJCTt6bHDQU4MTvvUwWZclrEw87Xhny0l0d+uwtBv+wOjASgN6Rd0aa45toA/doSq2Vy30H7uUBvX/+9SgzvtnVepi7Eu2xx/f6Nel21fpP5yKWLhr97QEMeieYTa/VVjst9QoLE0o8Qk9/fxyZ44a9UZaQ1PJyoRVlmjxxDCoU2rMnYQlQjE+Yb2QE3zhX5+/UK4/lGj/8JHoyEjLeXePsvcSVlm8tIcSZe5j4V72T/H00Ww2P1lW5tEzMzOsz/4D48v69ft4Tk06LE3Ayyyvd+iYFhcSvO9CI5/8MU2b5kw9e7rvlZ27YkbrTIqKm3Y4diwyom16S63D2usXiOMHh2GTdb02dP+XKRiJ4T4Y0OgIiku9kZM2AKsK/teB+EwrYGc326/Og/R76bB0qU0yTcb08BXocr0IZekVrzV8HWGbtnNJWK9+eOBOXuXF0dC/jQ72b569/+rVdn7H0iP1gLWlhPh2tpaa3t73TXS4Wu4239VrDSmb57YJ7b5jwo/nekLMSqA/UXNaSrrqEsRMq6TEZ9GgQWtOBjTPWrT+w7ejI/omDbtZ3ATHjg3WXgrV5j1iiLxi/f9E9N9wqKHpZog+K9PnV9P+MsUkZjcZZ8IDv/zyuYaOTmzyeu8uvbbuadXyTNihtBEoyG9hO+ZhPFF8w/dl45JQ74C8Zy9eExa2JSYnJ1hcj3it4XGxhBRzripLQhfp1WdYqopTYvDdYu7cDQY+Fa99TLcM8W1y+f/Cwr7AmTN983OyQ8YLmXXrunN7eHhK27stCe3C6iOOIb4wmvmfT1ZUBLmpWLDKYnlRiKxNm+/xbdrw7etvbhoch4l4J3QBVL9CbRn4ubW3Fr3+8mZr32yt4/rdOdvgW59hGYfx1VWzqw4r82LV96xEB/fXiDbaoTJSh2gD/U6mbKSEg0P3B04X9R+Qyz/NMcyFqrzWIAa+4uZoWAw/8ZqD3sWIp17icrSnUeIJoYre+rJSH46Lbd2Aw8b9xD760FkcV/yuD4rFfMjlZ/bXGPTjqkC2OK+OM/YQxogv58u5Hd/Y/Nmc/8BNr2X6i6SO1x7E0L0P5jj/7uoJo3499qH70mej5//QpHGef6Wh+11yKWJSgXCdT6Whuz1eBbCogFlnarg+k+KO5W5lyK6Onf4Kh/4EUlWQ4xjs288hcrIyERm6gPyKbYP1/Z2rDtm/a297UnjeHzgX8Mu6HdGR6a8sOL+HpSNz3kbEpp+brzXUvyQepAju+LeEDskoaGwI2PGagVFCQixGYYntKz22F/9hf6LmvJ+zsMRNZ+xKyhphsf5iqHYYe6eix2Rcfun/57hRl1n6QFEfFctIoyCc9zEeUxeWPsOCompv04vryc9vOUy8htE84Pwajwa3Wjo/WLiXxBr5qCpuCSGJJbgmWwVT7dd6S3RxQr5QkOamIqUmwjIco+K1EENOQn/CcCGqDrnAsYdtS7vW16B1Ndcb2a6iQXn1S76aXqsrYbkSkuMpZB2e2zlGPiWsadYe3O1+E3/8bBdUXJkn4h0vktYkJ05viOtLzhkzpwSWK3ilNsKqyenv1zb3+09z7lfctT0uhVVbgvW//29CWPaOo53jJdR74G7oxhxv0xuXqfckwHs47/3clMK6n3R57PtJ4DchrNoCNL7rpS3VDLOh2h67PvansOqDOs9ZFwQorLqgKNkxKCzJEsZwHQQoLBYDCZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAQoLGlSxUBJgAQoLNYACZCANAT+H9FJng/hy/8wAAAAAElFTkSuQmCC' )
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
    Iii1iI = { }
    Iii1iI [ 'mediatype' ] = 'video'
    if 29 - 29: I1IiiI % OOooOOo - I1IiiI / OOooOOo . i1IIi
    i11III1111iIi = I1i111I = Ooo = Oo0oo0O0o00O = ''
    I1i11 = IiIi1I1 = ''
    if 39 - 39: II111iiii + OoOoOO00 - ooOoO0o . OoOoOO00
    OOOooo = oO0o0 [ 'live_code' ]
    i11III1111iIi = oO0o0 [ 'schedule' ] [ 'channel' ] [ 'name' ] [ 'ko' ]
    if 94 - 94: OoooooooOO + Oo0Ooo / OoOoOO00 * OOooOOo
    if oO0o0 [ 'schedule' ] [ 'episode' ] != None :
     I1i111I = oO0o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     I1i111I = I1i111I + ', ' + str ( oO0o0 [ 'schedule' ] [ 'episode' ] [ 'frequency' ] ) + '회'
     if oO0o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] != [ ] :
      Ooo = oO0o0 [ 'schedule' ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
     Oo0oo0O0o00O = oO0o0 [ 'schedule' ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    else :
     I1i111I = oO0o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
     if oO0o0 [ 'schedule' ] [ 'program' ] [ 'image' ] != [ ] :
      Ooo = oO0o0 [ 'schedule' ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
     Oo0oo0O0o00O = oO0o0 [ 'schedule' ] [ 'program' ] [ 'synopsis' ] [ 'ko' ]
     if 69 - 69: ooOoO0o % oO0o
     if 50 - 50: OoooooooOO % I11i
    Iii1iI [ 'title' ] = oO0o0 [ 'schedule' ] [ 'program' ] [ 'name' ] [ 'ko' ]
    Iii1iI [ 'studio' ] = i11III1111iIi
    try :
     IIii1111 = [ ]
     for I1iI in oO0o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'actor' ) : IIii1111 . append ( I1iI )
     if IIii1111 [ 0 ] != '' and IIii1111 [ 0 ] != u'없음' : Iii1iI [ 'cast' ] = IIii1111
    except :
     None
    try :
     IIIIiIiIi1 = [ ]
     if oO0o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      IIIIiIiIi1 . append ( oO0o0 [ 'schedule' ] [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
     if oO0o0 . get ( 'schedule' ) . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      IIIIiIiIi1 . append ( oO0o0 [ 'schedule' ] [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
     if IIIIiIiIi1 [ 0 ] != '' : Iii1iI [ 'genre' ] = IIIIiIiIi1
    except :
     None
     if 2 - 2: iII111i % iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / iII111i
     if 27 - 27: OoO0O00 + ooOoO0o - i1IIi
     if 69 - 69: IiII - O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoO0O00
     if 79 - 79: O0 * i11iIiiIii - IiII / IiII
    if Ooo == '' :
     Ooo = oO0o0 [ 'schedule' ] [ 'channel' ] [ 'image' ] [ 0 ] [ 'url' ]
    if Ooo != '' : Ooo = self . IMG_DOMAIN + Ooo
    if 48 - 48: O0
    I1i11 = str ( oO0o0 [ 'schedule' ] [ 'broadcast_start_time' ] ) [ 8 : 12 ]
    IiIi1I1 = str ( oO0o0 [ 'schedule' ] [ 'broadcast_end_time' ] ) [ 8 : 12 ]
    if 93 - 93: i11iIiiIii - I1IiiI * I1ii11iIi11i * I11i % O0 + OoooooooOO
    I1i1i1 = { 'channel' : unicode ( i11III1111iIi )
 , 'title' : unicode ( I1i111I )
 , 'mediacode' : OOOooo
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'channelepg' : ' [%s:%s ~ %s:%s]' % ( I1i11 [ 0 : 2 ] , I1i11 [ 2 : ] , IiIi1I1 [ 0 : 2 ] , IiIi1I1 [ 2 : ] )
 , 'info' : Iii1iI
 }
    if 73 - 73: O0 * iII111i + Ii1I + ooOoO0o
    o0oooOO00 . append ( I1i1i1 )
    if 40 - 40: II111iiii . OoOoOO00 * I1Ii111 + OOooOOo + OOooOOo
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 9 - 9: I11i % OoooooooOO . oO0o % I11i
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 32 - 32: i11iIiiIii
  return o0oooOO00 , iiIiii1IIIII
  if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
  if 41 - 41: Oo0Ooo
 def GetProgramList ( self , stype , orderby , page_int , landyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 10 - 10: Oo0Ooo / Oo0Ooo / I1Ii111 . I1Ii111
  try :
   O0O = '/v2/media/episodes'
   if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
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
   if 43 - 43: II111iiii . oO0o / I1ii11iIi11i
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 20 - 20: I1IiiI
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 95 - 95: iII111i - I1IiiI
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 34 - 34: ooOoO0o * I1IiiI . i1IIi * ooOoO0o / ooOoO0o
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
   if 55 - 55: ooOoO0o - I11i + II111iiii + iII111i % Ii1I
   for oO0o0 in ii :
    iiI11i1II = oO0o0 [ 'program' ] [ 'code' ]
    I1i111I = oO0o0 [ 'program' ] [ 'name' ] [ 'ko' ]
    if 51 - 51: o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * O0 - OOooOOo % Oo0Ooo
    Ooo = self . IMG_DOMAIN + oO0o0 [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    o0O00OooOOOOO = 'CAIP0200' if landyn else 'CAIP0900'
    if 40 - 40: o0oOOo0O0Ooo - i11iIiiIii + OoO0O00 . iIii1I11I1II1 * I1Ii111
    for iiIII1i in oO0o0 [ 'program' ] [ 'image' ] :
     if iiIII1i [ 'code' ] == o0O00OooOOOOO :
      Ooo = self . IMG_DOMAIN + iiIII1i [ 'url' ]
      break
      if 31 - 31: iII111i . OOooOOo - ooOoO0o . OoooooooOO / OoooooooOO
    Oo0oo0O0o00O = oO0o0 [ 'program' ] [ 'synopsis' ] [ 'ko' ]
    OOoO = oO0o0 [ 'program' ] [ 'channel_code' ]
    if 44 - 44: oO0o
    Iii1iI = { }
    Iii1iI [ 'title' ] = unicode ( I1i111I )
    Iii1iI [ 'mediatype' ] = 'episode'
    try :
     IIii1111 = [ ]
     for I1iI in oO0o0 . get ( 'program' ) . get ( 'actor' ) : IIii1111 . append ( I1iI )
     if IIii1111 [ 0 ] != '' and IIii1111 [ 0 ] != '-' : Iii1iI [ 'cast' ] = IIii1111
    except :
     None
    try :
     I1i11i = [ ]
     for IiIi in oO0o0 . get ( 'program' ) . get ( 'director' ) : I1i11i . append ( IiIi )
     if I1i11i [ 0 ] != '' and I1i11i [ 0 ] != '-' : Iii1iI [ 'director' ] = I1i11i
    except :
     None
     if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - iII111i + oO0o
    IIIIiIiIi1 = [ ]
    if oO0o0 . get ( 'program' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
     IIIIiIiIi1 . append ( oO0o0 [ 'program' ] [ 'category1_name' ] [ 'ko' ] )
    if oO0o0 . get ( 'program' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
     IIIIiIiIi1 . append ( oO0o0 [ 'program' ] [ 'category2_name' ] [ 'ko' ] )
    if IIIIiIiIi1 [ 0 ] != '' : Iii1iI [ 'genre' ] = IIIIiIiIi1
    if 82 - 82: oO0o / iIii1I11I1II1 . I1IiiI . OOooOOo / o0oOOo0O0Ooo
    try :
     if oO0o0 . get ( 'program' ) . get ( 'product_year' ) : Iii1iI [ 'year' ] = oO0o0 [ 'program' ] [ 'product_year' ]
     if 'broad_dt' in oO0o0 . get ( 'program' ) :
      iiI1I1 = oO0o0 . get ( 'program' ) . get ( 'broad_dt' )
      Iii1iI [ 'aired' ] = '%s-%s-%s' % ( iiI1I1 [ : 4 ] , iiI1I1 [ 4 : 6 ] , iiI1I1 [ 6 : ] )
    except :
     None
     if 56 - 56: I1IiiI . O0 + Oo0Ooo
     if 1 - 1: iII111i
    I1i1i1 = { 'program' : iiI11i1II
 , 'title' : unicode ( I1i111I )
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'channel' : OOoO
 , 'info' : Iii1iI
 }
    if 97 - 97: OOooOOo + iII111i + O0 + i11iIiiIii
    o0oooOO00 . append ( I1i1i1 )
    if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
    if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . iII111i % iII111i + i11iIiiIii
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 72 - 72: iIii1I11I1II1 * Ii1I % ooOoO0o / OoO0O00
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 35 - 35: ooOoO0o + i1IIi % I1ii11iIi11i % I11i + oO0o
  return o0oooOO00 , iiIiii1IIIII
  if 17 - 17: i1IIi
  if 21 - 21: Oo0Ooo
 def GetEpisodoList ( self , program_code , page_int , orderby = 'desc' ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 29 - 29: I11i / II111iiii / ooOoO0o * OOooOOo
  if 10 - 10: I1Ii111 % IiII * IiII . I11i / Ii1I % OOooOOo
  if 49 - 49: OoO0O00 / oO0o + O0 * o0oOOo0O0Ooo
  if 28 - 28: ooOoO0o + i11iIiiIii / I11i % OoOoOO00 % Oo0Ooo - O0
  if 54 - 54: i1IIi + II111iiii
  if 83 - 83: I1ii11iIi11i - I1IiiI + OOooOOo
  if 5 - 5: Ii1I
  try :
   O0O = '/v2/media/frequency/program/' + program_code
   if 46 - 46: IiII
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'order' : 'new'
 , 'free' : 'all'
 , 'adult' : 'all'
 , 'scope' : 'all'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 45 - 45: ooOoO0o
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 21 - 21: oO0o . I1Ii111 . OOooOOo / Oo0Ooo / I1Ii111
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 17 - 17: OOooOOo / OOooOOo / I11i
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 1 - 1: i1IIi . i11iIiiIii % OOooOOo
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 82 - 82: iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % IiII / Ii1I . Ii1I
   IIi = int ( OOOO0oo0 [ 'body' ] [ 'total_count' ] )
   if 66 - 66: oO0o % OoO0O00 . OOooOOo
   o0O = int ( IIi // ( self . EPISODE_LIMIT + 1 ) ) + 1
   if orderby == 'desc' :
    IiiiI = ( IIi - 1 ) - ( ( page_int - 1 ) * self . EPISODE_LIMIT )
   else :
    IiiiI = ( page_int - 1 ) * self . EPISODE_LIMIT
    if 61 - 61: OOooOOo % OOooOOo * o0oOOo0O0Ooo / o0oOOo0O0Ooo
   for o0 in range ( self . EPISODE_LIMIT ) :
    if orderby == 'desc' :
     oOO = IiiiI - o0
     if oOO < 0 : break
    else :
     oOO = IiiiI + o0
     if oOO >= IIi : break
     if 53 - 53: I1Ii111 * IiII . Oo0Ooo - Ii1I % Ii1I * i11iIiiIii
    iiOOO0oOOoo = ii [ oOO ] [ 'episode' ] [ 'code' ]
    I1i111I = ii [ oOO ] [ 'vod_name' ] [ 'ko' ]
    oOOO00o000o = ''
    try :
     iiI1I1 = str ( ii [ oOO ] [ 'episode' ] [ 'broadcast_date' ] )
     oOOO00o000o = '%s-%s-%s' % ( iiI1I1 [ : 4 ] , iiI1I1 [ 4 : 6 ] , iiI1I1 [ 6 : ] )
    except :
     None
    if ii [ oOO ] [ 'episode' ] [ 'image' ] != [ ] :
     Ooo = self . IMG_DOMAIN + ii [ oOO ] [ 'episode' ] [ 'image' ] [ 0 ] [ 'url' ]
    else :
     Ooo = self . IMG_DOMAIN + ii [ oOO ] [ 'program' ] [ 'image' ] [ 0 ] [ 'url' ]
    Oo0oo0O0o00O = ii [ oOO ] [ 'episode' ] [ 'synopsis' ] [ 'ko' ]
    if 9 - 9: oO0o + I11i / I11i
    Iii1iI = { }
    Iii1iI [ 'mediatype' ] = 'episode'
    try :
     Iii1iI [ 'title' ] = unicode ( ii [ oOO ] [ 'program' ] [ 'name' ] [ 'ko' ] )
     Iii1iI [ 'aired' ] = oOOO00o000o
     Iii1iI [ 'studio' ] = ii [ oOO ] [ 'channel' ] [ 'name' ] [ 'ko' ]
     if 'frequency' in ii [ oOO ] [ 'episode' ] : Iii1iI [ 'episode' ] = ii [ oOO ] [ 'episode' ] [ 'frequency' ]
    except :
     None
     if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * I11i % iIii1I11I1II1 / Ii1I
    I1i1i1 = { 'episode' : iiOOO0oOOoo
 , 'title' : unicode ( I1i111I )
 , 'subtitle' : oOOO00o000o
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'info' : Iii1iI
 }
    if 27 - 27: i11iIiiIii % II111iiii % I11i . O0 - Oo0Ooo + OoOoOO00
    o0oooOO00 . append ( I1i1i1 )
    if 57 - 57: iIii1I11I1II1 / I11i - i1IIi
   if o0O > page_int : iiIiii1IIIII = True
   if 51 - 51: IiII
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 25 - 25: OoooooooOO + IiII * I1ii11iIi11i
  return o0oooOO00 , iiIiii1IIIII , o0O
  if 92 - 92: I1IiiI + I11i + O0 / o0oOOo0O0Ooo + I1Ii111
  if 18 - 18: ooOoO0o * OoOoOO00 . iII111i / I1ii11iIi11i / i11iIiiIii
 def GetMovieList ( self , orderby , page_int , premiumyn = False , landyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 21 - 21: oO0o / I1ii11iIi11i + Ii1I + OoooooooOO
  if premiumyn == True :
   OoOo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   OoOo = self . MOVIE_LITE
   if 35 - 35: ooOoO0o * OOooOOo . I11i * o0oOOo0O0Ooo . OoOoOO00 / O0
  try :
   O0O = '/v2/media/movies'
   if 100 - 100: I1Ii111 . o0oOOo0O0Ooo * Oo0Ooo % O0 * O0
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'order' : orderby
   , 'free' : 'all'
 , 'adult' : 'all'
 , 'guest' : 'all'
 , 'scope' : 'all'
 , 'productPackageCode' : OoOo
   # iII111i
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 8 - 8: ooOoO0o + II111iiii / iII111i / I11i
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 74 - 74: O0 / i1IIi
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 78 - 78: OoooooooOO . OoO0O00 + ooOoO0o - i1IIi
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 31 - 31: OoooooooOO . OOooOOo
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 83 - 83: iII111i . O0 / Oo0Ooo / OOooOOo - II111iiii
   if 100 - 100: OoO0O00
   for oO0o0 in ii :
    II1i = oO0o0 [ 'movie' ] [ 'code' ]
    I1i111I = oO0o0 [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( )
    I1i111I += u' (%s년)' % ( oO0o0 . get ( 'movie' ) . get ( 'product_year' ) )
    Ooo = self . IMG_DOMAIN + oO0o0 [ 'movie' ] [ 'image' ] [ 0 ] [ 'url' ]
    o0O00OooOOOOO = 'CAIM0400' if landyn else 'CAIM2100'
    if 2 - 2: iIii1I11I1II1 * Oo0Ooo % oO0o - II111iiii - iII111i
    for iiIII1i in oO0o0 [ 'movie' ] [ 'image' ] :
     if iiIII1i [ 'code' ] == o0O00OooOOOOO :
      Ooo = self . IMG_DOMAIN + iiIII1i [ 'url' ]
      break
      if 3 - 3: I1Ii111
    Oo0oo0O0o00O = oO0o0 [ 'movie' ] [ 'story' ] [ 'ko' ]
    if 45 - 45: I1Ii111
    Iii1iI = { }
    Iii1iI [ 'mediatype' ] = 'movie'
    Iii1iI [ 'title' ] = unicode ( oO0o0 [ 'movie' ] [ 'name' ] [ 'ko' ] . strip ( ) )
    Iii1iI [ 'year' ] = oO0o0 . get ( 'movie' ) . get ( 'product_year' )
    try :
     IIii1111 = [ ]
     for I1iI in oO0o0 . get ( 'movie' ) . get ( 'actor' ) : IIii1111 . append ( I1iI )
     if IIii1111 [ 0 ] != '' : Iii1iI [ 'cast' ] = IIii1111
    except :
     None
    try :
     I1i11i = [ ]
     for IiIi in oO0o0 . get ( 'movie' ) . get ( 'director' ) : I1i11i . append ( IiIi )
     if I1i11i [ 0 ] != '' : Iii1iI [ 'director' ] = I1i11i
    except :
     None
    try :
     IIIIiIiIi1 = [ ]
     if oO0o0 . get ( 'movie' ) . get ( 'category1_name' ) . get ( 'ko' ) != '' :
      IIIIiIiIi1 . append ( oO0o0 [ 'movie' ] [ 'category1_name' ] [ 'ko' ] )
     if oO0o0 . get ( 'movie' ) . get ( 'category2_name' ) . get ( 'ko' ) != '' :
      IIIIiIiIi1 . append ( oO0o0 [ 'movie' ] [ 'category2_name' ] [ 'ko' ] )
     if IIIIiIiIi1 [ 0 ] != '' : Iii1iI [ 'genre' ] = IIIIiIiIi1
    except :
     None
    try :
     if 'release_date' in oO0o0 . get ( 'movie' ) :
      iiI1I1 = str ( oO0o0 . get ( 'movie' ) . get ( 'release_date' ) )
      Iii1iI [ 'aired' ] = '%s-%s-%s' % ( iiI1I1 [ : 4 ] , iiI1I1 [ 4 : 6 ] , iiI1I1 [ 6 : ] )
    except :
     None
    try :
     if 'duration' in oO0o0 . get ( 'movie' ) : Iii1iI [ 'duration' ] = oO0o0 . get ( 'movie' ) . get ( 'duration' )
    except :
     None
     if 83 - 83: OoOoOO00 . OoooooooOO
     if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / IiII / i11iIiiIii
    I1i1i1 = { 'moviecode' : II1i
 , 'title' : unicode ( I1i111I )
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'info' : Iii1iI
 }
    if 62 - 62: OoO0O00 / I1ii11iIi11i
    if premiumyn == True :
     ii1O000OOO0OOo = False
     for i1i1I111iIi1 in oO0o0 [ 'billing_package_id' ] :
      if i1i1I111iIi1 == self . MOVIE_LITE :
       ii1O000OOO0OOo = True
       break
     if ii1O000OOO0OOo == False :
      I1i1i1 [ 'title' ] = unicode ( I1i1i1 [ 'title' ] + ' [Premium]' )
      if 92 - 92: ooOoO0o
    o0oooOO00 . append ( I1i1i1 )
    if 22 - 22: Oo0Ooo % iII111i * I1ii11iIi11i / OOooOOo % i11iIiiIii * I11i
    if 95 - 95: OoooooooOO - IiII * I1IiiI + OoOoOO00
   if OOOO0oo0 [ 'body' ] [ 'has_more' ] == 'Y' : iiIiii1IIIII = True
   if 10 - 10: o0oOOo0O0Ooo / i11iIiiIii
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 92 - 92: I11i . I1Ii111
  return o0oooOO00 , iiIiii1IIIII
  if 85 - 85: I1ii11iIi11i . I1Ii111
  if 78 - 78: ooOoO0o * I1Ii111 + iIii1I11I1II1 + iIii1I11I1II1 / I1Ii111 . Ii1I
 def GetMovieListGenre ( self , genre , page_int , premiumyn = False ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 97 - 97: ooOoO0o / I1Ii111 % i1IIi % I1ii11iIi11i
  if premiumyn == True :
   OoOo = self . MOVIE_LITE + ',' + self . MOVIE_PREMIUM
  else :
   OoOo = self . MOVIE_LITE
   if 18 - 18: iIii1I11I1II1 % I11i
  try :
   O0O = '/v2/media/movie/curation/' + genre
   if 95 - 95: ooOoO0o + i11iIiiIii * I1Ii111 - i1IIi * I1Ii111 - iIii1I11I1II1
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : str ( page_int )
 , 'pageSize' : str ( self . MOVIE_LIMIT )
 , 'productPackageCode' : OoOo
   # ooOoO0o / IiII / I11i . IiII - OoO0O00
   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 27 - 27: II111iiii . iIii1I11I1II1
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 1 - 1: ooOoO0o % OoOoOO00 * Oo0Ooo
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 55 - 55: OoOoOO00
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 87 - 87: OoooooooOO % iII111i . I1IiiI / ooOoO0o
   if not ( 'movies' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'movies' ]
   if 8 - 8: I11i + o0oOOo0O0Ooo
   if 90 - 90: I1ii11iIi11i
   for oO0o0 in ii :
    II1i = oO0o0 [ 'code' ]
    I1i111I = oO0o0 [ 'name' ] [ 'ko' ]
    Ooo = self . IMG_DOMAIN + oO0o0 [ 'image' ] [ 0 ] [ 'url' ]
    for iiIII1i in oO0o0 [ 'image' ] :
     if iiIII1i [ 'code' ] == 'CAIM2100' :
      Ooo = self . IMG_DOMAIN + iiIII1i [ 'url' ]
    Oo0oo0O0o00O = oO0o0 [ 'story' ] [ 'ko' ]
    if 62 - 62: I1Ii111 . IiII . OoooooooOO
    I1i1i1 = { 'moviecode' : II1i
 , 'title' : unicode ( I1i111I . strip ( ) )
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 }
    if 11 - 11: OOooOOo / I11i
    if premiumyn == True :
     ii1O000OOO0OOo = False
     for i1i1I111iIi1 in oO0o0 [ 'billing_package_id' ] :
      if i1i1I111iIi1 == self . MOVIE_LITE :
       ii1O000OOO0OOo = True
       break
     if ii1O000OOO0OOo == False :
      I1i1i1 [ 'title' ] = unicode ( I1i1i1 [ 'title' ] + ' [Premium]' )
      if 73 - 73: i1IIi / i11iIiiIii
    o0oooOO00 . append ( I1i1i1 )
    if 58 - 58: Oo0Ooo . II111iiii + oO0o - i11iIiiIii / II111iiii / O0
    if 85 - 85: OoOoOO00 + OOooOOo
    if 10 - 10: IiII / OoO0O00 + OoOoOO00 / i1IIi
    if 27 - 27: Ii1I
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 67 - 67: I1IiiI
  return o0oooOO00 , iiIiii1IIIII
  if 55 - 55: I1ii11iIi11i - iII111i * o0oOOo0O0Ooo + OoOoOO00 * OoOoOO00 * O0
  if 91 - 91: I1Ii111 - OOooOOo % iIii1I11I1II1 - OoooooooOO % ooOoO0o
 def GetMovieGenre ( self ) :
  o0oooOO00 = [ ]
  iiIiii1IIIII = False
  if 98 - 98: OoO0O00 . OoO0O00 * oO0o * II111iiii * I1Ii111
  try :
   O0O = '/v2/media/movie/curations'
   if 92 - 92: Oo0Ooo
   OOooooO0Oo = self . GetDefaultParams ( )
   OO = { 'pageNo' : '1'
   , 'pageSize' : '10'
   , 'movieViewType' : 'sma'
 , 'curationSection' : 'view0002'
   , 'order' : 'curation_code'

   , '_' : str ( self . GetNoCache ( 2 ) )
 }
   if 40 - 40: OoOoOO00 / IiII
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO , OOooooO0Oo )
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + Ii1I - I1Ii111
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 93 - 93: II111iiii . I1IiiI - Oo0Ooo + OoOoOO00
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 61 - 61: II111iiii
   if not ( 'result' in OOOO0oo0 [ 'body' ] ) : return o0oooOO00 , iiIiii1IIIII
   ii = OOOO0oo0 [ 'body' ] [ 'result' ]
   if 15 - 15: i11iIiiIii % I1IiiI * I11i / I1Ii111
   if 90 - 90: iII111i
   for oO0o0 in ii :
    i1i1i1I = oO0o0 [ 'curation_code' ]
    oOoo000 = oO0o0 [ 'curation_name' ]
    if 87 - 87: OoooooooOO - o0oOOo0O0Ooo / IiII . i11iIiiIii * OoooooooOO
    I1i1i1 = { 'curation_code' : i1i1i1I
 , 'curation_name' : unicode ( oOoo000 )
 }
    o0oooOO00 . append ( I1i1i1 )
    if 84 - 84: OoOoOO00 / I11i * iII111i / oO0o - i11iIiiIii . Oo0Ooo
    if 60 - 60: I1ii11iIi11i * I1IiiI
    if 17 - 17: OOooOOo % Oo0Ooo / I1ii11iIi11i . IiII * OOooOOo - II111iiii
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 41 - 41: Ii1I
  return o0oooOO00 , iiIiii1IIIII
  if 77 - 77: I1Ii111
  if 65 - 65: II111iiii . I1IiiI % oO0o * OoO0O00
 def GetSearchList ( self , search_key , userid , page_int , stype , premiumyn = False , landyn = False ) :
  iI11I = [ ]
  iiIiii1IIIII = False
  if 11 - 11: iII111i - oO0o + II111iiii - iIii1I11I1II1
  try :
   O0O = '/search/getSearch.jsp'
   if 7 - 7: IiII - I11i / II111iiii * Ii1I . iII111i * iII111i
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
   if 61 - 61: I11i % ooOoO0o - OoO0O00 / Oo0Ooo
   Ii = self . makeurl ( self . SEARCH_DOMAIN , O0O , OO , None )
   if 4 - 4: OoooooooOO - i1IIi % Ii1I - OOooOOo * o0oOOo0O0Ooo
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , self . TVING_TOKEN , 'POC_USERINFO' , self . POC_USERINFO ) )
 ]
   if 85 - 85: OoooooooOO * iIii1I11I1II1 . iII111i / OoooooooOO % I1IiiI % O0
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 36 - 36: Ii1I / II111iiii / IiII / IiII + I1ii11iIi11i
   if stype == 'vod' :
    if not ( 'programRsb' in OOOO0oo0 ) : return iI11I , iiIiii1IIIII
    oO0Ooo0ooOO0 = OOOO0oo0 [ 'programRsb' ] [ 'dataList' ]
    i1IIiIii1i = int ( OOOO0oo0 [ 'programRsb' ] [ 'count' ] )
    if 77 - 77: O0 % oO0o - OoO0O00
    if 97 - 97: OoooooooOO . i11iIiiIii + I1IiiI
    for oO0o0 in oO0Ooo0ooOO0 :
     iiI11i1II = oO0o0 [ 'mast_cd' ]
     I1i111I = oO0o0 [ 'mast_nm' ]
     Ooo = self . IMG_DOMAIN + oO0o0 [ 'web_url' ]
     if landyn == False :
      Ooo = self . IMG_DOMAIN + oO0o0 [ 'web_url4' ]
      if 84 - 84: oO0o % i1IIi
     Oo0oo0O0o00O = oO0o0 [ 'mast_synop' ]
     if 70 - 70: Oo0Ooo . OoooooooOO - iII111i
     Iii1iI = { }
     Iii1iI [ 'title' ] = oO0o0 [ 'mast_nm' ]
     Iii1iI [ 'mediatype' ] = 'episode'
     if 30 - 30: I1ii11iIi11i % I1IiiI
     try :
      if oO0o0 . get ( 'actor' ) != '' and oO0o0 . get ( 'actor' ) != '-' : Iii1iI [ 'cast' ] = oO0o0 . get ( 'actor' ) . split ( ',' )
      if oO0o0 . get ( 'director' ) != '' and oO0o0 . get ( 'director' ) != '-' : Iii1iI [ 'director' ] = oO0o0 . get ( 'director' ) . split ( ',' )
      if oO0o0 . get ( 'cate_nm' ) != '' : Iii1iI [ 'genre' ] = oO0o0 . get ( 'cate_nm' ) . split ( '/' )
      if 'targetage' in oO0o0 : Iii1iI [ 'mpaa' ] = oO0o0 . get ( 'targetage' )
     except :
      None
     try :
      if 'broad_dt' in oO0o0 :
       iiI1I1 = oO0o0 . get ( 'broad_dt' )
       Iii1iI [ 'aired' ] = '%s-%s-%s' % ( iiI1I1 [ : 4 ] , iiI1I1 [ 4 : 6 ] , iiI1I1 [ 6 : ] )
     except :
      None
      if 89 - 89: I1Ii111 + OoooooooOO + I1Ii111 * i1IIi + iIii1I11I1II1 % I11i
     I1i1i1 = { 'program' : iiI11i1II
 , 'title' : unicode ( I1i111I )
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'info' : Iii1iI
 }
     if 59 - 59: OOooOOo + i11iIiiIii
     iI11I . append ( I1i1i1 )
   else :
    if not ( 'vodMVRsb' in OOOO0oo0 ) : return iI11I , iiIiii1IIIII
    oo0OOo0O = OOOO0oo0 [ 'vodMVRsb' ] [ 'dataList' ]
    i1IIiIii1i = int ( OOOO0oo0 [ 'vodMVRsb' ] [ 'count' ] )
    if 39 - 39: OoooooooOO + oO0o % OOooOOo / OOooOOo
    if 27 - 27: iII111i . I11i . iIii1I11I1II1 . iIii1I11I1II1
    for oO0o0 in oo0OOo0O :
     iiI11i1II = oO0o0 [ 'mast_cd' ]
     I1i111I = oO0o0 [ 'mast_nm' ] . strip ( )
     Ooo = self . IMG_DOMAIN + oO0o0 [ 'web_url' ]
     if landyn :
      Ooo = Ooo . replace ( 'CAIM2100' , 'CAIM0400' )
      if 20 - 20: o0oOOo0O0Ooo / i1IIi
     Oo0oo0O0o00O = oO0o0 [ 'mast_synop' ]
     if 71 - 71: OoOoOO00 . i1IIi
     o0OooO0ooo0o = False
     iii1 = False
     for i1i1I111iIi1 in oO0o0 [ 'bill' ] :
      if i1i1I111iIi1 == self . MOVIE_LITE : iii1 = True
      elif i1i1I111iIi1 == self . MOVIE_PREMIUM : o0OooO0ooo0o = True
      if 32 - 32: Ii1I . IiII . OoooooooOO - OoO0O00 + oO0o
     Iii1iI = { }
     Iii1iI [ 'title' ] = unicode ( I1i111I )
     Iii1iI [ 'mediatype' ] = 'movie'
     if 88 - 88: iII111i
     try :
      if oO0o0 . get ( 'actor' ) != '' : Iii1iI [ 'cast' ] = oO0o0 . get ( 'actor' ) . split ( ',' )
      if oO0o0 . get ( 'director' ) != '' : Iii1iI [ 'director' ] = oO0o0 . get ( 'director' ) . split ( ',' )
      if oO0o0 . get ( 'cate_nm' ) != '' : Iii1iI [ 'genre' ] = oO0o0 . get ( 'cate_nm' ) . split ( '/' )
      if oO0o0 . get ( 'runtime_sec' ) != '' : Iii1iI [ 'duration' ] = oO0o0 . get ( 'runtime_sec' )
      if 'grade_nm' in oO0o0 : Iii1iI [ 'mpaa' ] = oO0o0 . get ( 'grade_nm' )
     except :
      None
     try :
      iiI1I1 = oO0o0 . get ( 'broad_dt' )
      Iii1iI [ 'aired' ] = '%s-%s-%s' % ( iiI1I1 [ : 4 ] , iiI1I1 [ 4 : 6 ] , iiI1I1 [ 6 : ] )
      Iii1iI [ 'year' ] = iiI1I1 [ : 4 ]
     except :
      None
      if 19 - 19: II111iiii * IiII + Ii1I
      if 65 - 65: OOooOOo . I1Ii111 . OoO0O00 . iII111i - OOooOOo
     if iii1 or ( premiumyn == True and o0OooO0ooo0o ) :
      I1i1i1 = { 'movie' : iiI11i1II
 , 'title' : unicode ( I1i111I )
 , 'thumbnail' : Ooo
 , 'synopsis' : unicode ( Oo0oo0O0o00O )
 , 'info' : Iii1iI
 }
      if iii1 == False : I1i1i1 [ 'title' ] = unicode ( I1i1i1 [ 'title' ] + ' [Premium]' )
      iI11I . append ( I1i1i1 )
      if 19 - 19: i11iIiiIii + iII111i % ooOoO0o
      if 14 - 14: OoO0O00 . II111iiii . I11i / Ii1I % I1ii11iIi11i - ooOoO0o
      if 67 - 67: I11i - OOooOOo . i1IIi
      if 35 - 35: iII111i + ooOoO0o - oO0o . iII111i . IiII
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 87 - 87: OoOoOO00
  return iI11I , iiIiii1IIIII
  if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
  if 50 - 50: OoO0O00 . i11iIiiIii - oO0o . oO0o
 def GetDeviceList ( self , tving_token , poc_userinfo ) :
  o0oooOO00 = [ ]
  OOoO00 = '-'
  if 31 - 31: OOooOOo / Oo0Ooo * i1IIi . OoOoOO00
  try :
   O0O = '/v1/user/device/list'
   if 57 - 57: OOooOOo + iIii1I11I1II1 % i1IIi % I1IiiI
   if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . I11i % oO0o . OoooooooOO
   OO = { 'apiKey' : '4263d7d76161f4a19a9efe9ca7903ec4'
 , 'model' : 'PC'
 }
   if 94 - 94: Ii1I + iIii1I11I1II1 % OoO0O00
   Ii = self . makeurl ( self . API_DOMAIN , O0O , OO )
   if 93 - 93: Ii1I - OOooOOo + iIii1I11I1II1 * o0oOOo0O0Ooo + I1Ii111 . iII111i
   II1Iiii1111i = [
 ( 'User-Agent' , i1I1ii1II1iII )
 , ( 'Cookie' , '%s=%s; %s=%s' % ( '_tving_token' , tving_token , 'POC_USERINFO' , poc_userinfo ) )
 ]
   if 49 - 49: OoooooooOO * I11i - Oo0Ooo . oO0o
   i1IIi11111i = self . SESSION . Request ( Ii , params = None , cookie = II1Iiii1111i )
   OOOO0oo0 = json . loads ( i1IIi11111i )
   if 89 - 89: ooOoO0o + Ii1I * ooOoO0o / ooOoO0o
   if 46 - 46: OoO0O00
   o0oooOO00 = OOOO0oo0 [ 'body' ]
   if 71 - 71: I11i / I11i * oO0o * oO0o / II111iiii
   for oO0o0 in o0oooOO00 :
    if oO0o0 [ 'model' ] == 'PC' :
     OOoO00 = oO0o0 [ 'uuid' ]
     if 35 - 35: OOooOOo * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
     if 58 - 58: I11i + II111iiii * iII111i * i11iIiiIii - iIii1I11I1II1
  except Exception as II111iiiI1Ii :
   print ( II111iiiI1Ii )
   if 68 - 68: OoooooooOO % II111iiii
  return OOoO00
  if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % I11i * I11i * I1ii11iIi11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
