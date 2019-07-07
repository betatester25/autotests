
from selenium import webdriver
from time import sleep
from fixture.session import SessionHelper

class Methods:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get('https://vk.com')
        self.session = SessionHelper(self)

    def friend_requests(self):
        driver = self.driver
        # Промотр исходящих заявок в друзья
        driver.find_element_by_xpath('//span[@class="left_label inl_bl" and contains(text(), "Друзья")]').click()
        sleep(3)
        driver.find_element_by_xpath('//span[text()="Заявки в друзья"]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="friends_tab_out_requests"]/a').click()
        sleep(3)


    def write_post(self, parameters):
        driver = self.driver
        # Написание поста в группу
        driver.find_element_by_xpath('//div[@class="submit_post_field dark submit_post_inited"]').send_keys(
            parameters.text)
        sleep(7)
        driver.find_element_by_id('send_post').click()
        sleep(5)

    def choice_of_group(self, name):
        driver = self.driver
        # выбор группы
        driver.find_element_by_xpath('//span[text()="Группы"]').click()
        driver.find_element_by_xpath('//a[text()=%s]' % name).click()

    def destroy(self):
        self.driver.quit()