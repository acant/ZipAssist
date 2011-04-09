

def get_movie_title_and_upc_from_url(title,url,selected):
	if selected:
		return selected, None
	
	return None, None

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
