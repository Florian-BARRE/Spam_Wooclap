import time
import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Wooclap:
    base_url = "https://app.wooclap.com/"
    code = ""
    url = ""
    mot = ""
    FireFox = webdriver.Firefox(executable_path="geckodriver.exe")

    def __init__(self, code):
        self.code = code
        self.url = self.base_url + self.code
        print(self.url)

    def Start_Web(self):
        self.FireFox.get(self.url)

    def Start_Spam(self):
        while(True):
            input = self.FireFox.find_element(By.CSS_SELECTOR, "textarea")
            input.send_keys(self.mot)

            btns = self.FireFox.find_elements(By.TAG_NAME, 'button')
            btns[1].click()



x = Wooclap("your code")
x.Start_Web()
x.mot = "your word"
x.Start_Spam()
