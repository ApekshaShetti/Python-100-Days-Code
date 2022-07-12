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
login_button = driver.find_elements(By.XPATH,"//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button")
login_button.click()

sleep(2)
g_login = driver.find_elements(By.XPATH,'//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
g_login.click()

#Switch to google login window
sleep(2)
base_window = driver.window_handles[0]
g_login_window = driver.window_handles[1]
driver.switch_to.window(g_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_elements(By.XPATH,'//*[@id="email"]')
password = driver.find_elements(By.XPATH,'//*[@id="pass"]')
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_elements(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_elements(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_elements(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_elements(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_elements(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()