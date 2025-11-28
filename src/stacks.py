from typing import Any, Optional
from queue import Queue


class ListStack:
    """
    Стек на основе списка с поддержкой операции нахождения минимума
    """

    def __init__(self) -> None:
        """Инициализирует пустой стек"""
        self._items: list[Any] = []

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self._items)

    def min(self) -> Any:
        """
        Возвращает минимальный элемент в стеке

        :return: Минимальный элемент в стеке
        :raises IndexError: Если стек пуст
        """
        if len(self._items) == 0:
            raise IndexError('Stack is empty')
        return self._items[-1][1]

    def push(self, val: Any) -> None:
        """
        Добавляет элемент в вершину стека

        :param val: Значение для добавления в стек
        """
        min_val = self._items[-1][1] if self._items else val
        min_val = min(min_val, val)
        self._items.append((val, min_val))

    def pop(self) -> Any:
        """
        Удаляет и возвращает элемент с вершины стека

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if len(self._items) == 0:
            raise IndexError('Stack is empty')
        return self._items.pop()[0]

    def peek(self) -> Any:
        """
        Возвращает элемент с вершины стека без удаления

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if len(self._items) == 0:
            raise IndexError('Stack is empty')
        return self._items[-1][0]


class Node:
    """
    Узел для связанного списка с поддержкой отслеживания минимума
    """

    def __init__(self, val: Any, nxt: Optional['Node'] = None) -> None:
        """
        Инициализирует узел

        :param val: Значение узла
        :param nxt: Ссылка на следующий узел
        """
        self.val: Any = val
        self.nxt: Optional['Node'] = nxt
        self.min: Any
        if nxt is not None:
            self.min = min(nxt.min, val)
        else:
            self.min = val


class LinkedListStack:
    """
    Стек на основе связанного списка с поддержкой операции нахождения минимума
    """

    def __init__(self) -> None:
        """Инициализирует пустой стек"""
        self._top: Optional[Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return self._size

    def min(self) -> Any:
        """
        Возвращает минимальный элемент в стеке

        :return: Минимальный элемент в стеке
        :raises IndexError: Если стек пуст
        """
        if self._top is None:
            raise IndexError('Stack is empty')
        return self._top.min

    def push(self, val: Any) -> None:
        """
        Добавляет элемент в вершину стека

        :param val: Значение для добавления в стек
        """
        node = Node(val, self._top)
        self._top = node
        self._size += 1

    def pop(self) -> Any:
        """
        Удаляет и возвращает элемент с вершины стека

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if self._top is None:
            raise IndexError('Stack is empty')
        last_node = self._top
        self._top = last_node.nxt
        self._size -= 1
        return last_node.val

    def peek(self) -> Any:
        """
        Возвращает элемент с вершины стека без удаления

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if self._top is None:
            raise IndexError('Stack is empty')
        return self._top.val


class QueueStack:
    """
    Стек на основе двух очередей с поддержкой операции нахождения минимума
    """

    def __init__(self) -> None:
        """Инициализирует пустой стек"""
        self._q1: Queue[Any] = Queue()
        self._length: int = 0
        self._min_values: list[Any] = []

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return self._length

    def push(self, val: Any) -> None:
        """
        Добавляет элемент в вершину стека

        :param val: Значение для добавления в стек
        """
        min_val = self._min_values[-1] if self._min_values else val
        min_val = min(min_val, val)
        self._min_values.append(min_val)
        self._q1.put(val)
        self._length += 1

    def min(self) -> Any:
        """
        Возвращает минимальный элемент в стеке

        :return: Минимальный элемент в стеке
        :raises IndexError: Если стек пуст
        """
        if self._length == 0:
            raise IndexError('Stack is empty')
        return self._min_values[-1]

    def pop(self) -> Any:
        """
        Удаляет и возвращает элемент с вершины стека

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if self._length == 0:
            raise IndexError('Stack is empty')

        _q2: Queue[Any] = Queue()
        for i in range(self._length - 1):
            _q2.put(self._q1.get())
        value = self._q1.get()
        self._q1 = _q2
        self._length -= 1
        self._min_values.pop()
        return value

    def peek(self) -> Any:
        """
        Возвращает элемент с вершины стека без удаления

        :return: Элемент с вершины стека
        :raises IndexError: Если стек пуст
        """
        if self._length == 0:
            raise IndexError('Stack is empty')

        _q2: Queue[Any] = Queue()
        value: Any = None
        for i in range(self._length):
            value = self._q1.get()
            _q2.put(value)
        self._q1 = _q2
        return value
