import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re

import csv


class ChromeExtensions(scrapy.Spider):
    # Name of this spider
    name = 'chrome_extensions'
    start_urls = ['https://chrome.google.com/webstore/search/ledger?hl=en']
    headers = {
        # ":authority": "chrome.google.com",
        # ":method": "POST",
        # ":path": "/webstore/ajax/item?hl=en&gl=AU&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Car2%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&count=112&searchTerm=ledger&sortBy=0&container=CHROME&_reqid=131433&rt=j",
        # ":scheme": "https",
        # "accept": "*/*",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "en-US,en;q=0.9,vi;q=0.8",
        # "cache-control": "no-cache",
        # content-length: 7
        # content-type: application/x-www-form-urlencoded;charset=UTF-8
        # cookie: CONSENT=YES+AU.en+202005; __utmc=73091649; S=billing-ui-v3=oG8hLixmhCrcdjdIAWupoQ9iQgc8t9eU:billing-ui-v3-efe=oG8hLixmhCrcdjdIAWupoQ9iQgc8t9eU; OGPC=19018523-1:; SEARCH_SAMESITE=CgQIlpAB; __utmz=73091649.1595765044.18.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); 1P_JAR=2020-7-26-12; NID=204=WHt6fjlwzHlws9aFsUUgF2CZnJ-jVw_UziBQKIcRmTc_ALJ66oay6l5tahBlj0YbdiU0rxI0WkaKNM3ZEHslaUK1IZW8qiuevPAdMuXQkSWtJbCsgeDkOS8XAeeFjnJbOVW1OLdw6nsEp6pdWgAsQNqWMUG7f0st67oxbGRcoXCUShX4yQ9C6U3MJmC2mesxRhMFK7Qcsw7z6l_w; __utma=73091649.506141671.1592372278.1595765978.1595765978.20; __utmt=1; __utmb=73091649.4.9.1595803432622
        # origin: https://chrome.google.com
        # pragma: no-cache
        # referer: https://chrome.google.com/
        # sec-fetch-dest: empty
        # sec-fetch-mode: cors
        # sec-fetch-site: same-origin
        # user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36
        # x-client-data: CJK2yQEIprbJAQjBtskBCKmdygEI/rzKAQjnyMoB
        # x-same-domain: 1
    }

    def parse(self, response):
        url = 'https://chrome.google.com/webstore/ajax/item?hl=en&gl=AU&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Car2%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&count=112&searchTerm=ledger&sortBy=0&container=CHROME&_reqid=180379&rt=j'