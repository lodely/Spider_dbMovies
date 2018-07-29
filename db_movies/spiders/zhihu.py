# -*- coding: utf-8 -*-
# scrapy crawl zhihu
import scrapy

from db_movies.items import zhihuItem


class zhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            # 'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    }

    def parse(self, response):
        print(response.text)