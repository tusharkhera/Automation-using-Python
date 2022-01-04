from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('C:\chromeDriver\chromedriver.exe')
browser.get('https://www.instagram.com/')
time.sleep(4) 
Username=browser.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("tusharkhera346@gmail.com")
time.sleep(4)
password=browser.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("1221abcd")
password.submit()
time.sleep(5)
Notnow=browser.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
Notnow.click() 
time.sleep(3)
Noti=browser.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(7)

def firstpic():  
	time.sleep(5)
	pic = browser.find_element(By.CLASS_NAME, "fr66n") 
	# pic = browser.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div/div[3]/div/div/section[1]/span[1]/button")
	pic.click() 
def comment(): 
	time.sleep(5)
	# commentArea = browser.find_element_by_class_name('Ypffh')
	commentArea = browser.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div/div[2]/div/article[1]/div/div[3]/div/div/section[1]/span[2]/button")
	commentArea.click()
	time.sleep(5)
	# comment = browser.find_element(By.CLASS_NAME, 'Ypffh')
	comment = browser.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")
	comment.click()
	comment.send_keys("Test command")
	comment.submit()
	
firstpic()
comment()


