from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium import webdriver
chromeOptions=webdriver.ChromeOptions()
driver=webdriver.Chrome('sldr.exe')
driver.maximize_window()
driver.get('https://www.linkedin.com/')
driver.implicitly_wait(30)
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
try:
    WebDriverWait(driver,2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"[class*='jobs-apply-button artdeco-button artdeco-button--3']")))
except:
    driver.find_element(By.CSS_SELECTOR,"[class*='jobs-apply-button artdeco-button artdeco-button--3']").click()
def easyapply():
    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label*='Continue to next step']")))
    driver.find_element(By.CSS_SELECTOR,"[aria-label*='Continue to next step']").click()
    driver.find_element(By.CSS_SELECTOR,"[class*='button__text]").click()
    driver.find_element(By.CSS_SELECTOR,"[type*='text]").send_keys(5)
    driver.find_element(By.CSS_SELECTOR,"[type*='text]").send_keys(5)
    driver.find_element(By.CSS_SELECTOR,"[class*='button__text]").click()
    driver.find_element(By.CSS_SELECTOR,"[id*='follow-company]").click()
    driver.find_element(By.CSS_SELECTOR,"[class*='button__text]").click()
if len(driver.window_handles)==1:
    easyapply()
elif driver.current_url.find('myworkdayjobs')>0:
    True
else:
    exit()
driver.find_element(By.LINK_TEXT,"Apply").click()



