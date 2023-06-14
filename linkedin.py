from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json,time,random
from selenium.webdriver.common.proxy import Proxy,ProxyType as pt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user='test_1124'
passwrd='xsdf_~#@sdf'
# Fetch a random proxy from ProxyMesh
proxy_mesh_url = 'http://proxy.proxy-mesh.com:31280'  # Replace with the ProxyMesh URL
proxy_mesh_proxy_list = ['proxy1.proxy-mesh.com:31280', 'proxy2.proxy-mesh.com:31280']  # Add more proxies if available
random_proxy = random.choice(proxy_mesh_proxy_list)
# Configure the proxy server
proxy = Proxy()
proxy.proxy_type = pt.MANUAL
proxy.http_proxy = f'{user}:{passwrd}@{random_proxy}'
proxy.ssl_proxy = f'{user}:{passwrd}@{random_proxy}'
# Create a desired capabilities object and set the proxy
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
proxy.add_to_capabilities(capabilities)
chromeOptions=webdriver.ChromeOptions()
driver=webdriver.Chrome('sldr.exe',options=chromeOptions,desired_capabilities=capabilities)
# driver.implicitly_wait(5)
css=By.CSS_SELECTOR
find=driver.find_element
finds=driver.find_elements
located=EC.presence_of_all_elements_located
clkable=EC.element_to_be_clickable
driver.maximize_window()
driver.get('https://www.linkedin.com/')
elms=finds(By.TAG_NAME,'button')
if len(elms)==0:
    time.sleep(2)
    driver.get('https://www.linkedin.com/')
time.sleep(2)
# path = r'C:\Users\ajarabani\Downloads\job automation\{}'  
path = r"C:\Users\anves\Downloads\job automation\{}"
find(css,"input[id='session_key']").send_keys(json.load(open(path.format('encrypt.json'),'r'))['username'])
find(css,"input[id='session_password']").send_keys(json.load(open(path.format('encrypt.json'),'r'))['password'])
find(css,"button[data-id*='sign-in-form__submit-btn']").click()
wait(driver,100).until(located((css,"[title*='Jobs']"))) 
find(css,"[title*='Jobs']").click()
wait(driver,25).until(located((css,"[id*='jobs-search-box-keyword']")))
find(css,"[id*='jobs-search-box-keyword']").send_keys('data engineer\n')
wait(driver,25).until(located((css,"[aria-label*='Easy Apply filter.']")))
find(css,"button[aria-label*='Easy Apply filter.']").click()
find(css,"button[aria-label*='Salary filter.']").click()
find(css,"label[for*='V2-7']").click()
time.sleep(0.5)
[i for i in finds(css,"button[data-control-name*='filter_show_results']") if 'result' in i.text][0].click()
def select_yes(elem):
    try:
        elem.find_element(css,
        "label[data-test-text-selectable-option__label='Yes']").click()
    except:
        try:
            elem.find_element(
            css,"select[id*='text-entity']").click()
            elem.find_element(css,"option[value*='Yes']").click()
        except:
            elem.find_element(css,"input[type*='text']").send_keys('Yes')
