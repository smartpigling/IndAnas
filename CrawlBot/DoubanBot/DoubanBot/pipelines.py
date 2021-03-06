# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import MovieItem

class DoubanbotPipeline(object):
    def open_spider(self, spider):
        self.file = open('douban_movie.txt', 'w')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.seek(self.file.tell() -2 , 0)
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, MovieItem):
            line = json.dumps(dict(item)) + ',\n'
            self.file.write(line)
            return item
        
