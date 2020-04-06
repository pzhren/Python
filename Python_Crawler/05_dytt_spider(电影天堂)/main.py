#encoding: utf-8

from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
}

def get_detail_urls(url):
    #得到每个电影的详情页，返回的是当前页的所有电影的url链接，是url链接的列表
    response = requests.get(url, headers=HEADERS)
    # response.text #以猜测的方式进行解码
    # response.content
    # requests库，默认会使用自己猜测的编码方式将
    # 抓取下来的网页进行解码，然后存储到text属性上去
    # 在电影天堂的网页中，因为编码方式，requests库猜错了。所以就会产生乱码
    # text = response.content.decode('gbk')
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk') #以gbk的方式进行解码
    # text = response.text.encode('utf-8').decode('utf-8')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print('='*30)
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['actors'] = actors
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                movie["profile"] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie

def spider():
    base_url = "http://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):
        print('-'*50)
        print(x)
        # 第一个for循环，是用来控制总共有7页的
        url = base_url.format(x) #每一页的链接
        detail_urls = get_detail_urls(url)#每一页所有电影的url
        for detail_url in detail_urls:
            print(detail_url)
            # 第二个for循环，是用来遍历一页中所有电影的详情url
            movie = parse_detail_page(detail_url) #获得电影的具体信息
            movies.append(movie)
            print(movie)

    # print(movies)

if __name__ == '__main__':
    spider()
