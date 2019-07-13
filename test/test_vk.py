from model.parameters import Parameters
import pytest


def test_friends(method):
    method.friends.friend_requests()
    method.assert_text(word='Влад Чижов')


testdata = [Parameters(name='"Игровой AliExpress"', text='Я кодер'),
            Parameters(name='"Тестовая группа Pytest"', text='тестовый пост новый')]


@pytest.mark.parametrize('parameters', testdata, ids=[repr(x) for x in testdata])
def test_my_group(method, parameters):
    method.group.choice_of_group(parameters)
    method.group.write_post(parameters)
