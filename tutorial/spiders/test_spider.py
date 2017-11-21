# -*- coding: utf-8 -*-

import scrapy

from tutorial.items import DmozItem

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["http://dmoztools.net/"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/",
    ]

    def parse(self, response):
        for href in response.css("div.cat-item > a::attr('href')"):
            print('url list:', response.url, '------href: ', href.extract())
            url = response.urljoin(response.url, href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//*[@id="site-list-content"]/div[1]/div[3]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/div/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('div/text()').extract()
            yield item