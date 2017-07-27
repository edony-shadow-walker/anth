# -*- coding: utf-8 -*-
import scrapy

class OSCSpider(scrapy.Spider):
    name = "OSC"
    allowd_domains = ["oschina.net"]
    start_url = ['http://www.oschina.net/news/industry']
    def start_requests(self):
        yield scrapy.http.Request(self.start_url[0],
                                  headers={'User-Agent':
                                           "Mozilla/5.0 (Windows NT 6.1; WOW64) \
AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"})


    def parse(self, response):
        self.log("[ANTH::###{<edony.OSC.SPIDER>}###]Fetching the OSC: " + response.url)
        #with open('osc.html', 'wb') as filebuf:
        #   filebuf.write(response.body)
        xpath_reg = '//*[@id="kinds-of-news"]/div[{}]'
        flags = [item for item in range(1, 10)]
        for count in flags:
            url_ = response.xpath(xpath_reg.format(count)).css('a::attr(href)').extract()
            text_ = response.xpath(xpath_reg.format(count)).css('div::text').extract()
            for url in url_:
                print('[###]' + url + '[!!!]')
            for text in text_:
                print('[###]' + text + '[!!!]')
            #url = url_.css('a::attr(href)').extract_first()
            #if url is not None:
            #    if url.startswith('/'):
            #        url = self.start_url[0] + url
            #   self.log("[ANTH::***{<edony.OSC.SPIDER.XPATH.SELECTOR>}***]Fetching the OSC: " + url)
