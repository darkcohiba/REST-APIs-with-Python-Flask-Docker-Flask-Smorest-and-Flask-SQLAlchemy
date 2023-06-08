class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"
    

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book title: {self.name}"
    
potter = Book("Harry Potter")
python = Book("Python 101")

wood = Bookshelf(potter, python)
print(potter)
print(wood)

