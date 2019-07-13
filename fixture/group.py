from cgitb import text
from time import sleep
from model.parameters import Parameters



class GroupHelper:

    def __init__(self, method):
        self.method = method

    def write_post(self, parameters):
        driver = self.method.driver
        # Написание поста в группу
        driver.find_element_by_xpath('//div[@class="submit_post_field dark submit_post_inited"]').send_keys(
            parameters.text)
        driver.find_element_by_id('send_post').click()


    def choice_of_group(self, parameters):
        driver = self.method.driver
        # выбор группы
        driver.find_element_by_xpath('//span[text()="Группы"]').click()
        driver.find_element_by_xpath('//a[text()=%s]' % parameters.name).click()

    def add_new_group(self, name, number_of_result, name_of_button):
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_id('ts_input').click()
        driver.find_element_by_id('ts_input').send_keys('%s' % name)
        driver.find_element_by_xpath('//span[text()="Показать все результаты"]').click()
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_xpath('(//div[@class="labeled title"])[%s]' % number_of_result).click()
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_xpath('//button[text()="%s"]' % name_of_button).click()



