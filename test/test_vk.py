from model.parameters import Parameters
from fixture.methods import Methods
import pytest

@pytest.fixture
def method(request):
    fixture = Methods()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_friends(method):
        method.login(username='evgenikuznecov25@yandex.ru', password='English007')
        method.friend_requests()



def test_my_group(method):
        method.login(username='evgenikuznecov25@yandex.ru', password='English007')
        method.choice_of_group(name='"SmartBlog <дневник айтишника>"')
        method.write_post(Parameters(text='Данный пост создан написанной мной программой на '
                                        'базе Selenium WebDriver и драйвера Chrome'))



