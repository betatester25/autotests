from time import sleep


class GroupHelper:

    def __init__(self, method):
        self.method = method

    def write_post(self, parameters):
        driver = self.method.driver
        # Написание поста в группу
        driver.find_element_by_xpath('//div[@class="submit_post_field dark submit_post_inited"]').send_keys(
            parameters.text)
        sleep(7)
        driver.find_element_by_id('send_post').click()
        sleep(5)

    def choice_of_group(self, name):
        driver = self.method.driver
        # выбор группы
        driver.find_element_by_xpath('//span[text()="Группы"]').click()
        driver.find_element_by_xpath('//a[text()=%s]' % name).click()