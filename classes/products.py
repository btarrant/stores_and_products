from re import X


class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change 
            self.price -= percent_change
        return self.price
    print("hey")