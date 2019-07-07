from model.parameters import Parameters
from fixture.methods import Methods
import pytest

@pytest.fixture
def method(request):
    fixture = Methods()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_friends(method):
        method.session.login(username='evgenikuznecov25@yandex.ru', password='English007')
        method.friends.friend_requests()



def test_my_group(method):
        method.session.login(username='evgenikuznecov25@yandex.ru', password='English007')
        method.group.choice_of_group(name='"SmartBlog <дневник айтишника>"')
        method.group.write_post(Parameters(text='Данный пост создан написанной мной программой на '
                                        'базе Selenium WebDriver и драйвера Chrome'))



