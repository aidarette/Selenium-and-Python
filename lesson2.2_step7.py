from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
    
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys ("Aidar")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys ("Halimov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys ("Aidar@yandex.ru")
	
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
	
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
