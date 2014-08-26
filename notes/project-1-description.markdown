# Project 1 - Degree distributions for graphs

<br>

### Overview

源页面参考 [mini-project description](https://class.coursera.org/algorithmicthink-001/wiki/graph_degree).

实现代码参考 [project-1.py](https://github.com/HexTeto/algorithmic-thinking/blob/master/src/project-1-devel.py).

要求用字典表示一些简单的图, 并实现两个函数计算计算这些图中 "in-degrees" 的分布.
这些函数会用来实现 `module-1` 中的部分功能, 此外提交的代码使用 Python 2.x 版本.

### Representing directed graphs

关于如何在 Python 中如何使用字典结构来描述一个有向图参考 [1-2-graph-basic](https://github.com/HexTeto/algorithmic-thinking/blob/master/material/1-2-graph-basics.pdf).

用常量定义 `EX_GRAPH0`, `EX_GRAPH1`, `EX_GRAPH2`. 它们用来执行单元测试.

实现函数 `make_complete_graph(num_nodes)`, 接收节点个数 `num_nodes`, 返回指定节点个数的有向图. 包括所有可能的边 (不允许 self-loops) 和所有的节点 (`{node: edges}`),
不指定节点数量则返回一个空的有向图.

### Computing degree distributions

实现以下两个函数:

- `compute_in_degrees(digraph)` 接收以字典描述的有向图 `digraph`, 返回所有节点的 "in-degrees". 该函数的输出应该还是保持一个字典结构 `{node: edges}`.
- `in_degree_distribution(digraph)` 接收以字典描述的有向图 `digraph`, 计算非标准化分布的 "in-degree". 该函数返回的字典结构应该是 `{in-degree distribution: the number of nodes}`.

_注意在第二个函数中, 非标准化分布结果应该是一个整数._
