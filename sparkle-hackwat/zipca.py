import urllib
import logging
import json
from google.appengine.api import urlfetch

def search(title, upc):
  search = upc
  if search_term == 'None'
    search_term = title

  params = urllib.urlencode({'page': 1, 'pagesize': 1, 'searchTerm': search_term})
  result = urlfetch.fetch("http://hackott.zip.ca/opencatalog/search?%s" % params)

  if result.status_code == 200:
    return json.loads(result.content)['CatalogTitles'][0]

  return {}
