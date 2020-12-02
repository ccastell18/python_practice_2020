from selenium import webdriver
import os

chrome_browser = webdriver.Chrome("./chromedriver")

chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
button_text = chrome_browser.find_element_by_class_name("btn-default")
# print(button_text.get_attribute("innerHTML"))

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message2 = chrome_browser.find_element_by_css_selector("#get-input >.btn")
print(user_message2)
user_message.clear()
user_message.send_keys("I am Cool")

button_text.click()
output_message = chrome_browser.find_element_by_id("display")

assert "I am Cool" in output_message.text

chrome_browser.close()
