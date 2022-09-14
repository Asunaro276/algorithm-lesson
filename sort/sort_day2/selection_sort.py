from typing import List


def selection_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    data = data.copy()
    for i in range(len_data):
        min_num = float("inf")
        min_ind = -1
        for j in range(i, len_data):
            if data[j] < min_num:
                min_num = data[j]
                min_ind = j
        data[i], data[min_ind] = data[min_ind], data[i]
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(selection_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(selection_sort(data))
    print(selection_sort(data) == sorted(data))
