# complexity: O(n) ~ O(n^2)
# stability: True
from typing import List


# def insertion_sort(data: List[int]) -> List[int]:
#     len_data = len(data)
#     sorted_data = [data[0]]
#     for i in range(1, len_data):
#         left = 0
#         right = i - 1
#         ind = (left + right) // 2
#         num = data[i]
#         while right - left > 1:
#             if num < sorted_data[ind]:
#                 right = ind
#             else:
#                 left = ind
#             ind = (left + right) // 2
#         if sorted_data[right] < num:
#             ind += 1
#         if num < sorted_data[left]:
#             ind -= 1
#         sorted_data.insert(ind + 1, num)
#     return sorted_data


def insertion_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    data = data.copy()
    for i in range(1, len_data):
        j = 0
        while data[i-1-j] > data[i-j] and i-1-j >= 0:
            data[i-j], data[i-1-j] = data[i-1-j], data[i-j]
            j += 1
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(insertion_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(insertion_sort(data))
    print(insertion_sort(data) == sorted(data))
