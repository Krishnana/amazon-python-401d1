from array_shift import __version__
from array_shift.array_shift import insert_shift_array
import pytest

def test_version():
    assert __version__ == '0.1.0'

# Regular scenarios
@pytest.mark.parametrize("test_input1,test_input2,expected",[([],'x',['x']),([1,2],'x',[1,'x',2]),([1,2,3],'x',[1,2,'x',3]),([1,2,3,4],'x',[1,2,'x',3,4])])
def test_insert_shift_array(test_input1,test_input2,expected):
    assert insert_shift_array(test_input1,test_input2) == expected

# Edge cases
@pytest.mark.parametrize("test_input1,test_input2,expected",[([None],None,[None,None]),([],'',['']),([],None,[None])])
def test_insert_empty_array(test_input1,test_input2,expected):
    assert insert_shift_array(test_input1,test_input2) == expected   