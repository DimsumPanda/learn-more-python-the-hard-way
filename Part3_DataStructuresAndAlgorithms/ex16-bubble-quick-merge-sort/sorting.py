import sys
from pathlib import Path

HERE = Path(__file__).parent
EX14_PATH = HERE.parent.joinpath('ex14-double-linked-lists')

# Add ex14 to current system path
sys.path.append(str(EX14_PATH))

from double_linked_list import DoubleLinkedList

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        is_sorted = True
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                is_sorted = False
            node = node.next
        if is_sorted: break

def count(node):
    count = 0

    while node:
        node = node.next
        count += 1

    return count

def merge_sort(numbers):
    numbers.begin = merge_node(numbers.begin)

    node = numbers.begin
    while node.next:
        node = node.next
    numbers.end = node

def merge_node(start):
    """Sorts a list of numbers using merge sort."""

    # Base condition
    if start.next == None:
        return start

    mid = count(start) // 2

    # scan to the middle
    scanner = start
    for i in range(0, mid-1):
        scanner = scanner.next

    # set mid node right after the scan point
    mid_node = scanner.next
    # break at the mid point
    # We will now have two lists: 
    # 1. start (before mid where scanner ended)
    # and 2. mid_node (mid and the end of numbers)
    scanner.next = None
    mid_node.prev = None

    merged_left = merge_node(start)
    merged_right = merge_node(mid_node)

    return merge(merged_left, merged_right)

def merge(left, right):
    """Performs the merge of two lists."""
    result = None

    if left == None: return right
    if right == None: return left

    if left.value > right.value:
        result = right
        result.next = merge(left, right.next)
    else:
        result = left
        result.next = merge(left.next, right)

    result.next.prev = result
    return result

def quick_sort(numbers):
    quick_sort_list(numbers, 0, count(numbers.begin) - 1)
    return numbers

def quick_sort_list(array, low, high):
    """Sorts a list of numbers using quick sort."""
    if low < high:
        pi = partition(array, low, high)
        quick_sort_list(array, low, pi - 1)
        quick_sort_list(array, pi + 1, high)

def partition(array, low, high):
    pivot = array.begin
    for i in range(0, high):
        pivot = pivot.next

    i = low - 1
    node = array.begin
    for x in range(0, low):
        node = node.next

    for j in range(low, high):
        if node.value <= pivot.value:
            i += 1
            i_node = array.begin
            for x in range(0,i):
                i_node = i_node.next

            print(f"Before Switch: i= {i} j={j} i_node.value={i_node.value}, node.value={node.value}")
            # i_node prev and next will now switch with the j node
            i_node.value , node.value = node.value , i_node.value
            print(f"After Switch: i= {i} j={j} i_node.value={i_node.value}, node.value={node.value}")
        node = node.next
            
        
    i += 1
    i_node = array.begin
    for x in range(0, i):
        i_node = i_node.next
    print(f"Old Pivot Value: i= {i} i_node.value={i_node.value}, pivot.value={pivot.value}")
    i_node.value, pivot.value = pivot.value, i_node.value
    print(f"New Pivot Value: i= {i} i_node.value={i_node.value}, pivot.value={pivot.value}")

    return i
        




    