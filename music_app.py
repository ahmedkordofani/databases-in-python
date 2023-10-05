from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Pass the correct connection string to AlbumRepository
album_repository = AlbumRepository(connection.connection_string)

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all albums
albums = album_repository.all()

# Print out the list of albums
for album in albums:
    print(f"Album ID: {album.id}, Title: {album.title}, Year: {album.release_year}, Artist ID: {album.artist_id}")
