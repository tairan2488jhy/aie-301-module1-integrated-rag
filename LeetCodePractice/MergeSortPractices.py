
def merge_sort(need_sort: list[int])->list[int]:
    arr = need_sort.copy()

    if len(arr) <= 1:
        return arr

    middle_pos = len(arr)//2
    pre_arr = arr[:middle_pos]
    sub_arr = arr[middle_pos:]

    pre_arr = merge_sort(pre_arr)
    sub_arr = merge_sort(sub_arr)

    #merge
    if pre_arr[-1] <= sub_arr[0]:
        return pre_arr + sub_arr
    if sub_arr[-1] <= pre_arr[0]:
        return sub_arr + pre_arr

    i = j = 0
    new_arr: list[int] = []
    while i < len(pre_arr) and j < len(sub_arr):
        if pre_arr[i] <= sub_arr[j]:
            new_arr.append(pre_arr[i])
            i += 1
        else:
            new_arr.append(sub_arr[j])
            j += 1

    new_arr += pre_arr[i:] + sub_arr[j:]

    return new_arr


if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    # need_sort = [5, 7, 1, 12, 31, 77, 9, 5]
    # need_sort = [5, 7, 7, 5]
    print(f" before sort-->", need_sort)
    sorted = merge_sort(need_sort)
    print(f"sorted-->", sorted)
