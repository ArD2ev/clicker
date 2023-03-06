from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://ep4sh.cc/')

noteadded = '/html/body/div/div/div/div[2]/div/div/div/div/a/button'
browser.find_element(By.XPATH, noteadded).click()

added = '/html/body/section/div[2]/a'
browser.find_element(By.XPATH, added).click()

addedtext = '/html/body/div/form/div[1]/input'
browser.find_element(By.XPATH, addedtext).send_keys('BRZ_BOT')

addedtext2 = '/html/body/div/form/div[2]/textarea'
browser.find_element(By.XPATH, addedtext2).send_keys('hello pavel eto OBЪKTИВНО NE SLOZHNAH')

savedtext = '/html/body/div/form/button'
browser.find_element(By.XPATH, savedtext).click()
