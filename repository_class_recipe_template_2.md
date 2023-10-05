Sure, I can help you adapt the provided design template to create and test a `Book` class and a `BookRepository` class with an `all` method for a book database. Here are the steps:

### 1. Design and Create the Table

Ensure you have the `books` table created in your database with the necessary columns. If it's not created, follow the SQL schema design and create it.

### 2. Create Test SQL Seeds

Create a SQL seed file to insert test data into the `books` table. You can create a file named `seeds_books.sql` with the following content:

```sql
-- File: spec/seeds_books.sql

-- Truncate the books table to start with a fresh state.
TRUNCATE TABLE books RESTART IDENTITY;

-- Insert sample data into the books table.
INSERT INTO books (title, author, publication_year) VALUES ('Book A', 'Author A', 2020);
INSERT INTO books (title, author, publication_year) VALUES ('Book B', 'Author B', 2018);
```

Run this SQL file on your database to populate the `books` table with sample data.

### 3. Define the Class Names

Following the template, define the class names for the `Book` and `BookRepository` classes:

```python
# Model class (lib/book.py)
class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author = ""
        self.publication_year = 0

# Repository class (lib/book_repository.py)
class BookRepository:
    pass  # We will implement the methods in the next steps.
```

### 4. Implement the Model Class

Define the attributes of the `Book` class, mapping them to the columns in the `books` table. You can use the default empty values for now:

```python
# Model class (lib/book.py)
class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author = ""
        self.publication_year = 0
```

### 5. Define the Repository Class Interface

Define the method signatures and SQL queries for the `BookRepository` class. Since you only need an `all` method for now, you can define it as follows:

```python
# Repository class (lib/book_repository.py)
class BookRepository:
    def all(self):
        # Implement SQL query and logic here to fetch all books
        pass
```

You'll need to implement the SQL query and logic inside the `all` method to retrieve all books from the database.

### 6. Write Test Examples

Write test examples to define the expected behavior of the `BookRepository` class. These examples will later be converted into pytest tests. Here's an example:

```python
# Test Examples
# You can create a separate test file for these tests.

# Instantiate the repository
repo = BookRepository()

# Test fetching all books
books = repo.all()

# Check the number of books fetched
assert len(books) == 2

# Check attributes of the first book
assert books[0].id == 1
assert books[0].title == 'Book A'
assert books[0].author == 'Author A'
assert books[0].publication_year == 2020

# Check attributes of the second book
assert books[1].id == 2
assert books[1].title == 'Book B'
assert books[1].author == 'Author B'
assert books[1].publication_year == 2018
```

### 7. Test-Drive and Implement the Repository Class Behavior

Implement the `all` method inside the `BookRepository` class to retrieve all books from the database. You will need to write SQL queries and use a PostgreSQL client library (like psycopg2) to execute the queries.

Finally, write a small program in `app.py` using the `BookRepository` class to print out the list of books to the terminal.

Remember to install any required Python packages, such as psycopg2, to interact with your PostgreSQL database.

This completes the exercise of test-driving the `Book` and `BookRepository` classes for your book database following the provided design template.