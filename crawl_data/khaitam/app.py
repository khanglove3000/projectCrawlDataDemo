from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import numpy as np
class craigslist_crawler(object):
	def __init__(self, query):
		self.query = query
		self.url = f"https://www.khaitam.com/sach-tinh-tuyen?pagenumber={query}"
		self.driver = webdriver.Chrome("C:\\Users\\khang\\Desktop\\crawl_data\\chromedriver")
		self.delay = 5

	def load_page(self):
	
		driver = self.driver
		driver.get(self.url)
		i = 0
		all_data = driver.find_elements_by_class_name("product-variant")
		for data in all_data:
			
			title = data.text.split("$")
			if title[0] == "":
				title = title[1]
			else:
				title = title[0]
			title = data.text.split("\n")
			datas.append(title)
		return datas
			# tieude = title[0]
			# author = title[1]
			# discount = title[2]
			# price = title[3]

	def close_webdriver(self):
		self.webdriver.close()
		print("good bye")

datas = []
danhsachs = []
for query in range(1,3):
	crawler = craigslist_crawler(query)
	data = crawler.load_page()
	danhsachs.append(data)

for i in range(len(danhsachs[0][0])):
	print(danhsachs[0][0][i])


crawler.close_webdriver()


