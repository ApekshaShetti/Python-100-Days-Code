from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

ACCOUNT_EMAIL = "xyz"
ACCOUNT_PASSWORD = "Shetti"
PHONE = "7894561233"

chrome_driver_path = "D:\Python-100-Days-Code\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=python%20developer&location=United%20Kingdom")

sign_in_button = driver.find_elements(By.LINK_TEXT,"Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_elements(By.ID,"username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_elements(By.ID,"password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


#Locate the apply button
time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    #Locate the apply button
    try:
        apply_button = driver.find_elements(By.CSS_SELECTOR,".jobs-s-apply button")
        apply_button.click()

        #If application requires phone number and the field is empty, then fill in the number.
        time.sleep(5)
        phone = driver.find_elements(By.CLASS_NAME,"fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        #Submit the application
        submit_button = driver.find_elements(By.CSS_SELECTOR,"footer button")

             #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

         #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_elements(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue


time.sleep(5)
driver.quit()