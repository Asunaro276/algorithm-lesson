# complexity: O(nlogn) ~ O(n^2)
# stability: True
from typing import List


def sort(data: List[int]) -> List[int]:
    len_data = len(data)
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(sort(data))
    print(sort(data) == sorted(data))
