from array_to_set import array_to_set

@pytest.mark.parametrize([1, 2, 3, 4])
def test_array(input):
    assert array_to_set(input) == 1