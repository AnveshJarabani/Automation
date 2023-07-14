from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json, time
from selenium import webdriver
from auto_fills import apply_linkedin

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chromeOptions)
css = By.CSS_SELECTOR
xpath = By.XPATH
find = driver.find_element
finds = driver.find_elements
tag = By.TAG_NAME
located = EC.presence_of_all_elements_located
clkable = EC.element_to_be_clickable
driver.maximize_window()
driver.get("https://www.linkedin.com/")
elms = finds(tag, "button")
if len(elms) == 0:
    time.sleep(1)
    driver.get("https://www.linkedin.com/")
    time.sleep(1)
    [i for i in finds(css, "button") if i.text == "Sign in"][0].click()
time.sleep(2)
encrypt = json.load(open("../PYTHON/PRIVATE/encrypt_sg.json", "r"))


inp = "recommended"  # specific for specific jobs
role = "analyst"
slry_range = 1
apply_linkedin(driver, encrypt, inp, role, slry_range)
# salary range - 1 for Anvesh, 0 for sweeite to ignore range
