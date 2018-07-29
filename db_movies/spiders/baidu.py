# -*- coding: utf-8 -*-
# scrapy crawl baidu
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass

    # 修改回调函数
    def make_requests_from_url(self, url):
        return scrapy.Request(url=url, callback=self.parse_index)

    def parse_index(self, response):
        print('baidu', response.status)
