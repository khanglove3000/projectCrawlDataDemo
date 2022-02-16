import scrapy


class Top10cophieuSpider(scrapy.Spider):
    name = 'Top10CoPhieu'
    allowed_domains = ['https://s.cafef.vn/du-lieu.chn']
    start_urls = ['http://https://s.cafef.vn/du-lieu.chn/']

    def parse(self, response):
        top10CoPhieu = response.css('#topprice')
        for cophieu in top10CoPhieu:
            maCk = cophieu.css('td.title a::text').get()
            kl= cophieu.css(' td:nth-child(1)::text').get()
            gia = cophieu.css(' td:nth-child(2)::text').get()
            thaydoi = cophieu.css('td.change::text').get()
        yield{
            'Ma Ck': maCk,
            'kl':kl,
            'gia':gia,
            'thaydoi':thaydoi
        }