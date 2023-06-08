# exercise on oop
class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    # Create a dictionary with keys name and price, and append that to self.items.

    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.items.append(new_item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        sum = 0
        for item in self.items:
            sum += item["price"]
        return sum

walmart = Store(name='walmart')
walmart.add_item("rice", 2)
# print(walmart.items)
print(walmart.stock_price())

