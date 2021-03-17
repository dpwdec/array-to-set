from array_to_set import array_to_set

def test_array_singleton():
    assert array_to_set([1]) == [1]

def test_array_1d():
    assert array_to_set([1, 1, 1]) == [1, 1, 1]

def test_array_long():
    assert array_to_set([1, 1, 1, 2, 2, 3, 4]) == [1, 2, 3, 4, 1, 2, 1]