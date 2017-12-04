# -*- coding: utf-8 -*-
import scrapy

# response.xpath('//font/a/@href').extract()

class PgSpiderSpider(scrapy.Spider):
    name = 'PG_Spider'
    allowed_domains = ['http://www.paulgraham.com/articles.html']
    start_urls = ['http://paulgraham.com/articles.html']

    def parse(self, response):
        article_link = response.xpath('//font/a/@href').extract()
        article_name = response.xpath('//font/a/text()').extract()

        yield {'Article Name': article_name, 'Article URL': article_link}
