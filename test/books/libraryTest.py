import unittest

from src.books.library import Library

pap: str = "Pride and Prejudice"
lotr: str = "Lord of the Rings"
hamlet: str = "Hamlet"

starting_books: list[str] = [pap, hamlet]
library: Library = Library(starting_books)


class LibraryTest(unittest.TestCase):

    def test_initial_state(self):
        expected_books: list[str] = [lotr, hamlet]
        test_library = Library(expected_books)
        library_start = test_library.get_books()
        self.assertListEqual(library_start, expected_books)

    def test_check_book(self):
        test_library = Library([lotr])
        hamlet_is_available = test_library.check_for_book(hamlet)
        self.assertFalse(hamlet_is_available)

    def test_adding_book(self):
        test_library = Library([])
        test_library.add_book(lotr)
        updated_library = library.get_books()
        self.assertTrue(updated_library.__contains__(lotr))


if __name__ == '__main__':
    unittest.main()
