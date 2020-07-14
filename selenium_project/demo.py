from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
driverLocation = '/Users/thanhtrv/Documents/work/2020/winter_research_2020/malicious_browser_extensions_scrapy/selenium_project/chromedriver' 

url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome(driverLocation)
driver.get(url)


# style-scope ytd-grid-video-renderer
videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')
# //*[@id="video-title"]

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    print(title)