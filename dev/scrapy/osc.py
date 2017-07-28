#!/usr/bin/python3
# -*- coding: utf-8 -*-
import scrapy
import re

class OSCSpider(scrapy.Spider):
    agent_header = "Mozilla/5.0 (Windows NT 6.1; WOW64) \
13 AppleWebKit/537.1 (KHTML, like Gecko) \
Chrome/22.0.1207.1 Safari/537.1"
    name = "OSC"
    allowd_domains = ["oschina.net"]
    start_url = ['http://www.oschina.net/news/industry']
    def start_requests(self):
        agent_header = "Mozilla/5.0 (Windows NT 6.1; WOW64) \
13 AppleWebKit/537.1 (KHTML, like Gecko) \
Chrome/22.0.1207.1 Safari/537.1"
        yield scrapy.http.Request(self.start_url[0],
                                  headers={'User-Agent': agent_header})
    def _url_parser(self, url):
        if url.startswith('http'):
            return url
        else:
            return self.start_url[0] + url

    def _desc_parser(self, text):
        for desc in text:
            if re.match('\r\n +', desc) is not None:
                continue
            return desc

    def parse(self, response):
        self.log("[ANTH{<edony.OSC.SPIDER>}]Fetching the OSC news industry: " + response.url)
        xpath_reg = '//*[@id="kinds-of-news"]/div'
        for item in response.xpath(xpath_reg):
            url = self._url_parser(item.css('a::attr(href)').extract()[0])
            text = self._desc_parser(item.css('div::text').extract())
            yield {'url': url,
                   'text': text}
