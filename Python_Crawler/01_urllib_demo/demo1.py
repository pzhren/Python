#encoding: utf-8


from urllib import request
from urllib import parse

#resp = request.urlopen('http://www.baidu.com')
#print(resp.read())
#print(resp.read(10))
# print(resp.readlines())
# print(resp.getcode())

# urlretrieve函数的用法：下载文件，图片
# request.urlretrieve('http://www.baidu.com/','baidu.html')
# request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1561006725856&di=8d8eff66f58dbc45ee5ed53dced016d5&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Faf837ddedb1bd9b9ad99c9528b54ee2ca484f1da193535-jeAOc5_fw658','hanxin.jpg')
request.urlretrieve('http://downloads.editor.gitbook.com/download/windows','gitbook.exe')
# urlencode函数的用法：进行编码
# params = {'name':'张三',"age":18,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)


#https://www.baidu.com/s?ie=UTF-8&wd=%E5%88%98%E5%BE%B7%E5%8D%8E
# url = 'http://www.baidu.com/s'
# params = {"wd":"刘德华"}#对汉字进行编码
# qs = parse.urlencode(params)
# print(qs)
# url = url + "?" + qs #字符串链接
# resp = request.urlopen(url)
# print(resp.read())


# parse_qs函数的用法
# params = {'name':'张三',"age":18,'greet':'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)

