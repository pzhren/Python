#encoding: utf-8

import requests

response = requests.get("https://www.baidu.com/")
print(type(response.text)) #字符串数据str类型，可能存在乱码
print(response.text)
print(type(response.content)) #bytes数据类型
print(response.content)
print(response.content.decode('utf-8')) #指定解码方式，可以显示中文

print(response.url)
print(response.encoding) #编码方式
print(response.status_code) #状态码


params = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
response = requests.get("https://www.baidu.com/s",params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)