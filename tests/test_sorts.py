from random import randint
from typing import List, Any, Callable, Tuple, Union
from src.sorts import bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort

# Различные тестовые случаи для алгоритмов сортировки
different: List[List[Any]] = [
    # 1. Пустой список
    [],

    # 2. Один элемент
    [42],

    # 3. Уже отсортированный список
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],

    # 4. Обратно отсортированный список
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

    # 5. Случайные целые числа
    [64, 34, 25, 12, 22, 11, 90, 88, 76, 45],

    # 6. Случайные дробные числа
    [3.14, 2.71, 1.41, 1.61, 0.58, 4.67, 2.30, 3.33, 9.81, 0.01],

    # 7. Все одинаковые элементы
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],

    # 8. С дубликатами
    [3, 7, 3, 1, 4, 7, 2, 1, 9, 3],

    # 9. Большой список
    list(range(100, 0, -1)),  # [100, 99, 98, ..., 1]

    # 10. С отрицательными числами
    [-5, 3, -2, 8, -1, 4, 0, -3, 7, -4],

    # 11. Почти отсортированный
    [1, 2, 3, 5, 4, 6, 7, 9, 8, 10],

    # 12. Строки
    ["banana", "apple", "cherry", "date", "elderberry"],

    # 13. Случайный список с отрицательными числами
    [randint(-50, 50) for _ in range(15)],

    # 14. Список с повторяющимися отрицательными числами
    [-1, -5, -1, 0, -5, 3, -1, 2, -5, 0],

    # 15. Список с большим разбросом значений
    [randint(-1000, 1000) for _ in range(20)]
]

# Тестовые данные для натуральных чисел (подходят для radix sort)
natural_numbers: List[List[int]] = [
    [170, 45, 75, 90, 2, 802, 24, 66, 1, 456],
    [randint(0, 1000) for _ in range(15)],
    [100, 200, 300, 400, 500, 50, 150, 250],
    [0, 1, 10, 100, 1000, 10000, 100000],
    [999, 888, 777, 666, 555, 444, 333, 222, 111, 0]
]

# Тестовые данные для чисел (подходят для counting sort и bucket sort)
numbers: List[List[Union[int, float]]] = [
    [4, -2, 1, -5, 0, 4, -2, 8, 1, -3],
    [randint(-10, 10) for _ in range(20)],
    [1, 1, 1, 2, 2, 3, 3, 3, 3, 4],
    [-1, -1, 0, 0, 1, 1, 1],
    [randint(-5, 5) for _ in range(25)]
]

# Общие тестовые данные для ключей
key_test_cases: List[Tuple[List[Any], Callable]] = [
    # Сортировка по модулю
    ([-5, 3, -2, 8, -1], abs),
    ([3.14, -2.71, 1.41], abs),

    # Сортировка по убыванию (обратный порядок)
    ([5, 2, 8, 1, 9], lambda x: -x),
    ([3.14, 2.71, 1.41], lambda x: -x),

    # Сортировка строк по длине
    (["azazaza", "azaza", "aa", "a"], len),

    # Сортировка по последней цифре для целых чисел
    ([123, 456, 789, 234, 567], lambda x: x % 10),
]


def test_quick() -> None:
    """
    Тестирует алгоритм быстрой сортировки на различных наборах данных
    """
    for i in different:
        assert quick_sort(i) == sorted(i)


def test_quick_with_keys() -> None:
    """
    Тестирует алгоритм быстрой сортировки с использованием ключевых функций
    """
    for data, key_func in key_test_cases:
        assert quick_sort(data, key=key_func) == sorted(data, key=key_func)


def test_bubble() -> None:
    """
    Тестирует алгоритм пузырьковой сортировки на различных наборах данных
    """
    for i in different:
        assert bubble_sort(i) == sorted(i)


def test_bubble_with_keys() -> None:
    """
    Тестирует алгоритм пузырьковой сортировки с использованием ключевых функций
    """
    for data, key_func in key_test_cases:
        assert bubble_sort(data, key=key_func) == sorted(data, key=key_func)


def test_heap() -> None:
    """
    Тестирует алгоритм пирамидальной сортировки на различных наборах данных
    """
    for i in different:
        assert heap_sort(i) == sorted(i)


def test_heap_with_keys() -> None:
    """
    Тестирует алгоритм пирамидальной сортировки с использованием ключевых функций
    """
    for data, key_func in key_test_cases:
        assert heap_sort(data, key=key_func) == sorted(data, key=key_func)


def test_count() -> None:
    """
    Тестирует алгоритм сортировки подсчетом на числовых наборах данных
    """
    for i in numbers:
        # counting_sort работает только с целыми числами, фильтруем float
        if all(isinstance(x, int) for x in i):
            int_list = [x for x in i if isinstance(x, int)]  # Создаем список только из целых чисел
            assert counting_sort(int_list) == sorted(int_list)

def test_bucket() -> None:
    """
    Тестирует алгоритм блочной сортировки на числовых наборах данных
    """
    for i in numbers:
        assert bucket_sort(i) == sorted(i)


def test_radix() -> None:
    """
    Тестирует алгоритм поразрядной сортировки на наборах натуральных чисел
    """
    for i in natural_numbers:
        assert radix_sort(i) == sorted(i)
