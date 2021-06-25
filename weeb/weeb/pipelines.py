
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy.exporters import JsonItemExporter
import json
import requests
from requests.auth import HTTPBasicAuth


# class JsonWriterPipeline:
#     def open_spider(self, spider):
#         self.list = []

#     def close_spider(self, spider):
#         def flatten(n):
#             return n['episode_list'][0]
#         test = list(map(flatten, self.list))
#         dump = json.dumps(test)
#         with open('items.json', 'w') as f:
#             f.write(dump)

#     def process_item(self, item, spider):
#         line = ItemAdapter(item).asdict()
#         self.list.append(line)
#         return item


class EpisodeNamesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        extension = request.url.split('.')[-1]
        anime = item['weeb_name'][0]
        number = item['episode_number'][0]
        return 'files/{0}/ep-{1}.{2}'.format(anime, number, extension)


class AnimeCountPipeline:
    def __init__(self):
        self.db = json.loads(requests.get(
            'http://localhost:8000/api/animes/', auth=HTTPBasicAuth('admin', 'admin')).text)

    def process_item(self, item, spider):
        isNew = True
        for row in self.db:
            if row['anime_url'] == item['anime_url'][0]:
                isNew = False
                if row['episode_count'] < item['episode_count'][0]:

                    requests.patch('http://localhost:8000/api/animes/{}/'.format(row['id']),
                                   data={"episode_count": item['episode_count']}, auth=HTTPBasicAuth('admin', 'admin')).raise_for_status()
        if isNew:
            payload = {
                'title': item['title'][0],
                'anime_url': item['anime_url'][0],
                'episode_count': item['episode_count'][0]
            }
            requests.post(
                'http://localhost:8000/api/animes/', data=payload, auth=HTTPBasicAuth('admin', 'admin')).raise_for_status()

# class AnimeUrlListPipeline():
#     def open_spider(self, spider):
#         self.anime_url_to_exporter = {}

#     def close_spider(self, spider):
#         for exporter, json_file in self.anime_url_to_exporter.values():
#             exporter.finish_exporting()
#             json_file.close()

#     def _exporter_for_item(self, item):
#         adapter = ItemAdapter(item)
#         anime_url = adapter['anime_url']
#         if anime_url[0] not in self.anime_url_to_exporter:
#             json_file = open('xd.json', 'wb')
#             exporter = JsonItemExporter(json_file)
#             exporter.start_exporting()
#             self.anime_url_to_exporter['anime_url'] = (
#                 exporter, json_file)
#         return self.anime_url_to_exporter['anime_url'][0]

#     def process_item(self, item, spider):
#         exporter = self._exporter_for_item(item)
#         exporter.export_item(item)
#         return item
