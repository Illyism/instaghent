import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
from datetime import datetime, timedelta

class Query(object):
	"""docstring for Query"""
	def __init__(self):
		self.conn = psycopg2.connect("dbname=instaghent user=postgres")
		self.conn.set_client_encoding("UTF8")
		self.cur = self.conn.cursor()
	def execute(self, sql, values=None):
		if (values is not None):
			self.cur.execute(sql, values)
		else:
			self.cur.execute(sql)
		self.description = self.cur.description
	def fetchOne(self):
		return self.cur.fetchone()
	def fetchAll(self):
		self.items = []
		x = self.fetchOne()
		while (x is not None):
			self.items.append(x)
			x = self.fetchOne()
		return self.items
	def fetchDict(self):
		item = self.fetchOne()
		if item is None: return None
		return dict((self.description[i].name, item[i]) for i in range(0, len(self.description)))
	def fetchAllDict(self):
		self.items = []
		x = self.fetchDict()
		while (x is not None):
			self.items.append(x)
			x = self.fetchDict()
		return self.items
	def commit(self):
		self.conn.commit()
	def close(self):
		self.cur.close()
		self.conn.close()
				
def get_photos_by_author(author, order="DESC"):
	query = Query()
	if (order == "DESC"):
		query.execute("SELECT * from photos WHERE author=%(author)s ORDER BY time DESC;", {"author":author})
	else:
		query.execute("SELECT * from photos WHERE author=%(author)s ORDER BY time ASC;", {"author":author})
	photos = query.fetchAllDict()
	query.close()
	return photos

def get_photo_by_id(ID):
	query = Query()
	query.execute("SELECT * from photos WHERE id=%(ID)s LIMIT 1;", {"ID":ID})
	photo = query.fetchDict()
	query.close()
	return photo

def get_photos(filt="time", order="DESC", offset=0, limit=50, timeframe="all"):
	if (not (filt == "ghents" or filt == "likes" or filt == "comments" or filt == "time")):
		filt = "time"
	if (not (order == "DESC" or order == "ASC")):
		order = "DESC"

	query = Query()
	if (timeframe == "today" or timeframe == "week" or timeframe == "month" or timeframe == "year"):
		today = datetime.today()
		if (timeframe == "today"):
			timeDifference = today - timedelta(days=1)
		elif (timeframe == "week"):
			timeDifference = today - timedelta(days=7)
		elif (timeframe == "month"):
			timeDifference = today - timedelta(days=31)
		elif (timeframe == "year"):
			timeDifference = today - timedelta(days=365)
		query.execute("SELECT * from photos WHERE time >= %s ORDER BY "+ filt +" " + order + " LIMIT %s OFFSET %s;", [timeDifference, limit, offset])
	else:
		query.execute("SELECT * from photos ORDER BY "+ filt +" " + order + " LIMIT %s OFFSET %s;", [limit, offset])

	photos = query.fetchAllDict()
	query.close()
	return photos

def set_ghents(item):
	query = Query()
	if (item["thumbs"] == 0):
		query.execute("UPDATE photos SET ghents = ghents - 1 WHERE id=%s RETURNING ghents;", [item["item"]])
	else:
		query.execute("UPDATE photos SET ghents = ghents + 1 WHERE id=%s RETURNING ghents;", [item["item"]])
		
	ghents = query.fetchOne()
	query.commit()
	query.close()
	return ghents