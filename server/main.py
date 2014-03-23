from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from app.instaghent import photos
from app.instaghent import statistics

def index(request):
	items = photos.get_photos()
	meta = dict(filt="time", timeframe="all")
	return render_to_response('templates:index.mak', {'items': items, "meta": meta}, request=request)

def filt(request):
	filt = "time"
	if "filter" in request.matchdict:
		filt = request.matchdict["filter"]
	else:
		filt = request.path[1:]
	items = photos.get_photos(filt=filt)
	meta = dict(filt=filt, timeframe="all")
	return render_to_response('templates:index.mak', {'items': items, "meta": meta}, request=request)

def author(request):
	author = request.matchdict["author"]
	items = photos.get_photos_by_author(author)
	meta = dict(filt=filt, timeframe="all", author=author)
	return render_to_response('templates:index.mak', {'items': items, "meta": meta}, request=request)

def ID(request):
	author = request.matchdict["author"]
	ID = request.matchdict["ID"]
	photo = photos.get_photo_by_id(ID)
	meta = dict(filt=filt, timeframe="all", author=author, ID=ID)
	return render_to_response('templates:photo.mak', {'photo': photo, "meta": meta}, request=request)

def thumbs(request):
	if request.json_body is not None:
		return Response(body="%s" % photos.set_ghents(request.json_body), content_type="text/plain")

def about(request):
	meta = dict(filt=None)
	return render_to_response('templates:about.mak', {"meta": meta}, request=request)

def stat_filt(request):
	filt = statistics.get_most_used_tags()

	resp = ["%s,%s" % row for row in filt]
	resp.insert(0, "%s,%s" % ("Count", "Filter"))

	return Response(body=("\n".join(resp)), content_type="text/csv")

def stat_calendar(request):
	cal = statistics.get_calendar()

	resp = ["%d-%02d-%d,%d" % row for row in cal]
	resp.insert(0, "%s,%s" % ("Date", "Posts"))

	return Response(body=("\n".join(resp)), content_type="text/csv")


def stat_hours(request):
	cal = statistics.get_hours_usage()

	resp = ["%d,%d,%d" % row for row in cal]
	resp.insert(0, "%s,%s,%s" % ("day", "hour", "value"))

	return Response(body=("\n".join(resp)), content_type="text/csv")

def stat_users(request):
	users = statistics.get_top_users()

	resp = ["%s,%d,%d,%d,%d" % row for row in users]
	resp.insert(0, "%s,%s,%s,%s,%s" % ("author", "count","likes","comments","ghents"))

	return Response(body=("\n".join(resp)), content_type="text/csv")

def stat_maps(request):
	maps = statistics.get_map()
	
	resp = ["%f,%f" % row for row in maps]
	resp.insert(0, "%s,%s" % ("lat", "long"))

	return Response(body=("\n".join(resp)), content_type="application/json")

def notfound(request):
	return Response(body="404 Not Found")

if __name__ == '__main__':
	config = Configurator()
	config.add_route('index', '/')
	config.add_route('ghents', '/ghents')
	config.add_route('time', '/time')
	config.add_route('likes', '/likes')
	config.add_route('comments', '/comments')
	config.add_route('filter', '/filter/{filter}')
	config.add_route('ID', '/by/{author}/{ID}')
	config.add_route('author', '/by/{author}')
	config.add_route('thumbs', '/thumbs')
	config.add_route('about', '/about')
	config.add_route('stat_calendar', '/calendar.csv')
	config.add_route('stat_filt', '/filters.csv')
	config.add_route('stat_hours', '/hours.csv')
	config.add_route('stat_users', '/users.csv')
	config.add_route('stat_maps', '/maps.json')
	config.add_view(index, route_name="index")
	config.add_view(thumbs, route_name="thumbs")
	config.add_view(author, route_name="author")
	config.add_view(ID, route_name="ID")
	config.add_view(filt, route_name="filter")
	config.add_view(filt, route_name="ghents")
	config.add_view(filt, route_name="time")
	config.add_view(filt, route_name="likes")
	config.add_view(filt, route_name="comments")
	config.add_view(about, route_name="about")
	config.add_view(stat_calendar, route_name="stat_calendar")
	config.add_view(stat_filt, route_name="stat_filt")
	config.add_view(stat_hours, route_name="stat_hours")
	config.add_view(stat_users, route_name="stat_users")
	config.add_view(stat_maps, route_name="stat_maps")
	config.add_static_view(name='css', path='static:css')
	config.add_static_view(name='fonts', path='static:fonts')
	config.add_static_view(name='js', path='static:js')
	config.add_static_view(name='img', path='static:img')
	config.add_notfound_view(notfound, append_slash=True)
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 3020, app)
	server.serve_forever()

