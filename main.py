import pytest

dict_1 = {'name': 'surname'}


def test_dict_1():
    assert dict_1['name']

def test_dict_2():
    assert len(dict_1) == 1