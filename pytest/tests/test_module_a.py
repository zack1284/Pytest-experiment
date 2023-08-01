import sys
import pytest

sys.path.append('C:/Users/user/Desktop/pytest/src/..')
#sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 輸出 C:\Users\user\Desktop\pytest\tests\..
from src.module_a import square,concat


def test_square():
    assert square(8) == 64


def test_concat():
    str_1 = "Hello "
    str_2 = "World"
    assert concat(str_1=str_1, str_2=str_2) == "Hello World"


def test_concat_failed():
    str_1 = 555 # Error Type
    str_2 = 666 # Error Type
    with pytest.raises(TypeError, match="錯誤型態"):
        concat(str_1=str_1, str_2=str_2)

