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


    '''
    ```python
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
```
输出：
```
the list need to sort--> [23, 5, 31, 22, 7, 106, 9, 3]
the sorted list --> [3, 5, 7, 9, 22, 23, 31, 106]
```
✅ 优化版冒泡排序，正确。

### 要点
原理：相邻元素比较，逆序则交换；每一轮把未排序区间最大值“冒泡”到尾部。`swap` 标记用来提前退出：本轮没有交换，说明数组已经有序。
- 最坏、平均：$O(n^2)$
- 最好（已有序）：$\(O(n)\)$
- 空间：$\(O(1)\)$
- 稳定性：**稳定排序**

### 英文口述
Bubble sort compares adjacent elements and swaps them if out of order. The largest value bubbles to the end each pass. The swap flag allows early termination when the array becomes sorted. It is stable and runs in $O(n^2)$ average and worst time, $\(O(n)\)$ best time.

需要我把插入排序也贴过来，三个放一起方便一次性复习吗？
    '''