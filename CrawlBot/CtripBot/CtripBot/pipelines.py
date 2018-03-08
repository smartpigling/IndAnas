# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import logging
from scrapy.conf import settings
from .items import HotelItem


logger = logging.getLogger('pipeline')
logger.setLevel(logging.WARNING)

class HotelPipeline(object):
    def __init__(self, *args, **kwargs):
        client = pymongo.MongoClient(host=settings['MONGODB_HOST'], 
                                    port=settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DBNAME']]
        self.table = db['hotel']

    def process_item(self, item, spider):
        if isinstance(item, HotelItem):
            self.table.update_one({'hotel_name': item['hotel_name']}, {'$set': dict(item)}, upsert=True)


class CtripbotPipeline(object):
    def process_item(self, item, spider):
        return item
