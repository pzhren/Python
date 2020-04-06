#encoding: utf-8
#urlparse和urlsplit二者的用法几乎一样，只是urlsplit没有params参数

from urllib import parse

url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'

result1 = parse.urlparse(url)
result2 = parse.urlsplit(url) #没有params

print(result1)
print(result2)
# print('scheme:',result.scheme) #协议
# print('netloc:',result.netloc) #域名
# print('path:',result.path) #路径
# # print('params:',result.params) #参数
# print('query:',result.query) #查询字符串
# print('fragment:',result.fragment) #锚点