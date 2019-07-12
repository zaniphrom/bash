#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import csv

import datetime
now = datetime.datetime.now()
d = now.date() ; t = now.time()

# Create a dictionary of text wallets

filename = "wallets.csv"
reader = csv.reader(open(filename, 'rU'), dialect='excel')
# header = reader.next() ; print header
for rows in reader:
    wallet = dict((rows[0],rows[1]) for rows in reader)    

# create a list to extract the balance of each wallet
balancelist = []

driver = webdriver.Firefox() #; driver.get(wallet)  
# Run through each wallet and put that balance in the balance list
for w in wallet.values():
    driver.get(w)
    findbalance = driver.find_element_by_id("final_balance")
    btcbal = findbalance.get_attribute("innerHTML")
    btcpriceclean = BeautifulSoup(btcbal)
    cleaned = str(''.join(btcpriceclean.findAll(text=True))[:-3].replace(",", ""))
    balancelist.append(cleaned)

#This uses a filename that contains the bitcoin price from various exchanges
#And import a dictionary. Note the 'as inf' bit 
filename = "bitcoin.price"
with open(filename,'r') as inf:
    dict_from_file = eval(inf.read())
tx = dict_from_file

# The extracts the prices from the imported dictionary
price = []
prices = tx.values()
for p in tx.values():
    price.append(p)

# This floats the 2nd price in the dictionary to be used for approximation of
# BTC balance values
spot = 1
y = float(price[spot])
dictionary = dict(zip(wallet.keys(),balancelist))

#This runs through the values of each wallet balance
for key, value in dictionary.iteritems():
    print "%s's Balance is\t BTC %s \tApprox value: $%r" % \
          (key, value, round(y * float(value),2))

a = tx.keys()[spot]
# This lets you know what exchange and price was used for the approx
print "\nApprox based on %s @ $%s" % (a, y)

driver.quit() 

