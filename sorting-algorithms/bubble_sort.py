from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    length = len(arr) - 1
    for i in range(length):
        for j in range(length - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    print(bubble_sort([32, 6, 9, 1]))
    print(bubble_sort([33, 23, 13, 53, 43, 3]))