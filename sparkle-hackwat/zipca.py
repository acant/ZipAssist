import urllib
import logging
import json
import oauth2 as oauth
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

def zip_list():
  RESOURCE_URL= "http://hackott.zip.ca/users/profile/3b76374683cf47dea3e92c3b0eb3c523/ziplist"

  logging.error(RESOURCE_URL)

  consumer = oauth.Consumer(
    's6NEeuT34WVDYR0uaSq6m0zp6Ck=', #CONSUEMR_KEY
    'pwrf+IADmo5czaouZkU7Z7/i2DY=' #consumer_secret
  )
  token = oauth.Token.from_string('oauth_token=H5%2FiKP3pp7Q4Cmw4h3oX1unMu5c%3D&oauth_token_secret=S06hAqO8TcfDujZoTEufgWy8OyY%3D')
  client = oauth.Client(consumer, token)

  resp, content = client.request(RESOURCE_URL, "GET")

  logging.error(resp)
  logging.error(content)

  return(json.load(content))

def zip(title_id):

  RESOURCE_URL= "http://hackott.zip.ca/users/profile/3b76374683cf47dea3e92c3b0eb3c523/zip/%s" % title_id

  logging.error(RESOURCE_URL)

  consumer = oauth.Consumer(
    's6NEeuT34WVDYR0uaSq6m0zp6Ck=', #CONSUEMR_KEY
    'pwrf+IADmo5czaouZkU7Z7/i2DY=' #consumer_secret
  )
  token = oauth.Token.from_string('oauth_token=H5%2FiKP3pp7Q4Cmw4h3oX1unMu5c%3D&oauth_token_secret=S06hAqO8TcfDujZoTEufgWy8OyY%3D')
  client = oauth.Client(consumer, token)

  resp, content = client.request(RESOURCE_URL, "POST")

  logging.error(resp)
  logging.error(content)

  return 'test'

#TODO
#def unzip(title_id):
