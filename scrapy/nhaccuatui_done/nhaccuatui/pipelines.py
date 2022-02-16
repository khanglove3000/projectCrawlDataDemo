# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class NhaccuatuiPipeline:
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost","khang","123456","nhaccuatui",charset="utf8",
                                )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):    
        try:
            self.cursor.execute("""INSERT INTO songs (name, singer, song, link)  
                        VALUES (%s, %s, %s, %s)""", 
                       (item['name'].encode('utf-8'), 
                        item['singer'].encode('utf-8'),
                        item['lyric'].encode('utf-8'), 
                        item['link'].encode('utf-8')))            
            self.db.commit()            
        except:
            self.db.rollback()
        return item