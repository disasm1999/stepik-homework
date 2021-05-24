#Открыть страницу http://suninjuly.github.io/alert_accept.html
#Нажать на кнопку
#Принять confirm
#На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    option1 = browser.find_element_by_id("input_value")
    x = option1.text 
    print(x)

    y = calc(x)
    print(y)
    option2 = browser.find_element_by_id("answer")
    option2.send_keys(str(y))

    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
