from typing import List


def insertion_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    data = data.copy()
    for i in range(len_data-1):
        j = 0
        while data[i-j] > data[i+1-j] and i-j >= 0:
            data[i-j], data[i+1-j] = data[i+1-j], data[i-j]
            j += 1
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(insertion_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(insertion_sort(data))
    print(insertion_sort(data) == sorted(data))
