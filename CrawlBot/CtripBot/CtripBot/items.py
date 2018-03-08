# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class HotelItem(Item):
    hotel_name = Field()
    # 二星级及以下/经济  三星级/舒适  四星级/高档  五星级/豪华
    hotel_level = Field() 
    hotel_addr = Field()
    hotel_addr_keys = Field()
    hotel_price = Field()
    # 早餐: 无早, 含早餐  ;  床型: 大床, 双床 
    hotel_feature = Field()
    commnet_score = Field()

