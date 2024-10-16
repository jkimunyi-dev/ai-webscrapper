import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

import time


def custon_webscrapper(website):
    print("Launching chrome broswer...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options = options)

    try:
        driver.get(website)
        print("Page loaded ...")
        html = driver.page_source
        time.sleep
        return html
    finally: 
        driver.quit()

# Bright Data


