# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AmazonPipeline:
    def process_item(self, item, spider):
        return item

class KhaitamBooksPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('ScrapedkhaitamBooks.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS khaitamBooks_tb""")
        self.curr.execute(""" 
            create table khaitamBooks_tb
            (   
                Ten_Sach text,
                Tac_Gia text,
                Link text,
                Gia_Cu text,
                Gia_Moi text
            )
        """)
    def process_item(self, item, spider):
        self.table_data(item)

    def table_data(self, item):
        for data in range(len(item['TenSach'])):
            self.curr.execute("""
            insert into khaitamBooks_tb value (?,?,?,?,?)""",
            (
                item['TenSach'][data],
                item['TacGia'][data],
                item['Link'][data],
                item['GiaCu'][data],
                item['GiaMoi'][data]
            ))
            self.conn.commit()