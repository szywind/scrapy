# -*- coding:gb2312 -*-
# encoding: utf-8

from scrapy.spiders import Spider
from scrapy.http import Request
import scrapy
from page import items
import traceback
import os
import urllib
import re
import sys
import datetime



def filterURL(url_list):
    # exist_page_list = os.listdir('../output/page_output')
    exist_page_list = os.listdir('/Users/shenzhenyuan/Desktop/page_output')

    # exist_page_id = [s.split("_")[1].split(".txt")[0] for s in exist_page_list]
    # filtered_url_list = [i for i in url_list if i.split("/")[-1] in exist_page_id]

    for a in exist_page_list:
        id = a[a.rfind("_")+1: a.rfind(".txt")]
        fname = 'https://www.dianping.com/shop/' + id
        try:
            url_list.remove(fname)
        except ValueError:
            pass
    print "left # of pages: ", len(url_list)    # total is 1194202

    # save left pages url to a file
    with open("/Users/shenzhenyuan/Desktop/left_links.txt", "wt") as fl:
        for link in url_list:
            fl.write(link + "\n")
    return url_list

#定义要抓取页面的爬虫类
class PageSpider(Spider):
    default = ""
    name = "page"    
    start_urls = []
    
    def __init__(self):        
        self.start_urls = self.set_url()

    #从jobs_task表中读出要抓取的链接列表，放入数组中
    def set_url(self):
        link_file = open('../output/link_output/link-2.txt', 'r')
        url_list = [line.replace('\r','').replace('\n','') for line in link_file]
        # url_list = url_list[:2]
        link_file.close()
        return filterURL(url_list)

    def parse(self, response):
        try:
            #从网址http://www.dianping.com/3428280中解析出3428280作为文件名
            file_id = response.url.split("/")[-1]
            homepage = response.url

            shop_name = scrapy.Selector(text=response.body).xpath('//h1[@class="shop-name"]/text()').extract()[0].encode('utf-8').strip()

            try:
                food_img_url = scrapy.Selector(text=response.body).xpath('//meta[@itemprop="image"]/@content').extract()[0]
            except IndexError:
                food_img_url = self.default
            try:
                rank_star = scrapy.Selector(text=response.body).xpath('//div[@class="brief-info"]/span[1]/@class').extract()[0].split()[1]
            except IndexError:
                rank_star = -1
            brief_info = scrapy.Selector(text=response.body).xpath('//div[@class="brief-info"]').extract()[0].encode('utf-8')
            tmp = brief_info.split('</span>')

            try:
                reviews = tmp[1].split('>')[1].decode("ascii", "ignore").encode('utf-8')
                reviews = int(reviews)
            except (IndexError, ValueError):
                reviews = -1

            try:
                cost_person = tmp[2].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
                cost_person = int(cost_person)
            except (IndexError, ValueError):
                cost_person = -1

            try:
                taste_score = tmp[3].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
                taste_score = float(taste_score)
            except (IndexError, ValueError):
                taste_score = -1

            try:
                environment_score = tmp[4].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
                environment_score = float(environment_score)
            except (IndexError, ValueError):
                environment_score = -1

            try:
                service_score = tmp[5].split('>')[-1].decode("ascii", "ignore").encode('utf-8')
                service_score = float(service_score)
            except (IndexError, ValueError):
                service_score = -1

            try:
                city = scrapy.Selector(text=response.body).xpath('//a[@class="city J-city"]/text()').extract()[0].encode('utf-8')
            except (IndexError, ValueError):
                city = self.default

            try:
                local_region = scrapy.Selector(text=response.body).xpath('//div[@class="expand-info address"]/a/span[@itemprop="locality region"]/text()').extract()[0].encode('utf-8')
            except (IndexError, ValueError):
                local_region = self.default


            try:
                street_address = scrapy.Selector(text=response.body).xpath('//div[@class="expand-info address"]/span[@itemprop="street-address"]/@title').extract()[0].encode('utf-8')
            except (IndexError, ValueError):
                street_address = self.default

            try:
                temp = response.body
                temp = temp[temp.find("lng:"):]
                raw_geo_point = temp[:temp.find("}")].split(",")

                lng = float(raw_geo_point[0].split(":")[1])
                lat = float(raw_geo_point[1].split(':')[1])
            except (IndexError, ValueError):
                lng = -1
                lat = -1

            try:
                phone = scrapy.Selector(text=response.body).xpath('//p[@class="expand-info tel"]/span[@itemprop="tel"]/text()').extract()   # may have multiple phone numbers
            except (IndexError, ValueError):
                phone = [self.default]
            other_info = scrapy.Selector(text=response.body).xpath('//div[@class="other J-other Hide"]/p').extract()

            open_time = self.default

            str_open_time = '<span class="info-name">\xe8\x90\xa5\xe4\xb8\x9a\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x9a</span>'
            for tmp in other_info:
                tmp = tmp.encode("utf-8")
                #if (tmp.find('<span class="info-name">营业时间：</span>')>-1):
                if(tmp.find(str_open_time)>-1):
                    open_time = tmp.split(str_open_time)[1].split('</span>')[0].split('>')[1].strip()
                    break

            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            # print("shop_name = ", shop_name)
            # print("food_img_url = ", food_img_url)
            # print("rank_star = ", rank_star)
            # print("reviews = ", reviews)
            # print("cost_person = ", cost_person)
            # print("taste_score = ", taste_score)
            # print("environment_score = ", environment_score)
            # print("service_score = ", service_score)
            # print("city = ", city)
            # print("local_region = ", local_region)
            # print("street_address =", street_address)
            # print("phone = ", phone)
            # print("open_time = ", open_time)
            # print("homepage = ", homepage)
            # print("lat = ", lat)
            # print("lng = ", lng)

            data = items.PageItem()

            data['file_id'] = file_id
            data['shop_name'] = shop_name
            data['food_img_url'] = food_img_url
            data['rank_star'] = rank_star
            data['reviews'] = reviews
            data['cost_person'] = cost_person
            data['taste_score'] = taste_score
            data['environment_score'] = environment_score
            data['service_score'] =service_score
            data['city'] = city
            data['local_region'] = local_region
            data['street_address'] = street_address
            data['phone'] = phone
            data['open_time'] = open_time
            data['homepage'] = homepage
            data['longitude'] = lng
            data['latitude'] = lat

            # print("file_id = ", data['file_id'])

            return data
        except Exception as e:
            print "ERROR PARSE"
            print response.url
            print traceback.format_exc()

