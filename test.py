from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import requests
import schedule

def chrome():
 driver = webdriver.Chrome()#Chomeを開く
 driver.maximize_window()
 driver.get('https://matcher.jp/')#matcherを開く

def job(id, pas):
 try:
  driver = webdriver.Chrome()#Chomeを開く
  driver.maximize_window()
  
  driver.get('https://matcher.jp/')#matcherを開く
  
  for i in range(10):
   elm_click = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/a')#login画面を開く
   elm_click.click()
   sleep(3)
   
   form = driver.find_element(By.ID, 'smsr-SignInForm_Telephone').send_keys(id)#phone number
   form = driver.find_element(By.ID, 'smsr-SignInForm_Password').send_keys(pas)#pass
   login_click = driver.find_element(By.XPATH, '//*[@id="signin"]/button')
   login_click.click() 
   sleep(3)
  
   plan_click = driver.find_element(By.XPATH, '//*[@id="icons"]/a[4]')#新規プラン作成画面
   plan_click.click()
   sleep(3)
   
   form = driver.find_element(By.XPATH, '//*[@id="plan_title"]').send_keys('***')#title
   form = driver.find_element(By.XPATH, '//*[@id="plan_comment"]').send_keys('***')#comment
   img_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/div[3]/div[1]/div[2]/div[1]/label').click()
   form = driver.find_element(By.XPATH, '//*[@id="plan_place_detail"]').send_keys('***')#detail station
   create_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/button').click()
   sleep(10)
  
   mypage_click = driver.find_element(By.XPATH, '//*[@id="h_mypage_link"]')#mypageへ
   mypage_click.click()
   sleep(3)
   
   edit = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[1]/div[2]/button')
   edit.click()
   sleep(3)
  
   delete = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div[1]')#planを削除
   delete.click()
   save = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[1]/div[2]/button[2]')
   save.click()
  
   logout = driver.find_element(By.XPATH, '//*[@id="footer_list"]/li[7]')#logout
   logout.click()
 except Exception:
  driver = webdriver.Chrome()#Chomeを開く
  driver.maximize_window()
  
  driver.get('https://matcher.jp/')#matcherを開く
  
  for i in range(10):
   elm_click = driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/a')#login画面を開く
   elm_click.click()
   sleep(3)
   
   form = driver.find_element(By.ID, 'smsr-SignInForm_Telephone').send_keys(id)#phone number
   form = driver.find_element(By.ID, 'smsr-SignInForm_Password').send_keys(pas)#pass
   login_click = driver.find_element(By.XPATH, '//*[@id="signin"]/button')
   login_click.click() 
   sleep(3)
  
   plan_click = driver.find_element(By.XPATH, '//*[@id="icons"]/a[4]')#新規プラン作成画面
   plan_click.click()
   sleep(3)
  
   form = driver.find_element(By.XPATH, '//*[@id="plan_title"]').send_keys('***')#title
   form = driver.find_element(By.XPATH, '//*[@id="plan_comment"]').send_keys('***')#comment
   img_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/div[3]/div[1]/div[2]/div[1]/label').click()
   form = driver.find_element(By.XPATH, '//*[@id="plan_place_detail"]').send_keys('***')#detail station
   create_click = driver.find_element(By.XPATH, '//*[@id="new_plan"]/button').click()
   sleep(10)
  
   mypage_click = driver.find_element(By.XPATH, '//*[@id="h_mypage_link"]')#mypageへ
   mypage_click.click()
   sleep(3)
   
   edit = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[1]/div[2]/button')
   edit.click()
   sleep(3)
  
   delete = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[2]/div/div/div/div/div[1]/div[2]/div[1]')#planを削除
   delete.click()
   save = driver.find_element(By.XPATH, '//*[@id="mypage"]/div/div/div[1]/div/div[7]/div[1]/div[2]/button[2]')
   save.click()
  
   logout = driver.find_element(By.XPATH, '//*[@id="footer_list"]/li[7]')#logout
   logout.click()
  
#date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
#line_notify_token = 'LINEアクセストークン'
#line_notify_api = 'https://notify-api.line.me/api/notify'
#headers = {'Authorization': f'Bearer {line_notify_token}'}
#data = {'message': f'message: {date}'}
#requests.post(line_notify_api, headers = headers, data = data)


def timer(start, id, pas):
 
 schedule.every().day.at(start).do(job, id=id, pas=pas)

 while True:
    schedule.run_pending()
    sleep(1)




