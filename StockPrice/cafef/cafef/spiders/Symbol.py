import scrapy


class SymbolSpider(scrapy.Spider):
    name = 'Symbol'
    allowed_domains = ['s.cafef.vn']
    start_urls = ['https://s.cafef.vn/du-lieu.chn']
    baseUrl = 'http://s.cafef.vn'

    def parse(self, response):
        pass
