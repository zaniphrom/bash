#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import requests
import datetime

# import csv
import requests
import json

# Create date time stamp
now = datetime.datetime.utcnow()
bitstamp = "https://www.bitstamp.net/api/ticker/"
filename = "wallets.csv"


def blockchain_all_wallets_in_one(*args):
    string_them = "|".join(args)
    url = "https://blockchain.info/multiaddr?active="
    address_url = url + string_them
    check = requests.get(address_url)
    raw = check.json()
    return json.dumps(raw, sort_keys=True, indent=4)
    # print(json.dumps(raw, sort_keys=True, indent=4))


def wallet_balances(block_json):
    for i in blockchain_all_wallets_in_one(*args):
        print("hello")
        print(i)
        print("hell")



def wallet_balances(*args):
    for i in blockchain_all_wallets_in_one(*args):
        print("hello")
        print(i)
        print("hell")
