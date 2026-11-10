# 逻辑：相邻两两比较，逆序就交换，大数慢慢 “浮” 到尾部；swapped 是提前终止优化。
def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n - 1):# python range 方法的 stop 参数是开区间 ;之所以是n-1，是因为n个数比较一趟，需要n-1轮
        print(f"i-->", i)
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    bubble_sort(need_sort)
    print("the sorted list -->", need_sort)