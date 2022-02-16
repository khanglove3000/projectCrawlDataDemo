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


# Association Table for Many-to-Many relationship between Quote and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
quote_tag = Table('finance_tag', Base.metadata,
    Column('finance_id', Integer, ForeignKey('finance.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True)
    title = Column('title', Text())
    date = Column('date', String(50))
    view = Column('view', String(50))
    content = Column('content', Text())    
    tags = relationship('Tag', secondary='finance_tag',
        lazy='dynamic', backref='finance') 

class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column('name', String(50))
    finances = relationship('Finance', secondary='finance_tag',
        lazy='dynamic', backref="tag")  # M-to-M for quote and tag