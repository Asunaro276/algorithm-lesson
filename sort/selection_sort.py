# complexity: O(n^2)
# stability: False
from typing import List


def selection_sort(data: List[int]) -> List[int]:
    data = data.copy()
    len_data = len(data)
    for i in range(len_data):
        min_num = float("inf")
        min_ind = -1
        for j in range(i, len_data):
            if data[j] < min_num:
                min_num = data[j]
                min_ind = j
        data.insert(i, data.pop(min_ind))
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(selection_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(selection_sort(data))
    print(selection_sort(data) == sorted(data))
