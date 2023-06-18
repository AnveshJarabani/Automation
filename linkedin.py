from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json, time, random
from selenium.webdriver.common.proxy import Proxy, ProxyType as pt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

cur_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chromeOptions)
css = By.CSS_SELECTOR
find = driver.find_element
finds = driver.find_elements
located = EC.presence_of_all_elements_located
clkable = EC.element_to_be_clickable
driver.maximize_window()
driver.get("https://www.linkedin.com/")
elms = finds(By.TAG_NAME, "button")
if len(elms) == 0:
    time.sleep(2)
    driver.get("https://www.linkedin.com/")
time.sleep(2)
find(css, "input[id='session_key']").send_keys(
    json.load(open(os.path.join(cur_dir, "encrypt.json"), "r"))["username"]
)
find(css, "input[id='session_password']").send_keys(
    json.load(open(os.path.join(cur_dir, "encrypt.json"), "r"))["password"]
)
find(css, "button[data-id*='sign-in-form__submit-btn']").click()
driver.get("https://www.linkedin.com/jobs/collections/recommended/")


def select_yes(elem):
    try:
        elem.find_element(
            css, "label[data-test-text-selectable-option__label='Yes']"
        ).click()
    except:
        try:
            elem.find_element(css, "select[id*='text-entity']").click()
            elem.find_element(css, "option[value*='Yes']").click()
        except:
            elem.find_element(css, "input[type*='text']").send_keys("Yes")


def apply_job():
    try:
        data = []
        time.sleep(1)
        finds(css, "div[class*='jobs-apply-button--']")[0].click()
        while True:
            if finds(css, 'div[aria-invalid="true"]'):
                invalid_elms = finds(css, 'div[aria-invalid="true"]')
                for elem in invalid_elms:
                    try:
                        if "City" in elem.text.lower():
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Chandler, Arizona, United States"
                            )
                            time.sleep(0.5)
                            elem.find_element(css, "input[type*='text']").send_keys(
                                Keys.TAB
                            )
                            time.sleep(0.5)
                        elif "years" in elem.text.lower():
                            elem.find_element(css, "input[type*='text']").send_keys(7)
                        elif (
                            "salary" in elem.text.lower()
                            or "pay" in elem.text.lower()
                            or "compensation" in elem.text.lower()
                        ):
                            elem.find_element(css, "input[type*='text']").send_keys(
                                190000
                            )
                        elif "name\n" in elem.text.lower():
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Anvesh Jarabani"
                            )
                        elif "commut" in elem.text.lower():
                            select_yes(elem)
                        elif (
                            "do you have" in elem.text.lower()
                            and "experience" in elem.text.lower()
                        ):
                            select_yes(elem)
                        elif (
                            "eligible to work" in elem.text.lower()
                            or "authorized to work" in elem.text.lower()
                        ):
                            select_yes(elem)
                        elif "sponsorship" in elem.text.lower():
                            select_yes(elem)
                        elif "how did you hear" in elem.text.lower():
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Linkedin"
                            )
                        elif (
                            "you able to begin" in elem.text.lower()
                            or "when can you start" in elem.text.lower()
                        ):
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "2 WEEKS FROM OFFER"
                            )
                        elif "i agree terms" in elem.text.lower():
                            elem.find_element(css, "label").click()
                    except:
                        pass
            elif (
                "Self-Identification"
                in find(css, "div[class*='jobs-easy-apply-content']").text
            ):
                options = find(
                    css, "div[class*='jobs-easy-apply-content']"
                ).find_elements(css, "select")
                for x in options:
                    if "veteran" in x.text.lower():
                        x.find_element(css, "option[value*='Select an option']").click()
                        x.find_element(css, "option[value*='I am not']").click()
                    elif "race" in x.text.lower():
                        x.find_element(css, "option[value*='Select an option']").click()
                        x.find_element(css, "option[value*='Asian']").click()
                    elif "male" in x.text.lower():
                        x.find_element(css, "option[value*='Select an option']").click()
                        x.find_element(css, "option[value*='Male']").click()
                    elif "disability" in x.text.lower():
                        x.find_element(css, "option[value*='Select an option']").click()
                        x.find_element(css, "option[value*='No']").click()
                if finds(css, "button[aria-label*='Continue to next step']"):
                    data.append(find(css, "div[class='jobs-easy-apply-content']").text)
                    find(css, "[aria-label*='Continue to next step']").click()
            elif finds(css, "button[aria-label*='Continue to next step']"):
                data.append(find(css, "div[class='jobs-easy-apply-content']").text)
                find(css, "[aria-label*='Continue to next step']").click()
            elif finds(css, "button[aria-label*='Review your application']"):
                data.append(find(css, "div[class='jobs-easy-apply-content']").text)
                find(css, "button[aria-label*='Review your application']").click()
            elif finds(css, "button[aria-label*='Submit application']"):
                data.append(find(css, "div[class='jobs-easy-apply-content']").text)
                if finds(css, "label[for*='follow-company']"):
                    find(css, "label[for*='follow-company']").click()
                find(css, "button[aria-label*='Submit application']").click()
                break
        while True:
            try:
                find(css, "button[aria-label*='Dismiss']").click()
                break
            except:
                pass
        return list(set(data[1:]))
    except:
        pass


page = 1
while page <= 40:
    time.sleep(2)
    with open(os.path.join(cur_dir, "job_data.json"), "r", encoding="utf-8") as f:
        cur_dict = json.load(f)
    time.sleep(2)
    for r in range(23):
        driver.execute_script(
            "arguments[0].scrollIntoView()",
            finds(css, "li[class*='jobs-search-results__list-item']")[r],
        )
        finds(css, "li[class*='jobs-search-results__list-item']")[r].find_element(
            css, "a"
        ).click()
        time.sleep(1)
        if finds(css, "div[class*='jobs-company__box']"):
            print(find(css, "div[class*='jobs-company__box']").text.split("\n")[1])
            cur_dict["Company Detail"].append(
                find(css, "div[class*='jobs-company__box']").text
            )
        else:
            print("No Company Detail Found")
            cur_dict["Company Detail"].append("No Company Detail Found")
        cur_dict["Details"].append(
            find(css, "div[class*='jobs-unified-top-card__content--two-pane']").text
        )
        cur_dict["Desc"].append(find(css, "div[class*='jobs-description']").text)
        cur_dict["Salary Detail"].append(find(css, "div[id*='SALARY']").text)
        if finds(css, "div[class*='jobs-apply-button--']"):
            if finds(css, "div[class*='jobs-apply-button--']")[0].text == "Easy Apply":
                cur_dict["Form Data"].append(apply_job())
    cur_dict["Form Data"] = [i for i in cur_dict["Form Data"] if i != []]
    with open(os.path.join(cur_dir, "job_data.json"), "w") as f:
        json.dump(cur_dict, f)
    page += 1
    time.sleep(2)
    find(css, "li[data-test-pagination-page-btn='{}']".format(page)).click()
