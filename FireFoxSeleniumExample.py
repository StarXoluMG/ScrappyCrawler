#import webdriver
from selenium import webdriver

#create a webdriver object
driver = webdriver.Firefox()

#get google.co.za
driver.get("https://google.co.za / search?q = geeksforgeeks")
