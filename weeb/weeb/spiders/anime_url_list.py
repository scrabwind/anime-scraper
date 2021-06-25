from scrapy import Spider
from scrapy.http import Request
from weeb.items import AnimeUrlList
from scrapy.loader import ItemLoader


class AnimeUrlSpider(Spider):
    name = "anime_url_list"
    start_urls = ['https://www1.animeshow.tv/anime-list.html']
    custom_settings = {
        'FEEDS': {
            'items.csv': {
                'format': 'csv',
                'fields': ['anime_url'],
                'overwrite': True
            }
        }
    }

    def parse(self, response):
        groups = response.xpath('//*[@id="anime_list"]/div')
        for group in groups:
            rows = group.xpath('ul/li')
            for row in rows:
                loader = ItemLoader(item=AnimeUrlList())
                url = row.xpath('a/@href').get()
                loader.add_value('anime_url', url)
                yield loader.load_item()
