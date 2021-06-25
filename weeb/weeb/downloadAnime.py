from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import csv
from time import time
from multiprocessing import Pool


def preFetch():
    process = CrawlerProcess(get_project_settings())
    process.crawl('anime_list',
                  url='https://www1.animeshow.tv/Tokyo-Revengers/')
    process.start()


def download(url):
    process = CrawlerProcess(get_project_settings())
    process.crawl('anime_episode', url=url)
    process.start()


if __name__ == "__main__":
    preFetch()
    start = time()
    with open('episodes.csv', newline='') as f:
        urls = []
        csv = csv.reader(f, delimiter=' ')
        next(csv, None)
        for url in csv:
            urls.append(url[0])
        urls.reverse()
    try:
        p = Pool(processes=None, maxtasksperchild=1)
        p.map_async(download, urls)
        p.close()
        p.join()
    except Exception as e:
        raise e
    finally:
        print("----- %s seconds -----" % (round(time() - start)))
