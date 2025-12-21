from random import choice
from typing import List, TypeVar, Optional, Callable

T = TypeVar('T')
R = TypeVar('R')


def key_val(var: T, key: Optional[Callable[[T], T | R]] = None) -> T | R:
    """
    применяет функцию key к значению, если она не None, либо
    возвращает значение в исходном виде

    :param var: значение
    :param key: key функция
    :return: значение после применения функции, либо исходное
    """
    if key is None:
        return var
    return key(var)


def bubble_sort(arr: List[T], key: Optional[Callable[[T], R]] = None) -> List[T]:
    """
    пузырьковая сортировка

    :param arr: список для сортировки
    :param key: key функция (опционально)
    :return: отсортированный список
    """
    arr = arr.copy()
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if key_val(arr[j], key) > key_val(arr[j + 1], key):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr: List[T], key: Optional[Callable[[T], R]] = None) -> List[T]:
    """
    быстрая сортировка

    :param arr: список для сортировки
    :param key: key функция (опционально)
    :return: отсортированный список
    """
    arr = arr.copy()
    if not arr:
        return arr

    start = key_val(choice(arr), key)
    higher: List[T] = []
    equal: List[T] = []
    lower: List[T] = []

    for item in arr:
        item_key = key_val(item, key)
        if item_key > start:
            higher.append(item)
        elif item_key == start:
            equal.append(item)
        else:
            lower.append(item)

    return quick_sort(lower, key) + equal + quick_sort(higher, key)


def heapify(arr: List[T], index: int, length: int, key: Optional[Callable[[T], R]] = None) -> None:
    """
    операция heapify для построения max-heap

    :param arr: список-куча
    :param index: индекс элемента
    :param length: размер кучи
    :param key: key функция (опционально)
    """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and key_val(arr[left], key) > key_val(arr[largest], key):
        largest = left

    if right < length and key_val(arr[right], key) > key_val(arr[largest], key):
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, length, key)


def heap_sort(arr: List[T], key: Optional[Callable[[T], R]] = None) -> List[T]:
    """
    пирамидальная сортировка

    :param arr: список для сортировки
    :param key: key функция (опционально)
    :return: отсортированный список
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i, key)

    return arr


def bucket_sort(arr: List[int | float], key: Optional[Callable[[int | float], int | float]] = None) -> List[int | float]:
    """
    корзинная сортировка

    :param arr: список для сортировки
    :param key: key функция (опционально)
    :return: отсортированный список
    """
    for i in arr:
        if not isinstance(i, (int, float)):
            raise TypeError("bucket sort only works with numbers")

    arr = arr.copy()
    if not arr:
        return arr

    buckets: List[List[int | float]] = [[] for _ in range(10)]
    min_element = min(key_val(item, key) for item in arr)
    max_element = max(key_val(item, key) for item in arr)

    if min_element == max_element:
        return arr

    delta = (max_element - min_element) / 10

    for item in arr:
        index = int((key_val(item, key) - min_element) / delta)
        index = min(index, 9)
        buckets[index].append(item)

    arr.clear()
    for bucket in buckets:
        if bucket:
            arr.extend(heap_sort(bucket, key))

    return arr


def counting_sort(arr: List[int]) -> List[int]:
    """
    сортировка подсчетом для целых чисел

    :param arr: список для сортировки
    :return: отсортированный список
    """
    for i in arr:
        if not isinstance(i, int):
            raise TypeError("counting sort only works with integer numbers")

    arr = arr.copy()
    if not arr:
        return arr

    min_element = min(arr)
    max_element = max(arr)

    count_list = [0] * (max_element - min_element + 1)

    for num in arr:
        count_list[num - min_element] += 1

    arr.clear()
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            arr.append(min_element + i)

    return arr

def get_digit(num: int, digit: int) -> int:
    """
    получение цифры целого неотрицательного
    десятичного числа по индексу,
    где 0 - последняя цифра

    :param num: целое десятичное число
    :param digit: индекс цифры
    :return: цифра
    """
    return (num // (10 ** digit)) % 10


def radix_sort(arr: List[int]) -> List[int]:
    """
    поразрядная сортировка целых неотрицательных чисел

    :param arr: список для сортировки
    :return: отсортированный список
    """
    arr = arr.copy()
    if not arr:
        return arr

    for i in arr:
        if not isinstance(i, int) or i < 0:
            raise TypeError("counting sort only works with integer non-negative numbers")

    max_digits = len(str(max(arr)))

    for digit in range(max_digits):
        buckets: List[List[int]] = [[] for _ in range(10)]

        for num in arr:
            current_digit = get_digit(num, digit)
            buckets[current_digit].append(num)

        arr.clear()
        for bucket in buckets:
            arr.extend(bucket)

    return arr
