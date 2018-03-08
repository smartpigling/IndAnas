import scrapy


class CtripSpider(scrapy.Spider):
    name = 'ctrip'

    def start_requests(self):
        pass
    
    def parse(self, response):
        pass