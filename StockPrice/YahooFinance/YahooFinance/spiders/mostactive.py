from urllib import response
import scrapy
from scrapy.loader import ItemLoader
from ..items import YahoofinanceItem
from ..pipelines import LoadSymbol

class MostactiveSpider(scrapy.Spider):
    name = 'mostactive'
    allowed_domains = ['finance.yahoo.com']
    #start_urls = ['https://finance.yahoo.com/most-active/']
    baseUrl = 'https://finance.yahoo.com'

    urls = []
    run = LoadSymbol.connectDB()
    for i in range(len(run)):
        urls.append(run[i][2])

    # print(urls) 
    def start_requests(self):
        for url in range(len(self.run)):
            yield scrapy.Request(self.run[url][2], self.parse)

    def parse(self, response):
        historicaldata = response.css('#quote-nav > ul > li:nth-child(5) > a::attr(href)').get()
        urlHIstoricalData = self.baseUrl + historicaldata
        yield scrapy.Request(url=urlHIstoricalData, callback=self.parseHistoryData,dont_filter=True)
       
    def parseHistoryData(self, response):
      
        items = YahoofinanceItem()
        #name = response.css('#quote-header-info div > h1::text').get()
        url = response.url
        symbol = url.split('=')[-1]
        for row in response.css('table tbody tr'):
            items['symbol'] = symbol
            items['date'] = row.css('td.Py\(10px\).Ta\(start\).Pend\(10px\) > span::text').get()
            items['open'] = row.css('td:nth-child(2)> span::text').get()
            items['high'] = row.css('td:nth-child(3)> span::text').get()
            items['low'] = row.css('td:nth-child(4)> span::text').get()
            items['close'] = row.css('td:nth-child(5)> span::text').get()  
            items['adjclose'] = row.css('td:nth-child(6)> span::text').get()
            items['volume'] = row.css('td:nth-child(7)> span::text').get()
            yield items
