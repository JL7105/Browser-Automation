from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
chrome_browser = webdriver.Chrome(options=options)

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert('Selenium Easy' in chrome_browser.title)
button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
print(button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I am cool')

button.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'I am cool' in output_message.text

chrome_browser.quit()