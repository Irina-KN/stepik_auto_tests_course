import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/find_link_text"
# browser = webdriver.Chrome()
field_name = 'input'
field_last_name = 'last_name'
field_city = 'form-control.city'
field_country = 'country'
button_submit = 'button.btn'


def form(browser):
    input1 = browser.find_element(By.TAG_NAME, field_name)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, field_last_name)
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, field_city)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, field_country)
    input4.send_keys("Russia")


def click_submit(browser):
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


def href():
    try:
        # browser.get(link)
        href_element = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        get_href_element = browser.find_element(By.LINK_TEXT, href_element)
        get_href_element.click()
        form()
    finally:
        browser.quit()
