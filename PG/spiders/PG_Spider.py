# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import scrapy
import pprint

from gtts import gTTS
import os
import textract

class PgSpiderSpider(scrapy.Spider):
    name = 'PG_Spider'
    start_urls = ['http://paulgraham.com/articles.html']

    def parse(self, response):
        article_link = response.xpath('//font/a/@href').extract() 
        articles = []
        for item in article_link:
            articles.append("http://paulgraham.com/" + item)

        for link in articles:
            yield scrapy.Request(link, callback=self.parse_page)


    def parse_page(self, response):
        content = response.xpath('//font[1]/text()').extract()
        title = response.xpath('//img[1]/@alt').extract()

        scrubbed_content = []
        
        for item in content:
            if len(item) > 200:
                try:
                    scrubbed_content.append(item) 
                except IndexError:
                    pass
        
        #    item.rstrip()
        #" ".join(content) 
        #text = textract.process(content)
        #text = text.decode('utf-8')
        #tts = gTTS(text=text, lang='en')
        #tts.save(title + ".mp3")
        yield {'Title': title, 'Content': content}
