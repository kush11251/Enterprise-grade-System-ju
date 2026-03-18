from models import Product
from db import db
class ProductsRepository:
    def get_products(self):
        return db.query(Product).all()