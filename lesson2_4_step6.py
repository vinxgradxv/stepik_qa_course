import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/cats.html"
try:
    browser = webdriver.Chrome()
    browser.find_element(By.ID, "button")
finally:
    time.sleep(10)
    browser.quit()