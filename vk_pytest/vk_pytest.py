dict_1 = {'name': 'surname'}


def test_dict_1():
    assert dict_1['name']

def test_dict_2():
    assert len(dict_1) == 1

def test_dict_3():
    try:
        assert dict_1['name1']
    except KeyError:
        pass


set_1 = set('hello')
set_2 = set(set_1)


def test_set_1():
    assert 'l' in set_1

def test_set_2():
    assert set_1 <= set_2


a = ['a', 'b', 'c', 'd']
b = set(a)


def test_set_3():
    assert a != b