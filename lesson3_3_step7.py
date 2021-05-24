#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#Посчитать математическую функцию от x (сама функция остаётся неизменной).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию из группы radiobuttons, надо указать WebDriver метод поиска элемента и выполнить для найденного элемента метод click():
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

#radiobuttons В этом случае можно также отметить нужный checkbox с помощью WebDriver, выполнив метод click() на элементе label.
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

#  [id='treasure']
    option3 = browser.find_element_by_id("treasure")
    x = option3.get_attribute("valuex")  
    print(x)
    y = calc(x)
    print(y)

    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(str(y))

    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
