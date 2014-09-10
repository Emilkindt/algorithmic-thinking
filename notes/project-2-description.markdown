# Project 2 - Connected components and graph resilience

<br>

![bfs_visited](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/BFS-CC-Visited.jpg)

### Breadth-first search

定义一个函数 `bfs_visited(ugraph, start_node)` 实现图例中的 `BFS-Visited` 算法.

### Connected components

定义函数 `cc_visited(ugraph)` 实现图例中 `CC-Visited` 算法.
该函数返回一个以每个连通分量所包含的节点的集合为值的列表 (`[{cc0.nodes}, {cc1.nodes}, ...]`),

定义函数 `largest_cc_size(ugraph)` 返回传入的无向图的最大连通分量的值 (返回整数类型).

### Graph resilience

实现一个函数 `compute_resilience(ugraph, attack_order)`,
它接受一个无向图和一个节点列表, 通过迭代列表中的节点删除图中它所连接的边, 然后计算改变后的无向图的最大连通分量的值.

该函数要返回一个列表, 它的第 `k+1` 个元素为 "删除了 `attack_order` 中前 `k` 个节点" 后的无向图的最大连通分量的值;
第 `1 (index=0)` 个元素为原始无向图的最大连通分量的值.

实现该函数最简单的方法是每删除一个节点都调用一次 `largest_cc_size` 计算当前结果图中最大连通分量的值.
该方法的复杂度为 `O(n(n+m))` (`n` 为节点数, `m` 为边数).

__Challenge:__ 因为在 `Module 2` 中计算的图都有几千个节点和边,
在 CodeSkulptor 中计算这些会非常慢, 尝试使用更加快速的算法来实现 `compute_resilence`.

参考方法 [Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Disjoint-set_linked_lists)
