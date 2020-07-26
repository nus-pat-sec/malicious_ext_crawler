import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re

import csv
import codecs

class FirefoxDetails(scrapy.Spider):
    # Name of this spider
    name = 'firefox_details'

    # PREPARATION for Start Requests
    # before parsing
    def start_requests(self):
        # List of urls for crawling
        urls = []
        # Path to selected_extensions.csv
        path_keywords_csv = 'selected_extensions.csv'
        # READ and GENERATE urls with keywords 
        with open(path_keywords_csv, mode='r', encoding='utf-8-sig') as csv_file:
            data = csv.reader(csv_file)
            for row_keyword in data:
                combined_keyword_url = 'https://addons.mozilla.org/en-US/firefox/addon/%s/?src=search' % row_keyword[0]
                urls.append(combined_keyword_url)
        # SEND and REQUEST the urls using selenium driver/chrome
        for url in urls:
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)

    # PARSING the data from pages
    # @response :response from selenium requests
    def parse(self, response):
        # get full response
        extensions = response.css('.SearchResult')