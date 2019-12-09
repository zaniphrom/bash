#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

# https://uauth.iponweb.com/uauth/settings/
# scope uslicer.iponweb.com
token = ""
slicer = "https://uslicer.iponweb.com/API/v2/url_to_api"

get_info = requests.post(slicer, json=url_api)
raw = get_info.json()
print(json.dumps(raw, sort_keys=True, indent=4))

# print(get_info.text)
#
# //get dataOverall"
# function getDataOverall() {
#
#     var url = 'https://uslicer.iponweb.com/API/v2/export';
#
# //Step 1 - Add your API token below
#
# var apiParams = {
#     'slicer_name' : 'traffic',
#     'project_name': 'bidswitch',
#     'token': apiToken,
#     'split_by': ['granularity_quarter','granularity_month',  'dsp_id', 'ssp', 'geo_country' ],
#     'include_mappings': 1,
#     'start_date': '2019-01-01',
#     'end_date': '2019-09-30',
#     'data_fields': ['all_ssp_bid_requests','dsp_bid_requests','dsp_yes_bids', 'imps','dsp_final_price_usd', 'timeouts', 'dsp_no_bids', 'dsp_invalid_bids', 'dsp_invalid_responses', 'invalid_bid_violates_bidfloor', 'timeout_pct'],
#     'export_format' : 'csv',
#     'filters' : [{"name" : "dsp_id","value": ['16'],"match" : "equals"}, {"name" :"inventory_type", "value": ['application'], "match" : "equals"}],
#     'data_filters' : [{"name": "dsp_bid_requests", "value": "0", "match": ">"}]
# }
#
# var payload = JSON.stringify(apiParams);
# var params = {
#     'method': 'POST',
#     'payload': payload,
#     'muteHttpExceptions' : true,
# };
#
# var response = UrlFetchApp.fetch(url, params)
#
# var csvData = Utilities.parseCsv(response);
# //Step 8 - Add in the name of the spreadsheet that is collecting the data
# var ss = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("overall");
# ss.getRange(1, 1, csvData.length, csvData[0].length).setValues(csvData);
#
# }

#
# payload = {
#     "slicer_name": "traffic",
#     "project_name": "bidswitch",
#     "token": token,
# }
#
# audience = {
#     "slicer_name": "client",
#     "project_name": "bc-sparta",
#     "token": token,
#     "split_by": "bid_context_wrapper.user.agent.browser.name",
#     "start_date": "2019-10-15",
#     "end_date": "2019-10-28",
#     "filters": [
#         {
#             "name": "bid_context_wrapper.demand.advertiser_id",
#             "value": ["3"],
#             "match": "equals",
#         }
#     ],
# }
#
# export = {
#     "slicer_name": "client",
#     "project_name": "bc-sparta",
#     "token": token,
#     "split_by": "bid_context_wrapper.demand.campaign_id",
#     "start_date": "2019-10-15",
#     "end_date": "2019-10-28",
#     "export_format": "csv",
#     "filters": [
#         {
#             "name": "bid_context_wrapper.user.geo.country_region",
#             "value": ["US-NY-"],
#             "match": "equals",
#         },
#         {
#             "name": "bid_context_wrapper.user.agent.browser.name",
#             "value": ["Chrome"],
#             "match": "equals",
#         },
#     ],
# }
#
#
# query = {
#     "slicer_name": "client",
#     "project_name": "bc-sparta",
#     "token": token,
#     "split_by": [
#         # "bid_context_wrapper.bid.ssp",
#         # "bid_context_wrapper.supply.publisher_id",
#         # "bid_context_wrapper.demand.campaign_id",
#         # "bid_context_wrapper.user.agent.browser.name",
#         # "bid_context_wrapper.user.agent.browser.version",
#         # "bid_context_wrapper.user.agent.os.name",
#         # "bid_context_wrapper.user.agent.os.version",
#         # "bid_context_wrapper.user.agent.device.type",
#         # "bid_context_wrapper.user.agent.device.model",
#         # "languages_list",
#         # "bid_context_wrapper.supply.site_domain",
#         # "bid_context_wrapper.supply.page_domain",
#         "blocked_adv_categories"
#         # "bid_context_wrapper.supply.site_id",
#         # "bid_context_wrapper.supply.visibility"
#     ],
#     "start_date": "2019-10-16",
#     "end_date": "2019-10-28",
#     "include_mappings": 1,
#     "data_filters": [{"name": "imps", "value": "1", "match": ">="}],
#     "filters": [
#         {
#             "name": "bid_context_wrapper.demand.campaign_id",
#             "value": ["3"],
#             "match": "contains",
#             "case_insensitive": 1,
#             "search_mappings": 1,
#         },
#         {
#             "name": "bid_context_wrapper.user.agent.browser.name",
#             "value": ["Chrome"],
#             "match": "equals",
#         },
#     ],
#     "data_fields": [
#         "imps",
#         "clicks",
#         "payout.actual_pub",
#         "vast_start",
#         "bids",
#         "bid_amount",
#     ],
# }
#
# time_series = {
#     "slicer_name": "client",
#     "project_name": "bc-sparta",
#     "timezone": 1,
#     "token": token,
#     "limit": 400,
#     "split_by": [
#         "bid_context_wrapper.demand.campaign_id"
#     ],
#     "start_date": "2019-10-23",
#     "end_date": "2019-10-28",
#     "granularity": "year",
#     "chart_lines": ["bid_context_wrapper.demand.campaign_id"],
#     "filters": [
#         {
#             "name": "bid_context_wrapper.demand.campaign_id",
#             "value": ["3"],
#             "match": "equals"
#         }
#     ],
#     "data_field": "imps",
# }
#
#
url_api = {
    # "slicer_name": "traffic",
    # "project_name": "bidswitch",
    "token": token,
    "url": "https://uslicer.iponweb.com/bidswitch/UI/Reports/Traffic?category=country_region&chart_column=all_ssp_bid_requests&start_date=2019-10-16&end_date=2019-10-29&granularity=granularity_day&normalization=value&id_list=total&order_by=timeout_pct&order_direction=DESC&parent_key=dsp_id&parent_key=geo_country&parent_match=equals&parent_match=equals&parent_value=16&parent_value=PL&show=dsp_yes_bids%2Cimps%2Cdsp_final_price_usd%2Ctimeout_pct%2Cdsp_final_price_adj_usd%2Cdsp_invalid_bids&field_order=timeout_pct%2Cdsp_bid_requests%2Cdsp_no_bids%2Cdsp_final_price_adj_usd&version=23.11.2",
}
