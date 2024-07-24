#проверка с помощью unittest

import unittest
from main import count_vowels  # Предполагается, что функция находится в файле main.py

class TestCountVowels(unittest.TestCase):

    def test_all_vowels(self):
        # Строка, содержащая только гласные
        self.assertEqual(count_vowels("аеёиоуыэюя"), 10)
        self.assertEqual(count_vowels("АЕЁИОУЫЭЮЯ"), 10)

    def test_no_vowels(self):
        # Строка, не содержащая гласных
        self.assertEqual(count_vowels("клмн"), 0)
        self.assertEqual(count_vowels("КЛМН"), 0)

    def test_mixed_string(self):
        # Строка, содержащая смешанные буквы и символы
        self.assertEqual(count_vowels("Привет, Мир!"), 3)
        self.assertEqual(count_vowels("Питон"), 2)
        self.assertEqual(count_vowels("Это просто какое-то предложение"), 13)

if __name__ == '__main__':
    unittest.main()
