from shutil import which


SPIDER_MODULES = ['weeb.spiders']
NEWSPIDER_MODULE = 'weeb.spiders'
ROBOTSTXT_OBEY = True

# ITEM_PIPELINES = {'stack.pipelines.MongoDBPipeline': 300, }


#                   'weeb.pipelines.JsonWriterPipeline': 300}
FILES_STORE = 'E:/Projects/weeb_downloader/weeb'
DOWNLOAD_TIMEOUT = 1200
#                  bytes  kilobytes gigabytes
DOWNLOAD_MAXSIZE = 1024 * 1024 * 1024 * 5
DOWNLOAD_WARNSIZE = 0
LOG_LEVEL = 'ERROR'

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "stackoverflow"
# MONGODB_COLLECTION = "questions"
