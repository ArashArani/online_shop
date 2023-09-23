from sqlalchemy import *
from extentions import db

class Product(db.Model):
    __TABLENAME__="products"
    id = Column(Integer , primary_key= True)
    name=Column(String,unique=True,nullable=False,index=True)
    description=Column(String ,nullable=False , index=True)
    price=Column(INTEGER,nullable=False,index=True)