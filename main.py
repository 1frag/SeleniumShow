import logging
from selenium import webdriver
import traceback
import time
import os

logger = logging.getLogger(__name__)

CHROMEDRIVER_PATH = os.path.join(os.getcwd(), 'chromedriverr')

logger.info('preparing...')
time.sleep(2)
logger.info('starting...')

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               options=chrome_options)
    browser.close()
except Exception as e:
    logger.error(f'failed with {e}')
    logging.error(traceback.format_exc())
else:
    logger.info('exit 0')
