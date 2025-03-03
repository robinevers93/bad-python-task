import unittest

from src.books.library import BookDatabase, AuthorDatabase, LibraryService, Author, Book


class TestLibraryService(unittest.TestCase):
    def setUp(self):
        self.db = BookDatabase()
        self.db2 = AuthorDatabase()
        self.libService = LibraryService(self.db, self.db2)

        self.a1: Author = Author("Jack Smith")
        self.a2: Author = Author("George Woods")

        self.db2.add(self.a1)
        self.db2.add(self.a2)

        self.book1: Book = Book("foo", self.a1, "Action Comedy", 10)
        self.book2: Book = Book("foo", self.a2, "Horror", 100)
        self.book3: Book = Book("bar", self.a1, "Horror", 140)

        self.db.add(self.book1)
        self.db.add(self.book2)
        self.db.add(self.book3)

    def test_getBooksForGenre_empty(self):
        self.assertEqual(self.libService.get_books_for_genre("made up"), [])

    def test_getBooksForGenre(self):
        self.assertEqual(self.libService.get_books_for_genre("Horror"), [self.book2, self.book3])
        self.assertEqual(self.libService.get_books_for_genre("Action Comedy"), [self.book1])

    def test_getBooksForAuthor_empty(self):
        self.assertEqual(self.libService.get_books_for_author("made up"), [])

    def test_getBooksForAuthor(self):
        self.assertEqual(self.libService.get_books_for_author(self.a1.name), [self.book1, self.book3])
        self.assertEqual(self.libService.get_books_for_author(self.a2.name), [self.book2])

    def test_getAuthorTotalPages_empty(self):
        self.assertEqual(self.libService.get_author_total_pages("noone"), 0)

    def test_getAuthorTotalPages(self):
        self.assertEqual(self.libService.get_author_total_pages(self.a1.name),
                         sum(book.pages for book in [self.book1, self.book3]))

    def test_addBookToAuthor_none(self):
        a3 = Author("Nemo")
        self.assertIsNone(self.libService.add_book(Book("title", a3, "Romance", 1)))

    def test_addBookToAuthor_some(self):
        author: Author = Author("George Woods")
        book: Book = Book("title", author, "Romance", 1)
        self.assertEqual(self.libService.add_book(book), book)

    def test_AuthorDatabase_getByName_none(self):
        self.assertIsNone(self.db2.get_by_name("no name"))


if __name__ == '__main__':
    unittest.main()
