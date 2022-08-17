from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = int(x.text)

    y = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = int(y.text)

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(str(x + y))


    browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(10)
    browser.quit()
