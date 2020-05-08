# python pokespam.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


login_timer = 40            # how long you have before it tries to spam
spam_timer = 10             # how many seconds between each spam message will be
message_text = "Gimme really shitty ivs pokemans"


driver = webdriver.Chrome()
driver.get("http://discord.com/login")

sleep(login_timer)
# You have 40 seconds to login and get to the right channel before it spams whatever you want to spam below

# I originally had a counter here, so that I could see how much it counted up. 
# I replaced it, but left it here commented out if anyone wants to still use it.
i = 1
while i:
    message = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]/div')
    message.send_keys(message_text)
    # message.send_keys(str(i))
    message.send_keys(Keys.ENTER)
    sleep(spam_timer)
    # i += 1
