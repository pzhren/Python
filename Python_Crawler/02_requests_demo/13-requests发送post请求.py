#encoding: utf-8

import requests

data = {
    'first':"true",
    'pn': '1',
    'kd': 'python'
}
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Cookie': '_ga=GA1.2.1028913989.1560842578; user_trace_token=20190618152254-e3c6e155-9199-11e9-b0ec-525400f775ce; LGUID=20190618152254-e3c6e65e-9199-11e9-b0ec-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; gate_login_token=316ec0f1d9bd6a1e9f5dc5cfc0f04b94223981b4b885abaa7e9126f31cb5b74b; hasDeliver=0; JSESSIONID=ABAAABAABEEAAJAF476ADD5831DE1D92979E384085929C1; _putrc=327074865F889419123F89F2B170EADC; _gid=GA1.2.1450455718.1561283285; _gat=1; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B79285; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; LGSID=20190623174803-fe60dd23-959b-11e9-b746-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DbLcJy5cdy1-JMdFystR6gDwjo8SZDU8C2CMWnte9KPe%26wd%3D%26eqid%3Dc19db23000178030000000035d0f4acf; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=f7a5e5cf49d11ac51923821651cf980e650a69e4b1; LGRID=20190623174819-0845aeef-959c-11e9-a49e-5254005c3644; SEARCH_ID=f3b1a63e528b4edaa6f3bdf10786323e'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',data=data,headers=headers)
print(type(response.json()))
print(response.json())