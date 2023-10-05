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
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
                                album.title, album.release_year, album.artist_id])
        return None

    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id])
        return None
