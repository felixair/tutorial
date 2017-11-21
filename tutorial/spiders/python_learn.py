# -*- coding: utf-8 -*-

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "pythonlist"
    allowed_domains = ["readthedocs.io"]
    start_urls = [
        "http://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html"
    ]

    def parse(self, response):
        for href in response.css("div.wy-menu > ul > li > a::attr('href')"):
            url = response.urljoin(response.url, href.extract())
            print(url)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
