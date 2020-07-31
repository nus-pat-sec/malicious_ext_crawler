import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re
import json
import csv
# For beautiful soup using
from bs4 import BeautifulSoup
import requests

import dateutil.parser as dparser




class ChromeExtensions(scrapy.Spider):
    # Name of this spider
    name = 'chrome_extensions'
    # start_urls = ['https://chrome.google.com/webstore/search/ledger?hl=en']
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Length": "0",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    }

    def start_requests(self):
        url = 'https://chrome.google.com/webstore/ajax/item?hl=en&gl=AU&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Car2%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&count=100&category=extensions&searchTerm=ledger&sortBy=0&container=CHROME&_reqid=139507&rt=j'

        yield scrapy.Request(url, method='POST', callback=self.parseapi, headers = self.headers)

    # def parse(self, response):
    #     # Chrome store API only return 20 results per request.
    #     url = 'https://chrome.google.com/webstore/ajax/item?hl=en&gl=AU&pv=20200420&mce=atf%2Cpii%2Crtr%2Crlb%2Cgtc%2Chcn%2Csvp%2Cwtd%2Chap%2Cnma%2Cdpb%2Car2%2Cc3d%2Cncr%2Cctm%2Cac%2Chot%2Cmac%2Cepb%2Cfcf%2Crma&count=100&category=extensions&searchTerm=ledger&sortBy=0&container=CHROME&_reqid=139507&rt=j'
    #     request =  scrapy.Request(url, method='POST', callback=self.parseapi, headers = self.headers)
    #     yield request

    def parseapi(self, response):
        raw_data = response.body.decode("utf-8")
        removed = raw_data.replace(')]}\'','')
        data = json.loads(removed)
        # Get the list of extensions
        list_extensions = data[0][1][1]
        list_form = []
        
        # 20 for each request
        for each_extension in list_extensions:
            # previous_data = {
            #     "a": "0",
            #     "id_ex": "NaN"  
            # }
            id_ex = each_extension[0]
            key = each_extension[61]
            name = each_extension[1]
            creator = each_extension[2]
            rating = each_extension[12]
            user_numbers = re.findall("[-+]?\d*\,?\d+|\d+", each_extension[23])
            details_link = each_extension[37]

            if details_link is not None:
                # details_link = response.urljoin(details_link)
                r = requests.get(details_link)
                soup = BeautifulSoup(r.content, 'html.parser')
                # title = soup.title.text
                last_updated = soup.find('span', class_='C-b-p-D-Xe h-C-b-p-D-xh-hh').text
            #     details_link = response.urljoin(details_link)
                # request_temp = scrapy.Request(details_link, callback=self.parse_extension, cb_kwargs={'previous_data':previous_data})
                # yield request_temp
                formated_last_updated = dparser.parse(last_updated,fuzzy=True)

            
            # previous_data["id_ex"] = id_ex
            ext = {
                'platform': "chrome",
                'id': id_ex,
                'key': key,
                'name': name,
                'rating': rating,
                'user_numbers': user_numbers[0],
                'creator': creator,
                'last_updated': formated_last_updated.strftime('%Y-%m-%d 00:00:00')

            }

            list_form.append(ext)
#         # print()
#         # print(data)
#         # yield {
#         #     "name": each[1]
#         # }
# list_extensions[1][1]
        with open('aaa.json', 'w') as jsonfile:
            # a = (*list_form,sep='\n')
            json.dump(list_form, jsonfile, indent=2)
            # jsonfile.write('\n')
    
    
    
 