from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

def print_album_details(album):
    if album:
        print(f"Album ID: {album.id}")
        print(f"Title: {album.title}")
        print(f"Year: {album.release_year}")
        print(f"Artist ID: {album.artist_id}")
    else:
        print("No album found")

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Pass the correct connection string to AlbumRepository
album_repository = AlbumRepository(connection.connection_string)

# Retrieve and print the album with id 1
album_id_to_find = 1
album_to_find = album_repository.find(album_id_to_find)

print("\nAlbum Details:")
print("-" * 15)
print_album_details(album_to_find)

# Retrieve all artists (you can keep this part if needed)
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

print("\nAll Artists:")
print("-" * 12)
for artist in artists:
    print(artist)

# Retrieve all albums (you can keep this part if needed)
albums = album_repository.all()

print("\nAll Albums:")
print("-" * 11)
for album in albums:
    print_album_details(album)
    print("-" * 15)
