class Clothing:
    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price
        
    def display_info(self):
        print(f"Name: {self.name}, Size: {self.size}, Color: {self.color}, Price: {self.price}")

class Shirt(Clothing):
    def __init__(self, name, size, color, price, shirt_type):
        super().__init__(name, size, color, price)
        self.shirt_type = shirt_type
        
    def display_info(self):
        super().display_info()
        print(f"Type: {self.shirt_type}")

class Pants(Clothing):
    def __init__(self, name, size, color, price, length):
        super().__init__(name, size, color, price)
        self.length = length
        
    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}")

shirt = Shirt("Formal Shirt", "L", "White", 29.99, "Formal")
shirt.display_info()

pants = Pants("Jeans", "M", "Blue", 39.99, "Regular")
pants.display_info()
