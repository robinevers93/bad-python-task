from typing import Optional, List
import logging

logging.basicConfig(level=logging.INFO)


class Author:
    def __init__(self, id: str, name: str):
        self.author_id = id
        self.name = name  # Sensitive data


class Book:
    def __init__(self, id: str, title: str, author: Author, genre: str, pages: int):
        self.book_id = id
        self.title = title  # Sensitive data
        self.author = author  # Author name is sensitive data
        self.genre = genre
        self.pages = pages


class BookDatabase:
    def __init__(self):
        self.books = {}

    def add(self, book: Book) -> Book:
        self.books[book.book_id] = book
        return book

    def get(self, book_id: str) -> Book:
        return self.books[book_id]

    def list(self) -> list[Book]:
        return list(self.books.values())


class AuthorDatabase:
    def __init__(self):
        self.authors = {}

    def add(self, author: Author) -> Author:
        self.authors[author.author_id] = author
        return author

    def get(self, author_id: str) -> Optional[Author]:
        return self.authors.get(author_id)

    def get_by_name(self, name: str) -> Optional[Author]:
        return next((author for author in self.authors.values() if author.name == name), None)


class LibraryService:
    def __init__(self, book_database: BookDatabase, author_database: AuthorDatabase):
        self.book_db = book_database
        self.author_db = author_database
        self.logger = logging.getLogger(__name__)

    def add_book(self, book: Book) -> Optional[Book]:
        author = self.author_db.get(book.author.author_id)
        if author:
            self.logger.info(f"Adding book {book.title} for author {author.name}.")
            self.book_db.add(book)
            return book
        else:
            return None

    def get_books_for_genre(self, genre: str) -> list[Book]:
        self.logger.info(f"Getting books for {genre} genre.")
        books_for_genre = [book for book in self.book_db.list() if book.genre == genre]
        return books_for_genre

    def get_books_for_author(self, author_name: str) -> list[Book]:
        author = self.author_db.get_by_name(author_name)
        if not author:
            self.logger.info(f"Request was made to get books for author {author_name}, which does not exist.")
            return []
        self.logger.info(f"Getting books for author. [author: {author_name}]")
        books_for_author = [book for book in self.book_db.list() if book.author == author]
        return books_for_author

    def get_author_total_pages(self, author_name: str) -> int:
        author = self.author_db.get_by_name(author_name)
        if not author:
            self.logger.info(f"Request was made to count pages for non-existing author.")
            return 0
        self.logger.info(f"Counting pages for author.")
        books_for_author = [book for book in self.book_db.list() if book.author == author]
        return sum(book.pages for book in books_for_author)
