import logging, email
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class LogSenderHandler(InboundMailHandler):
    def receive(self, msg):
        tineye = TinEye()
        response = tineye.lookup(msg.attachments[0][0], msg.attachments[0][1])

        msg = email.EmailMessage(sender="Example.com Support <support@example.com>",
                            subject="Your account has been approved")

        msg.to = 'ben@bnmrrs.com'
        msg.body = response
        msg.send()


class TinEye:
    def lookup(self, filename, img_data):
        response = urlfetch.fetch(
            'http://pixmatch-m.hackdays.tineye.com/rest/',
            {
                'filename': filename,
                'image': img_data,
                'max_num_matches': 0
            },
            'GET'
        )

        logging.error(response)
        return response

