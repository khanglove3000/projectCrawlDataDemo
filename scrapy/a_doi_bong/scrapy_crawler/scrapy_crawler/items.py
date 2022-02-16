# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCrawlerItem(scrapy.Item):
    Name = scrapy.Field()
    Country = scrapy.Field()
    Date = scrapy.Field()
    Place = scrapy.Field()
    Height = scrapy.Field()
    Weight = scrapy.Field()
    Play_position = scrapy.Field()