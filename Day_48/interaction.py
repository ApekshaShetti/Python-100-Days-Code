from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)