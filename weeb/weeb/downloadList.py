from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import csv
from time import time
from multiprocessing import Pool


def fetchList():
    process = CrawlerProcess(get_project_settings())
    process.crawl('anime_url_list')
    process.start()


def download(url):
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl('anime_count', url=url)
        process.start()
    except Exception as e:
        raise e


if __name__ == "__main__":
    fetchList()
    start = time()
    with open('items.csv', newline='') as f:
        urls = []
        csv = csv.reader(f, delimiter=' ')
        next(csv, None)
        for url in csv:
            urls.append(url[0])
        urls.reverse()
    try:
        p = Pool(processes=None, maxtasksperchild=1,)
        p.imap_unordered(download, urls)
        p.close()
        p.join()
    except Exception as e:
        raise e
    finally:
        print("----- %s seconds -----" % (round(time() - start)))
