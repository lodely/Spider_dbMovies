# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DbMoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    name = scrapy.Field()
    time = scrapy.Field()
    actor = scrapy.Field()
    score = scrapy.Field()

class zhihuItem(scrapy.Item):
    pass
