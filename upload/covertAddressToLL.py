# -*- coding:gb2312 -*-
# encoding: utf-8
import os
import leancloud
from leancloud import Object
from leancloud import Query
from gevent import monkey
from leancloud import GeoPoint
from get_coordinates import get_coordinates
import string

monkey.patch_all()

from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError

leancloud.use_region('CN')

#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', 'ew9zGSqucKA9iPA8QpujFvGK')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', 'uA8skpMa6SKLrGr8MRGueBJ4')

# 或者您现在需要使用 master key 的权限
#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', master_key='eh5FdcA7o3xwMTLCUQluRDmJ')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', master_key='1ndDPyrzINegIp4WNcJDFGAd')

class Business(Object):
    @property
    def objectId(self):
        return self.get('objectId')

    @property
    def shop_name(self):
    # 可以使用property装饰器，方便获取属性
        return self.get('shop_name')

    @property
    def food_img_url(self):
        return self.get('food_img_url')

    @property
    def rank_star(self):
        return self.get('rank_star')

    @property
    def reviews(self):
        return self.get('reviews')

    @property
    def cost_person(self):
        return self.get('cost_person')

    @property
    def taste_score(self):
        return self.get('taste_score')

    @property
    def environment_score(self):
        return self.get('environment_score')

    @property
    def service_score(self):
        return self.get('service_score')

    @property
    def address(self):
        return self.get('address')

    @property
    def phone(self):
        return self.get('phone')

    @property
    def open_time(self):
        return self.get('open_time')

    @property
    def homepage(self):
        return self.get('homepage')

    @property
    def collectedAt(self):
        return self.get('collectedAt')

    @property
    def geo_point(self):
        return self.get('geo_point')

    @shop_name.setter
    def shop_name(self, value):
        # 同样的，可以给对象的score增加setter
        return self.set('shop_name', value)

    @food_img_url.setter
    def food_img_url(self, value):
        return self.set('food_img_url', value)

    @rank_star.setter
    def rank_star(self, value):
        return self.get('rank_star', value)

    @reviews.setter
    def reviews(self, value):
        return self.set('reviews', value)

    @cost_person.setter
    def cost_person(self, value):
        return self.set('cost_person', value)

    @taste_score.setter
    def taste_score(self, value):
        return self.set('taste_score', value)

    @environment_score.setter
    def environment_score(self, value):
        return self.set('environment_score', value)

    @service_score.setter
    def service_score(self, value):
        return self.set('service_score', value)

    @address.setter
    def address(self, value):
        return self.set('address', value)

    @phone.setter
    def phone(self, value):
        return self.set('phone', value)

    @homepage.setter
    def open_time(self, value):
        return self.set('open_time', value)

    @homepage.setter
    def homepage(self, value):
        return self.set('homepage', value)

    @collectedAt.setter
    def collectedAt(self, value):
        return self.set('collectedAt', value)

    @collectedAt.setter
    def geo_point(self, value):
        return self.set('geo_point', value)

def run():
    while 1:
        query = Query(Business)
        query.equal_to('geo_point', None)

        current_business = query.first()
        temp = current_business.address.values()
        current_address = " ".join(temp).replace("(", " ").replace(")", " ").replace(u'号', " ")

        try:
            lat, lon = get_coordinates(current_address)
            if lat == None or lon == None:
                print(1)
                lat, lon = get_coordinates(temp[1]+" "+temp[0]+" "+temp[2])
            if lat == None or lon == None:
                print(2)
                lat, lon = get_coordinates(temp[0] + " " + temp[1])
            if lat == None or lon == None:
                print(3)
                lat, lon = get_coordinates(current_address[:current_address.find(u'号')])
            if lat == None or lon == None:
                print(4)
                lat, lon = get_coordinates(temp[0]+" "+temp[2])
            if lat == None or lon == None:
                print(5)
                lat, lon = get_coordinates(current_address.translate(None, string.digits))
        except (ValueError, TypeError):
            lat = 0
            lon = 0
            print("ERROR: ", current_business.attributes)
            print("----------------------------------------------")

        point = GeoPoint(latitude=lat, longitude=lon)
        current_business.set("geo_point", point)
        current_business.save()


if __name__ == "__main__":
    run()
