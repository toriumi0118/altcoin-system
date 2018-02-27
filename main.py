# -*- coding: utf-8 -*-
import webapp2
import logging
import traceback
from alt import required_orders

class App(webapp2.RequestHandler):
    def ok(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("ok")

    def error(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("error")

class MainPage(App):
    def get(self):
        ok()

class CoinHandler(App):
    def get(self):
        try:
            req_orders = required_orders()
            self.ok()
        except Exception as e:
            logging.error(e)
            logging.error(traceback.format_exc())
            self.error()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/coin', CoinHandler),
], debug=True)
