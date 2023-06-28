from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chromeOptions)
css = By.CSS_SELECTOR
xpath = By.XPATH
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
encrypt = json.load(open("../PYTHON/PRIVATE/encrypt.json", "r"))
find(css, "input[id='session_key']").send_keys(encrypt["username"])
find(css, "input[id='session_password']").send_keys(encrypt["password"])
find(css, "button[data-id*='sign-in-form__submit-btn']").click()
# ! USE BELOW LINE FOR RECOMMENDED JOBS ONLY _________________________________
# driver.get("https://www.linkedin.com/jobs/collections/recommended/")

#!SELECTING QUALTIY ROLES/ 165K+ ROLES ONLY ___________________________________
wait(driver, 10).until(located((css, "[title*='Jobs']")))
find(css, "[title*='Jobs']").click()
wait(driver, 25).until(located((css, "[id*='jobs-search-box-keyword']")))
find(css, "[id*='jobs-search-box-keyword']").send_keys("QUALITY\n")
# wait(driver, 25).until(located((css, "[aria-label*='Easy Apply filter.']")))
# find(css, "[aria-label*='Easy Apply filter.']").click()  # EASY APPLY FILTER
time.sleep(2)
# find(css, "button[aria-label*='Salary filter.']").click()
# find(css, "label[for*='V2-7']").click()
time.sleep(2)
# [
#     i
#     for i in finds(css, "button[data-control-name*='filter_show_results']")
#     if "result" in i.text
# ][0].click()
# ! ________________________________________________________________


def select(elem, selection):
    try:
        elem.find_element(
            css, f"label[data-test-text-selectable-option__label={selection}]"
        ).click()
        return
    except:...
    try:
        elem.find_element(css, "select[id*='text-entity']").click()
        elem.find_element(css, "input[type*='text']").send_keys(selection)
        time.sleep(0.5)
        elem.find_element(css, "input[type*='text']").send_keys(Keys.TAB)
        return
    except:...
    try:
        elem.find_element(css, f"option[value*={selection}]").click()
        return
    except: ...


yes_words = [
    "commut",
    "do you have experience",
    "eligible to work",
    "authorized to work",
    "sponsorship",
    "vaccinated",
    "w2",
]
def fill_self_identification(data):
    options = find(
                    css, "div[class*='jobs-easy-apply-content']"
                ).find_elements(css, "select")
    for x in options:
        msg = x.text.lower()
        if "veteran" in msg:
            x.find_element(css, "option[value*='Select an option']").click()
            x.find_element(css, "option[value*='I am not']").click()
        elif "race" in msg:
            x.find_element(css, "option[value*='Select an option']").click()
            x.find_element(css, "option[value*='Asian']").click()
        elif "male" in msg:
            x.find_element(css, "option[value*='Select an option']").click()
            x.find_element(css, "option[value*='Male']").click()
        elif "disability" in msg:
            x.find_element(css, "option[value*='Select an option']").click()
            x.find_element(css, "option[value*='No']").click()
    if finds(css, "button[aria-label*='Continue to next step']"):
        data.append(find(css, "div[class='jobs-easy-apply-content']").text)
        find(css, "[aria-label*='Continue to next step']").click()

def easy_apply():
    try:
        data = []
        time.sleep(1)
        finds(css, "div[class*='jobs-apply-button--']")[0].click()
        while True:
            if finds(css, 'div[aria-invalid="true"]'):
                invalid_elms = finds(css, 'div[aria-invalid="true"]')
                for elem in invalid_elms:
                    try:
                        phrase = elem.text.lower()
                        if "city" in phrase:
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Chandler, Arizona, United States"
                            )
                            time.sleep(0.5)
                            elem.find_element(css, "input[type*='text']").send_keys(
                                Keys.TAB
                            )
                            time.sleep(0.5)
                        elif "how many year" in phrase:
                            elem.find_element(css, "input[type*='text']").send_keys(7)
                        elif (
                            "salary" in phrase
                            or "pay" in phrase
                            or "compensation" in phrase
                        ):
                            elem.find_element(css, "input[type*='text']").send_keys(
                                190000
                            )
                        elif "name\n" in phrase:
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Anvesh Jarabani"
                            )
                        elif any(i in phrase for i in yes_words):
                            select(elem, "Yes")
                        elif "c2c" in phrase:
                            select(elem, "No")
                        elif "how did you hear" in phrase:
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "Linkedin"
                            )
                        elif (
                            "you able to begin" in phrase
                            or "when can you start" in phrase
                        ):
                            elem.find_element(css, "input[type*='text']").send_keys(
                                "2 WEEKS FROM OFFER"
                            )
                        elif "i agree terms" in phrase:
                            elem.find_element(css, "label").click()
                        elif ("Self-Identification"
                        in find(css, "div[class*='jobs-easy-apply-content']").text):
                            fill_self_identification(data)
                    except:
                        pass
            elif (
                "Self-Identification"
                in find(css, "div[class*='jobs-easy-apply-content']").text
            ):
                fill_self_identification(data)
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


