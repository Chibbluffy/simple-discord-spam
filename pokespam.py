# python pokespam.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# You have 40 seconds to login and get to the right channel before it spams whatever you want to spam below


driver = webdriver.Chrome()
driver.get("http://discord.com/login")

sleep(40)
# You have 40 seconds to login and get to the right channel before it spams whatever you want to spam below

i = 1
while i:
    message = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
    message.send_keys("Gimme really shitty ivs pokemans")
    # message.send_keys(str(i))
    message.send_keys(Keys.ENTER)
    sleep(10)
    i += 1
