#encoding: utf-8
import requests
#将验证信息设置为verify=False
resp = requests.get('http://www.12306.cn/mormhweb/',verify=True)
with open('12306.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)