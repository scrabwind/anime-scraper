from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import csv
from time import time
from multiprocessing import Pool
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--ran', type=int, nargs=2)
parser.add_argument('--url', type=ascii, nargs=1)
args = vars(parser.parse_args())
url_list = args['url'][0]
ran = args['ran']


def preFetch():
    process = CrawlerProcess(get_project_settings())
    process.crawl('anime_list',
                  url=url_list)
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
        urls = urls[ran[0]-1:ran[1]]
    try:
        p = Pool(processes=None, maxtasksperchild=1)
        p.map_async(download, urls)
        p.close()
        p.join()
    except Exception as e:
        raise e
    finally:
        print("----- %s seconds -----" % (round(time() - start)))
