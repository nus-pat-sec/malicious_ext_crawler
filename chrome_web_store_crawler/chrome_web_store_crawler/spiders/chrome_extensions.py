import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re
import json
import csv


class ChromeExtensions(scrapy.Spider):
    # Name of this spider
    name = 'chrome_extensions'
    start_urls = ['https://chrome.google.com/webstore/search/ledger?hl=en']
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Length": "0",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    }

    def parse(self, response):
        url = 'https://chrome.google.com/webstore/ajax/item?hl=en&gl=AU&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Car2%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&count=112&searchTerm=ledger&sortBy=0&container=CHROME&_reqid=180379&rt=j'
        request = scrapy.Request(url, method='POST', callback=self.parse_api, headers = self.headers)

        yield request

    def parse_api(self, response):
        raw_data = response.body.decode("utf-8")
        removed = raw_data.replace(')]}\'','')
        data = json.loads(removed)

        # Get the list of extensions
        list_extensions = data[0][1][1]
#       
        for each_extension in list_extensions:
            name = each_extension[1]
        # print()
        # print(data)
        # yield {
        #     "name": each[1]
        # }
# list_extensions[1][1]
        with open('aaa.json', 'w') as jsonfile:
	        json.dump(len(list_extensions), jsonfile)