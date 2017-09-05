# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                    'author name': quote.css('small.author::text').extract_first(),
                    'text': quote.css('span.text::text').extract_first(),
                    'tag': quote.css('a.tag::text').extract(),
                    }
            yield item

#        yield {
#                'author name': response.css('small.author::text').extract_first(),
#                'text': response.css('span.text::text').extract_first(),
#                'tag': response.css('a.tag::text').extract(),
#        }
