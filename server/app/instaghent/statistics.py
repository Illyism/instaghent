import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
import re
import photos


def get_most_used_tags():
	query = photos.Query()
	query.execute("SELECT count(filters) count, filters FROM photos GROUP BY filters HAVING filters is not NULL ORDER BY count DESC;")
	tags = query.fetchAll()
	query.close()
	return tags

def get_calendar():
	query = photos.Query()
	query.execute("""
SELECT
extract(year from time) as yyyy,
extract(month from time) as mm,
extract(day from time) as dd,
count(*) posts
from photos
group by 1,2,3 ORDER BY yyyy DESC, mm DESC, dd DESC, posts DESC;
""")
	calendar = query.fetchAll()
	query.close()
	return calendar

def get_hours_usage():
	query = photos.Query()
	query.execute("""
SELECT
extract(dow from time) as day,
extract(hour from time) as hour,
count(*) posts 
from photos
group by 1,2 ORDER BY day ASC, hour ASC;
""")
	hours = query.fetchAll()
	query.close()
	return hours

def get_top_users():
	query = photos.Query()
	query.execute("""
SELECT
author,
count(*) count,
sum(likes), sum(comments), sum(ghents)
from photos
group by 1 ORDER BY count DESC, author DESC
LIMIT 10;
""")
	users = query.fetchAll()
	query.close()
	return users

def get_map():
	query = photos.Query()
	query.execute("""select location from photos where location is not null""")
	maps = query.fetchAll()
	items = []
	for item in maps:
		item = item[0].split(",")
		items.append((float(item[0][1:]), float(item[1][:-1])))
	query.close()
	return items
	