

class MyPageHelper:

    def __init__(self, method):
        self.method = method

    def open(self):
        driver = self.method.driver
        # переход на мою страницу
        driver.find_element_by_xpath('//span[text()="Моя Страница"]').click()

    def statistic(self):
        driver = self.method.driver
        driver.find_element_by_xpath('//div[@onclick="Page.actionsDropdown(domNS(this))"]').click()
        driver.find_element_by_xpath('//a[text()="Статистика страницы"]').click()
        # Просмотр посещаемости
        driver.find_element_by_xpath('(//a[@onclick="return uiTabs.goTab(this, event, 0);"])[2]').click()

