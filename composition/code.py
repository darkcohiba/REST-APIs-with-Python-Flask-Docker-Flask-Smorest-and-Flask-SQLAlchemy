class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"
    
wood = Bookshelf()
print(wood)