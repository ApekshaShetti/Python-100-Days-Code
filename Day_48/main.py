from selenium import webdriver

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
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