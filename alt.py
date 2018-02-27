# -*- coding: utf-8 -*-
import logging
import ujson
import alt_util as au
from bb import BB
from model import Tick

def required_orders():
    bb = BB('xrp_jpy')
    current, previous = ticks(bb)
    orders = active_orders(bb)
    reqs = au.requests(current, previous, orders)
    if not reqs: None
    bb.post_orders(reqs)

def active_orders(bb):
    orders = dict(map(
         lambda x: (int(float(x.price)), x.side),
         filter(
             lambda x: x.order_id not in [17228280],
             bb.get_active_orders().orders,
         )
     ))
    logging.info('active orders: %s', ujson.dumps(orders))
    return orders

def ticks(bb):
    current = bb.get_ticker()
    previous = Tick.find_previous()
    Tick.update_current(current)
    logging.info('ticks: %s(current), %s(previous)', current.last, previous.last)
    return float(current.last), float(previous.last) # 切り捨て
