# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapamazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.in/Books-Last-30-days/s?i=stripbooks&bbn=1318158031&rh=n%3A976389031%2Cn%3A1318158031%2Cp_n_publication_date%3A2684819031%2Cp_n_availability%3A1318484031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_36%3A1741391031&dc&qid=1593872368&rnid=1741387031&ref=sr_nr_p_36_4'
    ]

    def parse(self, response):
        item = ScrapamazonItem()     ## creating object

        product_name = response.css(".a-color-base.a-text-normal").css("::text").extract()
        product_author = response.css(".a-color-secondary .a-size-base+ .a-size-base").css("::text").extract()
        product_price = response.css(".a-spacing-top-small .a-price-whole").css("::text").extract()
        product_imagelink = response.css(".a-spacing-top-small .a-price span").extract()

        item['product_name'] = product_name
        item['product_author'] = product_author
        item['product_price'] = product_price
        item['product_imagelink'] = product_imagelink

        yield item

