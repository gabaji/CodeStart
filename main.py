# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:43:55 2020

@author: Ayush Gaba
"""

import os
os.listdir()

# #lauching spyder
f = open('spyderpath.txt','r')
pathtospyder=f.read()
f.close()
import os
print(pathtospyder)
os.startfile(pathtospyder)


# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

options = webdriver.ChromeOptions()
cap = DesiredCapabilities.CHROME.copy()
options.add_argument('user-data-dir=C://Users//Ayush Gaba//AppData//Local//Google//Chrome//User Data')

browser = webdriver.Chrome(executable_path='C://Users//Ayush Gaba//Desktop//CodeStart//chromedriver.exe',
chrome_options=options,
desired_capabilities=cap)

browser.get('https://leetcode.com')
time.sleep(3)

try:
    elem=browser.find_element_by_xpath('//*[@id="landing-page-app"]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]/span')
    elem.click()
    time.sleep(3)
except :
    import sys
    sys.exit()

elem=browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/button/div')
elem.click()