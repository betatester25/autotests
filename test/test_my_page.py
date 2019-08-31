import pytest


@pytest.allure.step('Просмотр моей страницы')
def test_view_my_page(method):
    method.my_page.open()


@pytest.allure.step('Переход в раздел "Фотографии"')
def test_view_my_foto(method):
    method.my_page.open_foto_section()


def test_view_my_message(method):
    method.my_page.open_my_message()
