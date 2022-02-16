import scrapy


class Top10cophieuSpider(scrapy.Spider):
    name = 'Top10CoPhieu'
    allowed_domains = ['https://s.cafef.vn/du-lieu.chn']
    start_urls = ['http://https://s.cafef.vn/du-lieu.chn/']

    def parse(self, response):
        pass
