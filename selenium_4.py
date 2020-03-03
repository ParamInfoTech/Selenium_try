from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

driver.get("https://www.w3schools.com/js/js_statements.asp")

driver.set_window_size(480, 480)
original_size = driver.get_window_size()
required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(required_width, required_height)
# driver.save_screenshot(path)  # has scrollbar
driver.find_element_by_tag_name('body').screenshot('check.png')  # avoids scrollbar
driver.set_window_size(original_size['width'], original_size['height'])

driver.quit()