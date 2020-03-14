import logging
from selenium import webdriver
import traceback
import time

logger = logging.getLogger(__name__)

logger.info('preparing...')
time.sleep(15)
logger.info('starting...')

try:
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               chrome_options=chrome_options)
    browser.close()
except Exception as e:
    logger.error(f'failed with {e}')
    logging.error(traceback.format_exc())
else:
    logger.info('exit 0')
