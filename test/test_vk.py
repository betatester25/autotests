from model.parameters import Parameters






def test_friends(method):
        method.friends.friend_requests()




def test_my_group(method):
        method.group.choice_of_group(name='"SmartBlog <дневник айтишника>"')
        method.group.write_post(Parameters(text='Данный пост создан написанной мной программой на '
                                        'базе Selenium WebDriver и драйвера Chrome'))




