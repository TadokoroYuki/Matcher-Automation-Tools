from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import requests


driver = webdriver.Chrome()#Chomeを開く
driver.get('https://matcher.jp/')#matcherを開く
for i in range(10):
 elm_click = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/a')#login画面を開く
 elm_click.click()
 time.sleep(3)
 
 form = driver.find_element(By.ID, 'smsr-SignInForm_Telephone').send_keys('00000000000')#phone number
 form = driver.find_element(By.ID, 'smsr-SignInForm_Password').send_keys('***')#pass
 login_click = driver.find_element(By.XPATH, '//*[@id="signin"]/button')
 login_click.click() 
 time.sleep(3)

 plan_click = driver.find_element(By.XPATH, '//*[@id="icons"]/a[4]')#新規プラン作成画面
 plan_click.click()
 time.sleep(3)
 
 form = driver.find_element(By.XPATH, '//*[@id="plan_title"]').send_keys('***')#title
 form = driver.find_element(By.XPATH, '//*[@id="plan_comment"]').send_keys('***')#comment
 img_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/div[3]/div[1]/div[2]/div[1]/label').click()
 form = driver.find_element(By.XPATH, '//*[@id="plan_place_detail"]').send_keys('***')#detail station
 create_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/button').click()
 time.sleep(10)

 mypage_click = driver.find_element(By.XPATH, '//*[@id="h_mypage_link"]')#mypageへ
 mypage_click.click()
 time.sleep(3)
 
 edit = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[1]/div/div[2]/div/div/span[1]/button')
 edit.click()
 time.sleep(3)

 delete = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[3]/div/div/div[2]/div/div[1]/div/div/a/span[2]')#planを削除
 delete.click()
 save = driver.find_element(By.XPATH, '//*[@id="plan"]/div/div[1]/div/div[2]/div/div/span[2]/button[2]')
 save.click()

 logout = driver.find_element(By.XPATH, '//*[@id="footer_list"]/li[7]/a')#logout
 logout.click()
 date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
 line_notify_token = 'LINEアクセストークン'
 line_notify_api = 'https://notify-api.line.me/api/notify'
 headers = {'Authorization': f'Bearer {line_notify_token}'}
 data = {'message': f'message: {date}'}
 requests.post(line_notify_api, headers = headers, data = data)




#田所　lineトークン　gXLvjTCaxsgSdGIf8XlcLv7P1c32CDtfzdnqiKEif4a　悪用しないでくださいWW



