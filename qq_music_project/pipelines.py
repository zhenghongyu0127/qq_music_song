# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
m = pymongo.MongoClient('127.0.0.1')['music_ceshi']['t1']


class QqMusicProjectPipeline(object):
    def process_item(self, item, spider):
        m.insert(dict(item))
        return item
