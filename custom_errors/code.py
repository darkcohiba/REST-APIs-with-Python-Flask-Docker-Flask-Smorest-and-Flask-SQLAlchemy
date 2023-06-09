# define out TooManyPagesReadError, it will inherit from ValueError. we dont need to anything to it, the message will come from the error call.
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return f"Book: {self.name}, read {self.pages_read} out of {self.page_count}."
    

    def read(self, pages: int):
        # add a custom error hear to check if pages + pages_read is greater than page count
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages!")
        self.pages_read += pages
        print(f"Read {self.pages_read} out of {self.page_count}.")

potter = Book("Harry", 50)
# potter.read(50)
# to start if we run this second read 50 we have an output of "Read 100 out of 50.", which isn't possible so goal is to add our custom error to catch this.
# potter.read(50)

# updated with a try except to catch our new error
try:
    potter.read(50)
    potter.read(50)
except TooManyPagesReadError as e:
    print(e)


