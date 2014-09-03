# Question 5 的分析结果简述

<br>

![Figure 1. Citation graph](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/app-1-1.png)
![Figure 2. DPA graph](https://github.com/HexTeto/algorithmic-thinking/blob/master/ref/app-1-4.png)

通过比较 Citation graph 和 DPA graph 的入度分布,
它们从结果上非常相似. 都是呈现出一个按照
[帕瑞托分布 (Pareto distribution)](http://en.wikipedia.org/wiki/Pareto_distribution)
分布的
[无标度网络 (Scale-free network)](http://en.wikipedia.org/wiki/Scale-free_network).
但是我认为它们的成因是不同的, 无法使用相同的理论来解释.

<br>

## DPA graph

逐步分析 DPA graph 的产生过程:

- 初始拥有一个包含 12 个节点的完全有向图.
- 每次迭代加入的新节点随机连接至多 12 个已有节点 (不允许平行边).
- 本次迭代产生的新节点和它所连接的节点被加入集合中, 进行下次迭代.
- 重复这个迭代过程直到最终完成一个 27770 个节点的随机有向图.

对比 [参考代码](http://www.codeskulptor.org/#alg_dpa_trial.py)
中 `DPATrial.__init__` 的部分,
初始的有向图表示为:

```
[
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
  ...,
  ...,
  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11
]
```

在进行第一次迭代时, 因为每次新节点要尝试连接 12 个节点,
而当前正好只存在 12 个节点. 于是它们被连接的概率是 1/12.
假设我们运气很好没有出现平行边, 那么新节点 `12` 就会连接全部这 12 个已有节点.
于是在 `DPATrial.run_trial` 执行到最后会更新上边的列表为:

```
[
  0, ...,
  1, ...,
  2, ...,
  ...
  11, ...,
  12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
]
```

此时列表中概率的分布就发生了变化.
在下次迭代中, 节点 `0` ~ `11` 它们就会获得一个相对较高的概率 13/157;
而上次迭代产生的新节点 `12` 只得到了一个极低的概率 1/157.
于是第二次迭代产生的新节点 `13` 就会有更大的几率去连接 `0` ~ `11` 而不是上次产生的 `12`.

于是随着迭代过程的继续, 这种概率差距就逐步被拉大, 形成一种优势累积.
这就是所谓 "富人越富, 穷人越穷" 的现象. 故而我认为这就是一种
[择优连接的过程 (Preferential attachment process)](http://en.wikipedia.org/wiki/Preferential_attachment).

<br>

## Citation graph

尽管 DPA graph 和 Citation graph 的结果非常相似,
但通过对 DPA graph 的产生过程分析,
我认为它只能说明一部分原因,
这明显不足以解释为何论文引用关系会呈现这种分布.
对于一个现实世界的真实问题来说, 影响它的因素是综合而复杂的,
很难使用某个理论就解释清楚这一现象, 它涉及了下列众多内容:

- [Six degrees of separation](http://en.wikipedia.org/wiki/Six_degrees_of_separation),
- [Matthew effect](http://en.wikipedia.org/wiki/Matthew_effect),
- [Wealth concentration](http://en.wikipedia.org/wiki/Wealth_concentration),
- [Network science](http://en.wikipedia.org/wiki/Network_science)
- More ...
