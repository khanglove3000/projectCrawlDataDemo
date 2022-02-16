from urllib.request import Request
import scrapy
from selenium import webdriver
from sqlalchemy import true
from ..items import StockNew, EventNew
from scrapy.loader import ItemLoader

class ChungkhoangSpider(scrapy.Spider):
    name = 'chungkhoang'
    allowed_domains = ['cafef.vn']
    cafef = 'https://cafef.vn'
    start_urls  = ['https://cafef.vn/thi-truong-chung-khoan.chn']
    
    def parse(self, response):
        #stocknews = response.css('#LoadListNewsCat > li > h3 > a::attr(href)').extract()
        stocknews = response.css('#LoadListNewsCat > li')
        for new in stocknews:
            loader = ItemLoader(item=StockNew(), response=response)
            StockNewItem = loader.load_item()
            #title = response.css('#LoadListNewsCat > li > h3 > a::attr(title)').get()
            # loader = ItemLoader(item=CafefItem(), selector=new)
            # StockNewItem = loader.load_item()
            href = new.css('h3 > a::attr(href)').get()
            link = self.cafef + href
            #yield response.follow(link, callback=self.parse_detail)
            yield response.follow(link, self.parse_detail, meta={'StockNewItem':StockNewItem})

    def  parse_detail(self, response):
        title =  response.css('h1.title::text').get().strip()
        date = response.css('span.pdate::text').get().strip()
        subtitle = response.css('h2.sapo::text').get().strip()
        content =  response.css('#mainContent>p::text').extract()
        author = response.css('p.author::text').get()
        source = response.css('p.source::text').get()
        tags =response.css('div.row2>a::text').extract()
        url = response.url
        StockEventUrl = response.css('#aViewMoreLink::attr(href)').get()
        MaCophieu = StockEventUrl.split("/")[-2]
     
        StockNewItem = response.meta['StockNewItem']
        loader = ItemLoader(item=StockNewItem, response=response)
        loader.add_value('StockNewMaCoPhieu', MaCophieu)
        loader.add_value('StockNewTitle',title)
        loader.add_value('StockNewDate',date)
        loader.add_value('StockNewSubtitle',subtitle)
        loader.add_value('StockNewContent',content)
        loader.add_value('StockNewAuthor',author)
        loader.add_value('StockNewSource',source)
       
        loader.add_value('StockNewUrl', url)
        loader.add_value('StockEventUrl', StockEventUrl)
        loader.add_value('tags', tags)
        #EventNewAll = loader.load_item()
        # yield response.follow(StockEventUrl, self.parse_EventNewAll)
        
        yield loader.load_item()

    # def parse_EventNewAll(self, response):
    #     #EventNewAll = response.meta['EventNewAll']
    #     AllEnventNews = response.css('#divEvents > ul > li')
    #     for EnventNew in AllEnventNews:
    #         #EventNewsLoader = ItemLoader(item=EventNewAll, response=response)
    #         EventNewsLoader = ItemLoader(item=EventNew(), response=EnventNew)
    #         dateTime = EnventNew.css('span::text').get()
    #         EventTitle = EnventNew.css('a::attr(title)').get()
    #         EventUrl = EnventNew.css('a::attr(href)').get()
    #         # EventNewsLoader.add_value('dateTime', dateTime)
    #         # EventNewsLoader.add_value('EventTitle', EventTitle)
    #         # EventNewsLoader.add_value('EventUrl', self.cafef + EventUrl)  
    #         yield {
    #             'EventTitle': EventTitle,
    #             'dateTime': dateTime,
    #             'EventUrl': EventUrl
    #         }
         

           
            
        


