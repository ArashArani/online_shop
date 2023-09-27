from sqlalchemy import *
from extentions import db

class Cart(db.Model):
    __tabalebame__="carts"
    id = Column(Integer , primary_key= True)
    product_id = Column(INTEGER , ForeignKey('products.id'), nullable=False)
    cart_id = Column(INTEGER , ForeignKey('carts.id'), nullable=False)
    quantity = Column(INTEGER)
    prodct = db.relationship("Product" , backref="cart_items")
    cart = db.relationship("Cart" , backref="cart_items")
