"""
    This script implements the merge sort algorithm using recursion.

    Then Generates a list of 10 random integers between 1 and 50,
    prints the original list, and prints the sorted list.
"""

import random

def combine(first_list,second_list):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
        first_list (list): A list of comparable elements sorted in ascending order.
        second_list (list): Another list of comparable elements sorted in ascending order.

    Returns:
        list: A merged and sorted list containing all elements from both input lists.
    """
    _list = []
    length = len(first_list)
    length2 = len(second_list)
    i = j = 0
    while i < length and j < length2:
        if first_list[i] < second_list[j]:
            _list.append(first_list[i])
            i += 1
        else:
            _list.append(second_list[j])
            j += 1

    _list += first_list[i:]
    _list += second_list[j:]

    return _list


def merge(_list):
    """
    Recursively sorts a list using the merge sort algorithm.

    Parameters:
        _list (list): A list of comparable elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """

    if len(_list) == 1:
        return _list
    else:
        mid = len(_list) // 2
        right = _list[mid:]
        left = _list[:mid]
        right = merge(right)
        left = merge(left)
        return combine(left, right)

l1 = [random.randint(1,50) for i in range(10)]
print(l1)
print(merge(l1))
