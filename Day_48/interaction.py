from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_elements(By.CSS_SELECTOR,"#articlecount a")
article_count.click()

all_portals = driver.find_elements(By.LINK_TEXT, "All portals")
all_portals.click()

search = driver.find_elements(By.CLASS_NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
