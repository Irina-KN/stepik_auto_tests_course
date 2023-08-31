from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
old_link = "http://suninjuly.github.io/registration1.html"   # успешно проходит
new_link = "http://suninjuly.github.io/registration2.html"   # падает с ошибкой NoSuchElementException
first_name = '.first_block .first'
last_name = '.first_block .second'
email = '.first_block .third'

try:
    browser.get(new_link)

    # Ваш код, который заполняет обязательные поля
    first_name_field = browser.find_element(By.CSS_SELECTOR, first_name)
    first_name_field.send_keys("Ivan")
    last_name_field = browser.find_element(By.CSS_SELECTOR, last_name)
    last_name_field.send_keys("Petrov")
    email_field = browser.find_element(By.CSS_SELECTOR, email)
    email_field.send_keys("last_of_us@firefly.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться и ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()