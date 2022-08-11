class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimension = dimensions

    def __str__(self):
        return f'{self.price} {self.description} {self.dimension};'

x = Product(456, "White", "10")
y = Product(234, "Black", 12)


class Buyer:
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name}, {self.phone}'

class Order:
    def __init__(self, buyer: Buyer = None):
        self.buyer = buyer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)




