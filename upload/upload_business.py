# -*- coding:gb2312 -*-
# encoding: utf-8
import os
import leancloud
from leancloud import Object
from leancloud import Query
from leancloud import GeoPoint
from gevent import monkey
monkey.patch_all()

from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError

leancloud.use_region('CN')

#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', 'ew9zGSqucKA9iPA8QpujFvGK')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', 'uA8skpMa6SKLrGr8MRGueBJ4')

# 或者您现在需要使用 master key 的权限
#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', master_key='eh5FdcA7o3xwMTLCUQluRDmJ')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', master_key='1ndDPyrzINegIp4WNcJDFGAd')

spliter = " [&%@$] "
class Business(Object):
    '''
    def __init__(self, shop_name, food_img_url, rank_star, reviews, cost_person, taste_score, environment_score,\
                       service_score, city, local_region, street_address, phone, open_time, homepage):
        super.__init__(self)
        self.shop_name = shop_name
        self.food_img_url = food_img_url
        self.rank_star = rank_star
        self.reviews = reviews
        self.cost_person = cost_person
        self.taste_score = taste_score
        self.environment_score = environment_score
        self.service_score = service_score
        self.address = {
            "city": city,
            "region": local_region,
            "street": street_address
        }
        self.phone = phone
        self.open_time = open_time
        self.homepage = homepage

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

    @shop_name.setter
    def shop_name(self):
        # 同样的，可以给对象的score增加setter
        return self.set('shop_name', self.shop_name)

    @food_img_url.setter
    def food_img_url(self):
        return self.set('food_img_url', self.food_img_url)

    @rank_star.setter
    def rank_star(self):
        return self.get('rank_star', self.rank_star)

    @reviews.setter
    def reviews(self):
        return self.set('reviews', self.reviews)

    @cost_person.setter
    def cost_person(self):
        return self.set('cost_person', self.cost_person)

    @taste_score.setter
    def taste_score(self):
        return self.set('taste_score', self.taste_score)

    @environment_score.setter
    def environment_score(self):
        return self.set('environment_score', self.environment_score)

    @service_score.setter
    def service_score(self):
        return self.set('service_score', self.service_score)

    @address.setter
    def address(self):
        return self.set('address', self.address)

    @phone.setter
    def phone(self):
        return self.set('phone', self.phone)

    @homepage.setter
    def open_time(self):
        return self.set('open_time', self.open_time)

    @homepage.setter
    def homepage(self):
        return self.set('homepage', self.homepage)
    '''


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


    @geo_point.setter
    def geo_point(self, value):
        return self.set('geo_point', value)

def already_exist(q_homepage):
    '''
    Check whether the item has already existed in the DB
    :param q_homepage:
    :return: Business object
    '''
    try:
        query = Query(Business)
        query.equal_to('homepage', q_homepage)
        # print("query.count = ", query.count())
        assert(query.count() <= 1)
        current_business = query.first()
        return current_business
    except leancloud.errors.LeanCloudError:
        return None

def upload_one_file(filename):
    '''
    Upload one file's content to LeanCloud
    :param filename: file name
    :return:
    '''

    try:
        with open(filename, "rt") as fl:
            segments = fl.readlines()
            segments = "".join(segments).replace('\n','').replace('\r','').replace('\t','').strip().split(spliter)

            if(len(segments) != 17):
                return False

            # check if the item is already exist in the db
            business = already_exist(segments[15])

            if business is None:
                business = Business()

            elif business.get("geo_point") != None:
                return True

            print(filename)

            try:
                business.set('shop_name', segments[0])
            except (TypeError, IndexError):
                print(filename)
                print('shop_name')
                return False

            try:
                business.set('food_img_url', segments[1])
            except (TypeError, IndexError):
                print(filename)
                print('food_img_url')
                return False

            try:
                business.set('rank_star', segments[2][-2:])
            except (TypeError, IndexError):
                print(filename)
                print('rank_star')
                return False
            try:
                business.set('reviews', segments[3])
            except (TypeError, IndexError):
                print(filename)
                print('reviews')
                return False

            try:
                business.set('cost_person', segments[4])
            except (TypeError, IndexError):
                print(filename)
                print('cost_person')
                return False

            try:
                business.set('taste_score', segments[5])
            except (TypeError, IndexError):
                print(filename)
                print('taste_score')
                return False

            try:
                business.set('environment_score', segments[6])
            except (TypeError, IndexError):
                print(filename)
                print('environment_score')
                return False

            try:
                business.set('service_score', segments[7])
            except (TypeError, IndexError):
                print(filename)
                print('service_score')
                return False

            try:
                business.set('address', {
                "city": segments[8],
                "region": segments[9],
                "street": segments[12]
            })
            except (TypeError, IndexError):
                print(filename)
                print('address')
                return False

            try:
                business.set('phone', segments[13].split(","))
            except (TypeError, IndexError):
                print(filename)
                print('phone')
                return False

            try:
                business.set('open_time', segments[14])
            except (TypeError, IndexError):
                print(filename)
                print('open_time')
                return False

            try:
                business.set('homepage', segments[15])
            except (TypeError, IndexError):
                print(filename)
                print('homepage')
                return False

            try:
                business.set('collectedAt', segments[16])
            except (TypeError, IndexError):
                print(filename)
                print('collectedAt')
                return False

            try:
                lat = float(segments[10])
                lon = float(segments[11])
                point = GeoPoint(latitude=lat, longitude=lon)
                business.set("geo_point", point)
            except (ValueError, TypeError, IndexError):
                print(filename)
                print('geo_point')
                return False

            business.save()
            return True

    except (ReadTimeout, ConnectionError):
        return False

if __name__ == "__main__":
    dir_path = "/Users/shenzhenyuan/Desktop/page_output/"
    # file_names = os.listdir(dir_path)

    with open("/Users/shenzhenyuan/Desktop/temp.txt", "r") as leftBusiness: #leftBusiness
        file_names = leftBusiness.readlines()

    for file_name in file_names:

        if upload_one_file(dir_path+file_name.strip()):

            file_names.remove(file_name)

    with open("/Users/shenzhenyuan/Desktop/new.txt", "w") as leftBusiness:
        for i in file_names:
            leftBusiness.write(i)



def getSegment(fname):
    with open(fname, 'r') as fl:
        segments = fl.readlines()
        segments = "".join(segments).replace('\n', '').replace('\n', '').replace('\r', '').replace('\t', '').strip().split(spliter)
    return segments

