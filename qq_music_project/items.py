# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqMusicProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    music_info = scrapy.Field()
    music_track_info = scrapy.Field()
    pass
