import scrapy
from ..pipelines import LoadSymbol
from ..items import HistoryData
class HistorydataSpider(scrapy.Spider):
    name = 'historyData'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['http://s.cafef.vn/']
    baseUrl = 'http://s.cafef.vn'
    urls = []
    
    run = LoadSymbol.connectDB()
    for i in range(len(run)):
        urls.append(run[i][2])

    # print(urls) 
    def start_requests(self):
        for url in range(len(self.run)):
            yield scrapy.Request(self.run[url][2], self.parse)

    def parse(self, response):
        href = response.css('#content > div > div.tracuu.clearfix > a.tc-ls::attr(href)').get()
        tracudulieulichsu = self.baseUrl + href
        yield scrapy.Request(tracudulieulichsu, callback=self.parseHistoryData)
    
    def parseHistoryData(self, response):
        items = HistoryData()
        name = response.css('#ctl00_ContentPlaceHolder1_LabelUpdatePanel > h1::text').get()
        date = response.css('td.Item_DateItem::text').extract()
        close = response.css('td:nth-child(3).Item_Price1::text').extract()
        open = response.css('td:nth-child(11).Item_Price1::text').extract()
        high = response.css('td:nth-child(12).Item_Price1::text').extract()
        low = response.css('td:nth-child(13).Item_Price1::text').extract()
        for lichsu in zip(date, close, open, high, low):
            items['date'] = lichsu[0]
            items['close'] = lichsu[1]
            items['open'] = lichsu[2]
            items['high'] = lichsu[3]
            items['low'] = lichsu[4]
            items['name'] = name
            yield items