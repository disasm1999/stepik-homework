from selenium import webdriver
import time 

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")

#Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскролить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:
#
#"return arguments[0].scrollIntoView(true);"
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#Обратите внимание, что в коде в WebDriver нужно использовать ключевое слово return. Также его нужно будет использовать, когда вы захотите получить какие-то данные после выполнения скрипта. При этом при тестировании скрипта в консоли браузера слово return использовать не надо.
    button.click()
    assert True

#Также можно проскролить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:
#browser.execute_script("window.scrollBy(0, 100);")

#!Важно. Мы не будем в этом курсе изучать, как работает JavaScript, и обойдемся только приведенным выше примером скрипта с прокруткой страницы. Для сравнения приведем скрипт на этом языке, который делает то же, что приведенный выше пример для WebDriver:
#// javascript
#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView();

#    browser.execute_script("document.title='Script executing';")    
#    browser.execute_script("alert('Robots at work');")

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
