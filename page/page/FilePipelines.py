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

        # fname = '/Users/shenzhenyuan/Desktop/zhenyuan/myDianping/output/page_output/' + "business_" + item['file_id'] + '.txt'
        fname = '/Users/shenzhenyuan/Desktop/page_output/' + "business_" + item['file_id'] + '.txt'

        try:
            outfile = open(fname, 'wt')
            line = self.getJobFieldSpt().join([
                item['shop_name'],
                item['food_img_url'],
                item['rank_star'],
                str(item['reviews']),
                str(item['cost_person']),
                str(item['taste_score']),
                str(item['environment_score']),
                str(item['service_score']),
                item['city'],
                item['local_region'],
                str(item['latitude']),
                str(item['longitude']),
                item['street_address'],
                ",".join(item['phone']),
                item['open_time'],
                item['homepage'],
                self.getCurrentTimestamp()
            ])
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
        return " [&%@$] "