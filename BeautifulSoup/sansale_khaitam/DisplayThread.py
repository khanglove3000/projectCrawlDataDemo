from threading import Thread
from HunterThread import HunterThread
import time
from os import system
from sys import platform

class DisplayThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.hunters = []
        self.index = 0

    def addHunter(self, hunter):
        self.hunters.append(hunter)
    
    def show(self):
        for h in self.hunters:
            if(h.bestItem!=None):
                print(h.bestItem.info())
                print("----------------------")
    def run(self):
            while True:
                self.index = (self.index + 1) % 100
                print("index: " + str(self.index))
                self.show()
                time.sleep(3)
                if platform == "win32": # for Windows
                    system("cls")
                else:                   # for others
                    system("clear")
    
