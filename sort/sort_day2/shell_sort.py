from typing import List


def shell_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    gap = len_data // 2
    while gap > 0:
        for i in range(gap, len_data):
            j = 0
            while data[i-j-gap] > data[i-j] and i-j-gap >= 0:
                data[i-j-gap], data[i-j] = data[i-j], data[i-j-gap]
                j += gap
        gap //= 2
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(shell_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(shell_sort(data))
    print(shell_sort(data) == sorted(data))
