#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []

def parse_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    # html5lib
    # pip install html5lib
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({"city":city,"min_temp":int(min_temp)})
            # print({"city":city,"min_temp":int(min_temp)})

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)

    # 分析数据
    # 根据最低气温进行排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])

    data = ALL_DATA[0:10]
    cities = list(map(lambda x:x['city'],data))
    temps = list(map(lambda x:x['min_temp'],data))
    # pyecharts
    # pip install pyecharts
    chart = Bar("中国天气最低气温排行榜")
    chart.add('',cities,temps)
    chart.render('temperature.html')


if __name__ == '__main__':
    main()
    # ALL_DATA = [
    #     {"city": "北京", 'min_temp': 0},
    #     {"city": "天津", 'min_temp': -8},
    #     {"city": "石家庄", 'min_temp': -10}
    # ]
    #
    # ALL_DATA.sort(key=lambda data:data['min_temp'])
    # print(ALL_DATA)