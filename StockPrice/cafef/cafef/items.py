# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,  Field
import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime

def StockNew(text):
    return text

class StockNew(Item):
    StockNewMaCoPhieu = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewTitle = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewDate = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewSubtitle = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewContent = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewAuthor = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockNewSource = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    # StockNewTags = Field(
    #     input_processor=MapCompose(StockNew),
    #     output_processor=TakeFirst()
    # )
    StockNewUrl = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    StockEventUrl = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    tags = Field()

class EventNew(Item):
    dateTime = Field()
    EventTitle = Field()
    EventUrl = Field()

 

#   'title': response.css('h1.title::text').get(),
#             'date': response.css('span.pdate::text').get(),
#             'subtitle': response.css('h2.sapo::text').get(),
#             'content': response.css('#mainContent>p::text').extract(),
#             'author': response.css('p.author::text').get(),
#             'source': response.css('p.source::text').get(),



class TaiChinhQuocTe(Item):

   TaiChinhQuocTeTitle = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
   TaiChinhQuocTeDate = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
   TaiChinhQuocTeSubtitle = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
   TaiChinhQuocTeContent = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
   TaiChinhQuocTeAuthor = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
   TaiChinhQuocTeSource = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )
    #TaiChinhQuocTeTags = Field(
    #     input_processor=MapCompose(StockNew),
    #     output_processor=TakeFirst()
    # )
   TaiChinhQuocTeUrl = Field(
        input_processor=MapCompose(StockNew),
        output_processor=TakeFirst()
    )

class Symbol(scrapy.Item):
    symbol = scrapy.Field()
    urlsymbol = scrapy.Field()

class HistoryData(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    # adjclose = scrapy.Field()
    # volume = scrapy.Field()
    pass