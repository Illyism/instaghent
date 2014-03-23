import psycopg2
import psycopg2.extensions
from psycopg2.extensions import adapt, register_adapter, AsIs
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import photos
from instagram import client

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def adapt_point(point):
     return AsIs("'(%s, %s)'" % (adapt(point.x), adapt(point.y)))

register_adapter(Point, adapt_point)

CONFIG = {
	'client_id': 'a5a67115f0fc45d6b97d318ac915aa91',
	'client_secret': '76458a657e8c4317a32ebb9b8b224219',
	'redirect_uri': 'http://localhost:8002/oauth_callback'
}

api = client.InstagramAPI(**CONFIG)

def addToDatabase(items):
	query = photos.Query();
	query.cur.executemany("""
INSERT INTO photos (id, author, caption, filters, comments, ghents, likes, location, link, thumb, low, standard, profile_picture, tags, time)
SELECT %(id)s, %(author)s, %(caption)s, %(filters)s, %(comments)s, %(ghents)s, %(likes)s, %(location)s, %(link)s, %(thumb)s, %(low)s, %(standard)s, %(profile_picture)s, %(tags)s, %(time)s
WHERE NOT EXISTS (SELECT 1 FROM photos WHERE id = %(id)s);
""", items)
	query.commit()
	print query.cur.rowcount
	print query.cur.statusmessage
	query.close()
	

def prepare_photo(photo):
	tags = []
	for tag in photo.tags:
		tags.append(tag.name)
	item = dict(
			id = photo.id,
			author = photo.user.username,
			profile_picture = photo.user.profile_picture,
			filters = photo.filter,
			time = photo.created_time,
			ghents = 0,
			tags = tags,
			likes = len(photo.likes),
			comments = len(photo.comments),
			link = photo.link,
			low = photo.images["low_resolution"].url,
			thumb = photo.images["thumbnail"].url,
			standard = photo.images["standard_resolution"].url,
			caption = None,
			location = None
		)

	if hasattr(photo.caption, "text"):
		item["caption"] = photo.caption.text
	if hasattr(photo, "location"):
		if (photo.location.point != None):
			item["location"] = Point(photo.location.point.latitude, photo.location.point.longitude)
	return item

def collectInsta():
	items, next = api.tag_recent_media(count=5, tag_name="instaghent")
	newItems = []
	for photo in items:
		newItems.append(prepare_photo(photo))
	addToDatabase(newItems)

def deleteBad():
	query = photos.Query();
	query.execute("DELETE FROM photos WHERE ghents < 0;")
	query.commit()
	print query.cur.rowcount
	print query.cur.statusmessage
	query.close()

if __name__ == '__main__':
	print "---- Run ----"
	collectInsta()
	deleteBad()
	print "---- Done ----"