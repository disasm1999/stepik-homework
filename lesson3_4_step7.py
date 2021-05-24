#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".

from selenium import webdriver
import os 
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


#Загрузка файлов
#Бывает так, что нам необходимо загрузить файл на веб-странице. Элементом на странице, с помощью которого эту задачу решает человек, как правило является обычный input, но с особенным значением атрибута type

#<input type="file"/> 

#На странице этот элемент выглядит как кнопка выбора файла.

#Для selenium такой вид input'ов ничем не отличается от любого другого input'а, так что мы можем использовать уже знакомый нам метод send_keys() для добавления туда данных. Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.

#Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой - os. В этом случае ваш код не будет зависеть от операционной системы, которую вы используете. Добавление файла будет работать и на Windows, и на Linux.

#Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете:

#import os 

#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)
#Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__)) и print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу. Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html. Обратите внимание, что это будет работать только при запуске кода из файла, в интерпретаторе не сработает.

#Если совсем непонятно, что происходит, пример: 

#Допустим, мы написали код скрипта и сохранили код в lesson2_step7.py в свой локальной папке D:\stepik_homework.
#Кроме того,  в эту же папку мы положили файл, который хотим прикрепить, например file.txt.
#Активируем виртуальное окружение и запускаем его python lesson2_step7.py.
#Конструкция current_dir = os.path.abspath(os.path.dirname(__file__)) запишет в переменную current_dir путь до директории файла с кодом, то есть D:\stepik_homework.
#Конструкция file_path = os.path.join(current_dir, 'file.txt' присоединит к строке в current_dir имя файла file.txt и запишет полученный путь в переменную file_path
#В переменной file_path будет полный путь к файлу 'D:\homework\file.txt'. Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt перенесем в другую папку, или на компьютер с другой ОС, то такой код без правок заработает и там. 

#Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)


#    button = browser.find_element_by_css_selector(".btn")
#    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
