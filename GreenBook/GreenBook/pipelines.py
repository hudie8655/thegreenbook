# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class GreenBookPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        self.file = open('test.json','a')
	self.file.write(json.dumps({'name':item['name']})+'\n')
        self.file.close() 
        return item

    def spider_closed(self,spider):
        pass
