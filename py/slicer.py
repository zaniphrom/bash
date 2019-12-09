#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# https://uauth.iponweb.com/uauth/settings/
# scope uslicer.iponweb.com
slicer = "https://uslicer.iponweb.com/API/v2/query"

payload = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "token": token,
}

audience = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "token": token,
    "split_by": "bid_context_wrapper.user.agent.browser.name",
    "start_date": "2019-10-15",
    "end_date": "2019-10-28",
    "filters": [
        {
            "name": "bid_context_wrapper.demand.advertiser_id",
            "value": ["3"],
            "match": "equals",
        }
    ],
}

export = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "token": token,
    "split_by": "bid_context_wrapper.demand.campaign_id",
    "start_date": "2019-10-15",
    "end_date": "2019-10-28",
    "export_format": "csv",
    "filters": [
        {
            "name": "bid_context_wrapper.user.geo.country_region",
            "value": ["US-NY-"],
            "match": "equals",
        },
        {
            "name": "bid_context_wrapper.user.agent.browser.name",
            "value": ["Chrome"],
            "match": "equals",
        },
    ],
}


query = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "token": token,
    "split_by": [
        # "bid_context_wrapper.bid.ssp",
        # "bid_context_wrapper.supply.publisher_id",
        # "bid_context_wrapper.demand.campaign_id",
        # "bid_context_wrapper.user.agent.browser.name",
        # "bid_context_wrapper.user.agent.browser.version",
        # "bid_context_wrapper.user.agent.os.name",
        # "bid_context_wrapper.user.agent.os.version",
        # "bid_context_wrapper.user.agent.device.type",
        # "bid_context_wrapper.user.agent.device.model",
        # "languages_list",
        # "bid_context_wrapper.supply.site_domain",
        # "bid_context_wrapper.supply.page_domain",
        # "blocked_adv_categories",
        # "is_app",
        # "hour_str",
        # "content_categories",
        # "anomaly_segment",,
        # "requested_sizes",
        "segments_list"
        # "bid_context_wrapper.demand.tag_type"
        # "bid_context_wrapper.supply.site_id",
        # "bid_context_wrapper.supply.visibility"
    ],
    "start_date": "2019-10-16",
    "end_date": "2019-10-28",
    "include_mappings": 1,
    "data_filters": [{"name": "imps", "value": "1", "match": ">="}],
    "filters": [
        {
            "name": "bid_context_wrapper.demand.campaign_id",
            "value": ["3"],
            "match": "contains",
            "case_insensitive": 1,
            "search_mappings": 1,
        },
        {
            "name": "bid_context_wrapper.user.agent.browser.name",
            "value": ["Chrome"],
            "match": "equals",
        },
    ],
    "data_fields": [
        "imps",
        "clicks",
        "payout.actual_pub",
        "vast_start",
        "bids",
        "bid_amount",
    ],
}

time_series = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "timezone": 1,
    "token": token,
    "limit": 400,
    "split_by": ["bid_context_wrapper.demand.campaign_id"],
    "start_date": "2019-10-23",
    "end_date": "2019-10-28",
    "granularity": "year",
    "chart_lines": ["bid_context_wrapper.demand.campaign_id"],
    "filters": [
        {
            "name": "bid_context_wrapper.demand.campaign_id",
            "value": ["3"],
            "match": "equals",
        }
    ],
    "data_field": "imps",
}


url_api = {
    "slicer_name": "client",
    "project_name": "bc-sparta",
    "token": token,
    "url": "https://uslicer.iponweb.com/bc-sparta/UI/Reports/Traffic?category=bid_context_wrapper.user.agent.device.type&chart_column=bids&start_date=2019-10-16&end_date=2019-10-29&granularity=granularity_hour&normalization=value&id_list=total&order_by=win_bid_amount&order_direction=ASC&parent_key=bid_context_wrapper.demand.advertiser_id&parent_key=bid_context_wrapper.user.agent.os.version&parent_match=equals&parent_match=equals&parent_value=3&parent_value=Windows_10&show=bids%2Cnobids%2Cimps%2Cclicks%2Cbid_amount%2Cwin_bid_amount%2Cpv_convs%2Cpc_convs%2Cpayout.adv_payout%2Cpayout.actual_pub%2Cpv_conversions%2Cpc_conversions%2Cviewable_imps&version=23.11.2",
}


get_info = requests.post(slicer, json=query)
raw = get_info.json()
print(json.dumps(raw, sort_keys=True, indent=4))

# print(get_info.text)
