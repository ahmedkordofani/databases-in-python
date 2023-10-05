# tests/test_book.py
from lib.book import Book

def test_first_book_attributes():
# Check attributes of the first book
    book = Book() # Create an instance of Book
    book.id = 1
    book.title = 'Book A'
    book.author_name = 'Author A'
    
    
    assert book.id == 1
    assert book.title == 'Book A'
    assert book.author_name == 'Author A'
    

def test_second_book_attributes():
# Check attributes of the first book
    book = Book() # Create an instance of Book
    book.id = 2
    book.title = 'Book B'
    book.author_name = 'Author B'
    
    assert book.id == 2
    assert book.title == 'Book B'
    assert book.author_name == 'Author B'
    
