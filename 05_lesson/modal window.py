from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1: Открытие страницы
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    # 2 Очень сильно жду появления модального окна T____T
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "modal"))
    )

    # 3: Наконец-то жму на кнопку Close =__=
    close_button = (driver.find_element
                    (By.XPATH, "//p[contains(text(), 'Close')]"))
    close_button.click()
finally:
    # Закрыть все
    driver.quit()
