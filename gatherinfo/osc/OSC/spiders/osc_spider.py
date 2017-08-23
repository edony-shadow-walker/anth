#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import logging
import scrapy
from scrapy.selector import Selector
from OSC.items import OscItem

class OSCSpider(scrapy.Spider):
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
        return self.start_url[0] + url

    def parse(self, response):
        # setup log
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.basicConfig(level=logging.DEBUG,
                            format=
                            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='cataline.log',
                            filemode='w')

        self.log("[ANTH] parsing OSC news industry: " + response.url)
        selector = Selector(response)
        if selector.xpath('//*[@id="all-news"]/div[*]/div[*]/a[@href]').\
                css('a::attr(href)').extract():
            logging.debug('[ANTH] parse url: ' + self.start_url[0])
            item = OscItem()
            selector = Selector(response)
            hrefs = selector.xpath('//*[@id="all-news"]/div[*]/div[*]/a[@href]').\
                    css('a::attr(href)').extract()
            hrefs = list(set(hrefs))
            for link_item in hrefs:
                item['link'] = self._url_parser(link_item)
                reg = '//*[@href="{}"]/span'.format(link_item)
                if selector.xpath(reg).extract_first():
                    item['description'] = selector.xpath(reg).css('span::text').extract_first()
                else:
                    item['description'] = ''
                yield item

        # next page
        url_next = selector.xpath('//*[@id="all-news"]/a[@href]').css('a::attr(href)').extract()
        logging.debug(url_next)
        if url_next:
            # if self.test:
            logging.debug('[ANTH] next page: ' + self.start_url[0] + url_next[0])
            #yield scrapy.http.Request(url=self.start_url[0] + url_next[0],
            #              callback=self.parse)
