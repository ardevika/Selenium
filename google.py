from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    time.sleep(3)
    searchTextBox = driver.find_element(By.ID,"APjFqb")
    searchTextBox.send_keys("fisat")
    searchTextBox.send_keys(Keys.ENTER)
    time.sleep(15)


    print("pass")
finally:
    driver.quit()