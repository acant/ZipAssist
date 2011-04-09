import urllib
import logging
import json
from google.appengine.api import urlfetch

def search(title, upc):
  params = urllib.urlencode({'page': 1, 'pagesize': 1, 'searchTerm': title.lower()})
  result = urlfetch.fetch("http://hackott.zip.ca/opencatalog/search?%s" % params)

  if result.status_code == 200:
    titles = json.loads(result.content)['CatalogTitles']
    if len(titles) != 0:
      return titles[0]
    else:
      return {}

  return {}
