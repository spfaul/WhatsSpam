from src.consts import msg_box_SELECTOR
from selenium.webdriver.common.keys import Keys
import time

def spam(browser, message, spam_times):
    print('\nSpam Starting...')
    print('Press Ctrl-C To Force Stop And Exit.')
    msg_box = browser.find_element_by_css_selector(msg_box_SELECTOR)

    for _ in range(spam_times):
        msgs = message.split("\n")
        for msg in msgs:
            msg_box.send_keys(msg)
            msg_box.send_keys(Keys.SHIFT+Keys.ENTER)

        time.sleep(0.02)
        msg_box.send_keys(Keys.ENTER)

    print('Spam Finished Successfully!')


