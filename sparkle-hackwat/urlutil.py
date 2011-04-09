import urllib2

################################################################################
# Python 'enum'
class SpecialPages():
	NONE = 0
	IMDB_MOVIE_PAGE = 1
	ROTTEN_REVIEW_PAGE = 2

def map_url_to_special_page(url):
	if "www.imdb.com" in url and "/title/" in url:
		return SpecialPages.IMDB_MOVIE_PAGE
	if "www.rottentomatoes.com" in url and "/m/" in url:
		return SpecialPages.ROTTEN_REVIEW_PAGE
	
	return SpecialPages.NONE

################################################################################
# Utils

def imdb_movie_page_title_to_movie_title(title):
	return title[:title.rfind('(')-1]

def rotten_review_page_title_to_movie_title(title):
	return title[:title.rfind('Movie Reviews')-1]

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
	elif sp is SpecialPages.ROTTEN_REVIEW_PAGE:
		return rotten_review_page_title_to_movie_title(title), None

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
		{
			'url': 'http%3A%2F%2Fwww.rottentomatoes.com%2Fm%2Fhop_2011%2F',
			'title': 'Hop%20Movie%20Reviews%20-%20ROTTEN%20TOMATOES',
			'selected': '',
		},
		{
			'url': '',
			'title': '',
			'selected': '',
		},
	]

	for url,selected,title in (test.values() for test in tests):
		print get_movie_title_and_upc_from_url(title,url,selected)

if __name__ == "__main__":
	test_with_sample_imdb_page()
