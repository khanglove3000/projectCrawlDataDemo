import scrapy

class post(scrapy.Item):
	Name = scrapy.Field()
	Country = scrapy.Field()
	Date = scrapy.Field()
	Place = scrapy.Field()
	Height = scrapy.Field()
	Weight = scrapy.Field()
	Play_position = scrapy.Field()

class crawling(scrapy.Spider):
	name = "crawling"

	def start_requests(self):
		url = [
			"https://thethao247.vn/doi-bong/manchester-united-tt33.html",
			"https://thethao247.vn/doi-bong/arsenal-tt42.html"]
		for i in url:
			yield scrapy.Request(url=i, callback=self.parser)

	def parser(self, response):
		link = response.xpath('//div[@class="box_league_clb mb-15"]//@href').extract()
		allow_domains = 'https://thethao247.vn'
		#print(link)
		for url in link:
			total_links = allow_domains + url
			yield scrapy.Request(url=total_links, callback=self.parse_post)

	def parse_post(self, response):
		items = post()
		items['Name']  = response.xpath('//h1[@class="name_player"]//text()').get()
		print(items['Name'])
		items['Play_position'] = response.xpath('/html/body/main/div/div/div[2]/div/div[2]/div/p/strong//text()').get()
		items['Country'] = response.xpath('/html/body/main/div/div/div[2]/div/div[2]/div/ul/li[1]/div[2]//text()').get()
		items['Date'] = response.xpath('/html/body/main/div/div/div[2]/div/div[2]/div/ul/li[2]/div[2]//text()').get()
		items['Height'] = response.xpath('/html/body/main/div/div/div[2]/div/div[2]/div/ul/li[4]/div[2]//text()').get()
		items['Weight'] = response.xpath('/html/body/main/div/div/div[2]/div/div[2]/div/ul/li[5]/div[2]//text()').get()
		
		yield items
