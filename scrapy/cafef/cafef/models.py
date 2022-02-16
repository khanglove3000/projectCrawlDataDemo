from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


# Association Table for Many-to-Many relationship between stocknew and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
stocknew_tag = Table('stocknew_tag', Base.metadata,
    Column('stocknew_id', Integer, ForeignKey('stocknew.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)


class StockNew(Base):
    __tablename__ = "stocknew"

    id = Column(Integer, primary_key=True)
    StockNewMaCoPhieu = Column('StockNewMaCoPhieu', Text())
    StockNewTitle = Column('StockNewTitle', Text())
    StockNewDate = Column('StockNewDate', Text())
    StockNewSubtitle = Column('StockNewSubtitle', Text())
    StockNewContent = Column('StockNewContent', Text())
    StockNewAuthor = Column('StockNewAuthor', Text())
    StockNewSource = Column('StockNewSource', Text())
    #StockNewTags = Column('', Text())
    StockNewUrl = Column('StockNewUrl', Text())
    StockEventUrl = Column('StockEventUrl', Text())
    tags = relationship('Tag', secondary='stocknew_tag',
        lazy='dynamic', backref="stocknew")  # M-to-M for stocknew and tag

class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(100))
    stocknews = relationship('StockNew', secondary='stocknew_tag',
        lazy='dynamic', backref="tag")  # M-to-M for stocknew and tag