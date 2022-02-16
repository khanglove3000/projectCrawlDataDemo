import scrapy
from scrapy.loader import ItemLoader

from ..items import NhaccuatuiItem
from ..pipelines import *

class CrawlinglyricsSpider(scrapy.Spider):
    name = 'CrawlingLyrics'
    start_urls = ['https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html']

    def parse(self, response):
        for linklyric in response.css('div.box-content-music-list>div.info_song>a::attr(href)').extract():
            yield response.follow(linklyric, callback=self.saveFile)

        finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-2].extract()
        for page in finalPage:
            yield response.follow(page, callback=self.parse)
       
    def saveFile(self, response):
        loader = ItemLoader(item=NhaccuatuiItem())
        loader.add_xpath('name', '//h2[@class="name_lyric"]//text()')
        loader.add_xpath('singer', '//p[@class="name_post"]//text()')
        loader.add_css('lyric', '#divLyric::text')
        yield loader.load_item()
       