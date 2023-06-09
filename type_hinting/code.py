# we could do it this way but it wont check to make sure sequence is a list so instead...
# def list_avg(sequence):
#     return sum(sequence) / len(sequence)

# we can do this...
def list_avg(sequence : list) -> float:
    return sum(sequence) / len(sequence)
# above we are specifying sequence should be a list datatype and the function will return a float
# print(list_avg([1,2,3]))

# with our class example:
# import list from types
from typing import List

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Book title: {self.name}"
    
class Bookshelf:
    def __init__(self, *books:List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books"
    
potter = Book("Harry Potter")
python = Book("Python 101")

wood = Bookshelf(potter, python)
print(potter)
print(wood)