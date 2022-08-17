from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button").click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x.text
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(10)
    browser.quit()