# Application 1 - Analysis of citation graphs

<br>

## Overview

在 `module 1` 中, 我们将结合之前学习过的数理分析方法来解决实际问题.
我们的目标是通过这些模拟任务让你所学的知识能够真正在生活实践中使用.

在这部分你需要编写代码处理一些中等大小的数据集.
代码部分可以在本地来完成, 而数据需要在 CodeSkulptor 上来完成,
这可能需要提高 CodeSkulptor 的默认超时时间.

```python
import codeskulptor
codeskulptor.set_timeout(60)
```

### Citation graphs

在这个应用中, 我们需要从论文中引用并生成图, 然后分析它的结构.
每篇学术论文都会引用多篇论文, 通常一篇论文的作者只大概了解它所引用的多篇论文中的一小部分.
由此就产生一个问题: 被引用的论文的选择是随机的还是存在一定内在联系的?

假设我们要寻找 "论文 x 引用了论文 y" 的关系, 我们需要把引用数据描述为有向图.
图中的节点表示论文, 一个 `x → y` 的边表示 `x` 引用了 `y`.
然后我们将分析这个有向图的 "in-degree distribution" 并与其它的图进行对比.

<br>

## Question 1

__把原始数据格式化为字典描述的有向图__

读取一个引用关系图, 它有 27770 个节点和 352807 条边.

```python
import urllib2
import codeskulptor
codeskulptor.set_timeout(30)

CITATION_URL = 'http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt'

def load_graph(graph_url):
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph.file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print("Loaded graph with", len(graph_lines), "nodes")

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
```

作为额外的挑战内容, 你也可以使用自己的代码来导入
[数据](http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt)
完成上边的内容.

```python
def loadGraph(originalData):
    data_lines = []
    digraph = {}

    with open(originalData) as f:
        for line in f.readlines():
            data_lines.append(line[ : -1])

    for line in data_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        digraph[node] = set()
        for edge in neighbors[1 : -1]:
            digraph[node].add(int(edge))

    return digraph
```

__绘图__

计算这个有向图的 in-degree 分布,
标准化的格式参考 `projectOne.py` 中实现的函数,
修改 `in_degree_distribution()` 的循环体, 添加一个计数器统计所有节点,
然后一个入度分布即 `float(nodes) / float(all_nodes)`.

利用这组数据创建一个双对数坐标图 (在 CodeSkulptor 上只支持 simpleplot 模块).
注意注明图中各轴的标签和基准 (入度为 0 的节点可以忽略, 因为 `log(0) = - ∞`).

<br>

## Question 2

在 Homework 1 中给出了一个基本的算法 `ER` 来生成一个随机图并对其结果进行简单分析.

```python
# Algorithm 1: ER.
# Input: Number of nodes n; probability p.
# Output: A graph g = (V,E) where g ∈ G(n, p)

 V = {i for i in range(n)}
 E = {}

for i in V:
    for j in V:
        if i != j:
            a = random.random()
            if a < p:
                E[i] = {i, j}
return E
```

在这个算法的基础上进行修改, 生成一个随机有向图:
对于每一对节点 `i` 和 `j`, 改良后的算法应该会进行两次判断,
首先根据概率参数 `p` 决定是否生成边 `i → j`,
然后再次根据概率参数 `p` 决定是否生成边 `j → i`.

在这个问题中, 你需要用 `ER` 算法生成一个随机有向图并计算它的 in-degree 分布,
以此绘图并与上一题中的引用图进行对比. 在示例算法中给定了概率参数 `p ∈ [0,1]` 和 入度 `k`,
现在因为我们关注的是入度分布, 故而你可以指定若干个入度分布的例子来决定图形的形状.

通过这个过程来回答以下问题:

- Is the expected in-degree the same for every node in an ER graph?
Answer yes or no and include a short explanation for your answer.
- What does the in-degree distribution for an ER graph look like?
Provide a plot (linear or log-log) of the degree distribution for a small value.
- Does the shape of the in-degree distribution plot for ER look similar to the
shape of the in-degree distribution for the citation graph?
Provide a short explanation of the similarities of differences.

比较两个图参考以下几点:

- 比较两个图中点或线的数量, 以及它们的分布 (是随机分布的还是具有一定的连贯性?).
- 如果图中的点可以用一条近似的曲线来表示, 比较曲线的形状, 斜率等因素, 分析它们的原因.

## Question 3

通过迭代生成一个随机有向图, 每次迭代添加一个节点并将该节点随机连接到已有节点的子集中.
子集的选择基于已有节点的 in-degree.

这个函数需要接受两个用户指定的参数: 最终整个图的节点数 `n`,
以及每次迭代时产生的新节点将连接 `m (m ≤ n)` 个已存在节点.

这个算法首先创建一个拥有 `m` 个节点的完整有向图,
然后通过不断迭代继续增加 `n - m` 个节点, 其中每个新节点都随机选择连接已有节点来连接.
在单次迭代过程中, 一个已存在的节点可能会被多次选择, 我们需要消除重复以避免平行边,
因此在每次迭代结果中, 新节点可能并不会连接到 `m` 个已有节点.

算法参考 `ref/DPA.jpg`

根据 question 1 中的 citation graph(27770,352807), 我们确定 dpa(V,E) 的节点数
`n = 27770`, 每次增加的边则取平均值 `m = 352807 / 27770 = 12`.

## Question 4

现在我们使用 question 3 中确定的值来实现 DPA 算法, 并绘制 in-degree 分布图.
这里一个关键的问题是需要避免每次都迭代所有的节点 (参考算法伪码中第 6 行),
否则这个程序执行起来将会消耗非常长的时间.

上述问题的解决方法可以参考 [这段代码](http://www.codeskulptor.org/#alg_dpa_trial.py)
实现一个 `DPATrial` 类.
该类实现了两个方法:

- `__init__(num_nodes)` 方法创建 `DPATrial` 对象, 它是一个拥有 `num_nodes` 个节点的完全图.
- `run_trial(num_nodes)` 方法运行 `num_nodes` 次 DPA trials (lines 4-6),
通过概率计算出一组节点, 它们即该次迭代产生的新节点的相邻节点.

即可以通过前边课程已经完成的代码先生成完全图,然后 `for range(m, n)` 迭代产生所有的新节点,
每次新节点所连接的节点通过调用 `DPATrial` 的一个实例的 `run_trial` 方法计算并将结果添加到已有的图中.

<br>

## Question 5

通过 question 4 的 DPA graph 可以发现, 它与 question 1 的 citation graph 非常相似.
尝试通过下列理论之一来解释导致这种相似的原因:

- "six degrees of separation"
- "rich gets richer"
- "Hierarchical structure of networks"
