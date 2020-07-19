import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re

import csv
import codecs


#Class for defining how your spider is gonna work~!
class FirefoxExtensions(scrapy.Spider):
    # Name of this spider
    name = 'firefox_extensions'

    # PREPARATION for Start Requests
    # before parsing
    def start_requests(self):
        # List of urls for crawling
        urls = []
        # Path to keywords.csv
        path_keywords_csv = '/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/malicious_ext_crawler/malicious_ext_crawler/spiders/keywords.csv'
        # READ and GENERATE urls with keywords 
        with open(path_keywords_csv, mode='r', encoding='utf-8-sig') as csv_file:
            data = csv.reader(csv_file)
            for row_keyword in data:
                combined_keyword_url = 'https://addons.mozilla.org/en-US/firefox/search/?q=%s&type=extension' % row_keyword[0]
                urls.append(combined_keyword_url)
        # SEND and REQUEST the urls using selenium driver/chrome
        for url in urls:
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)

    # PARSING the data from pages
    # @response :response from selenium requests
    def parse(self, response):
        # get full response
        extensions = response.css('.SearchResult')
        # test = response.request.meta['driver'].find_elements_by_class_name('SearchResult').text
        # response.request.meta['driver'].title
        # print(response.request.meta['driver'].title)
        # name_extension = response.css('SearchResult::text')
        # page = response.css('.a-na-d-w').extract()
        # extensions = response.request.meta['driver'].find_elements_by_class_name('SearchResult')
        # print(response.request.meta['driver'].title)
        for extension in extensions:
            # Extract metadata of each extensions
            # name = extension.find_element_by_css_selector('.SearchResult-link').text
            name = extension.css('.SearchResult-link::text').get()
            text_user_numbers = extension.css('.SearchResult-users-text::text').get()
            # text_user_numbers = extension.find_element_by_css_selector('.SearchResult-users-text').text
            user_numbers = re.findall("[-+]?\d*\,?\d+|\d+", text_user_numbers)
            text_rating = extension.css('.visually-hidden::text').get()
            # text_rating  = extension.find_element_by_css_selector('.visually-hidden').text
            rating = re.findall("[-+]?\d*\.?\d+|\d+", text_rating)
            
            if len(rating) == 0:
                rating = [0]

            creator = extension.css('h3.SearchResult-author.SearchResult--meta-section::text').get()
            
            # text_user_numbers = extension.find_element_by_css_selector('.SearchResult-users-text').text
            # user_numbers = re.findall("[-+]?\d*\,?\d+|\d+", text_user_numbers)
            
            # details = extension.find_element_by_css_selector('.SearchResult-link')
            # link = details.find_element_by_
            details_link = extension.css('.SearchResult-link::attr(href)').get()
            # ext_item = {
            #     'name': name,
            #     'user_numbers': user_numbers[0],
            #     'rating': rating[0],
            #     'link': details
            # }
            if details_link is not None:
                details_link = response.urljoin(details_link)
                # yield scrapy.Request(next_page, callback=self.parse)
                yield scrapy_selenium.SeleniumRequest(url=details_link, callback=self.parse_extension, cb_kwargs={'name':name, 'user_numbers' :user_numbers[0], 'rating' :float(rating[0]), 'creator' :creator})
        
        # NEXT PAGE and repeat parse method.
        next_page = response.css('a.Button.Button--cancel.Paginate-item.Paginate-item--next::attr("href")').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy_selenium.SeleniumRequest(url=next_page, callback=self.parse)
            # yield {
            #     'name': name,
            #     'user_numbers': user_numbers[0],
            #     'rating': rating[0],
            #     'details_link': details_link
            # }
            # ext_item = {
            #     'name': name,
            #     'user_numbers': user_numbers[0],
            #     'rating': rating[0],
            #     'details_link': details_link
            # }
            # extension_list.append(ext_item)
        # yield {'body': name}


        # CREATE DATAFRAME for storing data
        # df = pd.DataFrame(extension_list)       
        # # with open('test', 'wb') as f:
        # #     f.write()
        # # # filename = 'test-%s.html' % page
        # # # with open(filename, 'wb') as f:
        # # #     f.write(response.body)
        # # df = pd.DataFrame(test)
        # df.to_csv (r'/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/malicious_ext_crawler/malicious_ext_crawler/export_dataframe.csv', index = False, header=True)


    def parse_extension(self, response, name, user_numbers, rating, creator):
        # response.css('title::text').get()
        
        yield {
            'platform': "firefox",
            'name': name,
            'rating': rating,
            'creator': creator,
            # 'details_link': details_link,
            'last_updated': response.css('dd.Definition-dd.AddonMoreInfo-last-updated::text').get()
        }