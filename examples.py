# examples.py

from heap import MinHeap
from heapsort import heap_sort


def demo_min_heap() -> None:
    print("=== MinHeap demo ===")
    values = [5, 3, 8, 1, 2]
    print("Initial values:", values)

    heap = MinHeap()
    for v in values:
        heap.push(v)
        print(f"After push({v}): heap internal state = {heap.to_list()}")

    print("Peek (min):", heap.peek())

    print("Popping all elements:")
    while not heap.is_empty():
        print("pop() ->", heap.pop(), "; heap =", heap.to_list())


def demo_heap_sort() -> None:
    print("\n=== Heap sort demo ===")
    values = [9, 4, 7, 1, 3, 6, 5]
    print("Original list:", values)
    sorted_values = heap_sort(values)
    print("Sorted list  :", sorted_values)
    print("Original list (unchanged):", values)


if __name__ == "__main__":
    demo_min_heap()
    demo_heap_sort()
