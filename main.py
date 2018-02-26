# -*- coding: utf-8 -*-
import webapp2
from bb import BB

class App(webapp2.RequestHandler):
    def ok(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("ok")

class MainPage(App):
    def get(self):
        self.ok()

class CoinHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(
            BB().get_histories()
        )
        # self.ok()

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/api/coin', CoinHandler),
], debug=True)
