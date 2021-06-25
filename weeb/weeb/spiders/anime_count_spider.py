from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from weeb.items import AnimeCountItem


class AnimeCountSpider(Spider):
    name = "anime_count"
    custom_settings = {
        "ITEM_PIPELINES": {'weeb.pipelines.AnimeCountPipeline': 1, }
    }

    def start_requests(self):
        print(self.url)
        yield Request(url=self.url, callback=self.parse)

    def parse(self, response):
        try:
            loader = ItemLoader(item=AnimeCountItem(), response=response)
            loader.add_value('anime_url', response.url)
            loader.add_xpath('title', '//*[@id="anime"]/h1/text()')
            loader.add_value('episode_count', len(
                response.css('#episodes_list > div')))
            yield loader.load_item()
        except Exception as e:
            raise e
