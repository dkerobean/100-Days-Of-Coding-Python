from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



ACCOUNT_EMAIL = "email"
ACCOUNT_PASSWORD = "password"
PHONE = "phone"


service_obj = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.linkedin.com/")

username = driver.find_element(by=By.ID, value="session_key")
username.send_keys(ACCOUNT_EMAIL)

password = driver.find_element(by=By.ID, value="session_password")
password.send_keys(ACCOUNT_PASSWORD)

sign_in = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()




