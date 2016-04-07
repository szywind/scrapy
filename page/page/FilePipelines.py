# encoding: utf-8
import sys
import traceback
import datetime
sys.path.append("../../../")
reload(sys)
sys.setdefaultencoding("utf-8")

class PagePipeline(object):
    
    #把解析后的内容放入文件中
    def process_item(self, item, spider):

        fname = '/Users/shenzhenyuan/Desktop/zhenyuan/myDianping/output/page_output/' + "business_" + item['file_id'] + '.txt'
        try:
            outfile = open(fname, 'wb')
            line = item['shop_name']+self.getJobFieldSpt()+item['food_img_url']+self.getJobFieldSpt()\
                          +item['rank_star']+self.getJobFieldSpt()+str(item['reviews'])+self.getJobFieldSpt()\
                          +str(item['cost_person'])+self.getJobFieldSpt()+str(item['taste_score'])+self.getJobFieldSpt()\
                          +str(item['environment_score'])+self.getJobFieldSpt()+str(item['service_score'])+self.getJobFieldSpt()\
                          +item['city']+self.getJobFieldSpt()+item['local_region']+self.getJobFieldSpt()\
                          +item['street_address']+self.getJobFieldSpt()+",".join(item['phone'])+self.getJobFieldSpt()\
                          +item['open_time']+self.getJobFieldSpt()+item['homepage']+self.getJobFieldSpt()+self.getCurrentTimestamp()
            outfile.write(line)

        except Exception as e:
            print "ERROR GEN FILE!! >>> " + fname
            print traceback.format_exc()

    def getCurrentTimestamp(self):
	# 得到时间戳
	    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def getJobFieldSpt(self):
	#得到生成的职位文件字段间的分隔符。使用ascii码1，和hive中默认的分隔符相同        
	    # return chr(1)
        return "    "