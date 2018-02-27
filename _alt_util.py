# -*- coding: utf-8 -*-
from collections import OrderedDict
import logging
import ujson

LOWER_LIMIT = 90
STEP = 1

def create_requests(current, previous, orders):
    seed = create_seed(current)
    sanitize_by_orders(seed, orders)
    add_buy_now(seed, current, previous, orders)
    logging.info('requests: %s', ujson.dumps(seed))
    return seed

def add_buy_now(seed, current, previous, orders):
    buy_now = should_buy_now(current, previous, orders)
    logging.info('should_buy_now?: %s', ujson.dumps(buy_now))
    if buy_now: seed[buy_now] = "buy_now"

def sanitize_by_orders(seed, orders):
    for price, side in orders.items():
        if side == "buy": seed.pop(price, None)
        if side == "sell": seed.pop(price - STEP, None)

def create_seed(current):
    return OrderedDict(map(
        lambda x: (x, "buy"),
        range(LOWER_LIMIT, int(current) + 1, STEP)
    ))

def should_buy_now(current, previous, orders):
    bp = buy_price(current, previous)
    if not bp: return None
    for price, side in orders.items():
        if not side == "sell": continue
        if bp == price - 1: return None
    return bp

def buy_price(current, previous):
    c, p = int(current), int(previous)
    if c == p: return None
    if c < p: return None
    return c
