# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import DmozItem

class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = [
        'https://blog.scrapinghub.com'
    ]

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            item = DmozItem()
            item['title'] = title.css('a ::text').extract_first()   #extract_first()返回字符串 extract()返回数组
            item['link'] = title.css('a ::attr("href")').extract_first()
            yield item
        
        #各个页面数据循环获取
        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page, self.parse)

