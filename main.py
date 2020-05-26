from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

browser = webdriver.Firefox(executable_path='M:\gecko\geckodriver.exe')
browser.get('https://web.whatsapp.com')


bot_users = {}  # A dictionary that stores all the users that sent activate bot
while True:
    unread = browser.find_elements_by_class_name("OUeyt")  # The green dot tells us that the message is new
    name, message = '', ''
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(browser)
        action.move_to_element_with_offset(ele, 0, -20)  # move a bit to the left from the green dot

        # Clicking couple of times because sometimes whatsapp web responds after two clicks
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:

            name = browser.find_element_by_class_name("_3TEwt").text  # Contact name
            message = browser.find_elements_by_class_name("vW7d1")[-1]  # the message content
            #if 'activate bot' in message.text.lower():
            if name not in bot_users:
                bot_users[name] = True
                text_box = browser.find_element_by_class_name("_2S1VP")
                response = "Hi " + name + ". Fireboy Bot here :). Now I am activated for you\n"
                text_box.send_keys(response)
            if name in bot_users:
                if 'show' in message.text.lower() and 'news' in message.text.lower():
                    getNews()
            if 'deactivate' in message.text.lower():
                if name in bot_users:
                    text_box = browser.find_element_by_class_name("_2S1VP")
                    response = "Bye " + name + ".\n"
                    text_box.send_keys(response)
                    del bot_users[name]
        except Exception as e:
            print(e)
            pass
    sleep(2)  # A 2 second pause so that the program doesn't run too fast