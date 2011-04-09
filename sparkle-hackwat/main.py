import os
import cgi
import logging
import urllib
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

def main():
    application = webapp.WSGIApplication([('/', MainPage)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
