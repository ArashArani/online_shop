from sqlalchemy import *
from sqlalchemy.orm import backref
from extentions import db

class Cart(db.Model):
    __tablename__="carts"
    id = Column(Integer , primary_key= True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    status = Column(String,default="pending")
    user = db.relationship('User',backref=backref('carts', lazy ='dynamic'))


