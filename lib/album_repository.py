import psycopg2
from lib.album import Album

class AlbumRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def all(self):
        albums = []
        conn = None  # Initialize the connection variable
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM albums;")
            for row in cursor.fetchall():
                album = Album()
                album.id = row[0]
                album.title = row[1]
                album.release_year = row[2]
                album.artist_id = row[3]
                albums.append(album)
        except psycopg2.Error as e:
            print(f"Error fetching albums: {e}")
        finally:
            if conn:
                conn.close()
        return albums

    def find(self, album_id):
        conn = None  # Initialize the connection variable
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM albums WHERE id = %s', [album_id])
            row = cursor.fetchone()
            if row:
                return Album(row[0], row[1], row[2], row[3])
            else:
                return None  # Return None if no album with the given ID is found
        except psycopg2.Error as e:
            print(f"Error fetching album: {e}")
        finally:
            if conn:
                conn.close()
            return None


    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                album.title, album.release_year, album.artist_id])
        return None

    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None
