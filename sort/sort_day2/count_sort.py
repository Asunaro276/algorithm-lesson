from typing import List


def count_sort(data: List[int]) -> List[int]:
    len_data = len(data)
    max_num = max(data)
    count_dict = {i: 0 for i in range(max_num+1)}
    sorted_data = [0] * len_data
    for num in data:
        count_dict[num] += 1
    for i in range(1, max_num+1):
        count_dict[i] += count_dict[i-1]
    for num in data:
        count_dict[num] -= 1
        sorted_data[count_dict[num]] = num
    return sorted_data


if __name__ == "__main__":
    data = [1, 10, 4, 5, 2, 8, 6]
    print(count_sort(data))
    import random
    data = [random.randint(0, 100) for _ in range(10)]
    print(count_sort(data))
    print(count_sort(data) == sorted(data))
