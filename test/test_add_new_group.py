from model.parameters import Parameters


def test_add_group(method):
    old_groups = method.group.get_list()
    method.group.add_new_group(Parameters(name='Подслушано Ростов-на-Дону',
                               number_of_result='2',
                               name_of_button='Подписаться'))
    new_groups = method.group.get_list()
    assert len(old_groups) + 1 == len(new_groups)