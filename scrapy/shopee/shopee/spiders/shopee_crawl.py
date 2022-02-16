import scrapy


class ShopeeCrawlSpider(scrapy.Spider):
    name = 'shopee_crawl1'
    allowed_domains = ['https://shopee.vn']
    start_urls = ['http://https://shopee.vn/']

    def parse(self, response):
        pass
