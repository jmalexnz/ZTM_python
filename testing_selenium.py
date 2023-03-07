# Selenium lets us use a browser without a human involved
# click around the mouse etc
# useful for testing websites quickly 
# install selenium and webdriver
# you can add in waits to make sure pauses happen between
# actions.
# https://selenium-python.readthedocs.io/index.html


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# to stop the browser closing as soon as code is complete
options = Options()
options.add_experimental_option('detach', True)

chrome_browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# chrome_browser.maximize_window()

# andrei uses a test case from seleniumeasy
# but i don't think that exists anymore
# so using another practice form ...
chrome_browser.get('https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm#')
# selenium looks at the page and looks for elements

# Get the title to check the browser has opened properly
# the code will error out if the assert is false
assert('Selenium - Automation Practice Form' in chrome_browser.title)
# chrome_browser.page_source looks in all the HTML for the page

# selectors cheat sheet
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
# right click on elements and click Inspect to look at the html 
# and find way to select.
# select previous page button
# get the class name by looking in html
pre_button = chrome_browser.find_element(By.CLASS_NAME, 'pre-btn')
submit_button = chrome_browser.find_element(By.NAME, 'submit')
# we can do different things with the elements once we have 
# them 
# print(submit_button.get_attribute('innerHTML'))
# pre_button.click()
# we can use name, id, heaps of options to select by

# lets enter some text in the boxes
first_name = chrome_browser.find_element(By.NAME, 'firstname')
first_name.clear()
first_name.send_keys('Jane')
# assert is useful to check stuff is working

# can also select by CSS to select everything that has a specific CSS
# e.g., button style.

chrome_browser.quit()