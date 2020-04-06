#encoding: utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

# #百度cookie信息
# cookiejar = MozillaCookieJar('cookie_百度.txt')#要把Cookie信息放在该.txt文件中
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
#
# resp = opener.open('http://www.baidu.com/')
# cookiejar.save()

'''httpbin'''
cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)#加载Cookie
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies')
for cookie in cookiejar:
    print(cookie)

# cookiejar.save(ignore_discard=True)#保存即将过期的Cookie信息