import random as rand
from typing import List


def quick_sort(arr: List[int]):
    if len(arr) < 2:
        return arr
    pivot = rand.choice(arr)
    smaller = []
    equal = []
    greater = []
    while arr:
        if arr[0] < pivot:
            smaller.append((arr[0]))
            del arr[0]
        elif arr[0] > pivot:
            greater.append(arr[0])
            del arr[0]
        else:
            equal.append(arr[0])
            del arr[0]
    quick_sort(smaller)
    quick_sort(greater)
    while smaller:
        arr.append(smaller[0])
        del smaller[0]
    while equal:
        arr.append(equal[0])
        del equal[0]
    while greater:
        arr.append(greater[0])
        del greater[0]
    return arr


if __name__ == '__main__':
    print(quick_sort([32, 6, 9, 1]))
    print(quick_sort([33, 23, 13, 53, 43, 3]))
    print(quick_sort([2, 5, 3, 22, 22, 22, 65, 21, 0, -2, 34]))
