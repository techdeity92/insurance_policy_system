class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.status = "available"

    def update(self, new_name, new_price):
        self.name = new_name
        self.price = new_price

    def suspend(self):
        self.status = "suspended"

    def display_product(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Status: {self.status}")