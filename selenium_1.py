from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("chromedriver.exe")

#pages = ["https://www.w3schools.com/js/js_statements.asp", "https://www.w3schools.com/js/js_comments.asp", "https://www.w3schools.com/js/js_variables.asp" ]


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
driver.save_screenshot("1.jpg")

from Screenshot import Screenshot_Clipping
ob=Screenshot_Clipping.Screenshot()
img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)

#time.sleep(5)
#driver.execute_script("window.resizeTo(800,600)")
#time.sleep(25)
#driver.quit()