from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Screenshot import Screenshot_Clipping
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1400,800")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
#driver = webdriver.Chrome("chromedriver.exe")

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

driver.quit()