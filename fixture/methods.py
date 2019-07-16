from selenium import webdriver
from time import sleep
from fixture.session import SessionHelper
from fixture.friends import FriendsHelper
from fixture.group import GroupHelper
from fixture.my_page import MyPageHelper


class Methods:

    def __init__(self, browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        else:
            raise ValueError('Ошибка с выбором браузера')
        self.driver.get('https://vk.com')
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.friends = FriendsHelper(self)
        self.group = GroupHelper(self)
        self.my_page = MyPageHelper(self)

    def assert_text(self, word):
        driver = self.driver
        sleep(5)
        assert ('%s' % word) in driver.page_source

    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()
