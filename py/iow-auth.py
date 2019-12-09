#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import csv
import requests
from requests.exceptions import ConnectionError


auth_url = "https://uauth.iponweb.com/oauth2/token/"
payload = {
    "grant_type": "password",
    "scope": "service_id=api.bidswitch.com",
    "username": "",
    "password": "",
}

x = requests.post(auth_url, data=payload)

print(x.headers)

#
# grant_type=password
# scope=service_id=api.bidswitch.com
# username=<USERNAME> <!-- Your BidSwitch UI login -->
# password=<PASSWORD> <!-- Your Bidswitch UI password -->
#
