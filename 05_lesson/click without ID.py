from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открытие страницы
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

try:
    # Ожидать появления кнопки на странице
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "button"))
    )

    # Клик по синей кнопке
    blue_button = driver.find_element(By.CSS_SELECTOR, '#button')
    blue_button.click()

except Exception as e:
    print(f"Там нет такой кнопки, алё!: {e}")
finally:
    # Закрытие браузера
    driver.quit()
