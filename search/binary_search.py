from typing import List


def binary_search(data: List[int], value: int) -> int:
    len_data = len(data)
    ind = len_data // 2
    num = data[ind]
    right = len_data - 1
    left = 0
    while num != value:
        if num < value:
            left = ind
        else:
            right = ind
        ind = (right + left) // 2
        num = data[ind]
    return ind


if __name__ == "__main__":
    data = [1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
    value = 2
    print(data, value, binary_search(data, value))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    value = data[0]
    data.sort()
    print(data, value, binary_search(data, value))
