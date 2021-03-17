from recursive_to_set import array_to_sets as recursive_array_to_sets
from array_to_set import array_to_sets as basic_array_to_sets

def test_recursive_singleton():
    assert recursive_array_to_sets([1]) == [{1}]
    assert basic_array_to_sets([1]) == [{1}]

def test_recursive_singular():
    assert recursive_array_to_sets([1, 1, 1]) == [{1}, {1}, {1}]
    assert basic_array_to_sets([1, 1, 1]) == [{1}, {1}, {1}]

def test_recursive_long_basic():
    assert recursive_array_to_sets([1, 1, 1, 2, 2, 3, 4]) == [{1, 2, 3, 4}, {1, 2}, {1}]
    assert basic_array_to_sets([1, 1, 1, 2, 2, 3, 4]) == [{1, 2, 3, 4}, {1, 2}, {1}]

def test_recursive_long_non_zero():
    assert recursive_array_to_sets([1, 2, 2, 3, 4, 4, 4]) == [{1, 2, 3, 4}, {2, 4}, {4}]
    assert basic_array_to_sets([1, 2, 2, 3, 4, 4, 4]) == [{1, 2, 3, 4}, {2, 4}, {4}]