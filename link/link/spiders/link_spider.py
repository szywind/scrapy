# encoding: utf-8

from scrapy.spiders import Spider
from scrapy.http import Request
import scrapy

#定义爬虫的业务逻辑实现类
class LinkSpider(Spider):
    name = "link"
    start_urls = []
    dianping_urlpattern = "https://www.dianping.com/search/category/{CITY}/10/p{CURR_PAGE}"

    def __init__(self):
        self.start_urls = self.set_url()

    #set_url方法动态设定要抓取的链接列表
    def set_url(self):
        url_list = []

        for i in xrange(2320):  #2310 SanSha
            url = self.dianping_urlpattern
            url = url.format(CITY=str(i), CURR_PAGE=1)
            url_list.append(url)
        return url_list

    #parse方法从html源代码中解析要抓取的内容
    def parse(self, response):
        # hxs = HtmlXPathSelector(response)

        raw_pg_info = scrapy.Selector(text=response.body).xpath('//a[@class="PageLink"][last()]/@title')
        pgNum = -1
        # print("foo = ", hxs)
        # print("pg_info = ", raw_pg_info)

        raw_city = scrapy.Selector(text=response.body).xpath('//input[@class="J-search-input"]/@data-s-cityid').extract()
        try:
            city = int(raw_city[0])
        except IndexError:
            return

        print("city = ", city)
        # 如果没有找到末页的连接，说明只有一页
        if (len(raw_pg_info)==0):
            pgNum = 1
        else:
            pg_info = raw_pg_info[0].extract()
            pgNum = int(pg_info)

        print("pgNum = ", pgNum)

        #根据总页数，拼成分页时使用的url
        i = 1
        url = self.dianping_urlpattern
        for i in range(pgNum):
            each_url = url.format(CITY=city, CURR_PAGE=i+1)
            #调用分页后的页面
            yield Request(each_url,callback=self.get_joburls_bypage, headers={'referer': 'http://www.dianping.com'})

    #解析职位检索结果页面上的所有职位的链接，插入表中
    def get_joburls_bypage(self, response):
        print("#"*20)

        links = scrapy.Selector(text=response.body).xpath('//li[@class=""]/div[@class="pic"]/a/@href').extract()

        print("links = ", links)

        for link in links:
            if 1:   # keep all posts
                open('../output/link_output/link-2.txt', 'ab').write('https://www.dianping.com'+link+'\n')


    # def start_requests(self):
    #     yield Request("http://www.dianping.com",
    #                   headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"})
