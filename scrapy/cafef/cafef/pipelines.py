from itemadapter import ItemAdapter
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from cafef.models import StockNew, create_table, db_connect, Tag
class SaveStockNewPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save quotes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        stocknew = StockNew()
        tag = Tag()
        stocknew.StockNewMaCoPhieu = item["StockNewMaCoPhieu"]
        stocknew.StockNewTitle = item['StockNewTitle']
        stocknew.StockNewDate = item['StockNewDate']
        stocknew.StockNewSubtitle = item['StockNewSubtitle']
        stocknew.StockNewContent = item['StockNewContent']
        stocknew.StockNewAuthor = item['StockNewAuthor']
        stocknew.StockNewSource = item['StockNewSource']
        stocknew.StockNewUrl = item['StockNewUrl']
        stocknew.StockEventUrl = item['StockEventUrl']
        # check whether the current quote has tags or not
        if "tags" in item:
            for tag_name in item["tags"]:
                tag = Tag(name=tag_name)
                # check whether the current tag already exists in the database
                exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                if exist_tag is not None:  # the current tag exists
                    tag = exist_tag
                stocknew.tags.append(tag)

        try:
            session.add(stocknew)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item