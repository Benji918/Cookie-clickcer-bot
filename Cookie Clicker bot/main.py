from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

python_url = 'http://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(url=python_url)
five_mins = time.time() + 60 * 5
five_secs = time.time() + 5
iterations = 1

cookie = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')
# list of upgrade id's from the most expensive to lest expensive
upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine",
               "buyFactory", "buyGrandma", "buyCursor"]

while time.time() <= five_mins:
    for _ in range(iterations):
        cookie.click()
        cookie.click()
        cookie.click()
    if time.time() > five_secs:
        for upgrade_id in upgrades_id:
            try:
                driver.find_element(by=By.ID, value=upgrade_id).click()
                driver.find_element(by=By.ID, value=upgrade_id).click()
            except:
                continue

    iterations += 100

# cookies per second
cps = driver.find_element(By.ID, "cps").text
print(cps)

driver.quit()
