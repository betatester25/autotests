from fixture.methods import Methods

import pytest

fixture = None


@pytest.fixture()
def method(request):
    global fixture
    if fixture is None:
        fixture = Methods()
        fixture.session.login(username='evgenikuznecov25@yandex.ru', password='English007')
    else:
        if not fixture.is_valid():
            fixture = Methods()
            fixture.session.login(username='evgenikuznecov25@yandex.ru', password='English007')
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
