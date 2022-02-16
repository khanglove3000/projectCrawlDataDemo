import scrapy


class HistorydataSpider(scrapy.Spider):
    name = 'HistoryData'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/']
    baseUrl = 'http://finance.yahoo.com'
    def parse(self, response):
        pass
