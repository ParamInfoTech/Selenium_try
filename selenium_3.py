from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)

driver.get("http://www.google.com/")
driver.find_element_by_name("q").send_keys("Test it")
driver.find_element_by_name("btnK").click()

driver.maximize_window()
driver.refresh()

driver.set_window_size(640, 480)

from Screenshot import Screenshot_Clipping
ob=Screenshot_Clipping.Screenshot()
img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')