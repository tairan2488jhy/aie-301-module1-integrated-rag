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
