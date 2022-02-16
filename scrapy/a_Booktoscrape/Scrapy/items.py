# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BooksItem(scrapy.Item):
    title = scrapy.Field()
    final_image = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    stars = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_inc_tax = scrapy.Field()
    tax = scrapy.Field()