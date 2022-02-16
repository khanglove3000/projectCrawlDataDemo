# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker
from AiTrends.models import Finance, create_table, db_connect, Tag

class AitrendsPipeline:
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
        finance = Finance()
        tag = Tag()
        finance.title = item["title"]
        finance.date = item["date"]
        finance.view = item["view"]
        finance.content = item["content"]

        # check whether the current quote has tags or not
        if "tags" in item:
            for tag_name in item["tags"]:
                tag = Tag(name=tag_name)
                # check whether the current tag already exists in the database
                exist_tag = session.query(Tag).filter_by(name = tag.name).first()
                if exist_tag is not None:  # the current tag exists
                    tag = exist_tag
                finance.tags.append(tag)

        try:
            session.add(finance)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item