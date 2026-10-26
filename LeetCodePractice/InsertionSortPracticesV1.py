

def insertion_sort_from_min(need_sort: list[int]) -> list[int]:
    arr = need_sort.copy()
    idx = 1
    while idx < len(arr):
        idx2 = idx - 1
        current = arr[idx]
        while idx2 >= 0 and arr[idx2] > current:
            arr[idx2 + 1] = arr[idx2]
            idx2 -= 1

        arr[idx2 + 1] = current
        idx += 1

    return arr

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    print(f" before sort-->", need_sort)
    # sorted = insertion_sort_from_min(need_sort)
    sorted = insertion_sort_from_min(need_sort)
    print(f"sorted-->", sorted)