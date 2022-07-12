from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 

ACCOUNT_EMAIL = "suzieboo1012@gmail.com"
ACCOUNT_PASSWORD = "Suzieboo@12"

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_elements(By.XPATH,"")