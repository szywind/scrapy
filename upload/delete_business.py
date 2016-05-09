# -*- coding:gb2312 -*-
# encoding: utf-8
import leancloud
from leancloud import Object
from leancloud import Query
from gevent import monkey
monkey.patch_all()

leancloud.use_region('CN')

#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', 'ew9zGSqucKA9iPA8QpujFvGK')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', 'uA8skpMa6SKLrGr8MRGueBJ4')

# 或者您现在需要使用 master key 的权限
#leancloud.init('98Cd74VcfnCth6nNWdb4R10D-gzGzoHsz', master_key='eh5FdcA7o3xwMTLCUQluRDmJ')
leancloud.init('6PQXOhQhDC4BmC2osjdMlPR1-gzGzoHsz', master_key='1ndDPyrzINegIp4WNcJDFGAd')

spliter = " [&%@$] "
class Business(Object):

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


def already_exist(q_homepage):
    '''
    Check whether the item has already existed in the DB
    :param q_homepage:
    :return:
    '''
    try:
        query = Query(Business)
        query.equal_to('homepage', q_homepage)
        # current_business = query.first()
        current_business =query.find()
        for i in current_business:
            i.destroy()
        return current_business
    except leancloud.errors.LeanCloudError:
         return None

def delete_one_file(filename):
    '''
    Upload one file's content to LeanCloud
    :param filename: file name
    :return:
    '''

    if 1:
        with open(filename, "rt") as fl:
            segments = fl.readlines()
            segments = "".join(segments).replace('\n','').replace('\r','').replace('\t','').strip().split(spliter)

            print("file: ", filename)

            if(len(segments) != 17):
                return False

            # check if the item is already exist in the db
            business = already_exist(segments[15])


if __name__ == "__main__":
    dir_path = "/Users/shenzhenyuan/Desktop/page_output/"
    # file_names = os.listdir(dir_path)

    with open("/Users/shenzhenyuan/Desktop/temp.txt", "r") as leftBusiness: #leftBusiness
        file_names = leftBusiness.readlines()

    for file_name in file_names:
        delete_one_file(dir_path + file_name.strip())


def getSegment(fname):
    with open(fname, 'r') as fl:
        segments = fl.readlines()
        segments = "".join(segments).replace('\n', '').replace('\n', '').replace('\r', '').replace('\t', '').strip().split(spliter)
    return segments

