from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Шаг 1: Открытие страницы
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

try:
    # Шаг 2: Поиск поля ввода текста
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input")))

    # Шаг 3: Ввожу текстом "1000"
    input_field.send_keys("1000")

    # Шаг 4: Почистить с clear
    input_field.clear()

    # Шаг 5: Вводимс текстом "999" в пропылесосенное поле
    input_field.send_keys("999")
finally:
    # Закрываемс браузер
    driver.quit()
