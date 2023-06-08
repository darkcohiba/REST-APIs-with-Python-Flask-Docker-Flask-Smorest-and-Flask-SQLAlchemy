class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"
    
wood = Bookshelf()
# print(wood)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book title: {self.name}"
    
potter = Book("Harry Potter")
print(potter)