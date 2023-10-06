import unittest
from unittest.mock import Mock
from lib.album_repository import AlbumRepository
from lib.album import Album


class TestAlbumRepository(unittest.TestCase):
    def test_album_repository_all(self):
        # You can create a test database or use a mock database for testing.
        # Initialize AlbumRepository with the test database connection.
        connection_string = "music_library"
        repo = AlbumRepository(connection_string)

        # Perform tests for the AlbumRepository methods here.
        # Test fetching all albums and assert the results.

if __name__ == "__main__":
    unittest.main()

    def test_find_existing_album(self):
        # Mock the psycopg2.connect method and cursor.execute method
        with unittest.mock.patch('psycopg2.connect') as mock_connect:
            mock_cursor = Mock()
            mock_connect.return_value.cursor.return_value = mock_cursor

            # Mock the data that will be returned from the database
            mock_cursor.fetchone.return_value = (1, 'Album Title', 2023, 101)  # Replace with your test data

            # Call the find method with an album_id
            album_id = 1
            result = self.album_repository.find(album_id)

            # Assert that the correct SQL query was executed
            mock_cursor.execute.assert_called_with('SELECT * FROM albums WHERE id = %s', [album_id])

            # Assert that the result is an instance of Album
            self.assertIsInstance(result, Album)

            # Assert that the attributes of the returned album match the expected values
            self.assertEqual(result.id, 1)
            self.assertEqual(result.title, 'Album Title')
            self.assertEqual(result.release_year, 2023)
            self.assertEqual(result.artist_id, 101)

    def test_find_non_existing_album(self):
        # Mock the psycopg2.connect method and cursor.execute method
        with unittest.mock.patch('psycopg2.connect') as mock_connect:
            mock_cursor = Mock()
            mock_connect.return_value.cursor.return_value = mock_cursor

            # Mock the data to indicate that no album was found
            mock_cursor.fetchone.return_value = None

            # Call the find method with a non-existing album_id
            album_id = 9999  # An ID that doesn't exist in the database
            result = self.album_repository.find(album_id)

            # Assert that the correct SQL query was executed
            mock_cursor.execute.assert_called_with('SELECT * FROM albums WHERE id = %s', [album_id])

            # Assert that the result is None (indicating no album was found)
            self.assertIsNone(result)
