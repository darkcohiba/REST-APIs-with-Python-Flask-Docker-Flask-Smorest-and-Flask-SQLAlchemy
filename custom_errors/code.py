class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return f"Book: {self.name}, read {self.pages_read} out of {self.page_count}."
    

    def read(self, pages: int):
        self.pages_read += pages
        print(f"Read {self.pages_read} out of {self.page_count}.")

potter = Book("Harry", 50)
potter.read(50)
# to start if we run this second read 50 we have an output of "Read 100 out of 50.", which isn't possible so goal is to add our custom error to catch this.
potter.read(50)