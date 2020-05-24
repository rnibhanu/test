from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys

print("sample test case started")  
driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
driver.get("https://www.google.com/")  
driver.find_element_by_name("q").send_keys("Python Tutorials")  
time.sleep(3)  
#click on the Google search button  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  
