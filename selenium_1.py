from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get("http://www.google.com/")
driver.find_element_by_name("q").send_keys("Test it")
driver.find_element_by_name("btnK").click()

driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
driver.refresh()

driver.set_window_size(640, 480)

body = driver.find_element_by_css_selector("body")
for i in range(5):
    body.send_keys(Keys.PAGE_DOWN)
#time.sleep(5)
#driver.execute_script("window.resizeTo(800,600)")
#time.sleep(25)
#driver.quit()