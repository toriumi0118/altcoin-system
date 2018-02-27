# -*- coding: utf-8 -*-
import os
import python_bitbankcc
from attrdict import AttrDict

API_KEY    = os.environ.get('API_KEY')
API_SECRET = os.environ.get('API_SECRET')
if API_KEY    is None: raise EnvironmentError('API_KEY is not set')
if API_SECRET is None: raise EnvironmentError('API_SECRET is not set')

class BB(object):
    def __init__(self, pair):
        self.pair = pair
        self.pub = python_bitbankcc.public()
        self.prv = python_bitbankcc.private(API_KEY, API_SECRET)

    def get_ticker(self):
        """
        {
          "success":1,
          "data":{
            "sell":"98.198",
            "buy":"98.104",
            "high":"99.500",
            "low":"92.000",
            "last":"98.104",
            "vol":"34933423.2282",
            "timestamp":1519652216593
          }
        }
        """
        return AttrDict(self.pub.get_ticker(self.pair))

    def get_active_orders(self):
        """
        {
          "success": 1,
          "data": {
            "orders": [
              {
                "order_id": 16922967,
                "pair": "xrp_jpy",
                "side": "buy",
                "type": "limit",
                "start_amount": "10000.000000",
                "remaining_amount": "10000.000000",
                "executed_amount": "0.000000",
                "price": "50.0000",
                "average_price": "0.0000",
                "ordered_at": 1519622043476,
                "status": "UNFILLED"
              },
              {
                "order_id": 16722137,
                "pair": "xrp_jpy",
                "side": "sell",
                "type": "limit",
                "start_amount": "3681.166700",
                "remaining_amount": "3681.166700",
                "executed_amount": "0.000000",
                "price": "130.0000",
                "average_price": "0.0000",
                "ordered_at": 1519563735199,
                "status": "UNFILLED"
              }
            ]
          }
        }
        """
        return AttrDict(self.prv.get_active_orders(self.pair))

    def post_orders(self, requests):
        for req in requests:
            self.prv.order(
                self.pair,
                req["price"],
                req["amount"],
                req["side"],
                req["type"]
            )
