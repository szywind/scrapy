# encoding: utf-8

from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import scrapy
import os
import sys
import datetime

#定义爬虫的业务逻辑实现类
class LinkSpider(Spider):
    name = "link"
    start_urls = []
    liepin_urlpatten = "https://www.liepin.com/zhaopin/?searchField=1&key={KEYWORD}&curPage={CURR_PAGE}"

    def __init__(self):
        self.start_urls = self.set_url()        
        
    #set_url方法动态设定要抓取的链接列表
    def set_url(self):
        url_list = []
        #从配置文件中取出所有的关键字列表，逐个去liepin做检索
        keys = '大数据,hadoop,hive,hbase,spark,storm,sqoop,pig'
        for keyword in keys.split(','):
            url = self.liepin_urlpatten
            url = url.format(KEYWORD=keyword, CURR_PAGE=1)
            url_list.append(url)
        return url_list
    
    #parse方法从html源代码中解析要抓取的内容
    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        raw_pg_info = scrapy.Selector(text=response.body).xpath('//a[@class="last"]/@href')
        pgNum = -1
        # print("foo = ", hxs)
        # print("pg_info = ", raw_pg_info)

        try:
            keyword = scrapy.Selector(text=response.body).xpath('//input[@name="key"]/@value')[0].extract()
            # keyword = hxs.select('//input[@name="key"]/@value').extract()[0]
            print("keyword = ", keyword)
            keyword = keyword.encode('utf-8')
        except IndexError:
            return

        # 如果没有找到末页的连接，说明只有一页
        if (len(raw_pg_info)==0):
            pgNum = 1
        else:
            pg_info = raw_pg_info[0].extract()
            print("pg_info = ", pg_info)
            if (pg_info.find("curPage=")>-1):
                pg_info = pg_info.split("curPage=")[1]
                pgNum = int(pg_info)

        #根据总页数，拼成分页时使用的url
        i = 1
        url = self.liepin_urlpatten
        for i in range(pgNum):
            each_url = url.format(KEYWORD=keyword, CURR_PAGE=i+1)
            #调用分页后的页面
            yield Request(each_url,callback=self.get_joburls_bypage)

    #解析职位检索结果页面上的所有职位的链接，插入表中            
    def get_joburls_bypage(self, response):
        print("#"*20)
        # hxs = HtmlXPathSelector(response)
        # links = hxs.select('//ul[@class="sojob-result-list"]/li/a/@href').extract()
        # links_jobdate = hxs.select('//ul[@class="sojob-result-list"]/li/a/dl/dt[@class="date"]/span/text()').extract()
        try:
            links = scrapy.Selector(text=response.body).xpath('//ul[@class="sojob-list"]/li/div[@class="sojob-item-main clearfix"]/div[@class="job-info"]/h3/a/@href').extract()
            links_jobdate = scrapy.Selector(text=response.body).xpath('//div[@class="job-info"]/p[@class="time-info clearfix"]/time/text()').extract()
        except IndexError:
            return

        today = self.getYYYYMMDD()
        today2 = self.getYYYYMMDD2()

        print("links = ", links)
        print()
        # 找到每个职位的发布日期，如果发布日期是当天的，就入库
        for idx,link in enumerate(links):
            print("links_jobdate[idx] = ", links_jobdate[idx])
            print("today2 = ", today2)
            print("*"*20)
            #if (links_jobdate[idx].find(today2)>-1):    # screen out today's post
            if 1:   # keep all posts
                open('../output/link_output/link.txt', 'ab').write(link+'\n')
                #open('/Users/shenzhenyuan/Desktop/link.txt', 'ab').write(link+'\n')

    #得到yyyymmdd格式的当期日期
    def getYYYYMMDD(self):
        return datetime.datetime.now().strftime('%Y%m%d')
						
    #得到yyyy-mm-dd格式的当期日期
    def getYYYYMMDD2(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')
