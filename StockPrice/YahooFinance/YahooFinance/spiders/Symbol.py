import scrapy
from ..items import Symbol

class SymbolSpider(scrapy.Spider):
    name = 'symbol'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/']
    baseUrl = 'https://finance.yahoo.com'

    def start_requests(self):
        urls = [
            'https://finance.yahoo.com/most-active/', 
            'https://finance.yahoo.com/most-active?count=25&offset=75',
            'https://finance.yahoo.com/most-active?count=25&offset=100',
            'https://finance.yahoo.com/most-active?count=25&offset=125',
            'https://finance.yahoo.com/most-active?count=25&offset=150',
            'https://finance.yahoo.com/most-active?count=25&offset=175',
            'https://finance.yahoo.com/most-active?count=25&offset=200',
            'https://finance.yahoo.com/most-active?count=25&offset=225',
            'https://finance.yahoo.com/most-active?count=25&offset=250',
            'https://finance.yahoo.com/most-active?count=25&offset=275',
            'https://finance.yahoo.com/most-active?count=25&offset=300'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        financeyahoolists = response.css('table > tbody > tr >  td > a ::attr(href)').extract()
        tickers = response.css('table > tbody > tr >  td > a ::text').extract()
        urls = []
        for href in financeyahoolists:
            url = self.baseUrl + href
            urls.append(url)
        item = Symbol()
        for  ticker in zip(tickers, urls):
            #  hrefF = href.css('::attr(href)').get()      
           item['symbol'] = ticker[0]
           item['urlsymbol'] = ticker[1]
           yield item

        
        

