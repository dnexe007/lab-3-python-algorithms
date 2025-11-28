from pytest import raises
from src.stacks import ListStack, LinkedListStack, QueueStack
from typing import Union


def test() -> None:
    """
    Запускает тестирование всех реализаций стеков
    """
    stack_test(ListStack())
    stack_test(LinkedListStack())
    stack_test(QueueStack())


def stack_test(stack: Union[ListStack, LinkedListStack, QueueStack]) -> None:
    """
    Тестирует базовую функциональность стека

    :param stack: Экземпляр стека для тестирования
    """
    # Тестирование исключений при работе с пустым стеком
    with raises(IndexError):
        stack.pop()
    with raises(IndexError):
        stack.peek()

    # Добавление элементов в стек
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Проверка минимального элемента
    assert stack.min() == 1

    # Тестирование операций pop и peek
    assert stack.pop() == 3
    assert stack.peek() == 2

    # Проверка размера стека
    assert len(stack) == 2
