# encoding: utf-8

from scrapy.item import Item, Field

#定义存放帖子内容的类
class PageItem(Item):
    #网站标识
    web_id = Field()
    #生成的文件名
    file_id = Field()
    #职位来源网址
    job_url = Field()
    #工作名称
    job_name = Field()
    #工作地点    
    job_location = Field()
    #职位描述 
    job_desc = Field()
    #学历要求   
    edu = Field()
    #性别要求      
    gender = Field()
    #语言要求       
    language = Field()
    #专业要求        
    major = Field()
    #工作年限    
    work_years = Field()
    #薪水范围         
    salary = Field()
    #职位发布时间
    job_datetime = Field()
    #公司名称      
    company_name = Field()
    #企业介绍
    company_desc = Field()
    #公司地址
    company_address = Field()
    #行业
    company_worktype = Field()
    #规模
    company_scale = Field()
    #性质
    company_prop = Field()
    #网址
    company_website = Field()
