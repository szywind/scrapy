# -*- coding:gb2312 -*-
# encoding: utf-8

from scrapy.spiders import Spider
from scrapy.http import Request
import scrapy
from page import items
import traceback
import sys
import datetime

#定义要抓取页面的爬虫类
class PageSpider(Spider):
    default = "None"
    name = "page"    
    start_urls = []
    
    def __init__(self):        
        self.start_urls = self.set_url()

    #从jobs_task表中读出要抓取的链接列表，放入数组中
    def set_url(self):
        url_list = []
        link_file = open('../output/link_output/link.txt', 'r')
        loops = 0
        for each_link in link_file:
            each_link = each_link.replace('\r','')
            each_link = each_link.replace('\n','')
            url_list.append(each_link)
            # loops+=1
            # if (loops == 100):
            #     break
        link_file.close()
        return url_list

    def parse(self, response):
        try:
            #从网址http://www.dianping.com/3428280中解析出3428280作为文件名
            file_id = response.url.split("/")[-1]
            homepage = response.url

            shop_name = scrapy.Selector(text=response.body).xpath('//h1[@class="shop-name"]/text()').extract()[0].encode('utf-8').strip()
            food_img_url = scrapy.Selector(text=response.body).xpath('//meta[@itemprop="image"]/@content').extract()[0]
            rank_star = scrapy.Selector(text=response.body).xpath('//div[@class="brief-info"]/span[1]/@class').extract()[0].split()[1]

            brief_info = scrapy.Selector(text=response.body).xpath('//div[@class="brief-info"]').extract()[0].encode('utf-8')
            tmp = brief_info.split('</span>')

            reviews = tmp[1].split('>')[1].decode("ascii", "ignore").encode('utf-8')
            cost_person = tmp[2].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
            taste_score = tmp[3].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
            environment_score = tmp[4].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
            service_score = tmp[5].split('>')[-1].decode("ascii", "ignore").encode('utf-8')

            city = scrapy.Selector(text=response.body).xpath('//a[@class="city J-city"]/text()').extract()[0].encode('utf-8')
            local_region = scrapy.Selector(text=response.body).xpath('//div[@class="expand-info address"]/a/span[@itemprop="locality region"]/text()').extract()[0].encode('utf-8')
            street_address = scrapy.Selector(text=response.body).xpath('//div[@class="expand-info address"]/span[@itemprop="street-address"]/@title').extract()[0].encode('utf-8')
            phone = scrapy.Selector(text=response.body).xpath('//p[@class="expand-info tel"]/span[@itemprop="tel"]/text()').extract()   # may have multiple phone numbers

            other_info = scrapy.Selector(text=response.body).xpath('//div[@class="other J-other Hide"]/p').extract()

            open_time = self.default

            str_open_time = '<span class="info-name">\xe8\x90\xa5\xe4\xb8\x9a\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x9a</span>'
            for tmp in other_info:
                tmp = tmp.encode("utf-8")
                #if (tmp.find('<span class="info-name">营业时间：</span>')>-1):
                if(tmp.find(str_open_time)>-1):
                    open_time = tmp.split(str_open_time)[1].split('</span>')[0].split('>')[1].strip()
                    break

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("shop_name = ", shop_name)
            print("food_img_url = ", food_img_url)
            print("rank_star = ", rank_star)
            print("reviews = ", reviews)
            print("cost_person = ", cost_person)
            print("taste_score = ", taste_score)
            print("environment_score = ", environment_score)
            print("service_score = ", service_score)
            print("city = ", city)
            print("local_region = ", local_region)
            print("street_address =", street_address)
            print("phone = ", phone)
            print("open_time = ", open_time)
            print("homepage = ", homepage)


            data = items.PageItem()

            data['file_id'] = file_id
            data['shop_name'] = shop_name
            data['food_img_url'] = food_img_url
            data['rank_star'] = rank_star
            data['reviews'] = int(reviews)
            data['cost_person'] = int(cost_person)
            data['taste_score'] = float(taste_score)
            data['environment_score'] = float(environment_score)
            data['service_score'] = float(service_score)
            data['city'] = city
            data['local_region'] = local_region
            data['street_address'] = street_address
            data['phone'] = phone
            data['open_time'] = open_time
            data['homepage'] = homepage

            print("file_id = ", data['file_id'])

            return data
        except Exception as e:
            print "ERROR PARSE"
            print response.url
            print traceback.format_exc()
			#self.jobsTool.updateCrulInfo(ConfigPropObj.liepin_webid, response.url, 2, e)
