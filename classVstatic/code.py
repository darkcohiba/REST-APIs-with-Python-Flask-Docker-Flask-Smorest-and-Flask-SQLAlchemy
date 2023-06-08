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

# print(Book.TYPES)

potter = Book("Harry Potter", "harcover", 1500)

print(potter)