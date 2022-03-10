from time import sleep
from classes.products import Product

class Store:

    def __init__(self, product_list):
        self.name = "K-Mart"
        self.product_list = [product_list]

    def add_product(self, new_product):
        new_product += self.product_list

    def sell_product(self, id):
        self.id = id
        id = self.product_list[id]
        self.product_list -= id
    print(Product.print_info)
