# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:07:24 2019

@author: Raval
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options
opts = Options()
#opts.set_headless()
#assert opts.headless
opts.binary_location = 'C:/Users/Raval/mystuff/chromedriver_win32/chromedriver.exe'
browser = Chrome(options=opts)
time.sleep(10)

maxtries=0

browser.get('https://music.amazon.com/stations')

time.sleep(5)
print ("title of the home page is - ", browser.title)
#browser.find_element_by_link_text('Sign In').click()
browser.find_element_by_class_name('signInButton').click()
time.sleep(5)
email_element = browser.find_element_by_id("ap_email")
email_element.send_keys('raviraval@yahoo.com')
time.sleep(2)

pwd_element = browser.find_element_by_id("ap_password")
pwd_element.send_keys("sw1tpr1t")
time.sleep(2)
#pwd_element.submit()
#time.sleep(5)
submit_element = browser.find_element_by_id("signInSubmit")
submit_element.submit()
time.sleep(20)

while maxtries < 2:
    nextpage = browser.title
    print ("entering while loop ")
    print ("title of the current page is - ", nextpage)

    if nextpage.endswith("Library"):
        print ("login successful ")
        search_element = browser.find_element_by_id("searchMusic")
        search_element.send_keys("thunderstruck by acdc")
        time.sleep(2)
        browser.find_element_by_class_name("playerIconSearch").click()
        
        time.sleep(5)
        
        browser.find_element_by_class_name("playerIconSearch").click()
        
        time.sleep(5)
        #browser.find_element_by_link_text("Thunderstruck").click()
        print ("playing song")
        
        #playbutton = browser.find_element_by_xpath("//*[@id=\"dragonflyView\"]/div/div[2]/div[2]/section/section/div[2]/div/div[1]/div[1]/div[1]/div/div/div[2]/div[2]")
        
        print("the button is selected? ", playbutton.is_selected())
        
        maxtries = maxtries+1
    elif nextpage.endswith("Sign In"):
        print ("Login Failed...trying again")
        email_element = browser.find_element_by_id("ap_email")
        email_element.send_keys('raviraval@yahoo.com')
        time.sleep(5)
        print ("entering password")
        pwd_element = browser.find_element_by_id("ap_password")
        pwd_element.send_keys("sw1tpr1t")
        
#        time.sleep(5)
#        pwd_element.submit()
#        time.sleep(5)
        print ("submitting ")
        submit_element = browser.find_element_by_id("signInSubmit")
        submit_element.submit()
        time.sleep(15)
        maxtries = maxtries+1
    else:
        print("sorry this doesnt seem to work")
        
time.sleep(15)
print ("title of the last page is - ", browser.title)
browser.close()




