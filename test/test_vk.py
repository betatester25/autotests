from data.write_post import testdata
import pytest


def test_friends(method):
    method.friends.friend_requests()
    method.assert_text(word='Влад Чижов')

  
@pytest.mark.parametrize('parameters', testdata, ids=[repr(x) for x in testdata])
def test_my_group(method, parameters):
    method.group.choice_of_group(parameters)
    method.group.write_post(parameters)
