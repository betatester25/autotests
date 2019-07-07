
from selenium import webdriver
from time import sleep
from fixture.session import SessionHelper
from fixture.friends import FriendsHelper
from fixture.group import GroupHelper


class Methods:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get('https://vk.com')
        self.session = SessionHelper(self)
        self.friends = FriendsHelper(self)
        self.group = GroupHelper(self)






    def destroy(self):
        self.driver.quit()