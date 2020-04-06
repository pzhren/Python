#encoding: utf-8

# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request
from urllib import parse
from http.cookiejar import CookieJar #用来保存cookie

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}


def get_opener():
#用来存储Cookie信息
    # 1. 登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    # 1.4 使用opener发送登录的请求（人人网的邮箱和密码）
    data = {
        'email':"970138074@qq.com",
        'password': "pythonspider"
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2. 访问个人主页
    dapeng_url = "http://www.renren.com/880151247/profile"
    # 获取个人主页的页面的时候，不要新建一个opener
    # 而应该使用之前的那个opener，因为之前的那个opener已经包含了
    # 登录所需要的cookie信息
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)
    with open('renren.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)