import unittest
from server.app.instaghent import photos

class TestGetPhotos(unittest.TestCase):
	def test_get_by_author(self):
		# My first photo ever
		photo = photos.get_photos_by_author("illyism", "ASC")
		self.assertEqual(photo[0]["id"], u'403576334775318533_217365605')

	def test_get_by_time(self):
		# First photo ever
		photo = photos.get_photos("time", "ASC")
		self.assertEqual(photo[0]["id"],  u'180784757526784125_22278097')
		self.assertEqual(len(photo), 50)

	def test_get_by_ghents(self):
		# Returns 10 pictures with most ghents > 200
		photo = photos.get_photos(filt="ghents", limit=1)
		self.assertGreaterEqual(photo[0]["ghents"], 200)
		self.assertEqual(len(photo), 1)


class TestSetGhents(unittest.TestCase):
	def setUp(self):
		self.query = photos.Query()
		self.item = u'403576334775318533_217365605'
		self.query.execute("SELECT ghents FROM photos WHERE id=%s;", [self.item])
		self.ghents = self.query.fetchOne()[0]

	def tearDown(self):
		self.query.close()

	def test_incr_ghent(self):
		# increment ghents
		incr_ghents = photos.set_ghents(dict(item=self.item, thumbs=1))
		self.assertEqual(incr_ghents[0], self.ghents + 1)

		# Does it stick?
		self.query.execute("SELECT ghents FROM photos WHERE id=%s;", [self.item])
		self.ghents = self.query.fetchOne()[0]
		self.assertEqual(incr_ghents[0], self.ghents)

	def test_decr_ghents(self):
		# decrement ghent
		photo = photos.get_photos("time", "ASC")
		decr_ghents = photos.set_ghents(dict(item=self.item, thumbs=0))
		self.assertEqual(decr_ghents[0],  self.ghents - 1)

		# Does it stick?
		self.query.execute("SELECT ghents FROM photos WHERE id=%s;", [self.item])
		self.ghents = self.query.fetchOne()[0]
		self.assertEqual(decr_ghents[0], self.ghents)

class TestEncoding(unittest.TestCase):
	def test_unicode(self):
		self.query = photos.Query()
		self.assertEqual(self.query.conn.encoding, "UTF8")


if __name__ == '__main__':
	unittest.main()