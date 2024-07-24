# test_vowels.py
import pytest
from main import count_vowels  # Предполагается, что функция находится в файле main.py

def test_all_vowels():
    # Строка, содержащая только гласные
    assert count_vowels("аеёиоуыэюя") == 10
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    # Строка, не содержащая гласных
    assert count_vowels("клмн") == 0
    assert count_vowels("КЛМН") == 0

def test_mixed_string():
    # Строка, содержащая смешанные буквы и символы
    assert count_vowels("Привет, Мир!") == 3
    assert count_vowels("Питон") == 2
    assert count_vowels("Это просто какое-то предложение") == 13
