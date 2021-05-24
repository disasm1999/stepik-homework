#http://suninjuly.github.io/selects1.html
#http://suninjuly.github.io/selects2.html

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    option1 = browser.find_element_by_id("num1")
    num1 = option1.text
    print(num1)

    option2 = browser.find_element_by_id("num2")
    num2 = option2.text
    print(num2)

    summa = int(num1)+int(num2)
    print(summa)
    select = Select(browser.find_element_by_tag_name("select"))
#    select.select_by_index(3) # ищем элемент с индексом 3 (нумирация с нуля)
    select.select_by_value(str(summa)) # ищем элемент с текстом "1"

#Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
