#Открыть страницу http://suninjuly.github.io/redirect_accept.html
#Нажать на кнопку
#Переключиться на новую вкладку
#Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn").click()
#    button.click()

#    confirm = browser.switch_to.alert
#    confirm.accept()

#first_window = browser.window_handles[0] 		#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

    new_window = browser.window_handles[1]  #переключаемся на новую вкладку
    print(new_window)
    print(browser.window_handles[0])
    browser.switch_to_window(new_window)

    option1 = browser.find_element_by_id("input_value")
    x = option1.text 
    print(x)

    y = calc(x)
    print(y)
    option2 = browser.find_element_by_id("answer")
    option2.send_keys(str(y))

    button = browser.find_element_by_css_selector(".btn").click()
#    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
