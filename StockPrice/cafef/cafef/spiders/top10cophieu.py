import scrapy
from ..items import *

class Top10cophieuSpider(scrapy.Spider):
    name = 'top10cophieu'
    allowed_domains = ['https://s.cafef.vn/du-lieu.chn']

    def start_requests(self):
        start_urls = 'https://s.cafef.vn/du-lieu.chn'
        yield scrapy.Request(url=start_urls, callback=self.parse)
            
    def parse(self, response):
        top10cophieu = response.css('#topprice-content')
        for cophieu in top10cophieu:
            macks = cophieu.css('td.title > a::text').extract()
            urls = cophieu.css('td.title > a::attr(href)').extract()
        print(macks)
        print(urls)
        item = Symbol()
        for  ticker in zip(macks, urls):
            #  hrefF = href.css('::attr(href)').get()      
           item['symbol'] = ticker[0]
           item['urlsymbol'] = ticker[1]
           yield item
        