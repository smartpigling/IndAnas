import scrapy
from scrapy_splash import SplashRequest
from CtripBot.items import HotelItem

class CtripHotelSpider(scrapy.Spider):
    name = 'ctrip_hotel'
    start_urls = [
        'http://hotels.ctrip.com/hotel/chongqing4/p0',
    ]

    def start_requests(self):
        for request_url in self.start_urls:
            yield SplashRequest(request_url, self.parse_page)
    
    def parse_page(self, response):
        for hotel_item in response.xpath('//*[@id="hotel_list"]/div'):
            hotel_url = hotel_item.xpath('//div[@class="action_info"]/p/a/@href').extract_first()
            yield SplashRequest(response.urljoin(hotel_url), self.parse_details, args={'wait': 0.5,})

        next_href = response.xpath('//div[contains(@class, "c_page_list")]/a[@class="current"]/following-sibling::a[1]/@href').extract_first()
        if next_href is not None:
            yield SplashRequest(next_href, self.parse_page)

    
    def parse_details(self, response):
        item = HotelItem()
        item['hotel_name'] = response.xpath('//div[@class="htl_info"]/div[2]/h2[1]/text()').extract_first()
        item['hotel_addr'] = response.xpath('//div[@class="htl_info"]/div[@class="adress"]/span/text()').re('[^，\s*]\w+')
        item['hotel_addr_keys'] = response.xpath('//div[@class="htl_info"]/div[@class="adress"]/a/text()').extract()
        item['hotel_price'] = response.xpath('//p[@class="staring_price"]/span[@class="price"]/text()').extract_first()
        item['commnet_score'] = response.xpath('//div[@class="comment_total_score"]/span[@class="score"]/span/text()').extract_first()
        self.logger.info(dict(item))
        yield item