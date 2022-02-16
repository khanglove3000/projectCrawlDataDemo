import scrapy
from ..items import TaiChinhQuocTe

class TaichinhquocteSpider(scrapy.Spider):
    name = 'taichinhquocte'
    allowed_domains = ['https://cafef.vn/tai-chinh-quoc-te.chn']
    start_urls = ['https://cafef.vn/tai-chinh-quoc-te.chn']
    cafef = 'https://cafef.vn'

    def parse(self, response):
        taichinhquoctes = response.css('.knswli-right')
        for new in taichinhquoctes:
            hrefTC = new.css('h3 > a::attr(href)').get()
            linkTC = self.cafef + hrefTC
            #yield response.follow(link, callback=self.parse_detail)
            yield response.follow(linkTC, self.TinTaiChinhQuocTe)
    
    def TinTaiChinhQuocTe(self, response):
        title =  response.css('h1.title::text').get().strip()
        date = response.css('span.pdate::text').get().strip()
        subtitle = response.css('h2.sapo::text').get().strip()
        content =  response.css('#mainContent>p::text').extract()
        author = response.css('p.author::text').get()
        source = response.css('p.source::text').get()
        tags =response.css('div.row2>a::text').extract()
        url = response.url
        StockEventUrl = response.css('#aViewMoreLink::attr(href)').get()

        TinTuc = TaiChinhQuocTe()
        TinTuc.add_value('TaiChinhQuocTeTitle',title)
        TinTuc.add_value('TaiChinhQuocTeDate',date)
        TinTuc.add_value('TaiChinhQuocTeSubtitle',subtitle)
        TinTuc.add_value('TaiChinhQuocTeContent',content)
        TinTuc.add_value('TaiChinhQuocTeAuthor',author)
        TinTuc.add_value('TaiChinhQuocTeSource',source)
       
        TinTuc.add_value('TaiChinhQuocTeUrl', url)
        TinTuc.add_value('StockEventUrl', StockEventUrl)
        yield TinTuc