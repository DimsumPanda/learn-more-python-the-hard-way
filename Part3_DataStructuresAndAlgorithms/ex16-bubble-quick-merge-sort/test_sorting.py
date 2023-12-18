import sys
from pathlib import Path

HERE = Path(__file__).parent
EX14_PATH = HERE.parent.joinpath('ex14-double-linked-lists')

# Add ex14 to current system path
sys.path.append(str(EX14_PATH))

from double_linked_list import DoubleLinkedList
import sorting
from random import randint

max_numbers = 5

# Creates a random double-linked list of numbers
def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers

# checks through a list to determine if the line is sorted
def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            print(f"node.value > node.next.value: {node.value} > node.next.value")
            return False
        else:
            node = node.next

    return True

def test_bubble_sort():
    numbers = random_list(max_numbers)
    numbers.dump("Bubble Sort Numbers (unsorted):")
    sorting.bubble_sort(numbers)
    numbers.dump("Bubble Sort Numbers (sorted):")
    assert is_sorted(numbers)

def test_merge_sort():
    numbers = random_list(max_numbers)
    numbers.dump("Numbers (unsorted):")

    sorting.merge_sort(numbers)
    numbers.dump("Numbers (sorted):")

    assert is_sorted(numbers)

def test_quick_sort():
    numbers = DoubleLinkedList()
    numbers.push(2)
    numbers.push(5)
    numbers.push(3)
    numbers.push(1)
    numbers.push(8)
    numbers.push(7)
    numbers.push(6)
    numbers.push(4)

    # numbers = random_list(max_numbers)
    numbers.dump("Numbers (unsorted):")

    sorting.quick_sort(numbers)
    numbers.dump("Numbers (sorted):")

    assert is_sorted(numbers)