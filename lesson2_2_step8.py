import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson2_2_step8.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]").send_keys("aboba")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("aboba")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("aboba")
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(10)
    browser.quit()




