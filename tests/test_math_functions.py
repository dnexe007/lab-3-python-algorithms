import pytest
from src.math_functions import factorial, factorial_recursive, fibonacci, fibonacci_recursive


def test_factorial()-> None:
    """Тесты для факториала"""
    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (10, 3628800)
    ]

    for n, expected in test_cases:
        assert factorial(n) == expected
        assert factorial_recursive(n) == expected


def test_fibonacci() -> None:
    """Тесты для чисел Фибоначчи"""
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (15, 610),
        (20, 6765)
    ]

    for n, expected in test_cases:
        assert fibonacci(n) == expected
        # Для рекурсии тестируем только небольшие значения
        if n <= 15:
            assert fibonacci_recursive(n) == expected


def test_consistency() -> None:
    """Проверка согласованности между разными реализациями"""
    for n in range(0, 11):
        assert factorial(n) == factorial_recursive(n)
        assert fibonacci(n) == fibonacci_recursive(n)


def test_negative_input() -> None:
    """Тестирование обработки отрицательных входных данных"""
    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial_recursive(-1)

    with pytest.raises(ValueError):
        fibonacci(-1)

    with pytest.raises(ValueError):
        fibonacci_recursive(-1)
