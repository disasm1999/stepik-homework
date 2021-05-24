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


    browser.execute_script("document.title='Script executing';")    
    browser.execute_script("alert('Robots at work');")

#  Прямо на этой странице жми ctrl+shift+j (или F12), открывай консоль и пиши
#    browser.execute_script("document.title='Script executing';alert('Robots at work');")

#    button = browser.find_element_by_css_selector(".btn")
#    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
