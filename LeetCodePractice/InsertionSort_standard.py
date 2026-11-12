# 逻辑：把数组分成已排序区、未排序区；逐个拿未排序区第一个元素，向前插入到有序区合适位置。
def insertion_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current: ## 条件放到while中与不放到while中是由差别的，不满足条件，就终止，无需循环到底
            arr[j+1] = arr[j] # j 向 j+1 位置挪位置 直到 找到当前值的合适位置j
            j -= 1
        arr[j+1] = current # 这里要注意循环要结束，因此j多减了一个1，因此这里赋值给j+1


if __name__ == "__main__":
    need_sort = [23, 7, 31, 22, 5, 106, 9, 3]
    print(f" before sort-->", need_sort)
    insertion_sort(need_sort)
    print(f" sorted-->", sorted)


    '''
    ### 代码校验
```python
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
```
输出：
```
the list need to sort--> [23, 5, 31, 22, 7, 106, 9, 3]
the sorted list --> [3, 5, 7, 9, 22, 23, 31, 106]
```
✅ 完全标准的插入排序，**移位而不是两两交换**，这是它和冒泡最大区别。

### 面试要点
1. 思路：`i` 指向无序区第一个元素，`val` 保存待插入值；`j` 向左扫描有序区，比 `val` 大的元素全部后移，直到找到插入位置。
2. 复杂度
    - 最好（已有序）：$\(O(n)\)$，while 循环不执行
    - 平均、最坏（逆序）：$O(n^2)$
3. 空间：$\(O(1)\)$ 原地
4. 稳定排序：相等元素不会挪动，相对顺序保留

### 英文口述（面试直接背）
Insertion sort maintains a sorted prefix on the left. We take the first element from the unsorted part, shift larger elements in the sorted prefix one position to the right, and insert the value into its correct spot. It runs in $O(n^2)$ average and worst case, $\(O(n)\)$ best case for already sorted arrays. It is in-place and stable.

### 三个O(n²)排序一句话区分
- 选择：找最值下标，一轮最多1次交换，**不能提前退出，不稳定**
- 冒泡：相邻对比交换，有序可以提前break，稳定，交换多
- 插入：有序区元素移位，有序时性能最优，稳定

需要我把冒泡、选择、插入、堆排放到同一个py文件里吗？
    '''