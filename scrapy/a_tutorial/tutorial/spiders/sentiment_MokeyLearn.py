import scrapy
from tutorial.items import HotelSentimentItem

class TripadvisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    start_urls = [
        "https://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html"
    ]
    
    