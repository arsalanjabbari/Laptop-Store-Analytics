
from sqlalchemy import create_engine, MetaData, create_engine, ForeignKey,text
from sqlalchemy import Table, Column, Integer, String, Float, Text, DateTime, Boolean,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Sequence
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker


#%%
meta = MetaData()
USERNAME = 'root'
PASSWORD = 'Af828-922'
SERVER = 'localhost'
engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}:3306/', echo=True)
conn = engine.connect()

database_name = 'Laptop_analysis_Scraping'

check_database_query = text(f"CREATE DATABASE IF NOT EXISTS {database_name}")
conn.execute(check_database_query)


#%%
engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}:3306/Laptop_analysis_Scraping', echo=True)
conn = engine.connect()


#%%
Base = declarative_base()

# Define SQLAlchemy table classes

class PriceChart (Base):
    __tablename__ = 'PriceChart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(String(64))
    average_price = Column(Float)
    min_price = Column(Float)
    date = Column(DateTime)

class Product(Base): 
    __tablename__ = 'Product'
    ID = Column(String(64), unique=True, primary_key=True)
    Title = Column(Text)
    Manufacturer = Column(String(32))
    StockSatus = Column((String(32)))
    Site = Column(String(32))

class Product_Attributes(Base):
    __tablename__ = 'Product_Attributes'
    ID = Column(String(64), unique=True, primary_key=True)
    Attributes = Column(Text)

class Dollar(Base):
    __tablename__ = 'dollar'
    id = Column(Integer, primary_key=True, autoincrement=True)
    open= Column(Integer)
    low = Column(Integer)
    high = Column(Integer)
    close = Column(Integer)
    jdate = Column(Text)
    gdate = Column(DateTime)

class Store(Base):
    __tablename__ = 'Store'
    ID = Column(Integer, unique=True, primary_key=True,autoincrement=False)
    Name = Column(String(64))
    City = Column(String(32))
    Type = Column(String(32))

class Product_Store(Base):
    __tablename__ = 'Product_Store'
    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Product_ID = Column(String(64))
    Store_ID = Column(Integer)
    Date = Column(String(32))
    Price = Column(BigInteger)



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

