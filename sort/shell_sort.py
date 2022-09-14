# complexity: O(nlogn) ~ O(n^2)
# stability: True
from typing import List


def shell_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    data = data.copy()
    gap = len_data
    gap = len_data // 2
    while gap > 0:
        for i in range(gap, len_data):
            tmp = data[i]
            j = 0
            while data[i-gap-j] > tmp and i - gap - j >= 0:
                data[i-gap-j], data[i-j] = data[i-j], data[i-gap-j]
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
