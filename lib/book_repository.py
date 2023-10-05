# Repository class (lib/book_repository.py)
import psycopg2
from lib.book import Book

class BookRepository:
    def  __init__(self, connection_params):
        # Initialize any necessary attributes or connection to the database
        self.connection_params = connection_params

    def all(self):
        # Implement SQL query and logic here to fetch all books
        try:
            # Connect to the database using the provided connection paramaters
            connection = psycopg2.connect(**self.connection_params)

            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to retrieve all books
            query = "SELECT * FROM books"

            # Execute the query
            cursor.execute(query)

            # Fetch all rows as a list of tuples
            book_data = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Process the data and create Book objects
            books = []
            for row in book_data:
                book = Book()
                book.id, book.title, book.author_name = row
                books.append(book)

            return books
        except Exception as e:
            # Handles any exceptions here
            print(f"Error fetching books: {e}")
            return []