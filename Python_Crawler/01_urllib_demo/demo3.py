#encoding: utf-8

from urllib import request,parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

#直接使用urlopen()不行
# resp = request.urlopen(url)
# print(resp.read())


url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#伪装
#User-Agent:用户代理，欺骗服务器，伪装成浏览器的正常请求
headers = {
    'Cookie': '_ga=GA1.2.1028913989.1560842578; user_trace_token=20190618152254-e3c6e155-9199-11e9-b0ec-525400f775ce; LGUID=20190618152254-e3c6e65e-9199-11e9-b0ec-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAIAACBI01FAB1D257EA1B5967ED64234ABFEA2F; _gid=GA1.2.760315193.1561000597; PRE_UTM=; _putrc=327074865F889419123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B79285; gate_login_token=316ec0f1d9bd6a1e9f5dc5cfc0f04b94223981b4b885abaa7e9126f31cb5b74b; hasDeliver=0; _gat=1; LGSID=20190620154234-f79f97b1-932e-11e9-b1b3-525400f775ce; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DrWebMZQ0FbH6XV_uSJU4yiAQ9n7PRuQVAwrRnB_jmXK%26ck%3D776.0.68.223.145.NaN.NaN.0NaN.NaN.0%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3Df1fb1d2b0000fff1000000035d0b38e6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=f7a5e5cf49d11ac54656101651cf980e650a69e4b1; LGRID=20190620154244-fd7a58bb-932e-11e9-a3eb-5254005c3644; SEARCH_ID=b17394c394444f588b162798cd25d4e1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))