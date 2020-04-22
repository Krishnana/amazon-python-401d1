from reverse_array import __version__
from reverse_array.reverse_array import reverse_array_list

empty_array = []

def test_array_reversal():
    assert __version__ == '0.1.0'  
    expected_array = [3,2,1]
    assert reverse_array_list([1,2,3]) == expected_array

def test_empty_array():
    assert __version__ == '0.1.0'  
    expected_array = []
    assert reverse_array_list([]) == expected_array


def test_large_array():
    assert __version__ == '0.1.0'  
    input_array = []
    for i in range(9999999):
        input_array.append(i)
    expected_array = list(reversed(input_array))
    assert reverse_array_list(input_array) == expected_array