import scrapy


class CrawldataSpider(scrapy.Spider):
    name = 'CrawlData'
    allowed_domains = ['dstock.vndirect.com.vn']
    start_urls = ['http://dstock.vndirect.com.vn']

    def parse(self, response):
        pass
