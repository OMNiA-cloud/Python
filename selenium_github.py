#selenium locating elements

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)


searchInput = driver.find_element_by_name("q") #xPath üzerinden ulaşımda sağlanabilir
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
#result = driver.page_source

result = driver.find_elements_by_css_selector(".repo-list-item a") # aradaki boşluklar alt eleman

for element in result:
    print(element.text)

driver.close()