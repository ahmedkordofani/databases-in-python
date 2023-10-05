import unittest
from lib.album import Album

class TestAlbum(unittest.TestCase):
    def test_album_initialization(self):
        album = Album()
        self.assertEqual(album.id, 0)
        self.assertEqual(album.title, "")
        self.assertEqual(album.release_year, 0)
        self.assertEqual(album.artist_id, 0)

if __name__ == "__main__":
    unittest.main()
