from chains import array_to_chain
from array_to_set import array_to_sets

def test_array_singleton():
    assert array_to_chain([1]) == [1]

def test_array_1d():
    assert array_to_chain([1, 1, 1]) == [1, 1, 1]

def test_array_long():
    assert array_to_chain([1, 1, 1, 2, 2, 3, 4]) == [1, 2, 3, 4, 1, 2, 1]

def test_array_long_2():
    assert array_to_chain([1, 2, 2, 3, 4, 4, 4]) == [1, 2, 3, 4, 2, 4, 4]

def test_array_to_sets():
    assert array_to_sets([1, 1, 2, 2, 3]) == [{1, 2, 3}, {1, 2}]