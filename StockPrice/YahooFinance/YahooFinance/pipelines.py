# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from symtable import Symbol
from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from YahooFinance.models import *
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class YahoofinancePipeline:
    def process_item(self, item, spider):
        return item

class SaveSymbolPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        symbol = Symbol()
        symbol.name = item['symbol']
        symbol.urlsymbol = item['urlsymbol']

        try:
            session.add(symbol)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class SaveHistoricalDataPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        symbol = HistoricalData()
        symbol.date = item['date']
        symbol.open = item['open']
        symbol.high = item['high']
        symbol.low = item['low']
        symbol.close = item['close']
        symbol.adjclose = item['adjclose']
        symbol.volume = item['volume']
        symbol.symbol = item['symbol']


        try:
            session.add(symbol)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class LoadSymbol(object):
    # Database Connectivity
    def connectDB():
        try:
            con = sqlite3.connect("YahooFinance.db")
            cursor = con.cursor()
            print("Connected to Database Successfully")
            #Data fetching Process-(One Record)
            query = "SELECT * from symbol"
            x = cursor.execute(query).fetchall()
            return x
        except:
            print("Database Error")