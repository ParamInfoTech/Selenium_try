from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Screenshot import Screenshot_Clipping
import time

driver = webdriver.Chrome("chromedriver.exe")

pages = ["https://www.w3schools.com/js/js_statements.asp", 
        "https://www.w3schools.com/js/js_comments.asp", 
        "https://www.w3schools.com/js/js_variables.asp"]

for link in pages:
    driver.get(link)
    driver.maximize_window()
    ob=Screenshot_Clipping.Screenshot()
    print(link)
    arr = link.split("/")
    img_url=ob.full_Screenshot(driver, save_path=r'.', image_name = arr[-1]+'.png')