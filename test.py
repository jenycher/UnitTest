import unittest
from main import add, subtract, multiply, divide, div
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_positive_numbers_div(self):
        self.assertEqual(div(10, 3), 1)
        self.assertEqual(div(25, 5), 0)
        self.assertEqual(div(9, 2), 1)

    def test_negative_numbers_div(self):
        self.assertEqual(div(-10, 3), -1)
        self.assertEqual(div(10, -3), 1)
        self.assertEqual(div(-10, -3), -1)

    def test_zero_div(self):
        self.assertEqual(div(0, 5), 0)
        self.assertEqual(div(0, -5), 0)

    def test_div_by_one(self):
        self.assertEqual(div(10, 1), 0)
        self.assertEqual(div(-10, 1), 0)

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            div(10, 0)

    def test_large_numbers_div(self):
        self.assertEqual(div(1_000_000_000, 3), 1)
        self.assertEqual(div(-1_000_000_000, 3), -1)

if __name__ == '__main__':
    unittest.main()