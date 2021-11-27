from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """

    :param arr: a list of numbers / integers in our case
    :return: sorted list

    Runtime Complexity: O(n^2)
    """

    length = len(arr)

    for i in range(1, length):
        current = arr[i]

        while i > 0 and arr[i-1] > current:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = current
    return arr


if __name__ == '__main__':
    print(insertion_sort([32, 6, 9, 1]))
    print(insertion_sort([33, 23, 13, 53, 43, 3]))
