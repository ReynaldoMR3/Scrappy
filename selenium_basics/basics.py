from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://duckduckgo.com")

search_bar = driver.find_element_by_id("search_form_input_homepage")
search_bar.send_keys("my user agent")

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()

search_bar.send_keys(Keys.ENTER)
