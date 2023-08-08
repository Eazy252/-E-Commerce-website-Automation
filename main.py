import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import strings as st

driver = webdriver.Chrome()
driver.maximize_window()

print(print(st.Prints.browser_opened))

# Open e-commere website
driver.get(st.Url.website)
print(st.Prints.website_opened)

# Wait for the post to be uploaded
time.sleep(st.Numbers.five)

# find email text filed and input email address
driver.find_element(By.ID, st.Find_elements_by_id.email_id).send_keys(st.strings.username_standard_user)
time.sleep(st.Numbers.two)

# find password text field and input password
play = driver.find_element(By.ID, st.Find_elements_by_id.password_id)
time.sleep(st.Numbers.two)
play.send_keys(st.strings.password)

# incite the enter key in the keyboard
play.send_keys(Keys.ENTER)

Home = driver.find_element(By.CLASS_NAME, st.find_elements_by_class.app_logo).is_displayed()
# assertThat(driver.find_element(By.CLASS_NAME).get_property(), is )

# driver.findElement(By.tagName("h1")).isDisplayed();
# assertThat(driver.findElement(By.tagName("h1")).getText(), is ("Hello userName"))

time.sleep(st.Numbers.five)
driver.close()
