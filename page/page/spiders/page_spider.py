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
            loops+=1
            if (loops == 100):
                break
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
                print('tmp = ', tmp)
                #if (tmp.find('<span class="info-name">营业时间：</span>')>-1):
                if(tmp.find(str_open_time)>-1):
                    print('$$$$$$$$$$$$$', tmp)
                    open_time = tmp.split(str_open_time)[1].split('</span>')[0].split('>')[1].strip()
                    print('opentime = ', open_time)
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
            # title_info = hxs.select('//title/text()').extract()[0].encode('utf8')
            # title_info = title_info.split('招聘信息_')
            # if (len(title_info)==2):
            #     job_name = title_info[0]
            #     company_name = title_info[1].replace('-猎聘网','')
            # else:
            #     #处理猎头职位
            #     job_name = hxs.select('//div[@class="title-info "]/h1/text()').extract()[0].encode('utf8')
            #     company_name = hxs.select('//div[@class="title-info "]/h3/text()').extract()[0].encode('utf8');
            #
            # #发布日期工作地点
            # job_datetime = self.getYYYYMMDD()
            # job_location = ""
            # work_years = ""
            # edu = ""
            # salary = ""
            # language = ""
            #
            # loc_infos = hxs.select('//div[@class="content"]/ul/li').extract()
            # for tmp in loc_infos:
            #     tmp = tmp.encode('utf8')
            #     if (tmp.find('工作地点')>-1):
            #         tmp = tmp.split('</a>')[0]
            #         tmp = tmp.split('>')[-1]
            #         job_location = tmp.strip()
            #
            #     if (tmp.find('<span>学历要求：</span>')>-1):
            #     ()    tmp = tmp.split('<span>学历要求：</span>')[1]
            #         tmp = tmp.replace('</li>','')
            #         edu = tmp.strip
            #
            #     if (tmp.find('<span>语言要求：</span>')>-1):
            #         tmp = tmp.split('<span>语言要求：</span>')[1]
            #         tmp = tmp.replace('</li>','')
            #         language = tmp.strip()
            #
            #     if (tmp.find('<span>工作年限：</span>')>-1):
            #         tmp = tmp.split('<span>工作年限：</span>')[1]
            #         tmp = tmp.replace('</li>','')
            #         work_years = tmp.strip()
            #
            # #薪资待遇
            # salary = hxs.select('//p[@class="job-main-title"]/text()').extract()[0].encode('utf-8')
            #
            # #公司地址网址
            # company_address = ""
            # company_website = ""
            # #公司行业性质规模
            # company_worktype = ""
            # company_scale = ""
            # company_prop = ""
            #
            # #根据网页地址来判断是否是猎头职位，格式不一样
            # if (response.url.find('a.liepin.com')>-1):
            #     loc_infos = hxs.select('//div[@class="resume clearfix"]').extract()[0].encode('utf-8')
            #     tmp = loc_infos.split('</span>');
            #     job_location = tmp[0]  #工作地点
            #     job_location = job_location.split('<span>')[1]
            #     job_location = job_location.strip()
            #     edu = tmp[1]  #学历要求
            #     edu = edu.split('<span>')[1]
            #     edu = edu.strip()
            #     language = tmp[2]  #语言要求
            #     language = language.split('>')[1]
            #     language = language.strip()
            #
            #     #职位描述
            #     job_desc = hxs.select('//div[@class="content content-word"]').extract()[0].encode('utf-8')
            #     job_desc = job_desc.split('content-word">')[1]
            #     job_desc = job_desc.split('</div>')[0]
            #     job_desc = job_desc.strip()
            #
            #     #企业介绍
            #     company_desc = hxs.select('//div[@class="job-main noborder main-message"]').extract()[0].encode('utf-8')
            #     company_desc = company_desc.split('content-word">')[1]
            #     company_desc = company_desc.split('</div>')[0]
            #     company_desc = company_desc.strip()
            #
            #     company_info = hxs.select('//div[@class="content content-word"]').extract()[0].encode('utf-8')
            #     if (company_info.find('行业：')>-1):
            #         company_worktype = company_info.split('行业：</span>')[1]
            #         company_worktype = company_worktype.split('</a>')[0]
            #         company_worktype = company_worktype.split('>')[1]
            #
            #     if (company_info.find('规模：')>-1):
            #         company_scale = company_info.split('规模：</span>')[1]
            #         company_scale = company_scale.split('</li>')[0]
            #         company_scale = company_scale.strip()
            #
            #     if (company_info.find('性质：')>-1):
            #         company_prop = company_info.split('性质：</span>')[1]
            #         company_prop = company_prop.split('</li>')[0]
            #         company_prop = company_prop.strip()
            # else:
            #     #职位描述
            #     job_desc = hxs.select('//div[@class="content content-word"]').extract()[0].encode('utf-8')
            #     job_desc = job_desc.split('content-word">')[1]
            #     job_desc = job_desc.split('</div>')[0]
            #     job_desc = job_desc.strip()
            #
            #     #企业介绍
            #     company_desc = hxs.select('//div[@class="content content-word"]').extract()[1].encode('utf-8')
            #     company_desc = company_desc.split('content-word">')[1]
            #     company_desc = company_desc.split('</div>')[0]
            #     company_desc = company_desc.strip()
            #
            #     company_info = hxs.select('//div[@class="content content-word"]').extract()[2].encode('utf-8')
            #
            #     if (company_info.find('行业：')>-1):
            #         company_worktype = company_info.split('行业：</span>')[1]
            #         company_worktype = company_worktype.split('</a>')[0]
            #         company_worktype = company_worktype.split('>')[1]
            #
            #     if (company_info.find('规模：')>-1):
            #         company_scale = company_info.split('<span>规模：</span>')[1]
            #         company_scale = company_scale.split('<br>')[0]
            #
            #     if (company_info.find('性质：')>-1):
            #         company_prop = company_info.split('<span>性质：</span>')[1]
            #         company_prop = company_prop.split('<br>')[0]
            #
            #     if (company_info.find('地址：')>-1):
            #         company_address = company_info.split('<span>地址：</span>')[1]
            #         company_address = company_address.split('<div>')[0]
            #         company_address = company_address.replace('</div>', '')
            #         company_address = company_address.strip()
            #
            # #根据网页地址来判断是否是一般职位，格式不一样
            # if (response.url.find('job.liepin.com/')>-1):
            #     basic_info = hxs.select('//p[@class="basic-infor"]').extract()[0].encode('utf-8')
            #     job_location = basic_info.split('</i>')
            #     job_location = job_location[1]
            #     job_location = job_location.split('</span>')
            #     job_location = job_location[0].strip()
            #     resume_info = hxs.select('//div[@class="resume clearfix"]/span/text()').extract()
            #     work_years = resume_info[1].encode('utf-8')
            #     edu = resume_info[0].encode('utf-8')
            #     language = resume_info[2].encode('utf-8')
            #     #print(work_years)
            #     #print(edu)
            #     #print(language)
            #
            # data = items.PageItem()
            # data['web_id'] = "liepin"
            # data['file_id'] = file_id
            # data['job_url'] = response.url
            # data['job_name'] = job_name
            # data['job_desc'] = job_desc
            # data['gender'] = ""
            # data['major'] = ""
            # data['company_name'] = company_name
            # data['job_datetime'] = job_datetime
            # data['job_location'] = job_location
            # data['work_years'] = work_years
            # data['edu'] = edu
            # data['salary'] = salary
            # data['company_desc'] = company_desc
            # data['company_address'] = company_address
            # data['company_website'] = company_website
            # data['language'] = language
            # data['company_worktype'] = company_worktype
            # data['company_prop'] = company_prop
            # data['company_scale'] = company_scale
            
            #更新任务表中抓取状态
			#self.jobsTool.updateCrulInfo(ConfigPropObj.liepin_webid, response.url, 1, "")

            return data
        except Exception as e:
            print "ERROR PARSE"
            print response.url
            print traceback.format_exc()
			#self.jobsTool.updateCrulInfo(ConfigPropObj.liepin_webid, response.url, 2, e)
