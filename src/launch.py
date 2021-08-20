import pathlib, os

import selenium as sl
from selenium.webdriver.chrome.options import Options

def launch_browser(session=None):
    print('Launching Automated Browser...')

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if session:
        options.add_argument(f'--user-data-dir={pathlib.Path().absolute()}/{session}')
    browser = sl.webdriver.Chrome(f'{os.path.dirname(__file__)}\\..\\chromedriver.exe', options=options)
    browser.get("https://web.whatsapp.com/")

    print('Successful Launch!')

    return browser
