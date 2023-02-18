class book():
    def __init__(self, title: str, publisher: str, author: str, year: int, price: float, stock: int, isbn: int, category_id: int):
        self.title = title
        self.publisher = publisher
        self.author = author
        self.year = year
        self.price = price
        self.stock = stock
        self.isbn = isbn
        self.category_id = category_id

def __str__(self):
    print(f"Title: {self.title}")