"""
Product Inventory Project
Create an application which manages an 
inventory of products. Create a product class which has a price, id, 
and quantity on hand. Then create an inventory class which keeps 
track of various products and can sum up the inventory value.
"""

class Product(object):

    __current_id = 0

    def __init__(self, price, quantity):
        Product.__current_id += 1
        self.id = Product.__current_id
        self.price = price
        self.quantity = quantity

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
        self.quantity = max(0, self.quantity - quantity)        

    def __str__(self):
        return "ID: {0}\tPrice: {1}\tQuantity: {2}".format(self.id, self.price, self.quantity)


class Inventory(object):

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def add_products(self, products):
        self.products.extend(products)

    def remove_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                break 

    def print_inventory(self):
        for product in self.products:
            print product

    def get_total_value(self):
        sum = 0
        for product in self.products:
            sum += product.quantity * product.price
        return sum

def print_separator():
    print "-" * 40

p1 = Product(100, 20)
p2 = Product(200, 2)

i = Inventory()

i.add_product(p1)
i.add_product(p2)

i.print_inventory()
print_separator()

i.remove_product(2)
i.print_inventory()
print_separator()

i.add_products([Product(300, 1), Product(400,2)])
i.print_inventory()

print i.get_total_value()