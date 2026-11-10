# 逻辑：把数组分成已排序区、未排序区；逐个拿未排序区第一个元素，向前插入到有序区合适位置。
def insertion_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j] # j 向 j+1 位置挪位置 直到 找到当前值的合适位置j
            j -= 1
        arr[j+1] = current # 这里要注意循环要结束，因此j多减了一个1，因此这里赋值给j+1


if __name__ == "__main__":
    need_sort = [23, 7, 31, 22, 5, 106, 9, 3]
    print(f" before sort-->", need_sort)
    insertion_sort(need_sort)
    print(f" sorted-->", sorted)