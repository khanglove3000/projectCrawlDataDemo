from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BooksItem # New line
import scrapy

class SpiderSpider(CrawlSpider):
    name = 'Booktoscrapy_Item'

    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    rules = [Rule(LinkExtractor(allow='catalogue'),
            callback='parse_filter_book', follow=True)]  

    def parse_filter_book(self, response):
        exists = response.xpath('//div[@id="product_gallery"]').extract_first()
        if exists:
            title = response.xpath('//div/h1/text()').extract_first()

            relative_image = response.xpath(
                '//div[@class="item active"]/img/@src').extract_first()
            final_image = self.base_url + relative_image.replace('../..', '')

            price = response.xpath(
                '//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract_first()
            stock = response.xpath(
                '//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()').extract()[1].strip()
            stars = response.xpath(
                '//div/p[contains(@class, "star-rating")]/@class').extract_first().replace('star-rating ', '')
            description = response.xpath(
                '//div[@id="product_description"]/following-sibling::p/text()').extract_first()
            upc = response.xpath(
                '//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
            price_excl_tax = response.xpath(
                '//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
            price_inc_tax = response.xpath(
                '//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
            tax = response.xpath(
                '//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()

            book = BooksItem()
            book['title'] = title
            book['final_image'] = final_image
            book['price'] = price
            book['stock'] = stock
            book['stars'] = stars
            book['description'] = description
            book['tax'] = tax
            yield book