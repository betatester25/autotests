

class MyPageHelper:

    def __init__(self, method):
        self.method = method

    def open(self):
        driver = self.method.driver
        # переход на мою страницу
        driver.find_element_by_xpath('//span[text()="Моя Страница"]').click()



