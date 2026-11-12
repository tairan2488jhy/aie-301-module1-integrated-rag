def insertion_sort(arr:list[int])->None:
    n = len(arr)
    for i in range(1,n):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    insertion_sort(need_sort)
    print("the sorted list -->", need_sort)
