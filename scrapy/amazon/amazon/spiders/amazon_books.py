from re import I
from statistics import variance
import scrapy
from ..items import KhaitamBooks

class AmazonBooksSpider(scrapy.Spider):
    name = 'amazon_books'
    allowed_domains = ['khaitam.com']
    start_urls = ['https://www.khaitam.com/sach-moi-1']

    def parse(self, response):
        item = KhaitamBooks()
        tenSach = response.css('.product-variant .product-name > a > span::text').extract() 
        tacGia = response.css('.product-variant .product-sign a::text').extract()
        link = response.css('.product-variant .product-name > a::attr(href)').extract()
        giaCu = response.css('.price-old::text').extract()
        giaMoi = response.css('.price-new::text').extract()

        item['TenSach'] = tenSach
        item['TacGia'] = tacGia
        item['Link'] = link
        item['GiaCu'] = giaCu
        item['GiaMoi'] = giaMoi

        yield item