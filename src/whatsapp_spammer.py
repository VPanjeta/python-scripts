import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox("Path/to/heckodriver")

driver = webdriver.Chrome("path/to/chromedriver")
driver.get("http://web.whatsapp.com/")

time.sleep(25)

newChat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[1]/button')
newChat.click()
find = driver.find_element_by_xpath('//input[@title="Search contacts"]')
find.send_keys('')
time.sleep(3)
elem = driver.find_element_by_xpath('//span[contains(text(),"")]')
elem.click()
time.sleep(5)
elem1 = driver.find_element_by_xpath('//div[@class="input"]')
i = 1
while True:
    elem1.send_keys("hello %d" % i)
    i += 1
    driver.find_element_by_class_name('send-container').click()