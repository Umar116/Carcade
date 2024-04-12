from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

link = "https://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    text1 = browser.find_element(By.ID, "num1")
    number1 = text1.text
    text2 = browser.find_element(By.ID, "num2")
    number2 = text2.text
    list_value = int(number1) + int(number2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(list_value))
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()