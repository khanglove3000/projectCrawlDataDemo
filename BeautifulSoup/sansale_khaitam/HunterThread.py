from threading import Thread
from Target import Target
from Item import *
from Helper import *
import time
from bs4 import BeautifulSoup
import requests

class HunterThread(Thread):
    MAX_PACE = 1

    def __init__(self, target):
        Thread.__init__(self)
        self.target = target
        self.bestItem = None
        self.name = target.getKeyword()

    def __findBestItem(self):
        searchLink = self.target.getSearchLink(1)
        response = requests.get(searchLink)

        if response.status_code != 200:
            return
        
        bsoup = BeautifulSoup(response.text, 'lxnl')
        listElement = bsoup.findAll('div', {'class':'product-variant'})

        i = 1
       
        for e in listElement:
            #print(str(i) + ": ")

            if(e.get_text().find("Liên hệ khi có hàng") >=0):
            #print("============= Đã Hết Hàng===============")
                continue

            newItem = Item()

            newItem.title = e.find("a", {"class":"img center-block"}).get("title")
            newItem.url = e.find("a", {"class":"img center-block"}).get("href")
            newItem.price = converToPrice(e.find("span", {"class":"price-new"}).contents[0])


            # title = e.find("a", {"class":"img center-block"}).get("title")
            # href = e.find("a", {"class":"img center-block"}).get("href")
            # span = e.find("span", {"class":"price-new"})

            span_off = e.find("span", {"class":"price-old"})
            if span_off != None:
                newItem.regularPrice = converToPrice(span_off.contents[0])
            else:
                print("============None===========")

            if(newItem.isValidItem(self.target.patterns)):
            #print(newItem.info())
                if (self.bestItem == None): 
                    self.bestItem = newItem
                else:
                    if(newItem.price < self.bestItem.price):
                        self.bestItem = newItem
            i = i+1

        # print("Best Item: " + self.name)
        # if(self.bestItem != None):
        # 	print(self.bestItem.info())
        # print("========================")

    def run(self):
        print("Start Thread: " + self.name)
        while True:
            self.__findBestItem()
            time.sleep(2)
        print("End Thread: "+ self.name)

