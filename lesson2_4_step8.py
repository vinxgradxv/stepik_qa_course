import math
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100'))
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    time.sleep(5)
    browser.quit()