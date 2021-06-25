import scrapy
from scrapy.item import Item, Field


class WeebItem(scrapy.Item):
    pass


class AnimeEpisodeItem(Item):
    file_urls = Field()
    files = Field()
    episode_number = Field()
    weeb_name = Field()


class AnimeList(Item):
    episode_list = Field()


class AnimeUrlList(Item):
    anime_url = Field()


class AnimeCountItem(Item):
    title = Field()
    episode_count = Field()
    anime_url = Field()
