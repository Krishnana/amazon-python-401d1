from binary_search import __version__
from binary_search.binary_search import binary_search
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize("test_input1,test_input2,expected",[([1,2,3,4],1,0),([1,2,3,4],4,3),([1,2,3,4],2,1),([1,2,3,4],0,-1)])
def test_binay_search(test_input1,test_input2,expected):
    assert binary_search(test_input1,test_input2) == expected

def test_binay_search_large_array():
    test_input1 = [None] * 9999
    for i in range(9999):
        test_input1[i] = i
    test_input2 = 700
    assert binary_search(test_input1,test_input2) == 700