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

result= -1_000_000_000 % 3
print(result)