# -*- coding: utf-8 -*-
# scrapy crawl movie
import scrapy

from db_movies.items import DbMoviesItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    }

    def parse(self, response):
        grid_view_li = response.css('.grid_view li')
        for data in grid_view_li:
            item = DbMoviesItem()
            ranking = data.css('.pic em::text').extract_first()
            name = data.css('.hd span::text').extract_first()
            actor = data.css('.bd p::text').extract()
            score = data.css('.star .rating_num::text').extract_first()

            item['ranking'] = ranking
            item['name'] = name
            item['actor'] = actor[0].strip()
            item['time'] = actor[1].strip()
            item['score'] = score
            yield item
        next_page = response.css('.paginator .next a::attr(href)').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            self.start_urls = url
            # dont_filter=True停用过滤
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)


    # def start_requests(self):
    #     urls = self.start_urls
    #     headers = {
    #         'accept-language': 'zh-CN,zh;q=0.9',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    #     }
    #     for url in urls:
    #         yield scrapy.Request(url=url, headers=headers, callback=self.parse, dont_filter=True)