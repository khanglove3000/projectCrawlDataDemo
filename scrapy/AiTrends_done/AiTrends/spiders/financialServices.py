from colorsys import yiq_to_rgb
from gc import callbacks
import imp
import scrapy
from scrapy.loader import ItemLoader
from ..items import FinancialServices

class FinancialservicesSpider(scrapy.Spider):
    name = 'financialServices'
    allowed_domains = ['www.aitrends.com']
    start_urls = ['https://www.aitrends.com/category/financial-services/']

    def parse(self, response):
        self.logger.info('hello this is my first spider')
        finalPage =  response.css('div.item-details')
        for link in finalPage:  
            loader = ItemLoader(item=FinancialServices(), selector=link)
            finaceItem = loader.load_item()
            href = link.css('div.item-details>h3>a::attr(href)').get()
            yield response.follow(href, self.parse_detail, meta={'finaceItem':finaceItem})
        
        # pageNav = response.css('#td-outer-wrap > div.td-main-content-wrap.td-container-wrap > div > div > div.td-pb-span8.td-main-content > div > div.page-nav.td-pb-padding-side')
        # for next in pageNav:
        #         next_page = next.css('a::attr(href)').extract()
        #         yield scrapy.Request(next_page[-1], callback=self.parse)

    def parse_detail(self, response):
        # financialservices = FinancialServices()
        # financialservices['title'] = response.css('div.td-post-header > header > h1::text').get()
        # financialservices['date'] = response.css('div.td-post-header > header > div > span > time::text').get()
        # financialservices['url'] = response.url
        # financialservices['view'] = response.css(' div.td-post-header > header > div > div > span::text').get()
        # financialservices['tags'] =  response.css('footer > div.td-post-source-tags > ul > li>a::text').extract()
        # financialservices['content'] = response.css('div.td-post-content > p::text').getall()
        # yield financialservices
        finaceItem = response.meta['finaceItem']
        loader = ItemLoader(item=finaceItem, response=response)
        loader.add_css('title', 'div.td-post-header > header > h1::text')
        loader.add_css('date', 'div.td-post-header > header > div > span > time::text')
        loader.add_css('view', 'div.td-post-header > header > div > div > span::text')
        loader.add_css('tags', 'footer > div.td-post-source-tags > ul > li>a::text')
        loader.add_css('content', 'div.td-post-content > p::text')
        yield loader.load_item()