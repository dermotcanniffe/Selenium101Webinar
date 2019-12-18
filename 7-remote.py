from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import time
from os import getcwd

# Create the webdriver instance
# instead of running against chrome, we're gonna run on CrossBrowserTesting

#user = "johnreese.vt@gmail.com"
#auth = "u0af4e32dc4fb29d"

# driver = webdriver.Remote(
#       desired_capabilities={"browserName": "chrome", "platform": "windows 10"}
#      command_executor="https://{}:{}@hub.crossbrowsertesting.com/wd/hub".format(user,auth) )

# Please visit http://selenium-python.readthedocs.io/ for detailed installation and instructions
# Getting started: http://docs.seleniumhq.org/docs/03_webdriver.jsp
# API details: https://github.com/SeleniumHQ/selenium#selenium

# Requests is the easiest way to make RESTful API calls in Python. You can install it by following the instructions here:
# http://docs.python-requests.org/en/master/user/install/

# Put your username and authey below
# You can find your authkey at crossbrowsertesting.com/account
username = "dermot.canniffe@smartbear.com"
authkey = "u1b26bf49cce3f32"

api_session = requests.Session()
api_session.auth = (username, authkey)

test_result = None

caps = {}

caps['name'] = 'Basic Test Example'
caps['build'] = '1.0'
caps['browserName'] = 'Chrome'
caps['version'] = '78x64'
caps['platform'] = 'Windows 10'
caps['screenResolution'] = '1366x768'
caps['record_video'] = 'true'

# start the remote browser on our server
driver = webdriver.Remote(
    desired_capabilities=caps,
    command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub" % (
        username, authkey)
)


# navigate
driver.get("http://crossbrowsertesting.github.io/login-form.html")

# find the search box
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login = driver.find_element_by_id('submit')

username.send_keys('not-a-user@crossbrowsertesting.com') # tester@crossbrowsertesting.com
password.send_keys('not-the-password') # test123
# Correct Credentials 
# username.send_keys('tester@crossbrowsertesting.com') # 
# password.send_keys('test123') # test123
login.click()

try:
    # selenium needs to wait for the login to finish before checking
    logged_in_message = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "logged-in")))

    header = driver.find_element_by_tag_name('h2')

    # check the angular class is set
    assert header.get_attribute('class') == 'ng-binding'

    # make sure the element isn't hidden
    assert header.is_displayed()

    # verify the text is what we expect
    assert logged_in_message.text == "You are now logged in!"

    print ("PASS: successfully logged in!")
except Exception:
    print ("FAIL: did not log in!")

    screenshot_fpath = getcwd() + '/on-error.png'
    driver.get_screenshot_as_file(screenshot_fpath)

    print('saved screenshot to ' + screenshot_fpath)

driver.quit()
