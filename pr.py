import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import time
from Confi import CHROME_PROFILE_PATH
import random
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8788")
s = Service(r"C:\Users\Shreeya\Desktop\College\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=opt)
# driver.get('https://web.whatsapp.com/')
# time.sleep(20)


def enter_text(name, text):
    for i in range(len(text)):
        name.send_keys(text[i])
        WebDriverWait(driver,5)
def find_name(index):
    name_xpath = "(//*/span[text()='TODAY']/parent::div/parent::div/following-sibling::div/child::div)[{}]/descendant::span[contains(@class,'i0jNr') and contains(@class,'edeob0r2')]".format(index + 1)
    try:
        name = driver.find_element(By.XPATH,name_xpath)
        return name
    except:
        return find_name(index - 1)


thanks = ['Thankyou for wishing me on my birthday :)', 'Thanks a lot :)', 'Thankyou so much :)', 'Thankyou for the birthday text :)']



# search_box = WebDriverWait(driver, timeout=50).until(lambda d: driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))
# enter_text(search_box, "My small sweet family")
# search_box.send_keys(Keys.ENTER)
# time.sleep(240)

list = driver.find_elements(By.XPATH,'.//*/span[text()="TODAY"]/parent::div/parent::div/following-sibling::div/child::div')
n = len(list)
h = ActionChains(driver)
print(list)
# for index,ind in enumerate(list):
for index in range(n):
    # print('looped')
    int = random.randint(0,3)
    i_x = ('(//*/span[text()="TODAY"]/parent::div/parent::div/following-sibling::div/child::div)[{}]'.format(index + 1))
    print(i_x)
    i = WebDriverWait(driver, timeout=50).until(lambda d: driver.find_element(By.XPATH, i_x))
    # i = driver.find_element(By.XPATH, i_x)
    driver.execute_script('arguments[0].scrollIntoView({block:"center", inline:"center"})', i)
    time.sleep(2)
    # print(i.text)
    # print(index)
    if "@Shreeya" in i.text:
        j = 0
        name = ""
        # time.sleep(5)
        h.move_to_element(i).perform()

        # reply_table = driver.find_element(By.XPATH, ('(//*/span[text()="TODAY"]/parent::div/parent::div/following-sibling::div)[{}]/descendant::span[@data-icon="down-context"]'.format(index+1)))
        reply_table=WebDriverWait(driver, timeout=50).until(lambda d: driver.find_element(By.XPATH, '(//*/span[text()="TODAY"]/parent::div/parent::div/following-sibling::div)[{}]/descendant::span[@data-icon="down-context"]'.format(index+1)))
        print('(//*/span[text()="TODAY"]/parent::div/parent::div/following-sibling::div)[{}]/descendant::span[@data-icon="down-context"]'.format(index+1))
        h.move_to_element(reply_table).click().perform()
        # reply = driver.find_element(By.XPATH, "//*/div[@aria-label='Reply']")
        reply = WebDriverWait(driver, timeout=100).until(lambda d: driver.find_element(By.XPATH, '//*/div[@aria-label="Reply"]'))
        h.move_to_element(reply).click().perform()
        # name = find_name(index)
        Final_message = thanks[int] + " @"
        Message = driver.find_element(By.CLASS_NAME, "p3_M1")
        Message.send_keys(Final_message)
        Message.send_keys(Keys.ENTER)
        Message.send_keys(Keys.ENTER)
        print('message sent')























