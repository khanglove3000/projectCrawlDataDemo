from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craigslist_crawler(object):
	def __init__(self, query, max_price):
		self.max_price = max_price
		self.query = query
		self.url = f"https://seoul.craigslist.org/search/sss?query={query}&purveyor-input=all"
		self.driver = webdriver.Chrome("C:\\Users\\khang\\Desktop\\crawl_data\chromedriver")
		self.delay = 5

	def load_page(self):
		driver = self.driver
		driver.get(self.url)
		all_data = driver.find_elements_by_class_name("result-row")
		for data in all_data:
			# print(data.text)
			title = data.text.split("$")
			if title[0] == "":
				title = title[1]
			else:
				title = title[0]

			title = data.text.split("\n")
			price = title[0]
			title = title[-1]
			
			title = title.split(" ")

			month = title[0]
			day = title[1]
			title = ' '.join(title[2:])
			date = month + " " + day

			print("Title: ", title)
			print("Price: ", price)
			print("Date: ", date)

	def close_webdriver(self):
		self.webdriver.close()
		print("good bye")

query = "iphone"
max_price = 500
crawler = craigslist_crawler(query, max_price)
crawler.load_page()
close_webdriver()


