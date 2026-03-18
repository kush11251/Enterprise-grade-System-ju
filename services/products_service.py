from models import Product
from repositories import products_repository
class ProductsService:
    def get_products(self):
        return products_repository.get_products()