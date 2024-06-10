import pytest
from src.strip_punctuation_ru import strip_punctuation_ru

def testirovanie_punctuation():
    assert strip_punctuation_ru("Привет, друг!") == "Привет друг"
    assert strip_punctuation_ru("Как дела?") == "Как дела"
    assert strip_punctuation_ru("Мы дарим вам подарочный сертификат!.") == "Это подарочный сертификат"
    assert strip_punctuation_ru("Тише!") == "Тише"

if __name__ == "__main__":
    pytest.main()
