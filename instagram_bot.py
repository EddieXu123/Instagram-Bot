from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password, account, compliments
from random import choice


class InstagramBot:
    def __init__(self):
        # Create a browser we can play on
        self.driver = webdriver.Chrome()

    def like_comment(self):
        keyboard = Controller()
        """First, we must log into our Instagram account"""
        # Go to LinkedIn
        self.driver.get('https://instagram.com')
        sleep(2)
        # Enter email
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(email)
        # Enter password
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(
            password + Keys.RETURN)
        sleep(3)
        # Don't turn on notifications
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        # Go to search bar and enter account
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(
            account)
        sleep(2)
        # Two 'enters': One to select the user and go to the user's page
        keyboard.press(Key.enter)
        keyboard.press(Key.enter)
        sleep(4)

        """Now I am on the account"""

        # 'posts' keeps track of all the posts on an account
        posts = self.driver.find_elements_by_class_name('v1Nh3')

        # I need to inspect element because Instagram hid the xPaths of commenting; I must open the elements pane to get the actual path
        # To do this, I can just control + left click to simulate right clicking and then go to inspect
        keyboard.press(Key.ctrl_l)
        pyautogui.click(500, 200)
        keyboard.release(Key.ctrl_l)
        # After right clicking, the inspect element option is 6 options down
        i = 0
        while i < 6:
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            i += 1
        keyboard.press(Key.enter)  # Open up insect element tab in order to like the video
        keyboard.release(Key.enter)
        sleep(1)
        # Maximize window so the comment bar appears when I select post
        # Otherwise, I will not be able to access comment
        keyboard.press(Keys.LEFT_ALT)
        pyautogui.click(86, 70)
        keyboard.release(Keys.LEFT_ALT)
        sleep(4)
        # select the first account because the "next post "key is different only
        # on the first post. Afterwards, the button to go to the next post is all the same
        posts[0].click()
        sleep(2)
        # Click the 'like' button
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        # Open the comment section
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
        sleep(2)  # wait for comment to load
        # Comment one of the 102 possible compliments
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(choice(compliments))
        # Post the comment
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # post the comment
        sleep(1)  # wait for comment to post
        # Go to the next post
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()

        # Now, I am at a post where I can do this forever
        while True:
            sleep(3)  # wait for post to load
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()  # like the post
            # Open comment section
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(
                choice(compliments))  # Comment message
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # post the comment
            sleep(1)  # wait for comment to post
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()  # Go to next post


bot = InstagramBot()
bot.like_comment()
