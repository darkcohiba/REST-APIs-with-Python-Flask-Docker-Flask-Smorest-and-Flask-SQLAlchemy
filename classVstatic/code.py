class ClassTest:
    def instance_method(self):
        print(f"instance of this class {self}")
    
    @classmethod
    def class_method(cls):
        print(f"class method {cls}")

    # this method doesn't take the instance or a class when we call it
    @staticmethod
    def static_method():
        print("calling static method")

# declare the class
# test = ClassTest()
# call the method on the instance
# test.instance_method()
# call the method on the class, passing in the instance
# ClassTest.instance_method(test)


# testing the class method
# ClassTest.class_method()

# testing the static method
# ClassTest.static_method()


# example of class variable in use
class Book:
    TYPES = ('hardcover', 'softcover')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book: {self.name}, {self.book_type}, weight: {self.weight}"
    
    # create a method that will create a new book using the types class variable
    @classmethod
    def hardcover(cls, name, weight):
        return Book(name, Book.TYPES[0], weight + 100)

    @classmethod
    def softcover(cls, name, weight):
        return Book(name, Book.TYPES[1], weight)
# print(Book.TYPES)

# potter = Book("Harry Potter", "harcover", 1500)
# using our hardcover method
potter = Book.hardcover("Harry Potter", 1500)
potter2 = Book.softcover("Harry Potter 2", 1500)

# print(potter2)


# exercise
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{store.name}, total stock price: {store.stock_price()}"
