# encoding: utf-8

from scrapy.item import Item, Field

#定义存放帖子内容的类
class PageItem(Item):
    #生成的文件名
    file_id = Field()
    #商业名字
    shop_name = Field()
    #食物图片
    food_img_url = Field()
    #评分
    rank_star = Field()
    #评论数
    reviews = Field()
    #人均花费
    cost_person = Field()
    #口味
    taste_score = Field()
    #环境
    environment_score = Field()
    #服务
    service_score = Field()
    #城市
    city = Field()
    #区
    local_region = Field()
    #街道
    street_address = Field()
    #电话
    phone = Field()
    #营业时间
    open_time = Field()
    #主页
    homepage = Field()