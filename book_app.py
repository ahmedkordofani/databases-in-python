from lib.book_repository import BookRepository

if __name__ == "__main__":
    # Define your database connection parameters here
    connection_params = {
        "dbname": "book_library",
        "host": "localhost",
        "port": "5432"  # Port for PostgreSQL database
    }
    repo = BookRepository(connection_params)
    books = repo.all()
    for book in books:
        print(f"{book.id} - {book.title} - {book.author_name}")