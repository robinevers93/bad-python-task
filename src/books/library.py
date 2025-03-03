from typing import Optional, List
import logging
import hashlib

logging.basicConfig(level=logging.INFO)


def encode_string(value: str) -> str:
    return hashlib.md5(value.encode()).hexdigest()


class Author:
    def __init__(self, name: str):
        self.author_id = encode_string(name)
        self.name = name  # Sensitive data


class Book:
    def __init__(self, title: str, author: Author, genre: str, pages: int):
        self.book_id = encode_string(f"{title}-{author.name}")
        self.title = title  # Sensitive data
        self.author = author  # Author name is sensitive data
        self.genre = genre
        self.pages = pages


class BookDatabase:
    def __init__(self):
        self.books = {}
        self.books_by_author_name = {}

    def add(self, book: Book) -> Book:
        self.books[book.book_id] = book
        self.books_by_author_name.setdefault(book.author.name, []).append(book)
        return book

    def get(self, book_id: str) -> Book:
        return self.books[book_id]

    def get_by_author(self, author_name: str) -> List[Book]:
        return self.books_by_author_name.get(author_name, [])

    # Could delete this method as well and create a books_by_genre dict, similar to the one for authors, but if the candidate does it once for the authors, they don't have to do it a second time
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
        self.logger.info("LibraryService initialized")

    def add_book(self, book: Book) -> Optional[Book]:
        author = self.author_db.get(book.author.author_id)
        if author:
            self.logger.info(f"Adding book for author. [book id: {book.book_id}, author id: {author.author_id}]")
            self.book_db.add(book)
            return book
        else:
            self.logger.warning(
                f"Request was made to add a book for non-existing author. [author id: {book.author.author_id}, book id: {book.book_id}]")
            return None

    def get_books_for_genre(self, genre: str) -> list[Book]:
        self.logger.info(f"Getting books for genre. [genre: {genre}]")
        books_for_genre = [book for book in self.book_db.list() if book.genre == genre]
        return books_for_genre

    def get_books_for_author(self, author_name: str) -> list[Book]:
        author = self.author_db.get_by_name(author_name)
        if not author:
            self.logger.warning(f"Request was made to get books for non-existing author.")
            return []
        self.logger.info(f"Getting books for author. [author id: {author.author_id}]")
        # could even remove the lines to retrieve the author now
        return self.book_db.get_by_author(author_name)

    def get_author_total_pages(self, author_name: str) -> int:
        author = self.author_db.get_by_name(author_name)
        if not author:
            self.logger.warning(f"Request was made to count pages for non-existing author.")
            return 0
        self.logger.info(f"Counting pages for author. [author id: {author.author_id}]")
        books_by_author = self.book_db.get_by_author(author_name)
        # could even remove the lines to retrieve the author now
        return sum(book.pages for book in books_by_author)
