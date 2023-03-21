from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service_obj = Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# stats = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# #stats.click()
#
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Al portals")
# #all_portals.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
