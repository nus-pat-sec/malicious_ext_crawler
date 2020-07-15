from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
# for converting text to num and extract num
import re

import pandas as pd
driverLocation = '/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/selenium_project/chromedriver' 

# url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos?view=0&sort=p&flow=grid'
# url = 'https://chrome.google.com/webstore/search/ledger?hl=en&_category=extensions'
url = 'https://addons.mozilla.org/en-US/firefox/search/?q=ledger&type=extension'
driver = webdriver.Chrome(driverLocation)
driver.get(url)

# style-scope ytd-grid-video-renderer
# videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
# videos = driver.find_element_by_css_selector('body > div.F-ia-k.S-ph.S-Rc-qa > div.F-k > main > div > div.h-a-S > div > div.h-a-x > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a > div.a-na-d > div.a-na-d-B1neQd-cb > div.a-na-d-K-A-w > div.a-na-d-K-w > div.a-na-d-w')
# get_all = driver.html
extensions = driver.find_elements_by_class_name('SearchResult')

print(extensions)

# /html/body/div[10]/div[4]/main/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a/div[3]/div[1]/div[1]/div[2]/div[1]
# //*[@id="video-title"]

# video_list = []
# extension_list = []
# for video in videos:
#     title = video.find_element_by_xpath('./html/body/div[10]/div[4]/main/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a/div[3]/div[1]/div[1]/div[2]/div[1]').text
#     print(title)
#     vid_item = {
#         'title': title
#     }
#     video_list.append(vid_item)
# //*[@id="react-view"]/div/div/div/div[2]/div/section/div/ul/li[2]/div/div/div[2]/h2/a
# index = extensions.count()
# print(index)
extension_list = []
for extension in extensions:
    name = extension.find_element_by_css_selector('.SearchResult-link').text
    # print(name)
    
    text_user_numbers = extension.find_element_by_css_selector('.SearchResult-users-text').text
    text_rating  = extension.find_element_by_css_selector('.visually-hidden').text
    user_numbers = [int(i) for i in text_user_numbers.split() if i.isdigit()] 
    # if len(rating) == 0:
    #     user_numbers = [0]
    # take the first digit to be rating number. the format of text_rating is 4.5 out of 5.0
    rating = re.findall("\d+", text_rating)
    # rating = [int(i) for i in text_rating.split() if i.isdigit()] 
    if len(rating) == 0:
        rating = [0]
    # Checking basic requirements for malicious ext
    ext_item = {
        'name': name,
        'user_numbers': user_numbers,
        'rating': int(rating[0])
    }

    if int(rating[0]) <= 3: 
        extension_list.append(ext_item)

    
df = pd.DataFrame(extension_list)
# print(df)
df.to_csv (r'/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/selenium_project/export_dataframe.csv', index = False, header=True)


