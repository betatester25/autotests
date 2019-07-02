from selenium import webdriver
from time import sleep
import unittest


class YandexTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get('https://yandex.ru/')

    def test_search(self):
        driver = self.driver
        driver.find_element_by_id('text').send_keys('Чтение человека по невербальным признакам')
        sleep(3)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(10)








    def tearDown(self):
        self.driver.quit()



if __name__=='__main':
    unittest.main()