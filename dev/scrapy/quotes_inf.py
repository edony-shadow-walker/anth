# -*- coding: utf-8 -*-
import scrapy
import json


class QuotesInfSpider(scrapy.Spider):
    name = "quotes_inf"
    allowed_domains = ["toscrape.com"]
    url_api = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [url_api.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                    'author name': quote['author']['name'],
                    'text': quote['text'],
                    'tags': quote['tags'],
                  }
            if data['has_next']:
                next_page = data['page'] + 1
                yield scrapy.Request(url=self.url_api.format(next_page), callback=self.parse)
