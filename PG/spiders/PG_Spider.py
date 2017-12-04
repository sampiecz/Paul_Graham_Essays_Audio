# -*- coding: utf-8 -*-
import scrapy


class PgSpiderSpider(scrapy.Spider):
    name = 'PG_Spider'
    allowed_domains = ['http://www.paulgraham.com/articles.html']
    start_urls = ['http://http://www.paulgraham.com/articles.html/']

    def parse(self, response):
        pass
