from Helper import *
from DisplayThread import *


TARGET_FILE = 'target_list.txt'

targets = getTargetFromFile(TARGET_FILE)
threads = []
displayThread = DisplayThread()

for t in targets:
    hunter = HunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()

for t in threads:
    t.join()

print("-------------End Main-----------------")

