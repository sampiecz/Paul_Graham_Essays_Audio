# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import scrapy
import pprint

from gtts import gTTS
import os
import textract
from bs4 import BeautifulSoup

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
        raw_content = response.xpath('//font').extract()
        title = response.xpath('//img[1]/@alt').extract_first()

        joined_raw_content = " ".join(raw_content) 
        soup = BeautifulSoup(joined_raw_content, 'html.parser')
        no_html_tags = soup.get_text()
        no_end_lines = no_html_tags.replace("\n"," ")
        no_comma_slashes = no_end_lines.replace("\'", "'")
        no_slashes = no_comma_slashes.replace("\\", "")
        content = no_slashes

        
        #    item.rstrip()
        #" ".join(content) 
        #text = textract.process(content)
        #text = text.decode('utf-8')
        #tts = gTTS(text=text, lang='en')
        #tts.save(title + ".mp3")
        yield {'Title': title, 'Content': content}
