# Module 2 - Algorithmic efficiency and BFS

<br>

### Orders of growth

随着 input size 不断增加, 算法的运行时间增长曲线会是什么样的?
通常我们通过对比 `input size ← n` 和 `running times ← O(?)` 来描述一个算法的复杂度.
常见的有 `O(n)`, `O(log n)`, `O(n^2)`, `O(2^n)`.

比如对于一个复杂度为 `O(n^2)` 的算法:

- `input size = 2` - `running times = 4`
- `input size = 4` - `running times = 16`
- `input size = 16` - `running times = 256`
- `input size = 256` - `running times = 65536`

<br>

### Asymptotic

#### 如何设定上限?

设有 `f(n) = 1000 + 17n + 2n^2`;
我们设另外一个函数 `g(n)` 和两个常量 `c (c > 0)`, `n0 (n0 ≥ 0)`.
它们满足 `f(n) ≤ c·g(n); any(n) ≥ n0`.

表示为: `f(n) = O(g(n))`

#### 如何设定下限?

和上限设定类似, 同样设有 `g(n)`, `c (c > 0)`, `n0 (n0 ≥ 0)`.
它们满足 `f(n) ≥ c·g(n); any(n) ≥ n0`.

表示为: `f(n) = Ω(g(n))`

#### 通过两个时间常量来定义上下限

我们可以同时定义两个常量 `c1` 和 `c2`. 使得 `g(n)` 可以同时满足
`f(n) ≤ c1·g(n); any(n) ≥ n0`, `f(n) ≥ c2·g(n); any(n) ≥ n0`.

表示为: `f(n) = θ(g(n))`

通常对于算法的时间复杂度分析主要是关于上限 `O`.

<br>

### Illustrating "Big O"

结合上边的假设, 有:

- `f(n) = 1000 + 17n + 2n^2`
- `if n ≥ 1: 1000 + 17n + 2n^2 ≤ 1000n^2 + 17n^2 + 2n^2`
- `f(n) ≤ 1019·n^2`

对比之前的定义, 我们设 `n0 = 1`, `c = 1019`, 则它们满足 `f(n) ≥ c·g(n); any(n) ≥ n0`,
于是就有 `g(n) = n^2`.

<br>

### Illustrating BFS

假设有一无向图 `g(V,E)`, 求任意两点之间的距离 `d(i, j)`.

- 对于任意节点 `i` 到任意节点 `j` 的距离为 `dj`, 即 `di = 0`.
- 于是首先我们可以知道对于所有与 `i` 相邻的节点 `dj = 1`.
- 有了所有与起始节点相邻的节点, 我们又可以通过遍历这些__相邻节点的相邻节点__知道哪些节点的距离为 `dj = 1 + 1`, 而已经存在 `dj = 1` 的那些节点被忽略, 因为它们有与 `i` 直接相连的边.
- 反复这个过程, 我们就可以得到所有的节点距离 `dj = 1 + 1 + ... + 1`.

上述过程就称作 "Breadth-first search, BFS", 宽度优先搜索或广度优先搜索.

#### Queue

为了追踪整个搜索过程, 我们需要在遍历完所有 "Layer 1" 的节点后, 知道该从哪里开始遍历 "Layer 2" 的节点,
以及需要知道其中哪些节点是已经有与起始节点直接相连的边需要被忽略.

支撑这个算法的最基本的数据结构为队列:
队列 (`Q`) 中第一个元素为我们当前的起始节点,
所有的相邻节点添加到队列末尾 (`enqueue(Q, x)`),
每遍历完一个节点, 就将该元素移出队列 (`dequeue(Q)`).
至于需要被忽略的节点, 一个简单的想法是在进行搜索前, 先初始化到所有节点的距离 `dj ← ∞`,
以防止我们重复搜索已经计算过的节点. 即如果 `dj = ∞` 则说明该节点未处理过,
我们可以更新它的距离为一个具体数值; 反之则说明它已经被处理过, 我们就忽略它.
此外, 对于一个与 `i` 没有连通路径的节点 `j`, 则 `dj = ∞`.

<br>

### Pseudo-code

```
g = G(V,E)

1. Initialize Q to an empty queue   # Q[]
2. for each node j in V:
3.     dj = ∞
4. di = 0
5. enqueue(Q, i)
6. while Q is not empty:
7.     j = dequeue(Q)
8.     for each neighbor h of j:
9.         if dh == ∞:
10.            dh = dj + 1
11.            enqueue(Q, h)
12. return d
```

<br>

### BFS-based distance distribution

```
Input: g = G(V,E)
Output: the frequencies of each possible distance.
```

Q: How many possible distances can we have in a graph?

A: n - 1

```
Input: G = (V,E)
Output: the frequencies of each possible distance. f[0, |V|-1]

for d = 0 to |V|-1 :
    f[d] = 0

for each node i in V:
    dist = BFS(G, i)   # returns the distances from i to every other node
    for each node j in V:
        f[distj] = f[distj] + 1

return f
```

<br>

### BFS running time - loose analysis

```
# O(1), it takes a constant number of operations.
Initialize Q to an empty queue                           | O(1)

# O(n)
for each node j in V:                                    |
    # O(1)                                               | O(n)
    dj = ∞                                               |

# O(1)
di = 0                                                   |
# O(1)                                                   | O(1)
enqueue(Q, i)                                            |

# O(n), every node is added exactly once on to the queue.
while Q is not empty:                                    |
    # O(1)                                               |
    j = dequeue(Q)                                       |
    # O(n)                                               |
    for each neighbor h of j:                            |
        # O(1)                                           | O(n^2)
        if dh == ∞:                                      |
            # O(1)                                       |
            dh = dj + 1                                  |
            # O(1)                                       |
            enqueue(Q, h)                                |

# O(1)
return d                                                 | O(1)
================================================================
efficiency of this algorithm:                             O(n^2)
```

对于一个非常密集的图, `O(n^2)` 更接近它的实际效率;
而对于一个比较稀疏的图, `O(m+n)` 则更接近它的实际效率,
如果 `m>n` 则也可以直接描述为 `O(m)`.

[More...](https://wiki.python.org/moin/TimeComplexity)
