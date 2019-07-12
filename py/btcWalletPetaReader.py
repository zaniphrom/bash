#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver # pip install selenuin 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import html5lib
import urllib2
import csv
import sys
import datetime
from bs4 import BeautifulSoup
#from pyvirtualdisplay import Display
# pip install pyvirtualdisplay


# Set up a virtual display
#display = Display(visible=0, size=(1024, 768))
#display.start()


# Create date time stamp
now = datetime.datetime.now() ; d = now.date() ; t = now.time()
#Ask for number of Peta shares and float the number
shares = float(raw_input ("How many peta shares do you own?\n> ")) 

print "Financial records @ %s %s\n" % (d, t)
#===============================================================================
# part1 - get the bitcoin exchange prices
#===============================================================================

ids = { "Bitstamp":"market_bitstampbtcusd", "BTC-e":"market_btcebtcusd" }
classes = { "Houbi":"eprice" }
petaclass = {"PETA": "ws_lastprice_PETA"}

# Create a new instance of the Firefox driver
driver = webdriver.Firefox() ; driver.get("https://bitcoinwisdom.com/")  
testids = [];  testclasses = []

# Run through the ids and extract the price
for i in ids.values():
    try:
        findprice = driver.find_element_by_id(i)
        btcprice = float(findprice.get_attribute("innerHTML")) 
        testids.append(btcprice)
    except:
        print "Cannot get BTC prices"

# Run through the classes and extract the price
for c in classes.values():
    try:
        findprice = driver.find_element_by_class_name(c)
        btcprice = float(str(findprice.get_attribute("innerHTML")[:-1]))
        testclasses.append(btcprice)
    except:
        print "Cannot get BTC prices"
 
# Put together a dictionary of prices and exchange names
dictionary = dict(zip(ids.keys(),testids))
testclassesid = dict(zip(classes.keys(),testclasses))

dictionary2 = dict(dictionary.items() + testclassesid.items())

# print the exchange prices on screen

for key, value in dictionary2.iteritems():
    print "\t%s price\t $%r" % (key, value)
#===============================================================================
# 
# Part 2 - calculate peta price + dividends + holding
#===============================================================================

petaclass = {"PETA": "ws_lastprice_PETA"}
dividends = {"Dividends" : "//div[@class='tablewrap']/table/tbody/tr[17]/td[8]"}

driver.get("https://www.havelockinvestments.com/funds.php")
testids = [] ;  testclasses = []
#Get peta's last trade price
for i in petaclass.values():
    try:
        findprice = driver.find_element_by_class_name(i)
        btcprice = float(findprice.get_attribute("innerHTML")) 
        testids.append(btcprice)
    except:
        print "Cannot get Peta prices"

for key, value in petaclass.iteritems():
    print "\t\n%s %s %sBTC" % (key, driver.title, btcprice)
#Print Peta holdings value per exchange    
for key, value in dictionary2.iteritems():
    print "\t%s shares @ %s price\t $%r \t($%r)" % (shares, key, round(((value * btcprice)*shares),2), value)

#Get last dividends    
dividendlist = []
for d in dividends.values():
    try:
        findprice = driver.find_element_by_xpath(d)
        div = findprice.get_attribute("innerHTML")
        divclean = BeautifulSoup(div)
        cleaned = str(''.join(divclean.findAll(text=True))[1:].replace(",", ""))
        dividendlist.append(cleaned)
    except:
        print "Cannot get dividends"
    
d = dividendlist[0]
print "\nLatest dividends paid B%s (weekly)" % d
y =  shares * float(d)

for key, value in dictionary2.iteritems():
    print "\t(%sB) rtns @%s price\t $%r" % (d, key, round((value * y ),2))


#===============================================================================
# part 3 - get wallet balance and values
#===============================================================================
print "\nFind wallet balances:"

filename = "wallets.csv"
reader = csv.reader(open(filename, 'rU'), dialect='excel')
# header = reader.next() ; print header
for rows in reader:
    wallet = dict((rows[0],rows[1]) for rows in reader)    

balancelist = []

