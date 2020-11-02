
#askforcredentials

username=input("Enter User Name:")
password=input("Enter Password:")
from selenium import webdriver
import time

browser=webdriver.Chrome("D:\chromedriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(4)

    #Login
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys(username)
time.sleep(3)

Password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
Password.send_keys(password)
Password.submit()
time.sleep(2)

    #NotNow
Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
Notnow.click()
time.sleep(2)

    #Notification
Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(2)

def firstpic():
         time.sleep(1)
         pic=browser.find_element_by_class_name("_9AhH0")
         pic.click()

def likepic():
         time.sleep(1)
         like=browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div[3]/section[1]/span[1]/button")
         like.click()
firstpic()
likepic()
    
