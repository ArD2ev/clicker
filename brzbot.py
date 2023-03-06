from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://ep4sh.cc/paste/add')

addedtext = '/html/body/div/form/div[1]/input'
browser.find_element(By.XPATH, addedtext).send_keys('BRZ_BOT')

addedtext2 = '/html/body/div/form/div[2]/textarea'
browser.find_element(By.XPATH, addedtext2).send_keys('hello pavel eto OBЪKTИВНО NE SLOZHNAH')

savedtext = '/html/body/div/form/button'
browser.find_element(By.XPATH, savedtext).click()