
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2499337.m570.l1313&_nkw=iphone+13+pro+&_sacat=0")
# price = driver.find_element(by=By.CLASS_NAME, value="ITALIC")
# print(price.text)
#
# search = driver.find_element(by=By.XPATH, value='//*[@id="srp-river-results"]/ul/li[5]/div/div[2]/div[3]/div[2]/span[1]')
# print(search.text)



#exercise

driver.get("https://www.python.org/")

event_date = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_date)):
    events[n] = {
        "time":event_time[n].text,
        "date":event_date[n].text
    }

print(events)
