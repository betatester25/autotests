from time import sleep

class FriendsHelper:

    def __init__(self, method):
        self.method = method

    def friend_requests(self):
        driver = self.method.driver
        # Промотр исходящих заявок в друзья
        driver.find_element_by_xpath('//span[@class="left_label inl_bl" and contains(text(), "Друзья")]').click()
        sleep(3)
        driver.find_element_by_xpath('//span[text()="Заявки в друзья"]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="friends_tab_out_requests"]/a').click()
        sleep(3)


