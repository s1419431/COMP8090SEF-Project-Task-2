# heap.py

from typing import List, Optional, TypeVar, Generic

T = TypeVar("T")


class MinHeap(Generic[T]):
    """
    A simple array-based min-heap implementation.

    Invariant:
        - For every index i > 0, parent index p = (i - 1) // 2
          satisfies data[p] <= data[i].
    """

    def __init__(self, items: Optional[List[T]] = None) -> None:
        """
        Initialize the heap.

        :param items: optional initial items. If provided, they are heapified
                      in O(n) time.
        """
        if items is None:
            self._data: List[T] = []
        else:
            self._data = list(items)
            self._heapify()

    def _heapify(self) -> None:
        """
        Build the heap in-place from an arbitrary list in O(n) time
        by sifting down from the last non-leaf node.
        """
        n = len(self._data)
        # Start from last internal node down to root.
        for i in reversed(range(n // 2)):
            self._sift_down(i)

    def _sift_up(self, index: int) -> None:
        """
        Move the element at 'index' up until heap property is restored.
        """
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] < self._data[parent]:
                self._data[index], self._data[parent] = (
                    self._data[parent],
                    self._data[index],
                )
                index = parent
            else:
                break

    def _sift_down(self, index: int) -> None:
        """
        Move the element at 'index' down until heap property is restored.
        """
        n = len(self._data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest == index:
                break

            self._data[index], self._data[smallest] = (
                self._data[smallest],
                self._data[index],
            )
            index = smallest

    def push(self, value: T) -> None:
        """
        Insert a new value into the heap in O(log n) time.
        """
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        """
        Remove and return the minimum value (root) from the heap.

        :raises IndexError: if the heap is empty.
        """
        if not self._data:
            raise IndexError("pop from empty heap")

        min_value = self._data[0]
        last_value = self._data.pop()

        if self._data:
            self._data[0] = last_value
            self._sift_down(0)

        return min_value

    def peek(self) -> T:
        """
        Return the minimum value without removing it.

        :raises IndexError: if the heap is empty.
        """
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def is_empty(self) -> bool:
        """
        Check whether the heap is empty.
        """
        return len(self._data) == 0

    def __len__(self) -> int:
        """
        Number of elements in the heap.
        """
        return len(self._data)

    def to_list(self) -> List[T]:
        """
        Return a shallow copy of the internal list.
        This does NOT guarantee heap order if you modify it externally.
        """
        return list(self._data)