def apply_job():
    try:
        data=[]
        time.sleep(1)
        finds(css, "div[class*='jobs-apply-button--']")[0].click()
        # if len(apply_buttons)!=0:
        #     apply_buttons[0].click()
        # else:
        #     return
        while True:
            if finds(css, 'div[aria-invalid="true"]'):
                invalid_elms = finds(
                css, 'div[aria-invalid="true"]')
                for elem in invalid_elms:
                    try:
                        if 'City' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys('Chandler, Arizona, United States')
                            time.sleep(.5)
                            elem.find_element(css, "input[type*='text']").send_keys(Keys.TAB)
                            time.sleep(.5)
                        elif 'years' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys(5)
                        elif 'salary' in elem.text or 'pay' in elem.text or 'compensation' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys(190000)
                        elif 'Name\n' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys('Anvesh Jarabani')
                        elif 'commut' in elem.text:
                            select_yes(elem)
                        elif 'Do you have' in elem.text and 'experience' in elem.text:
                            select_yes(elem)
                        elif 'eligible to work' in elem.text or 'authorized to work' in elem.text:
                            select_yes(elem)
                        elif 'sponsorship' in elem.text or 'Sponsorship' in elem.text:
                            select_yes(elem)
                        elif 'How did you hear' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys('Linkedin')  
                        elif 'you able to begin' in elem.text or 'When can you start' in elem.text:
                            elem.find_element(
                            css, "input[type*='text']").send_keys('2 WEEKS FROM OFFER')  
                        elif 'I Agree Terms' in elem.text:
                            elem.find_element(css,'label').click()
                    except:
                        pass      
            elif 'Self-Identification' in find(css,"div[class*='jobs-easy-apply-content']").text:
                options=find(css,"div[class*='jobs-easy-apply-content']").find_elements(css,"select")
                for x in options:
                    if 'veteran' in x.text:
                        x.find_element(css,"option[value*='Select an option']").click()
                        x.find_element(css,"option[value*='I am not']").click()
                    elif 'Race' in x.text:
                        x.find_element(css,"option[value*='Select an option']").click()
                        x.find_element(css,"option[value*='Asian']").click()
                    elif 'Male' in x.text:
                        x.find_element(css,"option[value*='Select an option']").click()
                        x.find_element(css,"option[value*='Male']").click()
                    elif 'Disability' in x.text:
                        x.find_element(css,"option[value*='Select an option']").click()
                        x.find_element(css,"option[value*='No']").click()
                if finds(css, "button[aria-label*='Continue to next step']"):
                    data.append(find(css, "div[class='jobs-easy-apply-content']").text)
                    find(css, "[aria-label*='Continue to next step']").click()
            elif finds(css, "button[aria-label*='Continue to next step']"):
                data.append(
                    find(css, "div[class='jobs-easy-apply-content']").text)
                find(css, "[aria-label*='Continue to next step']").click()
            elif finds(css,"button[aria-label*='Review your application']"):
                data.append(
                    find(css, "div[class='jobs-easy-apply-content']").text)
                find(css,"button[aria-label*='Review your application']").click()
            elif finds(css,"button[aria-label*='Submit application']"): 
                data.append(
                    find(css, "div[class='jobs-easy-apply-content']").text)
                if finds(css,"label[for*='follow-company']"):
                    find(css,"label[for*='follow-company']").click()
                find(css,"button[aria-label*='Submit application']").click()
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
page=1
while page<=40:
    time.sleep(2)
    jobs=finds(css,"li[class*='jobs-search-results__list-item']")
    driver.execute_script("arguments[0].scrollIntoView()",jobs[10])
    driver.execute_script("arguments[0].scrollIntoView()",jobs[-1])
    with open(path.format('data_eng_job_source_data.json'),'r', encoding='utf-8') as f:
        dict=json.load(f)
    time.sleep(2)
    for r in range(len(jobs)):
        driver.execute_script("arguments[0].scrollIntoView()", finds(
            css, "li[class*='jobs-search-results__list-item']")[r])
        finds(css, "li[class*='jobs-search-results__list-item']")[r].find_element(css,'a').click()
        time.sleep(1)
        if finds(css, "div[class*='jobs-company__box']"):
            print(find(css, "div[class*='jobs-company__box']").text.split('\n')[1])
            dict['Company Detail'].append(
            find(css, "div[class*='jobs-company__box']").text)
        else:
            print('No Company Detail Found')
            dict['Company Detail'].append('No Company Detail Found')
        dict['Details'].append(
            find(css, "div[class*='jobs-unified-top-card__content--two-pane']").text)
        dict['Desc'].append(
            find(css, "div[class*='jobs-description']").text)
        dict['Salary Detail'].append(find(css, "div[id*='SALARY']").text)
        if finds(css, "div[class*='jobs-apply-button--']"):
            dict['Form Data'].append(apply_job())
    dict['Form Data'] = [i for i in dict['Form Data'] if i != []]
    with open(path.format('data_eng_job_source_data.json'),'w') as f:
        json.dump(dict,f)
    page+=1
    time.sleep(2)
    find(css,"li[data-test-pagination-page-btn='{}']".format(page)).click()
