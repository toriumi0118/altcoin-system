# -*- coding: utf-8 -*-
import webapp2
import os
import python_bitbankcc
import ujson

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        test_env1 = os.environ.get('CLIENT_SECRET')
        test_env2 = os.environ.get('CLIENT_SECRET2')
        test_env3 = os.environ.get('CLIENT_SECRET3', 'other')

        pub = python_bitbankcc.public()
        value = pub.get_ticker('btc_jpy')

        self.response.write("""
        1: %s, 2: %s, 3: %s, json: %s
        """ % (test_env1, test_env2, test_env3, ujson.dumps(value)))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
