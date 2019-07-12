#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import csv

# Create date time stamp
now = datetime.datetime.utcnow()
bitstamp = "https://www.bitstamp.net/api/ticker/"
filename = "wallets.csv"

# Get the BitStamp last sold price
bitstamp = requests.get(bitstamp, timeout=0.5)
source = bitstamp.json()
spot = source["last"]
print "\nTime: \t%s\nSpot: \t$%s" % \
      (now, (float(spot)))

# Get a list of BTC wallets saved in the CSV file
reader = csv.reader(open(filename, 'rU'))
wallets = reader.next()

# Empty tally list to tot them all up
tally = []

# Run through all the wallets and find out whats in each
for w in wallets:
    url = "https://blockchain.info/address/{}?format=json".format(w)
    print "\nWallet:\t%s" % w
    check = requests.get(url)
    raw = check.json()
    ubtc = raw["final_balance"]
    balance = round(float(ubtc * .00000001), 8)
    tally.append(balance)
    print "BTC: \t%s\nValue: \t$%s" % \
          (balance, round((float(spot) * balance), 7))

# Add up the totals
total_value = round(float(spot) * sum(tally))
print ("\nTotals\nBTC: \tB %s\nValue: \t$ {:,.2f}".format(total_value)) \
      % (sum(tally))
