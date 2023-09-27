from sqlalchemy import *
from extentions import db

class CartItem(db.Model):
    __tabalebame__="cart_items"
    id = Column(Integer , primary_key= True)
    status = Column(String , default='pending')
    user_id = Column(INTEGER , ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='carts')