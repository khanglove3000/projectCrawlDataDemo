# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from numpy import void
import scrapy

class Symbol(scrapy.Item):
    symbol = scrapy.Field()
    urlsymbol = scrapy.Field()

class YahoofinanceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    adjclose = scrapy.Field()
    volume = scrapy.Field()
    pass
