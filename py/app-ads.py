#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import requests
from requests.exceptions import ConnectionError


def apps():
    """gets the app-ads.txt file and parses it for app data"""
    url = "https://appadstxt.bidswitch.com/apps.json"
    raw = requests.get(url, timeout=5.5)
    return raw.json()["apps"]


# for obj in apps():
#   devurl = obj["dev_url"]
#   if "google_play" in obj:
#     gplay = obj["google_play"]["bundle"]
#     print("\"" + devurl + "\"" + "," + "\"" + gplay + "\"" )
#   else:
#     continue
#   if "iTunes" in obj:
#     istore = obj["iTunes"]["bundle"]
#     print("\"" + devurl  + "\"" + ", "  + "\"" + istore  + "\"" )
#   else:
#     continue

## check all dev URLs for an ads-app.txt file


def urls():
    urls = []
    for obj in apps():
        devurl = obj["dev_url"]
        urls.append(devurl)
    return list(set(urls))


def urlcheck():
    """takes all devurls and checks their header return"""
    count = 0
    urlstatus = []
    for num, devurl in enumerate(urls()):
        appads = "https://" + devurl + "/app-ads.txt"
        try:
            x = requests.head(appads, timeout=3.5)
        except requests.exceptions.Timeout:
            status = "Timeout"
        except ConnectionError:
            status = "404"
        else:
            status = x.status_code
        tt = '"{}", "{}"'.format(appads, status)
        urlstatus.append(tt)
        count += 1
        if (num + 1) % 5 == 0:
            break
    return urlstatus


def statuscsv():
    """write the output to this csv file"""
    with open("app-ads-txt.csv", "w") as outfile:
        for i in urlcheck():
            outfile.write(i)
            outfile.write("\n")
        # return(outfile)


print(statuscsv())


#

# import requests, json
#
# login = '***'
# password = '***'
#
# payload = {
#   "grant_type": "password",
#   "username": login,
#   "password": password,
#   "scope": "service_id=api.bidswitch.com"
# }
#
# url = "https://uauth.iponweb.com/oauth2/token/"
#
# response_decoded_json = requests.post(url, data=payload, headers={})
# response_json = response_decoded_json.json()
#
# token = response_json['access_token']
#
# url = "https://my.bidswitch.com/api/blocking/ssps/dsptest/creatives/"
#
# payload = {}
#
# headers = {'Authorization': 'Bearer ' + token}
#
# response_decoded_json = requests.post(url, data=payload, headers=headers)
# response_json = response_decoded_json.json()
#
# print response_json
