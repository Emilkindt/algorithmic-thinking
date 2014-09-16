# Application 2 - Analysis of a computer network

<br>

## Overview

在 Homework 和 Project 中, 我们已经学习了有关广度优先搜索和连通分量的基础知识.
在 Application 2 中, 我们将分析一个正在遭受攻击的计算机网络的连通性

我们通过一个无向图来表示一个计算机网络,
并通过不断删除图中的节点和它对应的边来模拟该网络中的服务器遭受攻击不断离线的场景.

### Example graphs

在 Application 2 中, 我们将计算几种不同类型的无向图的弹性:

- __[An example computer network](http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt)__
该样本数据为一个文本描述的计算机网络, 参考 [示例代码](http://www.codeskulptor.org/#alg_application2_provided.py) 从网络读取,
或者将文本文件下载到本地读取, 并将其转为无向图.

- 参考 ER 算法生成一个随机无向图.

![ER graph](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/ER-algorithm.jpg)

- 修改 DPA 算法生成一个随机无向图.

![DPA graph](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/DPA.jpg)


参考实现 [makeGraph.py](https://github.com/HexTeto/algorithmic-thinking/blob/master/src/makeGraph.py)

<br>

### Question 1

在 Question 1 中, 我们通过比较 `ER` 和 `UPA` 生成的随机网络来分析一个计算机网络中的主机在受到随机性攻击导致离线时整个网络的承受力.

首先已知示例网络中有 1347 个节点和 3112 条边,
需要指定 `ER` 算法的概率阈值, 和 `UPA` 算法中的已存在节点数量, 使得最终它们的边数近似于示例网络.

### Question 2

对网络中的节点进行随机攻击后，如果它的最大连通分量大致等于 (with in ~25%) 剩余节点数量,
我们就说一个网络在该类型攻击下是有弹性的.

检查 Question 1 中的三条曲线, 当移除了 20% 的节点后, 它们是否是弹性的?

### Question 3

在之后的三个问题中, 我们基于图的结构来改变攻击顺序, 一个简单的规则是优先攻击关键节点 (a node of maximum degree from the graph).

在示例代码中提供了函数 `targeted_order(ugraph)`, 该函数接受一个无向图参数然后迭代以下过程:

- 计算拥有最大 degree 的节点; 如果存在多个节点, 则任意选择其一.
- 删除该节点并移除对应的边.

`targeted_order` 会持续的更新无向图并计算当前拥有最大 degree 的节点, 其返回的节点序列作为 `compute_resilience` 的输入.

当阅读 `targeted_order` 的代码时, 你会发现它并不是非常高效的, 在计算最大 degree 节点的过程中有大量的重复工作.
我们将考虑一个替代方案来计算攻击序列.

![targetedorder](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/alg_fast_targeted.png)

如上图伪码所示, 在 Python 中, 该方法创建一个列表 `degree_sets`, 它的第 `k` 个元素为 `degree = k` 的节点的集合.
然后逆序迭代该列表, 当它遇到一个非空集合时, 该非空集合内的节点必定就是当前拥有最大 degree 的节点.
之后从这个集合中每次选出一个节点将它从图中移除, 并更新节点集合移除相应的边.

在 Q3 中, 我们将实现 `fast_targeted_order` 并通过和 `targeted_order` 比较, 分析它们在 UPA (`m=5`) 算法中的运行时间:

- 判定在 __worst-case__ 下的时间复杂度 `big-O`.
- 通过图表分析随着节点数量的增加, 运行时间的差异.

由于在 UPA 图中, 边的数量总是小于 `5n; (m=5)`, 用包括 `n` 的表达式来描述时间复杂度,
并假设 `fast_targeted_order` 中所有的集合操作复杂度为 `O(1)`.

之后计算多个 UPA graph, 节点范围为 `range(10, 1000, 10); m = 5`.
使用标准库中的 `time` 模块或其它工具来计算它们的运行时间.

绘图格式为:

- 纵轴为运行时间
- 横轴为节点数量 `n`
- 以两条曲线来表示两个函数的时间曲线
- 适当格式化图表, 包含 "legend", 并在标题中指出是使用何种 Python 环境制作.

### Question 4

修改 Q1 中的代码，这次使用在 Q3 中实现的 "关键节点优先" 的攻击顺序.
绘图要求同 Q1.

### Question 5

检查 Q4 的三条曲线, 根据 Q2 的要求进行简要分析.

### Question 6

如果发现了某条曲线在新的攻击模式下具有更好的弹性,
分析其原因以及一个健壮的网络设计是否应遵循与其类似的模型?
