from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть страницу
driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
time.sleep(2)  # Дать странице загрузиться

# Пять раз кликаем на кнопку Add Element
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()
    time.sleep(2)

# Собрать список кнопок Delete
delete_buttons = (driver.find_elements
                  (By.CLASS_NAME, "added-manually"))

# Выводим на экран размер списка
print(f"Кол-во кнопок Delete на странице: {len(delete_buttons)}")

# Закрыть браузер
driver.quit()
