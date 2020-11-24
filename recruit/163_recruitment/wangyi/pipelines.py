# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangyiPipeline:

    def __init__(self):

        # 初始化MongoDB
        self.client = MongoClient()
        self.db = self.client.hao123
        self.collection = self.db.wy163

    def process_item(self, item, spider):
        item = dict(item)
        self.collection.insert_one(item)

        return item

    def __del__(self):

        self.client.close()
