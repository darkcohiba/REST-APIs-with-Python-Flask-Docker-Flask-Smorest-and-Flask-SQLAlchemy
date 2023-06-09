class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return f"Book: {self.name}, read {self.pages_read} out of {self.page_count}."
