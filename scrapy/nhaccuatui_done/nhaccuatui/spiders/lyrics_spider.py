from ..items import NhaccuatuiItem
import scrapy
from ..pipelines import *
class Lyrics_spider(scrapy.Spider):
    name = 'lyric'
    start_urls = [
        'https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html'
    ]

    def parse(self, response):
        finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract()
        totalPage = int(finalPage.split(".")[-2])
        for page in range(0,1):
            link = finalPage.replace(str(totalPage), str(page+1))
            yield scrapy.Request(link, callback=self.crawlyric)

    def crawlyric(self, response):
        for linklyric in response.css('div.box-content-music-list>div.info_song>a::attr(href)').extract():
            yield scrapy.Request(linklyric, callback=self.saveFile)

    def saveFile(self, response):
        lyricRaw = response.css('#divLyric::text').extract()
        lyric = "\n".join(lyricRaw[1:])
        item = NhaccuatuiItem()
        item['name'] = response.xpath('//h2[@class="name_lyric"]//text()')[0].extract().split(':')[-1]
        item['singer'] = response.xpath('//p[@class="name_post"]//text()').get().strip().split(':')[-1]
        item['lyric'] = lyric
        item['lyric'] = lyric.replace('\n\n', ' ')
        item['lyric'] = lyric.replace('\n', ' ')
        item['link'] = response.url
        yield item
       