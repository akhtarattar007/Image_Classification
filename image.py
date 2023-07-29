import os

# selenuim 4
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_urls(query: str, dealy: int) ->set:
    images_url= set()
    browser= webdriver.Chrome()
    browser.get('https://images.google.com/')
    search_box= browser.find_element(By.CSS_SELECTOR, '#APjFqb.gLFyf')
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(5)
    return browser

'''
def setup_browser() -> webdriver.Chrome:
    browser= webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
    browser.get('https://images.google.com/')
    time.sleep(2)

    return browser

setup_browser()
'''

get_urls('narendra modi', 2)