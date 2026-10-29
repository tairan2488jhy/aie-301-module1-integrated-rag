

def select_sort_practices_v1(need_sort: list[int])->list[int]:
    arr = need_sort.copy()

    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j]>val:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = val
    return arr



















# 详细排序过程显示版本
def insertion_sort(need_sort: list[int])-> list[int]:
    arr = need_sort.copy()
    for i in range (1,len(arr)):
        val = arr[i]
        j = i - 1
        print(f"i--> ",i,"and arr[i]-->",arr[i], "and val --> ",val)
        print(f"j--> ",j, "and arr[j]-->",arr[j])
        print(f"arr before compare-->",arr)
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
            print(f"arr after compare-->", arr)
        arr[j+1] = val
        print(f"arr after for loop i -->",i ,"; arr->", arr)
    return arr


if __name__ == "__main__":
    # need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    need_sort = [5, 7, 1, 12, 31, 77, 9, 23, 22, 106, 18, 3]
    # need_sort = [5, 7, 7, 5]
    # need_sort = [5, 7, 3]
    print(f" before sort-->", need_sort)
    sorted = insertion_sort_practices_v1(need_sort)
    print(f"sorted-->", sorted)