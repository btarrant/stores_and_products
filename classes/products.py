from re import X


class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

#Updates the products price.
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change
        else:
            self.price -= percent_change

#Prints the product info.    
    def print_info(self):
        print(f"{self.name} , {self.category}, {self.price}")