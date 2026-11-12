'''
### 面试要点
- 思路：不断在未排序区间找到最小值，放到未排序区间最前面
- 时间复杂度：$O(n^2)$，最好最坏都是 $O(n^2)$
- 空间：原地 $\\(O(1)\\)$
- 稳定性：**不稳定**（交换会打乱相同元素相对顺序）

英文口述：
Selection sort repeatedly finds the minimum element in the unsorted region and swaps it to the front. It is in-place, $O(n^2)$ time, not stable.
# 在未排序区间找到最小值下标，一轮结束后交换到有序区末尾
 先找最小值下标，**最后一次性交换**
'''

def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    # 每一轮确定第i个位置的元素
    for i in range(n - 1): # python range 的 stop 参数是开区间
        print(f"i-->",i)
        min_idx = i
        # 从i后面找最小值下标
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 交换最小值到i的位置
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    selection_sort(need_sort)
    print("the sorted list -->", need_sort)


'''
```python
def selection_sort(arr:list[int])->None:
    n = len(arr)
    for i in range(n-1):
        min_val_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_val_idx]:
                min_val_idx = j
        if min_val_idx != i:
            arr[min_val_idx],arr[i] = arr[i],arr[min_val_idx]

if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    print("the list need to sort-->", need_sort)
    selection_sort(need_sort)
    print("the sorted list -->", need_sort)
```
运行输出
```
the list need to sort--> [23, 5, 31, 22, 7, 106, 9, 3]
the sorted list --> [3, 5, 7, 9, 22, 23, 31, 106]
```
✅ 代码标准正确

### 核心要点
逻辑：每一轮在未排序区间找到最小值下标，一轮结束后交换到有序区末尾（位置i）
- 时间复杂度：最好/平均/最坏 $O(n^2)$
- 空间复杂度：$\(O(1)\)$ 原地排序
- 稳定性：**不稳定**
- 特点：交换次数极少（最多 n-1 次）；**无法提前终止**，哪怕数组已经有序，内层循环依旧跑完

### 英文口述
Selection sort scans the unsorted region to find the index of the minimum element, then swaps it into place. 
It has $O(n^2)$ time complexity in all cases, uses constant extra space, and is unstable. It minimizes the number of swaps.

'''

