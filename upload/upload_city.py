# -*- coding:gb2312 -*-
# encoding: utf-8
import sys, urllib, urllib2, json
import os
import json
import leancloud
from leancloud import Object
from leancloud import Query
from leancloud import GeoPoint
from gevent import monkey
import simplejson

monkey.patch_all()

leancloud.use_region('CN')

leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', 'ew9zGSqucKA9iPA8QpujFvGK')
#leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', 'uA8skpMa6SKLrGr8MRGueBJ4')

# 或者您现在需要使用 master key 的权限
leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', master_key='eh5FdcA7o3xwMTLCUQluRDmJ')
#leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', master_key='1ndDPyrzINegIp4WNcJDFGAd')

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(query, from_sensor=False):
    query = query.encode('utf-8')
    params = {
        'address': query,
        'sensor': "true" if from_sensor else "false"
    }
    url = googleGeocodeUrl + urllib.urlencode(params)
    json_response = urllib.urlopen(url)
    response = simplejson.loads(json_response.read())
    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        print query, latitude, longitude
    else:
        latitude, longitude = None, None
        print query, "<no results>"
    return latitude, longitude


class City(Object):

    ## get functions

    @property
    def city_id(self):
    # 可以使用property装饰器，方便获取属性
        return self.get('city_id')

    @property
    def city_name(self):
        return self.get('city_name')

    @property
    def short_name(self):
        return self.get('short_name')

    @property
    def city_pinyin(self):
        return self.get('city_pinyin')

    @property
    def short_pinyin(self):
        return self.get('short_pinyin')

    @property
    def geo_point(self):
        return self.get('geo_point')


    ## set functions

    @city_id.setter
    def city_id(self, value):
        # 同样的，可以给对象的score增加setter
        return self.set('city_id', value)

    @city_name.setter
    def city_name(self, value):
        return self.set('city_name', value)

    @short_name.setter
    def short_name(self, value):
        return self.get('short_name', value)

    @city_pinyin.setter
    def city_pinyin(self, value):
        return self.set('city_pinyin', value)

    @short_pinyin.setter
    def short_pinyin(self, value):
        return self.set('short_pinyin', value)

    @geo_point.setter
    def geo_point(self, value):
        return self.set('geo_point', value)


def upload_city_info():
    url = 'http://apis.baidu.com/baidunuomi/openapi/cities'
    myApiKey = '1d1182a02878bfa992b58fff127959da'
    req = urllib2.Request(url)
    req.add_header("apikey", myApiKey)
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        # print(content)
        data = json.loads(content)
        cities = data["cities"]
        for ci in cities:
            # save city record to LeanCloud
            print(ci)
            city = City()
            city.set('city_id', ci["city_id"])
            city.set('city_name', ci["city_name"])
            city.set('city_pinyin', ci["city_pinyin"])
            city.set('short_name', ci["short_name"])
            city.set('short_pinyin', ci["short_pinyin"])

            city_name = ci["city_name"].encode('utf-8')
            print(city_name)
            lat, lon = get_coordinates(ci["city_name"])
            point = GeoPoint(latitude=lat, longitude=lon)
            city.set("geo_point", point)
            city.save()

if __name__ == "__main__":
    upload_city_info()