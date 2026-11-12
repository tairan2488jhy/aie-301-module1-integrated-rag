
def bubble_sort(arr:list[int])->None:
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(1,n-i):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                swap = True
        if not swap:
            break


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    bubble_sort(need_sort)
    print("the sorted list -->", need_sort)