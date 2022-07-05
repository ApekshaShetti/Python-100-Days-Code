from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

# event_times = driver.find_elements_by_css_selector(".event-widget time")
event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}


for n in range(len(event_times)):
    events[n] ={
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)


# driver.close()
# closes only the active tab or the current tab of chrome
driver.quit()
# closes the browser which is chrome