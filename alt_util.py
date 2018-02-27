# -*- coding: utf-8 -*-
from collections import OrderedDict
import logging
import ujson

UNIT = 100.0 # yen

def requests(current, previous, orders):
    buy_now = should_buy_now(current, previous, orders)
    logging.info('should_buy_now?: %s', ujson.dumps(buy_now))
    if not buy_now: return None
    amount = UNIT / buy_now
    reqs = [
        req(amount, buy_now,   "buy",  "market"), # 成行で即買
        req(amount, buy_now+1, "sell", "limit"),  # 指値で売入れる
    ]
    logging.info('reqs: %s', ujson.dumps(reqs))
    return reqs

def req(amount, price, side, typ):
    return {
        # "pair": pair,
        "amount": str(amount),
        "price": price,
        "side": side,
        "type": typ
    }

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
