#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# https://uauth.iponweb.com/uauth/settings/
# scope uslicer.iponweb.com
slicer = "https://uslicer.iponweb.com/API/v2/url_to_api"

url_api = {
    "token": token,
    "url": "https://uslicer.iponweb.com/bidswitch/UI/Reports/Traffic?category=dsp_id&chart_column=all_ssp_bid_requests&start_date=-3d&end_date=-1d&tzo=-3&granularity=granularity_day&normalization=value&id_list=total&order_by=dsp_final_price_adj_usd&order_direction=DESC&parent_key=granularity_day&parent_key=ssp&parent_match=equals&parent_match=equals&parent_value=2019-10-27&parent_value=emxdigital&show=dsp_no_bids%2Cdsp_final_price_adj_usd%2Cdsp_yes_bids%2Cimps%2Cdsp_final_price_usd&field_order=timeout_pct%2Cdsp_bid_requests%2Cdsp_no_bids%2Cdsp_final_price_adj_usd&version=23.11.2",
}

get_info = requests.post(slicer, json=url_api)
raw = get_info.json()
print(json.dumps(raw, sort_keys=True, indent=4))
