import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re

import csv


class ChromeExtensions(scrapy.Spider):
    # Name of this spider
    name = 'chrome_extensions'
    def start_requests(self):
        # List of urls for crawling
        urls = []
        # Path to keywords.csv
        path_keywords_csv = '/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/malicious_ext_crawler/malicious_ext_crawler/spiders/keywords.csv'
        # READ and GENERATE urls with keywords 
        with open(path_keywords_csv, mode='r', encoding='utf-8-sig') as csv_file:
            data = csv.reader(csv_file)
            for row_keyword in data:
                combined_keyword_url = 'https://chrome.google.com/webstore/search/%s?hl=en&_category=extensions' % row_keyword[0]
                urls.append(combined_keyword_url)
        # SEND and REQUEST the urls using selenium driver/chrome
        for url in urls:
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)


    def parse(self, response):
        print(response.css('title::text').get())