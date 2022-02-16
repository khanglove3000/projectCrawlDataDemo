from TikiTarget import TikiTarget
from TikiHelper import *
from TikiItem import *
from TikiHunterThread import TikiHunterThread
from TikiDisplayThread import TikiDisplayThread

from bs4 import BeautifulSoup
import requests
import time

TARGET_FILE = 'target_list.txt'

targets = getTargetFromFile(TARGET_FILE)
threads = []
displayThread = TikiDisplayThread()

for t in targets:
    hunter = TikiHunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()

for t in threads:
    t.join()

print ("===== END Main ====")


# Những step để improve project nâng cao hơn
# 1 Xem patterns chạy có đúng yêu cầu không && Thay đổi patterns: keywords, categorys, 
# 2 Thực hiện trên 2 pages
# 3 Thay đổi giá trong khoảng nhất định, xem nhiều sản phảm giá nhỏ nhất
# 4 Tìm thêm nhiều sản phẩm