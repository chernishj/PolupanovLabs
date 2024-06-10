import pytest
from palidrome_code import is_palindrome

def test_palindrome():
    assert is_palindrome("око") == True
    assert is_palindrome("казак") == True
    assert is_palindrome("кабаре") == False
    assert is_palindrome("дед") == True
    assert is_palindrome("молоко") == False

if __name__ == "__main__":
    pytest.main()
