# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    rating = Field()
    rank = Field()
    cover_url = Field()
    is_playable = Field()
    types = Field()
    regions = Field()
    title = Field()
    url = Field()
    release_date = Field()
    actor_count = Field()
    vote_count = Field()
    score = Field()
    actors = Field()
    is_watched = Field()