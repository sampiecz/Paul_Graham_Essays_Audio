# -*- coding: utf-8 -*-
import scrapy
import pprint

# response.xpath('//font/a/@href').extract()

class PgSpiderSpider(scrapy.Spider):
    name = 'PG_Spider'
    #allowed_domains = ['http://www.paulgraham.com/articles.html']
    start_urls = ['http://paulgraham.com/articles.html']

    def parse(self, response):
        article_link = response.xpath('//font/a/@href').extract()
        article_name = response.xpath('//font/a/text()').extract()

        #yield {'Article Name': article_name, 'Article URL': article_link}

        articles = {}

        num = 0
        for item in article_link:
            articles[article_name[num]] = "http://paulgraham.com/" + item
            num+=1


        # to extract each article: sel.xpath('//font/text()').extract()
        # print(articles.items())
        for link in articles.values():
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self, response):
        body = response.xpath('//font/text()').extract()
        print(body)
