from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1: Открытие страницы
driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    # 2 Ожидание модального окна
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "modal")))

    # 3: жму на кнопку Close
    close_button = (driver.find_element
                    (By.XPATH, "//p[contains(text(), 'Close')]"))
    close_button.click()
finally:
    # Закрыть все
    driver.quit()
