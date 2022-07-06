from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_elements(By.CLASS_NAME,"fName")
first_name.send_keys("Apeksha")
last_name = driver.find_elements(By.CLASS_NAME,"lName")
last_name.send_keys("Shetti")
email = driver.find_elements(By.CLASS_NAME,"email")
email.send_keys("shetti1012@gmail.com")

submit = driver.find_elements(By.CSS_SELECTOR,"form button")
submit.click()


# article_count = driver.find_elements(By.CSS_SELECTOR,"#articlecount a")
# article_count.click()

# all_portals = driver.find_elements(By.LINK_TEXT, "All portals")
# all_portals.click()

# search = driver.find_elements(By.CLASS_NAME,"search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


