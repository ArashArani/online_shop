from sqlalchemy import *
from extentions import db

class Payment(db.Model):
    __tabalebame__="Patments"
    id = Column(Integer , primary_key= True)
    status = Column(String , default='pending')
    cart_id = Column(INTEGER , ForeignKey('carts.id'), nullable=False)
    cart = db.relationship('Cart', backref='payments')