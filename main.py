from google.cloud import dialogflow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium_controls import SeleniumControls
from chat_bot import ChatBot

import time

chatbot = ChatBot()
selenium = SeleniumControls()


check = input("Are you logged in? y/n")

if check == "y":
    while True:
        selenium.unread_message()
        time.sleep(3)
        selenium.scrape_message()
        time.sleep(3)

else:
    print("failed to open")




