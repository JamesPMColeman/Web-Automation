from time import sleep
from selenium import webdriver


browser = webdriver.Firefox()

browser.get('https://www.google.com')

sleep(5)

browser.close()