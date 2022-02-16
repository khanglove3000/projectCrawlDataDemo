# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def FinaceText(text):
    return text

class AitrendsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FinancialServices(Item):
    title = Field(     
        input_processor=MapCompose(FinaceText),
        output_processor=TakeFirst()
        )
    date = Field(
        input_processor=MapCompose(FinaceText),
        output_processor=TakeFirst()
    )
    # url = Field(
    #     input_processor=MapCompose(Item),
    #     output_processor=Item()
    # )
    view = Field(  
        input_processor=MapCompose(FinaceText),
        output_processor=TakeFirst()
        )
    tags = Field()
    content = Field( 
        input_processor=MapCompose(FinaceText),
        output_processor=TakeFirst()
        )
    