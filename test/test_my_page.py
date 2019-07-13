

def test_assert_of_traffic_my_page(method):
    method.my_page.open()
    method.my_page.statistic()
    method.assert_text(word='Уникальные посетители и просмотры')

