import time

from selenium import webdriver
validate = "abdul"

driver = webdriver.Chrome(executable_path="F:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_css_selector("#name").send_keys("validate")
driver.find_element_by_id("alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alert2 = driver.switch_to.alert
validate = alert.text
assert validate in alert.text
alert.accept()
