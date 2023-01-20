

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


browser_chrome = webdriver.Chrome()
#browser_edge = webdriver.Edge()

browser_chrome.maximize_window()
# browser_edge.maximize_window()

browser_chrome.get('https://www.google.com/')
# browser_edge.get('https://www.selenium.dev/')

chromeAction = ActionChains(browser_chrome)
chromeAction.send_keys('action').perform()
chromeAction.key_down(Keys.ARROW_DOWN).key_down(
    Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


# ActionChains(browser_chrome).key_down(Keys.ESCAPE).perform()
# ActionChains(browser_chrome).send_keys("action").perform()
# .key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()


# WebElement
# target_searchbutton_chrome = browser_chrome.find_element(
#    By.ID, 'docsearch-input')
# target_searchbutton_chrome.send_keys('action')

# target_searchbutton_edge = browser_edge.find_element(
#    By.CLASS_NAME, 'DocSearch-Button')

# target_searchbutton_chrome.click()
# target_searchbutton_edge.click()

#target_searchbutton_chrome.send_keys('Selenium Test Automation on Chrome')
#target_searchbutton_edge.send_keys('Selenium Test Automation on Edge')

# target_searchbox_chrome.submit()
# target_searchbox_edge.submit()

# target_element = browser.find_element(
#    By.XPATH, '/html/body/div[1]/div[4]/main/div[1]/div[2]/div/div/div[2]/div[2]/form')
# email_textbox = target_element.find_element(By.TAG_NAME, 'input')
# email_textbox.send_keys('haroon.khan@canctb.ca')

input()
browser_chrome.quit()
# browser_edge.quit()


# By.XPATH
# By.ID
# By.CLASS-NAME
# By.TAG_NAME
# By.NAME
# By.CSS_SELECTOR


# //*[@id="user_email"]
