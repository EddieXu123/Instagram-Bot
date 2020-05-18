from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password, account, compliments
from random import choice


class InstagramBot:
    def __init__(self):
        # Create a browser we can play on
        self.driver = webdriver.Chrome()

    def log_on_like_comment(self):
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
        # You might be asked to Save your Login Info
        while True:
            # If you are asked,
            try:
                # Don't save info for now
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            except NoSuchElementException:
                # Otherwise, break out of the loop and continue normally
                break
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
        # 'posts' keeps track of all the posts on an account
        posts = self.driver.find_elements_by_class_name('v1Nh3')
        # select the first account because the "next post "key is different only
        # on the first post. Afterwards, the button to go to the next post is all the same
        posts[0].click()
        sleep(2)
        # Click the 'like' button
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()
        sleep(1)
        # Exit out of the bot detector
        while True:
            try:
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()
            except NoSuchElementException:
                break
        # Open the comment section
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
        sleep(2)  # wait for comment to load
        # Comment one of the 102 possible compliments
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(choice(compliments))
        # Post the comment
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # post the comment
        sleep(1)  # wait for comment to post
        # Go to the next post
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
        next_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        # While there are more posts
        while next_button:
            try:
                # Finite State Machine check if there is a bot detector pop-up
                self.close_popup()
            except NoSuchElementException:
                # If there isn't, continue to like + comment!
                self.like_comment()
                next_button.click()
        # At the end, there will be no more posts and you are done!
        print("You've liked every post and commented!")

    def like_comment(self):
        # Now, I am at a post where I can do this forever
        sleep(3)  # wait for post to load
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click()  # like the post
        # Open comment section
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(choice(compliments))  # Comment message
        while True:
            try:
                self.close_popup()
            except NoSuchElementException:
                break
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # post the comment
        sleep(1)  # wait for comment to post

    # Close the Action Blocked Popup that appears when you are being suspicious
    def close_popup(self):
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click()


bot = InstagramBot()
bot.log_on_like_comment()
