

class MyPageHelper:

    def __init__(self, method):
        self.method = method

    def open(self):
        driver = self.method.driver
        # переход на мою страницу
        driver.find_element_by_xpath('//span[text()="Моя страница"]').click()

    def open_foto_section(self):
        driver = self.method.driver
        driver.find_element_by_xpath('//span[text()="Фотографии"]').click()

    def open_my_message(self):
        driver = self.method.driver
        driver.find_element_by_xpath('//span[text()="Сообщения"]').click()