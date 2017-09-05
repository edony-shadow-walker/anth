import scrapy
from antspi.items import AntspiItem

class AntspiSpider(scrapy.Spider):
    name = "antspi"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
                  "http://stackoverflow.com/questions?pagesize=50&sort=newest",
                 ]
    def parse(self, response):
        questions = scrapy.Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = AntspiItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
