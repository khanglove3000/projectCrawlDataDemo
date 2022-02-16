# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, Join, MapCompose
from datetime import datetime, timedelta

class FbcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