for w in wallet.values():
    try:
        driver.get(w)
        findbalance = driver.find_element_by_id("final_balance")
        btcbal = findbalance.get_attribute("innerHTML")
        btcpriceclean = BeautifulSoup(btcbal)
        cleaned = str(''.join(btcpriceclean.findAll(text=True))[:-3].replace(",", ""))
        balancelist.append(cleaned)
    except:
        print "Blockchain problem, check if it is down"
        driver.quit()
        sys.exit()

price = []
prices = dictionary2.values()
for p in dictionary2.values():
    price.append(p)

spot = 0

y = float(price[spot])
walletdictionary = dict(zip(wallet.keys(),balancelist))
for key, value in walletdictionary.iteritems():
    print "\t%s's Balance is\t B%s \t value: $%r Approx**" % (key, value, round(y * float(value),2))

a = dictionary2.keys()[spot]

print "\t**Approx based on %s @ $%s" % (a, y)

filename = 'bitcoin.price' ; target = open(filename, 'w') ; target.truncate()
target.write("{0}".format(dictionary2)) ; target.close()
print "\nBase dictionary for older scripts also updated\n"

hashurl = ["https://blockchain.info/stats"]
hashxpath = "//div[@class='container']/table/tbody/tr[20]/td[2]"
totalpowerlist = []

for h in hashurl:
    btchashget = driver.get(hashurl)
    gethash = driver.find_element_by_xpath(hashxpath)
    hashpowerraw = gethash.get_attribute("innerHTML")
    totalpower = float(str(hashpowerraw)[:-4].replace(",", ""))
    totalpowerlist.append(totalpower)

hashbang = totalpowerlist[0]



#########Trying to add peta stats

hashurl = "http://www.peta-mine.co/stats/"
quarter_id = "requestNumber"
hour_id = "CPU"
day_id = "memoryConsumption"

# dividends = {"Dividends" : "//div[@class='tablewrap']/table/tbody/tr[17]/td[8]"}

hashdictionaryofids = { "15 minute" : quarter_id, "1 hour" : hour_id, "24 hour" : day_id }

hashpower = [] 
#driver = webdriver.Firefox()
driver.get(hashurl)

for ids in hashdictionaryofids.values(): 
    catch = driver.find_element_by_id(ids)
    raw = catch.get_attribute("innerHTML")
    soup = BeautifulSoup(raw)
    cleanedhash = float(str(''.join(soup.findAll(text=True))[:].replace(",", "")))
    hashpower.append(cleanedhash)
#    print "The hash rate for %s is %r" (id, cleanedhash) 


hashdictionary = {}
hashdictionary = dict(zip(hashdictionaryofids.keys(),hashpower))

print "Now checking the peta-mining stats:"
for key, value in hashdictionary.iteritems():
    print "\tThe %s hash rate in %s TH/s" % (key, value) 

# Calculations to follow later
# AMybe import some maths classes
current = float(hashdictionary.values()[2])
print "\nUsing the 24hr average hashrate: %sTH/s vs IPO commit to 700TH/s" % current
aim = 700
hashpercentage = (current / aim) 
print "The current hashrate is %s%% of the total IPO" % (round(hashpercentage,2) * 100)

## Trying some 100% mining stats

print "\tWeekly share rtn: %s = return @ %s%% of mining power" % (d, round(hashpercentage,2))
print "\tWeekly share rtn: %s = return @ 100%% of mining power" % (round((float(d) / hashpercentage), 5))
tt = float(d) / hashpercentage
fullshareyield = shares * tt
fullsharereturn = fullshareyield * y
print "\tFull hash @ %s shares would = B%s = $%s @ %s price" % (shares, round(fullshareyield,5), round(fullsharereturn,3), a) 

print "\nNow getting bitcoin network hashrate and peta's contribution"
print "Total network hashing power: %s" % hashpowerraw
currentinths = current * 1024
print "\nConverting both to GH/s \n\tBitcoin total network: %sGH/s\n\tPeta-mine total power: %sGH/s" % (hashbang, currentinths)
hashper = ((currentinths * 100) / hashbang)
print "\tPeta %% is: %s%%" % round(hashper,3)
petaall = (shares / 80600)
print "\nAnd finally"
print "\tIf you own %s of peta\n\tthen you have %s GH/s\n\tGiving you %s of all BTC mining power" % (petaall, currentinths * petaall, hashper * petaall)

driver.quit()
# display.stop()


