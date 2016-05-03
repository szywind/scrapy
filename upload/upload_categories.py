# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

myApiKey = '1d1182a02878bfa992b58fff127959da'
# url = 'http://apis.baidu.com/baidunuomi/openapi/searchshops?city_id=100010000&cat_ids=326&subcat_ids=962%2C994&district_ids=394%2C395&bizarea_ids=1322%2C1328&location=116.418993%2C39.915597&keyword=%E4%BF%8F%E6%B1%9F%E5%8D%97&radius=3000&page=1&page_size=5&deals_per_shop=10'

url = 'http://apis.baidu.com/baidunuomi/openapi/searchshops?city_id=100010000&location=116.38833,39.92889&radius=30000&page_size=50&deals_per_shop=1'

def runNuomi(keyword):
    url = 'http://apis.baidu.com/baidunuomi/openapi/searchshops?city_id=100010000&location=116.418993%2C39.915597&keyword=' + keyword

    req = urllib2.Request(url)

    req.add_header("apikey", myApiKey)

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        print(content)






url = 'http://apis.baidu.com/baidunuomi/openapi/categories'


req = urllib2.Request(url)

req.add_header("apikey", "您自己的apikey")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)