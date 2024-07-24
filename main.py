def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


#def divide(a, b):
#    return a / b

def divide(a, b):
   if b == 0:
       raise ValueError('На ноль делить нельзя')
   else:
       return a / b

def div(a, b):
    """Возвращает остаток от деления a на b."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a % b

def check(number):
    return number % 2 == 0

def isPalindrome(s):
    return s == s[::-1]

def sort_list(numbers):
    return sorted(numbers)

def count_vowels(s):
    """Возвращает количество гласных в строке."""
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
