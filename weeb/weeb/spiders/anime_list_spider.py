from scrapy import Spider
from scrapy.http import Request
from weeb.items import AnimeList


class AnimeListSpider(Spider):
    name = "anime_list"
    custom_settings = {
        "FEEDS": {
            'episodes.csv': {
                'format': 'csv',
                'fields': ['episode_list'],
                'overwrite': True
            }}
    }

    def start_requests(self):
        yield Request(url=self.url, callback=self.parse)

    def parse(self, response):
        episodes = response.css('#episodes_list > div')
        for episode in episodes:
            item = AnimeList()
            item['episode_list'] = episode.xpath('a/@href').extract()

            yield item
