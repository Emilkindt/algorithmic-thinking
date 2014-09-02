#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DPATrial import DPATrial as dpaT
from projectOne import make_complete_graph as makeG
from moduleOne import in_degree_distribution as inD

def synthetic_digraph(all_nodes, existed_nodes, add):
    complete_graph = makeG(existed_nodes)
    random_connect = dpaT(existed_nodes)

    for new_node in range(existed_nodes, all_nodes):
        complete_graph[new_node] = random_connect.run_trial(add)
    distribution = inD(complete_graph)
    distribution.pop(0)

    return distribution


if __name__ == '__main__':
    import scipy
    import matplotlib.pyplot as plt

    distribution = synthetic_digraph(27770, 12, 12)
    x = []
    y = []
    for k, v in distribution.items():
        x.append(k)
        y.append(v)
    x = scipy.array(x)
    y = scipy.array(y)
    plt.title("Synthetic Digraph")
    plt.xlabel("indegree, based on log10")
    plt.ylabel("normalized distribution, based on log10")
    plt.loglog(x, y, 'ro')
    plt.show()
