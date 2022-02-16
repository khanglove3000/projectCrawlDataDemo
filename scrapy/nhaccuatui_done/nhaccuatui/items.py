# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime


def remove_quotes(text):
    # strip the unicode quotes
    return text

class NhaccuatuiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    singer = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    lyric = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    #link = scrapy.Field()
    pass
