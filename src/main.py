from sorts import bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort
from time import time
from typing import List, Callable, Any


def apply_sort(arr: List[Any], func: Callable[[List[Any]], List[Any]]) -> None:
    """
    Применяет функцию сортировки к массиву и выводит результаты

    :param arr: Исходный массив для сортировки
    :param func: Функция сортировки
    """
    print(f"\nSorting with: {func.__name__}")
    t = time()
    sorted_arr = func(arr)
    print(sorted_arr)
    time_delta = time() - t
    print(f"Time: {time_delta * 1000:.2f} ms")


def main() -> None:
    """
    Основная функция программы.
    Запрашивает у пользователя список чисел и тестирует различные алгоритмы сортировки
    """
    nums = list(map(int, input("Enter list of numbers: ").split()))

    # Тестирование различных алгоритмов сортировки
    apply_sort(nums, bubble_sort)
    apply_sort(nums, quick_sort)
    apply_sort(nums, counting_sort)
    apply_sort(nums, radix_sort)
    apply_sort(nums, heap_sort)
    apply_sort(nums, bucket_sort)

    # Сравнение со встроенной сортировкой Python
    apply_sort(nums, sorted)


if __name__ == '__main__':
    main()
