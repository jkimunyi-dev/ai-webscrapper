import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Remote, ChromeOptions
from bs4 import BeautifulSoup
import time

def custom_webscrapper(website):
    print("Launching chrome browser...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded ...")
        html = driver.page_source
        time.sleep(2)  # Sleep for 2 seconds or a reasonable time
        return html
    finally:
        driver.quit()

# Bright Data
SBR_WEBDRIVER = 'https://brd-customer-hl_b7c1c997-zone-ai_scrapper:2g1s9v0nulmc@brd.superproxy.io:9515'

def scrape_website_with_brightdata(website):
    print('Connecting to Scraping Browser...')
    options = ChromeOptions()
    sbr_connection = Remote(SBR_WEBDRIVER, options=options)
    with sbr_connection as driver:
        driver.get(website)

        # CAPTCHA handling
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)
    ]
