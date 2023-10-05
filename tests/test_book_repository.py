from lib.book_repository import BookRepository

def test_first_book_attributes():

    # Define your database connection parameters here
    connection_params = {
        "dbname": "book_library",
        "host": "localhost",
        "port": "5432"  # Port for PostgreSQL database
    }

    # Instantiate the repository
    repo = BookRepository(connection_params)

    # Test fetching all books
    books = repo.all()

    # Check the number of books fetched
    assert len(books) == 5
    
    # Check attributes of the first book
    assert books[0].id == 1
    assert books[0].title == 'Nineteen Eighty-Four'
    assert books[0].author_name == 'George Orwell'



