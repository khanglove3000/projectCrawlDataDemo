# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class KhaitamBooks(scrapy.Item):
    TenSach = scrapy.Field()
    TacGia = scrapy.Field()
    Link = scrapy.Field()
    GiaCu = scrapy.Field()
    GiaMoi = scrapy.Field()
