# -*- coding: utf-8 -*-
import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['www.amazon.in']
    start_urls = ['http://www.amazon.in/']

    def parse(self, response):
        pass
