# examples.py

from heap import MinHeap
from heapsort import heap_sort
import sys


def parse_number(s: str):
    """Parse a string as int if whole, otherwise float."""
    try:
        f = float(s)
        return int(f) if f == int(f) else f
    except ValueError:
        raise ValueError(f"Not a number: {s}")


def fmt(n) -> str:
    """Format a number without trailing .0 for whole floats."""
    if isinstance(n, float) and n == int(n):
        return str(int(n))
    return str(n)


def fmt_list(lst: list) -> str:
    """Format a list of numbers without trailing .0."""
    return "[" + ", ".join(fmt(x) for x in lst) + "]"


def get_user_input() -> list:
    """
    Prompt the user to enter numbers separated by spaces.
    Returns a list of ints/floats.
    """
    raw = input("Enter numbers separated by spaces: ")
    try:
        numbers = [parse_number(x) for x in raw.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        sys.exit(1)
    return numbers


def demo_min_heap(values: list, output_lines: list) -> None:
    output_lines.append("=== MinHeap demo ===")
    output_lines.append(f"Initial values: {fmt_list(values)}")

    heap = MinHeap()
    for v in values:
        heap.push(v)
        output_lines.append(f"After push({fmt(v)}): heap internal state = {fmt_list(heap.to_list())}")

    output_lines.append(f"Peek (min): {fmt(heap.peek())}")
    output_lines.append("Popping all elements:")
    while not heap.is_empty():
        popped = heap.pop()
        output_lines.append(f"pop() -> {fmt(popped)} ; heap = {fmt_list(heap.to_list())}")


def demo_heap_sort(values: list, output_lines: list) -> None:
    output_lines.append("\n=== Heap sort demonstration ===")
    output_lines.append(f"Original list: {fmt_list(values)}")
    sorted_values = heap_sort(values)
    output_lines.append(f"Sorted list  : {fmt_list(sorted_values)}")


def run_test_cases(output_lines: list) -> None:
    """
    Run all demonstration test cases from the report's Demonstration Test Case table.
    """
    test_cases = [
        ("Basic integer",    [5, 3, 8, 1, 2],              [1, 2, 3, 5, 8]),
        ("Already sorted",   [1, 2, 3, 4, 5],              [1, 2, 3, 4, 5]),
        ("Reverse order",    [9, 7, 5, 3, 1],              [1, 3, 5, 7, 9]),
        ("Duplicate",        [4, 1, 4, 2, 1],              [1, 1, 2, 4, 4]),
        ("Mixed int/float",  [3, 2.5, 7, 1.0, 4],          [1.0, 2.5, 3, 4, 7]),
        ("Negative value",   [-5, 3, -1, 7, -3, 0],        [-5, -3, -1, 0, 3, 7]),
    ]

    output_lines.append("\n=== Demonstration Test Cases ===")
    output_lines.append(
        f"{'Test Case':<20} {'Input':<35} {'Expected Output':<30} {'Actual Output':<30} {'Pass'}"
    )
    output_lines.append("-" * 125)

    all_passed = True
    for name, inputs, expected in test_cases:
        result = heap_sort(inputs)
        passed = result == expected
        if not passed:
            all_passed = False
        output_lines.append(
            f"{name:<20} {fmt_list(inputs):<35} {fmt_list(expected):<30} {fmt_list(result):<30} {'OK' if passed else 'FAIL'}"
        )

    output_lines.append("")
    output_lines.append("All test cases passed." if all_passed else "Some test cases FAILED.")


if __name__ == "__main__":
    numbers = get_user_input()
    output_lines = []

    demo_min_heap(numbers, output_lines)
    demo_heap_sort(numbers, output_lines)
    run_test_cases(output_lines)

    # Print to console
    for line in output_lines:
        print(line)

    # Export to text file
    output_file = "output.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(output_lines) + "\n")

    print(f"\nOutput saved to {output_file}")
