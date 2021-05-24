from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#Чтобы снять/поставить галочку в элементе типа checkbox или выбрать опцию из группы radiobuttons, надо указать WebDriver метод поиска элемента и выполнить для найденного элемента метод click():
#    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
#    option1.click()

#radiobuttons В этом случае можно также отметить нужный checkbox с помощью WebDriver, выполнив метод click() на элементе label.
#    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
#    option2.click()

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
#    assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None

#    x_element = browser.find_element_by_css_selector("[id='input_value']")
#    x = x_element.text
#    y = calc(x)

#    input1 = browser.find_element_by_css_selector("[id='answer']")
#    input1.send_keys(str(y))

    button = browser.find_element_by_css_selector(".btn")
    button_disabled = button.get_attribute("disabled")
    print("buttons disabled: ", button_disabled)		#кнопка пока активна

    time.sleep(10) #ждем 10 секунд

    button_disabled = button.get_attribute("disabled")
    print("buttons disabled: ", button_disabled)		#кнопка отключена

#    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
