from sorts import bubble_sort, quick_sort, heap_sort, counting_sort, radix_sort, bucket_sort
from time import time
from typing import List, Callable, Any


def apply_sort(arr: List[Any], func: Callable[[List[Any]], List[Any]]) -> None:
    """
    Применяет функцию сортировки к массиву и выводит результаты

    :param arr: Исходный массив для сортировки
    :param func: Функция сортировки
    """
    try:
        print(f"Sorting with: {func.__name__}")
        t = time()
        sorted_arr = func(arr)
        print(sorted_arr)
        time_delta = time() - t
        print(f"Time: {time_delta * 1000:.4f} ms\n")
    except TypeError:
        print("Sorting type error\n")



def main() -> None:
    """
    Основная функция программы.
    Запрашивает у пользователя список чисел и тестирует различные алгоритмы сортировки
    """
    nums = list(map(float, input("Enter list of numbers: ").split()))
    nums = [int(i) if i % 1 == 0 else i for i in nums]
    print("")
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

#3 12 412 324 125 123 582 412 57 123 85 2 1
