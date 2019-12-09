#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests

# from requests.exceptions import ConnectionError
import datetime
import copy
import sys
import time

# Get the BitStamp last sold price


def last_price():
    bit_url = "https://www.bitstamp.net/api/ticker/"
    try:
        bitstamp = requests.get(bit_url, timeout=0.5)
        bitstamp.raise_for_status()
    except requests.exceptions.HTTPError as e:  # This is the correct syntax
        print(e)
        sys.exit(1)
    else:
        source = bitstamp.json()
        spot = source["last"]
        return float(spot)


def wallet_totals(*argv):
    totals = []
    dict = {}
    for arg in argv:
        block_url = "https://blockchain.info/rawaddr/{}".format(arg)
        now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
        check = requests.get(block_url)
        raw = check.json()
        ubtc = raw["final_balance"]
        # totals.append(ubtc)
        dict.update(
            timestamp=str(now),
            wallet=arg,
            holding=ubtc / int(100000000),
            spot_price_usd=last_price(),
            total_value_usd=round((ubtc * last_price()) / int(100000000), 2),
        )
        # print(dict)
        totals.append(copy.copy(dict))
    # return json.dumps(totals, sort_keys=True, indent=4)
    return pretty_json(totals)


def pretty_json(raw_json):
    return json.dumps(raw_json, sort_keys=True, indent=4)


# def myFun(*argv):
#   for arg in argv:
#     print (arg)
#
# myFun("1MgWyAqaD3AtJhYF66DoKJfBHKS8LHTaXs", "3JjPf13Rd8g6WAyvg8yiPnrsdjJt1NP4FC")
# wallet_totals()

print(
    wallet_totals(
    )
)
