from selenium import webdriver

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

driver.close()
# closes only the active tab or the current tab of chrome
driver.quit()
# closes the browser which is chrome