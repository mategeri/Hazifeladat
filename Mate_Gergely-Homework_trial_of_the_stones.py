import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=r'C:\chromedriver\chromedriver.exe')
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=service, options=options)

URL = "https://techstepacademy.com/trial-of-the-stones"
browser.get(URL)
browser.maximize_window()

riddle_of_the_stone_answer_input = browser.find_element(By.ID, 'r1Input')
riddle_of_the_stone_answer_input.send_keys('Rock')

time.sleep(2)

riddle_of_the_stone_answer_btn = browser.find_element(By.ID, 'r1Btn')
riddle_of_the_stone_answer_btn.click()


riddle_of_secrets_answer_input = browser.find_element(By.ID, 'r2Input')
riddle_of_secrets_answer_input.send_keys('bamboo')

time.sleep(2)

riddle_of_the_stone_answer_btn = browser.find_element(By.ID, 'r2Butn')
riddle_of_the_stone_answer_btn.click()

the_name_of_the_richest_merchant_input = browser.find_element(By.ID, 'r3Input')

Jessica = 3000
Bernard = 2000

def nagyobb_szam(Jessica, Bernard):
    if Jessica > Bernard:
        return 'Jessica'
    else:
        return 'Bernard'

the_name_of_the_richest_merchant_input.send_keys(nagyobb_szam(Jessica, Bernard))

time.sleep(2)

riddle_of_the_stone_answer_btn = browser.find_element(By.ID, 'r3Butn')
riddle_of_the_stone_answer_btn.click()

check_answers_btn = browser.find_element(By.ID, 'checkButn')
check_answers_btn.click()

trial_complete_text = browser.find_element(By.ID, 'trialCompleteBanner')

if trial_complete_text.is_displayed():
    print('<---' "Sikeres volt a küldetés." '--->')
else:
    print('<---' "Sikertelen volt a küldetés" '--->')
