import os
import cgi
import logging
import urllib
import urlutil
import zipca
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
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
        title = self.request.get('title'),
        url = self.request.get('url'),
        selected = self.request.get('selected')

        movie_title, movie_upc = urlutil.get_movie_title_and_upc_from_url(title,url,selected)
        title_id = zipca.search(movie_title, movie_upc)

        template_values = {
            'title': title,
            'url': url,
            'selected': selected,
            'movie_title': movie_title,
            'movie_upc': movie_upc,
            'title_id': title_id,
        }

        path = os.path.join(os.path.dirname(__file__), 'manage.html')
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([('/', MainPage), ('/manage', Manage)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
