#encoding: utf-8


import requests
response = requests.get("http://httpbin.org/ip")
print(response.text) #返回当前IP
#快代理

#使用代理服务器
proxy = {
    'http': '117.90.137.53:9000'
}
response = requests.get("http://httpbin.org/ip",proxies=proxy)
print(response.text)