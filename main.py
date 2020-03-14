import logging
from selenium import webdriver
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level='DEBUG')


def production():
    # https://github.com/heroku/heroku-buildpack-chromedriver
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    # https://github.com/heroku/heroku-buildpack-google-chrome
    GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google-chrome'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.binary_location = GOOGLE_CHROME_BIN

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               options=chrome_options)
    return browser


def local():
    path = os.path.join(os.getcwd(), 'chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(executable_path=path,
                               options=chrome_options)
    browser.close()
    return browser


def get_browser():
    if os.getenv('IS_PRODUCTION'):
        return production()
    else:
        return local()
