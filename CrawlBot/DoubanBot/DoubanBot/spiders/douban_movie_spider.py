import scrapy
import json
from DoubanBot.items import MovieItem

class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/j/chart/top_list_count?type=%d&interval_id=100:90' % x for x in range(100)
    ]

    def start_requests(self):
        for request_url in self.start_urls:
            yield scrapy.Request(url=request_url, callback=self.parse)

    
    def parse(self, response):
        results = json.loads(response.body_as_unicode())
        total = results['total']
        if total and total > 0:
            yield scrapy.Request(response.url.replace('_count', '')+'&action=&start=0&limit=%d' % total
                                , callback=self.parse_content)

    def parse_content(self, response):
        results = json.loads(response.body_as_unicode())
        for result in results:
            m_item = MovieItem()
            m_item['id'] = result['id']
            m_item['title'] = result['title']
            m_item['rating'] = result['rating']
            m_item['rank'] = result['rank']
            m_item['cover_url'] = result['cover_url']
            m_item['is_playable'] = result['is_playable']
            m_item['types'] = result['types']
            m_item['regions'] = result['regions']
            m_item['url'] = result['url']
            m_item['release_date'] = result['release_date']
            m_item['actor_count'] = result['actor_count']
            m_item['vote_count'] = result['vote_count']
            m_item['score'] = result['score']
            m_item['actors'] = result['actors']
            m_item['is_watched'] = result['is_watched']
            yield m_item