from scrapy import Spider
from scrapy.http import Request
from selenium import webdriver
from weeb.items import AnimeEpisodeItem
from scrapy.loader import ItemLoader
import time


class AnimeSpider(Spider):
    name = 'anime_episode'
    # allowed_domains = ['animeshow.tv', 'vidstreaming.io', 'gogo-stream.com']
    custom_settings = {
        "ITEM_PIPELINES": {'weeb.pipelines.EpisodeNamesPipeline': 1, }
    }

    def start_requests(self):
        yield Request(url=self.url, callback=self.parseSite)

    def parseSite(self, response):
        try:
            url = response.css('.embed-responsive-item::attr(src)').get()
            yield Request(url=url, callback=self.parseVideo)
        except Exception as e:
            raise e

    def parseVideo(self, response):
        options = webdriver.FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        options.set_preference("dom.popup_maximum", 0)
        options.set_preference("dom.disable_window_flip", True)
        profile.set_preference("media.volume.scale", "0.0")
        options.headless = True
        try:
            sel = webdriver.Firefox(
                options=options, firefox_profile=profile)
            sel.get(response.url)
            time.sleep(1)
            sel.execute_script(
                'document.getElementsByTagName("video")[0].click()')
            time.sleep(.5)
            sel.find_element_by_css_selector('.jw-icon-display').click()
            selector = sel.find_elements_by_css_selector(
                'video')[0]
            url = selector.get_attribute('src')

            ep_num = self.url.split('-')[-1][:-1]
            weeb_name = self.url.split('-episode')[0].split('/')[-1]
            loader = ItemLoader(item=AnimeEpisodeItem())
            loader.add_value('file_urls', url)
            loader.add_value('episode_number', ep_num)
            loader.add_value('weeb_name', weeb_name)
            yield loader.load_item()
        except Exception as e:
            raise e
        finally:
            sel.close()
