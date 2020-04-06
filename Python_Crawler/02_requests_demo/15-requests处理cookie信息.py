#encoding: utf-8
#如果想要在多次请求中共享cookie。那么应该使用session。
import requests
response = requests.get('https://www.baidu.com/')
print(response.cookies) #返回cookies
print(response.cookies.get_dict()) #以字典的形式返回

url = "http://www.renren.com/PLogin.do"
data = {"email":"970138074@qq.com",'password':"pythonspider"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

session = requests.Session()

session.post(url,data=data,headers=headers)

response = session.get('http://www.renren.com/880151247/profile')
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
