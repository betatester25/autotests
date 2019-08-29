

def test_assert_of_traffic_my_page(method):
    method.my_page.open()


def test_view_my_foto(method):
    method.my_page.open_foto_section()


def test_view_my_message(method):
    method.my_page.open_my_message()
