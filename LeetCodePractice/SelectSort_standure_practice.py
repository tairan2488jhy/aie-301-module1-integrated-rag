def selection_sort(arr:list[int])->None:
    n = len(arr)
    for i in range(n-1):
        min_val_idx = i
        for j in range(i+1,n):
            if arr[min_val_idx] > arr[j]:
                min_val_idx = j
        if min_val_idx != i:
            arr[min_val_idx],arr[i] = arr[i],arr[min_val_idx]

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    selection_sort(need_sort)
    print("the sorted list -->", need_sort)