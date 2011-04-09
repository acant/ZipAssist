import os
import cgi
import logging
import email
import urllib
import urlutil
import zipca
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp import util
from django.utils import simplejson as json
from google.appengine.api import urlfetch

class MainPage(webapp.RequestHandler):
    def get(self):
        bookmarklet_path = os.path.join(os.path.dirname(__file__), 'bookmarklet.js')

        template_values = {
            'bookmarklet': urllib.quote(template.render(bookmarklet_path, {}))
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class Manage(webapp.RequestHandler):
    def get(self):
        title = self.request.get('title')
        url = self.request.get('url')
        selected = self.request.get('selected')

        movie_title, movie_upc = urlutil.get_movie_title_and_upc_from_url(title,url,selected)
        zipdata = zipca.search(movie_title, movie_upc)
        logging.error(zipdata)

        template_values = {
            'title': title,
            'url': url,
            'selected': selected,
            'movie_title': movie_title,
            'movie_upc': movie_upc,
            'zipdata': zipdata,
            'id': re.search("([0-9]*)$", zipdata.Id).group(0)
        }

        path = None
        if zipdata:
            path = os.path.join(os.path.dirname(__file__), 'manage.html')
        else:
            path = os.path.join(os.path.dirname(__file__), 'manage_error.html')

        self.response.out.write(template.render(path, template_values))


class Add(webapp.RequestHandler):
    def get(self):
        url = self.request.get('title_id')
        path = os.path.join(os.path.dirname(__file__), 'added.json')
        self.response.out.write(template.render(path, {}))

def main():
    application = webapp.WSGIApplication([
      ('/', MainPage),
      ('/manage', Manage),
      ('/add', Add)
    ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
