import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" 23455", "23455"),
    (" Hello world", "Hello world"),
    (" python2", "python2"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Tutu", "T", "utu"),
    ("Ruri", "i", "Rur"),
    ("python2", "2", "python"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Tutu", "T"),
    ("Ruri No", "i"),
    ("python2", "2"),
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains(input_str, expected)


#negative

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])

def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Tu tu", "", "Tu tu"),
    ("", "i", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.delete_symbol(input_str, symbol)
    else:
        assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Tutu", ""),
    ("154875214 A23", ""),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str, expected)