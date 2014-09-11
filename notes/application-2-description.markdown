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

## Question 1

在 Question 1 中, 我们通过比较 `ER` 和 `UPA` 生成的随机网络来分析一个计算机网络中的主机在受到随机性攻击导致离线时整个网络的承受力.

首先已知示例网络中有 1347 个节点和 3112 条边,
需要指定 `ER` 算法的概率阈值, 和 `UPA` 算法中的已存在节点数量以及每次增加的边数, 使得最终它们的边数近似于示例网络.
这里我的取值为 `erGraph(num_nodes=1347, threshold=0.0017)`, `upaGraph(all_nodes=1347, existed_nodes=32, num_edges=2`.
