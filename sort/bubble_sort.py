# complexity: O(n^2)
# stability: True
from typing import List


# def bubble_sort(data: List[int]) -> List[int]:
#     len_data = len(data)
#     for i in range(len_data):
#         for j in range(len_data - 1):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#     return data

# improved version
def bubble_sort(data: List[int]) -> List[int]:
    data = data.copy()
    len_data = len(data)
    for i in range(len_data):
        change_flag = False
        for j in range(len_data - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                change_flag = True
        if not change_flag:
            break
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(bubble_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(bubble_sort(data))
    print(data)
    print(bubble_sort(data) == sorted(data))
