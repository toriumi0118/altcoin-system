# -*- coding: utf-8 -*-
from collections import OrderedDict
import logging
import ujson

UNIT = 100.0 # yen
MAX_PRICE = 120.0 # yen
BUY_SELL_DIFF = 0.5 # yen

STOPPER_SELL_PRICE = 1000.0 # yen

def requests(current, previous, orders):
    buy_now = should_buy_now(current, previous, orders)
    logging.info('should_buy_now?: %s', ujson.dumps(buy_now))
    if not buy_now: return None
    if buy_now > MAX_PRICE: return None
    return reqs(buy_now)

def reqs(buy_now):
    amount = UNIT / buy_now
    reqs = []
    reqs.append(req(amount, buy_now, "buy",  "market")) # 成行で即買
    if buy_now + BUY_SELL_DIFF > MAX_PRICE: 
        # 指値でストッパー用の値を入れる
        reqs.append(req(amount, STOPPER_SELL_PRICE, "sell", "limit"))
    else:
        # 指値で売入れる
        reqs.append(req(amount, buy_now + BUY_SELL_DIFF, "sell", "limit"))
    logging.info('reqs: %s', ujson.dumps(reqs))
    return reqs

def req(amount, price, side, typ):
    return {
        # "pair": pair,
        "amount": str(amount), "price": price,
        "side": side,
        "type": typ
    }

def should_buy_now(current, previous, orders):
    bp = buy_price(current, previous)
    if not bp: return None
    for price, side in orders.items():
        if not side == "sell": continue
        if bp == price - BUY_SELL_DIFF: return None
        if bp > MAX_PRICE: return None
        if bp == MAX_PRICE and price == STOPPER_SELL_PRICE: return None
    return bp

def buy_price(current, previous):
    if not previous: return None
    if current < previous: return None

    # 小数を扱うため10倍
    c, p = float(int(current * 10)), float(int(previous * 10))
    if c == p: return None
    boudary =  5 - (p % 5) + p # 0.5刻みで次の購入タイミングとなる境目を見つける
    if boudary > c: return None
    return boudary / 10
