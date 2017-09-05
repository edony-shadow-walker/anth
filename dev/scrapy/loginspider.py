# -*- coding: utf-8 -*-
import scrapy


class LoginspiderSpider(scrapy.Spider):
    name = "loginspider"
    #allowed_domains = ["quotes.toscrape.com/login"]
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        # extract csrf token value
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        # create a python dictionary with the form values
        data = {
                'csrf_token': token,
                'username': 'abc',
                'password': 'abc',
               }
        # submit a Post request to it
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quotes)

    def parse_quotes(self, response):
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                    'author name': quote.css('small.author::text').extract_first(),
                    'text': quote.css('span.text::text').extract_first(),
                    'tag': quote.css('a.tag::text').extract(),
                    }
            yield item
