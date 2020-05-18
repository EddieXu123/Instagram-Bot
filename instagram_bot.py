# Intro: I was scrolling through my LinkedIn feed and saw tons of posts of people whose internships
# got canceled due to COVID-19, but fortunately landed another remote internship. I knew that the recruiters
# helping these people were working extremely hard behind the scenes and wanted to acknowledge them in some way
# As a result, I built a LinkedIn bot that would log on, search a company's recruiters, and send them a
# note expressing gratitude for their hard work during these times. It was a short letter and only a few
# recruiters were actually accepting connection requests/messages, but many of the ones who did replied with
# thanks, making the whole experience worth it!


# Plan
# Log into my LinkedIn
# Go to search bar, at the start of the day, put in 3 companies.
# The bot will search company #1-3 + recruiters, connect with any recruiter by sending a message
# If it is possible to message them, then write them the same message. close, and continue
#
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import pyautogui
from contact import email, password, account, message


# Button to go to next page
# '/html/body/div[8]/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[3]/div/button[2]'
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
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(email)
        # Enter password
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password + Keys.RETURN)
        sleep(3)
        # Don't turn on notifications
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        # Go to search bar and enter account
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(account)
        sleep(2)
        keyboard.press(Key.enter)
        keyboard.press(Key.enter)
        sleep(4)
        # Now I am on the account

        # posts keeps track of all the posts on an account
        posts = self.driver.find_elements_by_class_name('v1Nh3')

        # I again need to inspect element pane because Instagram hid the xPaths of commenting
        # To do this, I can just control + left click to simulate right clicking and then go to inspect
        keyboard.press(Key.ctrl_l)
        pyautogui.click(500, 200)
        keyboard.release(Key.ctrl_l)
        # After right clicking, the inspect element option is 8 options down
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
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
        sleep(2)  # wait for comment to load
        # Comment something
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
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
                '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)  # Comment message
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # post the comment
            sleep(1)  # wait for comment to post
            self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()  # Go to next post

bot = InstagramBot()
bot.like_comment()
