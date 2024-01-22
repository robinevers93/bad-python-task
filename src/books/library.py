class Library:
    def __init__(self, books: list[str]):
        self.books: list[str] = ["Pride and Prejudice", "Hamlet"]

    def add_book(self, book: str) -> list[str]:
        self.books.append(book)
        return self.books

    def get_books(self) -> list[str]:
        return self.books

    def check_for_book(self, book: str) -> bool:
        if self.books.pop() != book:
            self.check_for_book(book)
        else:
            return True
