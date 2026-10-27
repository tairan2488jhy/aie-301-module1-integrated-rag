
'''

Perfect summary, this is the standard definition of quicksort.
总结得很好，这就是快速排序的标准定义。

### Key interview highlights (中英对照)
1. The pivot lands on its final sorted position after one partition.
一趟分区结束后，pivot 落在它最终的正确下标上，不再移动。
This is the biggest difference from merge sort.
这是它和归并排序最核心的区别。

2. Partition depends on value comparison, not index split.
分区依据元素大小对比，不是像归并那样按下标固定对半切。
So left and right subarrays can be wildly unbalanced.
所以左右子数组长度可能极度不均衡。

3. Base case: subarray length 0 or 1, already sorted, stop recursion.
基线条件：子数组长度0或者1，本身有序，终止递归。

4. Stability note: standard quicksort is **unstable**.
稳定性说明：标准快排是**不稳定排序**。
Reason: swap across elements can break the relative order of equal items.
原因：跨元素交换会打乱等值元素原本的先后顺序。

5. Time complexity
- Best / average: $O(n\\log n)$，when pivot splits evenly
最好/平均：$O(n\\log n)$，pivot划分均衡
- Worst: $O(n^2)$，when pivot is always min or max (sorted input with bad pivot choice)
最坏：$O(n^2)$，每次选到最大或最小值（有序数组+不好的pivot策略）

### One-line interview script based on your text
Quicksort picks a pivot, runs partition to place pivot into its final sorted position, then recursively sorts left and right subarrays
until subarrays are empty or single-element.
快速排序选取一个基准，执行分区把基准放到最终有序位置，然后递归排序左右子序列，直到子序列为空或者只有单个元素。

### Small detail correction for your wording
You wrote: all elements ≤ pivot on left, all ≥ pivot on right.
你原文写：小于等于放左边，大于等于放右边。
> Common safer convention in coding:
> left: `< pivot`; right: `>= pivot`  OR  left: `<= pivot`; right: `> pivot`
> 编码更常用规范：左边 < pivot、右边 >= pivot，或者左边 <= pivot、右边 > pivot
> If you write both sides `<=` and `>=`, equal values can go to both sides and may cause confusion in implementation.
> 如果两边同时写 ≤ 和 ≥，等值元素两边都可以放，写代码时容易逻辑混乱。

'''


def quick_sort(need_sort: list[int])->list[int]:
    arr = need_sort.copy()
    # select the first element as the pivot
    if len(arr) > 0:
        pivot = arr[0]

        left_arr:list[int] = []
        right_arr:list[int] = []
        idx = 1
        while idx < len(arr):
            if arr[idx] <= pivot:
                left_arr.append(arr[idx])
            else:
                right_arr.append(arr[idx])

            idx += 1

        left_sorted_arr = quick_sort(left_arr)
        right_sorted_arr = quick_sort(right_arr)

        return left_sorted_arr+ [pivot] + (right_sorted_arr)

    return arr




if __name__ == "__main__":
    need_sort = [23, 5, 31, 22, 7, 106, 9, 3]
    # need_sort = [106, 31, 23, 22, 9, 77, 5, 3]
    # need_sort = [5, 7, 1, 12, 31, 77, 9, 5]
    # need_sort = [5, 7, 7, 5]
    # need_sort = [5, 7, 3]
    print(f" before sort-->", need_sort)
    sorted = quick_sort(need_sort)
    print(f"sorted-->", sorted)