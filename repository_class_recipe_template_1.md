The provided design template outlines the process for designing and implementing Model and Repository classes for a database table. Below, I'll guide you through the exercise of creating an `Album` class and an `AlbumRepository` class for a music library project following this template.

### 1. Design and Create the Table (Skip if already created)

Ensure you have the `albums` table created in your database, as specified in the SQL schema. If it's not created, follow the SQL schema design and create it.

### 2. Create Test SQL Seeds

Create a SQL seed file to insert test data into the `albums` table. You can create a file named `seeds_albums.sql` with the following content:

```sql
-- File: spec/seeds_albums.sql

-- Truncate the albums table to start with a fresh state.
TRUNCATE TABLE albums RESTART IDENTITY;

-- Insert sample data into the albums table.
INSERT INTO albums (title, artist_id, release_year) VALUES ('Album A', 1, 2020);
INSERT INTO albums (title, artist_id, release_year) VALUES ('Album B', 2, 2018);
```

Run this SQL file on your database to populate the `albums` table with sample data.

### 3. Define the Class Names

Following the template, define the class names for the `Album` and `AlbumRepository` classes:

```python
# Model class (lib/album.py)
class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.artist_id = 0
        self.release_year = 0

# Repository class (lib/album_repository.py)
class AlbumRepository:
    pass  # We will implement the methods in the next steps.
```

### 4. Implement the Model Class

Define the attributes of the `Album` class, mapping them to the columns in the `albums` table. You can use the default empty values for now:

```python
# Model class (lib/album.py)
class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.artist_id = 0
        self.release_year = 0
```

### 5. Define the Repository Class Interface

Define the method signatures and SQL queries for the `AlbumRepository` class. Since you only need an `all` method for now, you can define it as follows:

```python
# Repository class (lib/album_repository.py)
class AlbumRepository:
    def all(self):
        # Implement SQL query and logic here to fetch all albums
        pass
```

You'll need to implement the SQL query and logic inside the `all` method to retrieve all albums from the database.

### 6. Write Test Examples

Write test examples to define the expected behavior of the `AlbumRepository` class. These examples will later be converted into pytest tests. Here's an example:

```python
# Test Examples
# You can create a separate test file for these tests.

# Instantiate the repository
repo = AlbumRepository()

# Test fetching all albums
albums = repo.all()

# Check the number of albums fetched
assert len(albums) == 2

# Check attributes of the first album
assert albums[0].id == 1
assert albums[0].title == 'Album A'
assert albums[0].artist_id == 1
assert albums[0].release_year == 2020

# Check attributes of the second album
assert albums[1].id == 2
assert albums[1].title == 'Album B'
assert albums[1].artist_id == 2
assert albums[1].release_year == 2018
```

### 7. Test-Drive and Implement the Repository Class Behavior

Implement the `all` method inside the `AlbumRepository` class to retrieve all albums from the database. You will need to write SQL queries and use a PostgreSQL client library (like psycopg2) to execute the queries.

Finally, write a small program in `app.py` using the `AlbumRepository` class to print out the list of albums to the terminal.

Remember to install any required Python packages, such as psycopg2, to interact with your PostgreSQL database.

This completes the exercise of test-driving the `Album` and `AlbumRepository` classes for your music library project following the provided design template.