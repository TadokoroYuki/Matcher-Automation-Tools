from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://matcher.jp/')
elm_click = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/a')
elm_click.click()
form = driver.find_element(By.XPATH, '//*[@id="smsr-SignInForm_Telephone"]').send_keys('000')
form = driver.find_element(By.XPATH, '//*[@id="smsr-SignInForm_Password"]').send_keys('pass')