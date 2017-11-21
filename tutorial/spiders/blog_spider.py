# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import DmozItem

class BlogSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        'https://blog.scrapinghub.com'
    ]

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            item = DmozItem()
            item['title'] = title.css('a ::text').extract_first()
            yield item
        
        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

