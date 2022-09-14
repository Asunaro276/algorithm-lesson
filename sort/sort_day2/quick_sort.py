from typing import List


def partition(data: List[int], low: int, high: int) -> int:
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    i += 1
    data[i], data[high] = data[high], data[i]
    return i


def quick_sort(data: List[int]) -> List[int]:
    len_data = len(data)

    def _quick_sort(data: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(data, low, high)
            _quick_sort(data, low, partition_index - 1)
            _quick_sort(data, partition_index + 1, high)
    _quick_sort(data, 0, len_data - 1)
    return data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(quick_sort(data))
    import random
    data = [random.randint(0, 10000) for _ in range(10)]
    print(quick_sort(data))
    print(quick_sort(data) == sorted(data))
