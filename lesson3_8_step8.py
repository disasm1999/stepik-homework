from selenium import webdriver


import time 
import math

def test_item_search():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get("http://selenium1py.pythonanywhere.com/ru")
    
        search_input = browser.find_element_by_id("id_q")
        search_input.clear()
    
        # Act
        search_input.send_keys("The shellcoder's handbook")
        browser.find_element_by_css_selector("input.btn.btn-default").click()
    
        # Assert
        result_page_title = browser.find_element_by_tag_name("h1")
        assert "The shellcoder's handbook" in result_page_title.text


    finally:
        browser.quit()

test_item_search()    
# не забываем оставить пустую строку в конце файла
