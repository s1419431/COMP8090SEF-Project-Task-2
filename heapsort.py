# heapsort.py

from typing import List, TypeVar
from heap import MinHeap

T = TypeVar("T")


def heap_sort(values: List[T]) -> List[T]:
    """
    Heap sort using MinHeap.

    Time complexity:
        - Building the heap: O(n)
        - n extractions: O(n log n)
        - Overall: O(n log n)

    :param values: list of comparable elements.
    :return: new list containing the elements in non-decreasing order.
    """
    heap = MinHeap(values)
    sorted_values: List[T] = []

    while not heap.is_empty():
        sorted_values.append(heap.pop())

    return sorted_values
