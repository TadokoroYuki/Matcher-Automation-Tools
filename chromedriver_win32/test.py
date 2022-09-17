from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://matcher.jp/')
elm_click = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/a')
elm_click.click()
time.sleep(3)
form = driver.find_element(By.ID, 'smsr-SignInForm_Telephone').send_keys('00000000000')#phone number
form = driver.find_element(By.ID, 'smsr-SignInForm_Password').send_keys('***')#pass
login_click = driver.find_element(By.XPATH, '//*[@id="signin"]/button')
login_click.click()
time.sleep(3)
plan_click = driver.find_element(By.XPATH, '//*[@id="icons"]/a[4]')
plan_click.click()
time.sleep(3)
form = driver.find_element(By.XPATH, '//*[@id="plan_title"]').send_keys('***')#title
form = driver.find_element(By.XPATH, '//*[@id="plan_comment"]').send_keys('***')#comment
img_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/div[3]/div[1]/div[2]/div[1]/label').click()
form = driver.find_element(By.XPATH, '//*[@id="plan_place_detail"]').send_keys('***')#detail station
create_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/button').click()
time.sleep(10)
mypage_click = driver.find_element(By.XPATH, '//*[@id="h_mypage_link"]')
mypage_click.click()
time.sleep(3)
edit = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[1]/div/div[2]/div/div/span[1]/button')
edit.click()
time.sleep(3)
delete = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/a/span[2]')
delete.click()
save = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[1]/div/div[2]/div/div/span[2]/button[2]')
save.click()
logout = driver.find_element(By.XPATH, '//*[@id="footer_list"]/li[7]/a')
logout.click()
