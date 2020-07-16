import scrapy
import scrapy_selenium
from scrapy_selenium import SeleniumRequest
import pandas as pd
import re



#Class for defining how your spider is gonna work~!
class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
    # start_urls = [
        
    #     # 'https://chrome.google.com/webstore/search/trezor?hl=en&_category=extensions'
    # ]

    # for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)



    def start_requests(self):
        urls = [
            'https://addons.mozilla.org/en-US/firefox/search/?q=ledger&type=extension'
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)

    # yield SeleniumRequest(url=url, callback=self.parse_result)
    # Loop through the urls to retrieve the expected data
    # for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # parsing the data from pages from the list of url
    def parse(self, response):
        extension_list = []

        # test = response.request.meta['driver'].find_elements_by_class_name('SearchResult').text
        # response.request.meta['driver'].title
        # print(response.request.meta['driver'].title)
        # name_extension = response.css('SearchResult::text')
        # page = response.css('.a-na-d-w').extract()
        extensions = response.request.meta['driver'].find_elements_by_class_name('SearchResult')
        # print(response.request.meta['driver'].title)
        for extension in extensions:
            # Extract metadata of each extensions
            name = extension.find_element_by_css_selector('.SearchResult-link').text

            text_user_numbers = extension.find_element_by_css_selector('.SearchResult-users-text').text
            user_numbers = re.findall("[-+]?\d*\,?\d+|\d+", text_user_numbers)

            text_rating  = extension.find_element_by_css_selector('.visually-hidden').text
            rating = re.findall("[-+]?\d*\.?\d+|\d+", text_rating)
            
            if len(rating) == 0:
                rating = [0]
            
            text_user_numbers = extension.find_element_by_css_selector('.SearchResult-users-text').text
            user_numbers = re.findall("[-+]?\d*\,?\d+|\d+", text_user_numbers)

            ext_item = {
                'name': name,
                'user_numbers': user_numbers[0],
                'rating': rating[0]
            }
            extension_list.append(ext_item)
        # yield {'body': name}


        # Create dataframe for it
        df = pd.DataFrame(extension_list)       
        # with open('test', 'wb') as f:
        #     f.write()
        # # filename = 'test-%s.html' % page
        # # with open(filename, 'wb') as f:
        # #     f.write(response.body)
        # df = pd.DataFrame(test)
        df.to_csv (r'/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/malicious_ext_crawler/malicious_ext_crawler/export_dataframe.csv', index = False, header=True)



    