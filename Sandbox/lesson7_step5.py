import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[value="robots"]')
    radiobutton.click()
    button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()