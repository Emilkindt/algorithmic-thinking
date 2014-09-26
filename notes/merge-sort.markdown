# Sort problem

<br>

- Bubble Sort `O(n) ~ O(n^2)` [stable]
- Quick Sort `O(nlogn) ~ O(n^2)` [unstable]
- Insert Sort `O(n^2)` [stable]
- Shell Sort `O(n^2)` [unstable]
- Selection Sort `O(n^2)` [unstable]
- Merge Sort `O(nlogn)` [stable]
- Heap Sort `O(nlogn)` [unstable]

## Merge Sort

归并排序是一个非常优雅的排序算法, 它将多个有序列表合并成一个新的有序列表,
即把待排序序列分为若干个有序的子序列, 再把有序的子序列合并成为整体有序的序列.
该算法是 "Divide and Conquer" 方法的一个典型应用, 其平均时间复杂度为 `O(nlogn)`,
所需辅助空间 `O(n)`. 归并排序是一个稳定的排序算法.

```
使用归并排序算法对长度为 n 的列表 L 进行排序

L = [7, 20, 5, 13, 100, 1, 19, 4]


step 1 - 将 L 拆分为多个子序列

[7, 20, 5, 13, 100, 1, 19, 4]
              ↓
[7, 20, 5, 13], [100, 1, 19, 4]
      ↓                 ↓
[7, 20], [5, 13], [100, 1], [19, 4]
   ↓        ↓         ↓        ↓
[7], [20], [5], [13], [100], [1], [19], [4]


当最终将序列 L 拆分为只有单个元素的序列时,
我们可以认为, 每个子序列就完成了排序(因为只有一个元素)

step 2 - 合并排序后的子序列
依次比较单元素序列, 假设我们要按升序排列

首先, 对于单元素序列来说:
因为 [7] < [20], 所以合并为 [7, 20]; 同理因为 [100] > [1], 所以合并为 [1, 100]

之后对于多元素序列:
A[7, 20], B[5, 13] → C[ , , , ]
    ↑        ↑         ↑
    i        j         k

当指针处于 i 和 j 时, 比较元素的大小, 将较小值添加给 k 位置;
因为选择了 B 中的元素, 则指针 j 右移, 指针 i 不变, 指针 k 右移;
同理当第二次比较时, 因为 7 < 13, 所以选择了 A 中的元素, 指针 i 右移而 j 不变.
最后结果 C 为: [5, 7, 13, 20]
反复这个过程最终便得到原始序列 L 的排序结果: [1, 4, 5, 7, 13, 19, 20, 100].
```

__为何归并排序的时间复杂度为__ `O(nlogn)`?

首先, 从算法描述中很容易就能想到利用__递归__可以非常简洁的实现该算法.
假设我们实现了函数 `mergeSort(L[0, ..., n-1])`.
则它执行的操作为:

1. `mergeSort(L1[0, ..., (n-1)/2])`
2. `mergeSort(L2[(n-1)/2+1, ..., n-1])`
3. `mergeSort(L1, L2)`

因为我们明确知道最终排序结果将比较 `n` 个元素, 所以最终的合并操作的复杂度为 `O(n)`;
而如何知道递归调用的前两个操作的时间复杂度?
我们可以认为, 设 `mergeSort(n)` 的时间复杂度 `T(n)`, 则 `mergeSort(n/2)` 为 `T(n/2)`.

综上我们得到 `T(n) = 2*T(n/2) + O(n)`, 对于递归函数, 我们称这种表达形式为 "Recurrence".
对于该表达式, 我们可以进行简单的计算有:

```
T(n) = 2*T(n/2) + O(n)
     = 2*(2*T(n/4) + O(n/2)) + O(n)
     = ...
```

我们知道, 最终子序列长度为 `1` 时, 则递归终止,
于是我们知道最终有常量 `T(1) = O(1)`, 称为 "base case".
所以就得到递归公式 "Recurrence Formula":

- `T(n) = 2*T(n/2) + O(n)`
- `T(1) = O(1)`

至此, 我们虽然明确了 `mergeSort` 的机制, 但是这并不足以转化为精确的函数表达.
我们的目的是要证明其时间复杂度为 `O(nlogn)`,
那么如何将递归公式转化为明确的 Big O 描述?

### Master Theorem

```
- T(n) = aT(n/b) + f(n)
- T(1) = c
- a ≥ 1, b ≥ 2, c > 0

if f(n) = O(n^d), d ≥ 0:

            - O(n^d); if a < b^d
    T(n) =  - O(n^d * log n); if a = b^d
            - O(n^(log b)^a); if a > b^d
```

根据定理我们回到递归公式, 则有:

- `a = 2`
- `b = 2`
- `d = 1`

因为 `a = b^d`, 所以 `T(n) = O(nlogn)`.

> Divide and conquer algorithm don't have to be implemented recursively.
> You can still implement it in iteration,
> but recursion is the natural way to implement a divide and conquer algorithm.
