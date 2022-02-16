from selenium import webdriver
import scrapy

class crawling(scrapy.Spider):
	name = 'demo2'

	def __init__(self):
		self.chrome_driver_path = "C:\\Users\\khang\\Desktop\\crawl_data\\chromedriver"
		self.chrome_options = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(options=self.chrome_options, executable_path=self.chrome_driver_path)

	def start_requests(self):
		url = "https://thethao247.vn/doi-bong/manchester-united-tt33.html"
		yield scrapy.Request(url=url, callback=self.parser)
	
	def parser(self, response):
		self.driver.get(response.url)
		self.driver.maximize_window()
		name = self.driver.find_elements_by_xpath('/html/body/main/div/div/div[2]/div/div[2]/div/p/strong//text()').get()
		for i in name:
			print(i.text)
	def close_chrome(self):
		self.driver.close()