# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from OSC.items import OscItem

class OscPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["OSC"]
        self.links = db["links"]

    def process_item(self, item, spider):
        if isinstance(item, OscItem):
            try:
                self.links.insert(dict(item))
            except Exception:
                pass
        return item
