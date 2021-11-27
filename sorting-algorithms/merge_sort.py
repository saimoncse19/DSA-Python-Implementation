from typing import List


def merge(left, right) -> List[int]:
    result: List[int] = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]
    if not left:
        result += right
    else:
        result += left
    return result


def merge_sort(getlist: List[int]) -> List[int]:
    """

    :param getlist: list of integers
    :return: sorted list

    Runtime complexity: O(n log n)
    """
    length = len(getlist)
    if length < 2:
        return getlist
    else:
        middle = length//2
        left_part = merge_sort(getlist[0:middle])
        right_part = merge_sort(getlist[middle:])
        return merge(left_part, right_part)


if __name__ == '__main__':
    print(merge_sort([32, 6, 9, 1]))
    print(merge_sort([33, 23, 13, 53, 43, 3]))
    print(merge_sort([2, 5, 3, 22, 65, 21, 0, -2, 34]))
