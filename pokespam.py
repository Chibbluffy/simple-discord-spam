# cd '.\Documents\CS\Pokecord Chrome spam\'
# python pokespam.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# You have 40 seconds to login and get to the right channel before it spams whatever you want to spam below


driver = webdriver.Chrome()
driver.get("http://discord.com/login")

'''
login_email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
login_pass = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
login_email.send_keys(username)
login_pass.send_keys(password)
login_pass.send_keys(Keys.ENTER)
'''
sleep(40)
# You have 40 seconds to login and get to the right channel before it spams whatever you want to spam below

i = 1
while i:
    message = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
    message.send_keys("Gimme really shitty ivs pokemans")
    # message.send_keys(str(i))
    message.send_keys(Keys.ENTER)
    sleep(5)
    i += 1


# driver.close()