def pop_apply():
    try:
        resume_path = encrypt["resume_path"]
        keys = list(encrypt.keys())
        finds(css, "div[class*='jobs-apply-button--']")[0].click()
        time.sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        page_list = finds(xpath, ".//*")

        for i in len([i for i in page_list if "apply" in i.text.lower()]):
            print(i.tag_name)

        inputs = [i for i in page_list if i.text.lower() in keys]
        for el in inputs:
            parent = el.find_element(xpath, "..")
            parent.find_elements(css, "input").send_keys(encrypt[el.text.lower()])

        if finds(css, "button[id*='linkedin']"):
            finds(css, "button[id*='linkedin']")[0].click()
        page_list = finds()
        if finds(css, "input[placeholder*='First Name']"):
            finds(css, "input[placeholder*='First Name']")[0].send_keys(
                encrypt["first name"]
            )
        if finds(css, "input[placeholder*='Last Name']"):
            finds(css, "input[placeholder*='Last Name']")[0].send_keys(
                encrypt["last name"]
            )

        find(css, "input[id*='resume']").send_keys(resume_path)
        find(css, "input[name*='name']").send_keys(encrypt["name"])
        find(css, "input[name*='email']").send_keys(encrypt["email"])
        find(css, "input[name*='Phone']").send_keys(encrypt["phone"])
        find(css, "input[name*='company']").send_keys(encrypt["Company"])
        find(css, "input[name*='Linkedin']").send_keys(encrypt["Linkedin url"])
        find(css, "input[name*='GitHub']").send_keys(encrypt["github url"])
        find(css, "div:contains('salary')").find(css, "input").send_keys(
            encrypt["salary"]
        )
        for i in yes_words:
            if finds(css, f"div:contains('{i}')"):
                select(find(css, f"div:contains('{i}')"), "Yes")
    except:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return


page = 1
while page <= 40:
    time.sleep(2)
    with open("./job_data_quality.json", "r", encoding="utf-8") as f:
        cur_dict = json.load(f)
    time.sleep(2)
    for r in range(24):
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView()",
                finds(css, "li[class*='jobs-search-results__list-item']")[r],
            )
            finds(css, "li[class*='jobs-search-results__list-item']")[r].find_element(
                css, "a"
            ).click()
            time.sleep(1)
            if finds(css, "div[class*='jobs-company__box']"):
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
            print(
                [
                    cur_dict["Company Detail"][-1].split("\n")[1],
                    [i for i in cur_dict["Salary Detail"][-1].split("\n") if "$" in i],
                ]
            )

            # if finds(css, "div[class*='jobs-apply-button--']"):
            #     if (
            #         finds(css, "div[class*='jobs-apply-button--']")[0].text
            #         == "Easy Apply"
            #     ):
            #         cur_dict["Form Data"].append(easy_apply())
                # else:
                    # cur_dict["Form Data"].append(pop_apply())
            cur_dict["Form Data"] = [i for i in cur_dict["Form Data"] if i != []]
            for i in list(cur_dict.keys())[:-1]:
                cur_dict[i] = list(set(cur_dict[i]))
            with open("./job_data.json", "w") as f:
                json.dump(cur_dict, f)
        except Exception as e:
            print(e)
            traceback.print_exc()
    page += 1
    time.sleep(2)
    find(css, f"li[data-test-pagination-page-btn='{page}']").click()
