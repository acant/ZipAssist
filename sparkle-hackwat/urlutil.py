import urllib2

################################################################################
# Python 'enum'
class SpecialPages():
	NONE = 0
	IMDB_MOVIE_PAGE = 1

def map_url_to_special_page(url):
	return SpecialPages.IMDB_MOVIE_PAGE

################################################################################
# Utils

def imdb_movie_page_title_to_movie_title(title):
	return title[:title.rfind('(')-1]

################################################################################
# The bread and butter function right here:

def get_movie_title_and_upc_from_url(title,url,selected):
	title = urllib2.unquote(title)
	url = urllib2.unquote(url)
	selected = urllib2.unquote(selected)

	# This overrides everything else
	if selected:
		return selected, None

	sp = map_url_to_special_page(url)

	if sp is SpecialPages.NONE:
		return None, None
	elif sp is SpecialPages.IMDB_MOVIE_PAGE:
		return imdb_movie_page_title_to_movie_title(title), None

	return None, None

################################################################################

def test_with_sample_imdb_page():
	tests = [
		{
			'url': 'http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1411704%2F',
			'title': 'Hop%20(2011)%20-%20IMDb',
			'selected': '',
		},
		{
			'url': 'http%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1411704%2F',
			'title': 'Hop%20(2011)%20-%20IMDb',
			'selected': 'Hop',
		},
	]

	for url,selected,title in (test.values() for test in tests):
		print get_movie_title_and_upc_from_url(title,url,selected)

if __name__ == "__main__":
	test_with_sample_imdb_page()
