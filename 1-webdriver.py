from selenium import webdriver
import time

# Create the webdriver instance
# run test locally against chrome
driver = webdriver.Chrome("chromedriver")


# run test in CrossBrowserTesting:
# for more info on capabilities, check here:
# https://help.crossbrowsertesting.com/selenium-testing/getting-started/crossbrowsertesting-automation-capabilities/
# driver = webdriver.Remote(
#         command_executor = "https://hub.crossbrowsertesting.com/wd/hub",
#         desired_capabilities = { "browser": "chrome",
#                                  "version": "latest",
#                                  "platform": "windows",
#                                  # "deviceName": "Pixel 3",
#                                  "username": "user@domain.com",
#                                  "password": "password",
#                                  "recordVideo": True})

# navigate
driver.get("https://google.com")

# find the search box
search = driver.find_element_by_name('q')
search.send_keys('dogs in sunglasses')
search.submit()

input('press enter to end session')

driver.quit()


