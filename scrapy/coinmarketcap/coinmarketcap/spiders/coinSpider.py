import scrapy


class CoinspiderSpider(scrapy.Spider):
    name = 'coinSpider'
    allowed_domains = ['coinmarketcap.com']
    
    def start_requests(self):
        start_urls = ['https://coinmarketcap.com/all/views/all/']
        yield scrapy.Request(url=start_urls, callback=self.parse)
    
    def parse(self, response):
        for row in response.css("tbody tr"):
            yield {
                "name": row.css("a.cmc-table__column-name--name.cmc-link::text").extract_first(),
                "symbol": row.css("  td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--left.cmc-table__cell--hide-sm.cmc-table__cell--sort-by__symbol::text").extract_first(),
                "market_cap": row.css("td.cmc-table__cell.cmc-table__cell--sortable.cmc-table__cell--right.cmc-table__cell--sort-by__market-cap::text").extract_first(),
                "price": row.css("a.cmc-link::text").extract_first(),
                "circulating_supply": row.css("td.cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply div::attr(data-supply)").extract_first(),
                "volume": row.css("a.cmc-link::text").extract_first()
            }
 