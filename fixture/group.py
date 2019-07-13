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

    def add_new_group(self, parameters):
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_id('ts_input').click()
        driver.find_element_by_id('ts_input').send_keys('%s' % parameters.name)
        driver.find_element_by_xpath('//span[text()="Показать все результаты"]').click()
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_xpath('(//div[@class="labeled title"])[%s]' % parameters.number_of_result).click()
        driver = self.method.driver
        sleep(3)
        driver.find_element_by_xpath('//button[text()="%s"]' % parameters.name_of_button).click()

    def get_list(self):
        driver = self.method.driver
        driver.find_element_by_xpath('//span[text()="Группы"]').click()
        group_list = []
        for element in driver.find_elements_by_xpath('//a[@class="group_row_title"]'):
            text = element.text
            group_id = driver.find_element_by_xpath('//div[@class="group_list_row clear_fix _gl_row "]')
            id = group_id.get_attribute('id')
            group_list.append(Parameters(name=text, id=id))
        return group_list





