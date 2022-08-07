import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import

URL = 'https://www.instagram.com/accounts/login/'
USERNAME = 'Icone_graphics'
PWD = 'nXU@V5bJaN38r-g'
TARGET_ACCOUNT = 'https://www.instagram.com/logo.superb/'
chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  # Don't wait for page to fully load
# speed up driver performance by disabling images loading
op = webdriver.ChromeOptions()
chrome_prefs = {}
op.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}


class InstaFollower:
    def __init__(self, chrome_path):
        service = Service(chrome_path)
        self.driver = webdriver.Chrome(desired_capabilities=caps, service=service, options=op)

    def login(self):
        self.driver.get(url=URL)
        time.sleep(10)
        # sending details
        self.driver.find_element(By.NAME, 'username').send_keys(USERNAME)
        Pass = self.driver.find_element(By.NAME, 'password')
        Pass.send_keys(PWD)
        time.sleep(3)
        Pass.submit()
        time.sleep(10)
        # closing annoying popups
        turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body')
        turn_off_notifications.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
        time.sleep(10)
        turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body')
        turn_off_notifications.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)

    def find_followers(self):
        self.driver.get(TARGET_ACCOUNT)
        time.sleep(10)
        # button that leads to the followers pop-up.
        followers_button = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]'
                                                    '/section/main/div/header/section/ul/li[2]/a/div')
        followers_button.click()
        time.sleep(5)
        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        # scrolling three times in the popup
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)
            time.sleep(2)

    def follow(self):
        follow_btns = self.driver.find_elements(By.XPATH,
                                                "//li[contains(@class, '_aaei')]//button[@class='_acan _acap _acas']")
        # To follow each follower in the pop-up.
        for button in follow_btns:
            try:
                button.click()
                print('clicked!!!!!')
                time.sleep(1)
            except ElementClickInterceptedException:
                turn_off_notifications = self.driver.find_element(By.XPATH, '/html/body')
                turn_off_notifications.send_keys(Keys.TAB + Keys.ENTER)
        print('insta bot done!')


insta_bot = InstaFollower(chrome_path=chrome_driver_path)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
