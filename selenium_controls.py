from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chat_bot import ChatBot
import time


CHROME_DRIVE = "D:\dev-tools\chromedriver.exe"
USER_DATA = "user-data-dir=D:\\dev-tools\\bumbprof"
URL = "https://onlyfans.com/"

class SeleniumControls:

    def __init__(self):
        self.service = Service(CHROME_DRIVE)
        self.chroptions = webdriver.ChromeOptions()
        self.chroptions.add_argument(USER_DATA)
        self.driver = webdriver.Chrome(service=self.service, options=self.chroptions)
        self.driver.get(url=URL)
        self.chatbot = ChatBot()


    def go_to_messages(self):
        message_inbox = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/header/nav/a[4]/span[2]")
        message_inbox.click()
        time.sleep(3)

    def unread_message(self):
        blue_dot = self.driver.find_element(By.CLASS_NAME, "b-chats__item__uread-count")
        blue_dot.click()
        time.sleep(3)

    def scrape_message(self):

        self.get_messages = self.driver.find_elements(By.CLASS_NAME, "m-message-content-bg")
        self.messages = [message.text for message in self.get_messages]
        for i in range(0, len(self.messages)):
            if i == (len(self.messages) - 1):
                self.text_to_be_analyzed = str(self.messages[i])
                self.return_message = self.chatbot.convert_text(message_to_be_analyzed=self.text_to_be_analyzed)
                self.respond_move(to_send=self.return_message)

    def respond_move(self, to_send):
        self.textbox = self.driver.find_element(By.ID, "new_post_text_input")
        self.textbox.click()
        self.textbox.send_keys(to_send)
        time.sleep(3)

