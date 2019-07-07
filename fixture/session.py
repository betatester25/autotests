from time import sleep


class SessionHelper:

    def __init__(self, method):
        self.method = method

    def login(self, username, password):
        driver = self.method.driver
        # Авторизация
        driver.find_element_by_id('index_email').send_keys(username)
        driver.find_element_by_id('index_pass').send_keys(password)
        driver.find_element_by_xpath('//button[@class="index_login_button flat_button button_big_text"]').click()
        sleep(5)