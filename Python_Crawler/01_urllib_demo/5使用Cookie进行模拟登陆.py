#encoding: utf-8

# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request
from bs4 import BeautifulSoup


# 1. 不使用cookie去请求大鹏的主页
dapeng_url = "http://www.renren.com/880151247/profile"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))