import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

from selenium.webdriver.support.wait import WebDriverWait


# link = "https://suninjuly.github.io/execute_script.html"
#
#
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element(By.ID, 'input_value')
#     y = calc(int(x_element.text))
#     text_field = browser.find_element(By.ID, "answer")
#     text_field.send_keys(str(y))
#     checkbox = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
#     checkbox.click()
#     browser.execute_script("window.scrollBy(0, 100);")
#     radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
#     radiobutton.click()
#     button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
#     button.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# добавляем к этому пути имя файла

# try:
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'testsite')
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/file_input.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     file_button = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
#     file_button.send_keys(file_path)
#     button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/alert_accept.html")
#
#     button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#     button.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     time.sleep(1)
#     x_element = browser.find_element(By.ID, 'input_value')
#     y = calc(int(x_element.text))
#     text_field = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
#     text_field.send_keys(str(y))
#     button2 = button.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#     button2.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/redirect_accept.html")
#
#     button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#     button.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     x_element = browser.find_element(By.ID, 'input_value')
#     y = calc(int(x_element.text))
#     print(y)
#     text_field = browser.find_element(By.ID, 'answer')
#     text_field.send_keys(str(y))
#     button2 = button.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#     button2.click()
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    x_element = browser.find_element(By.ID, 'input_value')
    y = calc(int(x_element.text))
    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(str(y))
finally:
# успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()