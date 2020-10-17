import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://tinder.com/')
time.sleep(8)

# Clicks on Sign-in using Google
google=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
google.click()

# Handle your second window  
base_window =driver.window_handles[0]
driver.switch_to_window(driver.window_handles[1])

# Fill the Username and Password
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('__USER_NAME__')
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('__PASSWORD__')
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(2)

driver.switch_to_window(base_window)
time.sleep(8)

driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
