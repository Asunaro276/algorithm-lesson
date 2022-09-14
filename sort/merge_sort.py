# complexity: O(nlogn)
# stability: True
from typing import List


def merge_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    if len_data <= 1:
        return data

    mid = len_data // 2
    left = data[:mid]
    right = data[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(merge_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(merge_sort(data))
    print(merge_sort(data) == sorted(data))
