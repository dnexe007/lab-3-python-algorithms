def factorial(n: int) -> int:
    """
    вычисление факториала числа с помощью цикла

    :param n: неотрицательное целое число
    :return: факториал числа
    """
    if n % 1 != 0 or n < 0:
        raise ValueError("number is not integer or number is less than 0")
    current = 1
    for i in range(1, n + 1):
        current *= i
    return current


def factorial_recursive(n: int) -> int:
    """
    вычисление факториала числа с помощью рекурсии

    :param n: неотрицательное целое число
    :return: факториал числа
    """
    if n % 1 != 0 or n < 0:
        raise ValueError("number is not integer or number is less than 0")
    if n == 0 or n == 1:
        return 1
    else:
        return factorial_recursive(n - 1) * n


def fibonacci(n: int) -> int:
    """
    вычисление n-го члена последовательности Фибоначчи
    с помощью формулы

    :param n: индекс - неотрицательное целое число
    :return: элемент последовательности
    """
    if n % 1 != 0 or n < 0:
        raise ValueError("number is not integer or number is less than 0")
    num1 = ((1 + 5 ** 0.5) / 2) ** n
    num2 = ((1 - 5 ** 0.5) / 2) ** n
    return int((num1 - num2) / (5 ** 0.5))


def fibonacci_recursive(n: int) -> int:
    """
    вычисление n-го члена последовательности Фибоначчи
    с помощью рекурсии

    :param n: индекс - неотрицательное целое число
    :return: элемент последовательности
    """
    if n % 1 != 0 or n < 0:
        raise ValueError("number is not integer or number is less than 0")
    if n in [0, 1]:
        return n
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
