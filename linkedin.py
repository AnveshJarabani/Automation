from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium import webdriver
chromeOptions=webdriver.ChromeOptions()
driver=webdriver.Chrome('sldr.exe',options=chromeOptions)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.linkedin.com/')
elms=driver.find_elements(By.TAG_NAME,'button')
if len(elms)==0:
    driver.refresh()
driver.find_element(By.CSS_SELECTOR,"[id='session_key']").send_keys("anveshjarabani@gmail.com")
driver.find_element(By.CSS_SELECTOR,"[id='session_password']").send_keys(json.load(open('encrypt.json','r'))['password'])
driver.find_element(By.CSS_SELECTOR,"[data-id*='sign-in-form__submit-btn']").click()
WebDriverWait(driver,25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[title*='Jobs']")))
driver.find_element(By.CSS_SELECTOR,"[title*='Jobs']").click()
WebDriverWait(driver,25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[id*='jobs-search-box-keyword']")))
driver.find_element(By.CSS_SELECTOR,"[id*='jobs-search-box-keyword']").send_keys('data engineer\n')
WebDriverWait(driver,25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[aria-label*='Easy Apply filter.']")))
driver.find_element(By.CSS_SELECTOR,"[aria-label*='Easy Apply filter.']").click()
# WebDriverWait(driver,25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class*='jobs-apply-button']")))
def apply_job(i):
    apply_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label*='Easy Apply to']")
    if len(apply_buttons)!=0:
        apply_buttons[0].click()
    else:
        return
    flg = True
    while flg:
        try:
            driver.find_element(
                By.CSS_SELECTOR, "[aria-label*='Continue to next step']").click()
            invalid_elms = driver.find_elements(
                By.CSS_SELECTOR, 'div[aria-invalid="true"]')
            for elem in invalid_elms:
                try:
                    elem.find_element(
                        By.CSS_SELECTOR, "input[type*='text']").send_keys(5)
                except:
                    pass
                # try:


        except:
            flg = False
    try:
        driver.find_element(By.CSS_SELECTOR,
                        "[aria-label*='Review your application']").click()
    except:
        pass
    try:
        driver.find_element(By.CSS_SELECTOR,
                    "[aria-label*='Submit application']").click()
    except:
        pass
    driver.find_element(By.CSS_SELECTOR, "button[aria-label*='Dismiss']").click()

jobs = driver.find_elements(
    By.CSS_SELECTOR, "div[class*='job-card-container--clickable']")

for r,i in enumerate(jobs):
    apply_job(i)
    jobs = driver.find_elements(
        By.CSS_SELECTOR, "div[class*='job-card-container--clickable']")
    element = jobs[r+1]
    element.click()



