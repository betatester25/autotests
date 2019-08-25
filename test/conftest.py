from fixture.methods import Methods
import json
import pytest

fixture = None
target = None


@pytest.fixture()
def method(request):
    global fixture
    global target
    if target is None:
        with open(request.config.getoption('--target')) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Methods(browser=target["browser"])
    fixture.session.login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--target', action='store', default='target.json')
