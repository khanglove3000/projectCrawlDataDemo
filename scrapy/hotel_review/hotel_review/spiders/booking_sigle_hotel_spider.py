import scrapy
from scrapy.loader import ItemLoader
from ..items import BookingReviewItem

class BookingSigleHotelSpiderSpider(scrapy.Spider):
    name = 'booking_sigle_hotel_spider'
    start_urls = ['http://www.booking.com/hotel/us/new-york-inn.html']

    def parse(self, response):
        pass
