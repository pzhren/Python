#encoding: utf-8

from urllib import request
# 没有使用代理的
url = 'http://httpbin.org/ip' #用来测IP
resp = request.urlopen(url) #打开链接
print(resp.read()) #读取链接的内容


# 使用代理的
url = 'http://httpbin.org/ip' #用来测IP
# 1. 使用ProxyHandler，传入代理构建一个handler
#快代理
handler = request.ProxyHandler({"http":"112.14.47.6:52024"})
# 2. 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3. 使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())