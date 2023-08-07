from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import strings as st

driver = webdriver.Chrome()
driver.maximize_window()

print(print(st.Prints.browser_opened))

# Open e-commere website
driver.get(st.Url.website)
print(st.Prints.website_opened)

# Wait for the post to be uploaded
time.sleep(st.Numbers.five)

driver.close()
